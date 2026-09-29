import { useEffect, useMemo, useRef, useState } from 'react'
import './App.css'

type Criterion = { id: string; text: string; max: number }
type QuestionAsset = { asset_kind: 'exact' | 'fallback_range'; filename: string }
type ContextImage = { filename: string; label: string }
type Assignment = Record<string, string> & { question_asset: QuestionAsset; context_images: ContextImage[] }
type ReviewState = Record<string, Record<string, string> | number>

declare global {
  interface Window {
    katex?: { render: (formula: string, element: HTMLElement, options: Record<string, unknown>) => void }
  }
}

const storageKey = 'krugrade-vite-human-review-v1'

function getCriteria(row: Assignment): Criterion[] {
  return Array.from({ length: 5 }, (_, index) => index + 1)
    .map((number) => ({ id: row[`criterion_id_${number}`], text: row[`criterion_text_${number}`], max: Number(row[`criterion_max_${number}`]) }))
    .filter((criterion) => criterion.id)
}

function mathCandidates(text: string): string[] {
  const formulas = new Set<string>()
  const latex = (value: string) => value.trim()
    .replaceAll('≥', '\\ge').replaceAll('<=', '\\le').replaceAll('≥', '\\ge')
    .replaceAll('>=', '\\ge').replaceAll('≤', '\\le')
    .replace(/\s+/g, ' ')
  const add = (value: string, isLatex = false) => {
    const clean = value.trim().replace(/[,.!?;:]$/, '')
    if (clean.length < 2 || clean.length > 120) return
    if (!isLatex && (!/^[0-9A-Za-z_+*/^=<>(),.\s-]+$/.test(clean) || /\b(?:gives|hence|and|so|this|feasible|solution|profit|value)\b/i.test(clean))) return
    formulas.add(isLatex ? clean : latex(clean))
  }
  const clean = text.replaceAll('≥', '>=').replaceAll('≤', '<=')
  const lp = clean.match(/\b(max|min)\s+z\s*=\s*(.+?)\s+subject\s+to\s+(.+?)(?:[.!?]|$)/i)
  if (lp) {
    const objective = latex(lp[2])
    const pieces = lp[3].split(/,\s*(?=[+-]?(?:(?:\d+)?x_\d|x_\d|\d))/)
    const constraints: string[] = []
    let pending = ''
    for (const piece of pieces) {
      const candidate = `${pending}${piece}`.trim()
      if (/(?:>=|<=|=)/.test(candidate)) { constraints.push(latex(candidate)); pending = '' }
      else pending = `${candidate}, `
    }
    if (constraints.length) {
      const rows = constraints.map((constraint, index) => `${index === 0 ? '\\text{subject to}\\quad &' : '&'} ${constraint}`).join(' \\\\ ')
      return [`\\begin{aligned}\\${lp[1].toLowerCase()}\\quad & z = ${objective} \\\\ ${rows}\\end{aligned}`]
    }
  }
  for (const match of clean.matchAll(/\\\(([^)]+)\\\)|\$\$?([^$]+)\$\$?/g)) add(match[1] || match[2], true)
  const variable = '(?:\\d+)?x_\\d'
  const term = `(?:${variable}|\\d+(?:,\\d+)?(?:\\([^)]*\\))?|\\([^)]*\\))`
  const expression = `${term}(?:\\s*[+*/-]\\s*${term})*`
  const patterns = [
    /\([^)]*x_\d[^)]*\)\s*=\s*\([^)]*\)/g,
    new RegExp(`[-+]?\\s*${expression}\\s*(?:=|>=|<=)\\s*(?:${expression}|\\([^)]*\\))`, 'g'),
  ]
  for (const pattern of patterns) for (const match of clean.matchAll(pattern)) add(match[0])
  return [...formulas].slice(0, 8)
}

function questionOrder(row: Assignment): [number, number] {
  const match = row.question_id.match(/^EXAM_(\d{4})_Q(\d+)$/)
  return match ? [Number(match[1]), Number(match[2])] : [Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]
}

function compareAssignments(left: Assignment, right: Assignment): number {
  const [leftYear, leftQuestion] = questionOrder(left)
  const [rightYear, rightQuestion] = questionOrder(right)
  return leftYear - rightYear || leftQuestion - rightQuestion || left.review_item_id.localeCompare(right.review_item_id)
}

function MathAid({ text }: { text: string }) {
  const formulas = useMemo(() => mathCandidates(text), [text])
  const refs = useRef<(HTMLDivElement | null)[]>([])
  useEffect(() => {
    refs.current.forEach((element, index) => {
      if (!element) return
      element.replaceChildren()
      try {
        if (window.katex) window.katex.render(formulas[index], element, { displayMode: true, throwOnError: false })
        else element.textContent = formulas[index]
      } catch { element.textContent = formulas[index] }
    })
  }, [formulas])
  if (!formulas.length) return null
  const isLinearProgram = formulas[0].includes('\\begin{aligned}')
  return <div className="math-aid"><span>{isLinearProgram ? 'Mathematical form' : 'Key mathematical expressions'}</span><p>{isLinearProgram ? 'The objective and all constraints are shown together.' : 'Extracted from the text to make the equations easier to read.'}</p>{formulas.map((formula, index) => <div className="math-line" key={`${formula}-${index}`} ref={(element) => { refs.current[index] = element }} />)}</div>
}

function TextPanel({ label, help, text, answer = false }: { label: string; help?: string; text: string; answer?: boolean }) {
  return <section className={`text-panel ${answer ? 'student-answer' : ''}`}><span className="eyebrow">{label}</span>{help && <p className="panel-help">{help}</p>}<div className="raw-text">{text}</div><MathAid text={text} /></section>
}

function App() {
  const [assignments, setAssignments] = useState<Assignment[]>([])
  const [index, setIndex] = useState(0)
  const [state, setState] = useState<ReviewState>(() => { try { return JSON.parse(localStorage.getItem(storageKey) || '{}') as ReviewState } catch { return {} } })
  const [modalImage, setModalImage] = useState<string | null>(null)
  const [savedAt, setSavedAt] = useState('')

  useEffect(() => { fetch('/data/assignments.json').then((response) => response.json()).then((rows: Assignment[]) => setAssignments([...rows].sort(compareAssignments))) }, [])
  useEffect(() => { localStorage.setItem(storageKey, JSON.stringify({ ...state, __index: index })); setSavedAt(new Date().toLocaleTimeString()) }, [state, index])
  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      const editing = ['INPUT', 'TEXTAREA', 'SELECT'].includes((event.target as HTMLElement)?.tagName)
      if (event.key === 'Escape') setModalImage(null)
      if (!editing && event.key === 'ArrowLeft') setIndex((current) => Math.max(0, current - 1))
      if (!editing && event.key === 'ArrowRight') setIndex((current) => Math.min(assignments.length - 1, current + 1))
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [assignments.length])

  const row = assignments[index]
  const review = row ? (state[row.review_item_id] as Record<string, string> || {}) : {}
  const criteria = row ? getCriteria(row) : []
  const isComplete = (item: Assignment) => {
    const itemState = state[item.review_item_id] as Record<string, string> || {}
    return getCriteria(item).every((criterion) => itemState[`criterion_score_${criterion.id}`] !== undefined && itemState[`criterion_score_${criterion.id}`] !== '') && itemState.review_confidence && itemState.review_status === 'completed'
  }
  const completed = assignments.filter(isComplete).length
  const total = criteria.every((criterion) => review[`criterion_score_${criterion.id}`] !== undefined && review[`criterion_score_${criterion.id}`] !== '') ? criteria.reduce((sum, criterion) => sum + Number(review[`criterion_score_${criterion.id}`]), 0) : null

  const update = (field: string, value: string) => {
    if (!row) return
    setState((current) => ({ ...current, [row.review_item_id]: { ...(current[row.review_item_id] as Record<string, string> || {}), [field]: value, review_started_at: (current[row.review_item_id] as Record<string, string> || {}).review_started_at || new Date().toISOString(), ...(field === 'review_status' ? { reviewed_at: value === 'completed' ? new Date().toISOString() : '' } : {}) } }))
  }
  const exportCsv = () => {
    const headers = Object.keys(assignments[0]).filter((header) => header !== 'question_asset')
    const quote = (value: unknown) => `"${String(value ?? '').replaceAll('"', '""')}"`
    const lines = [headers.map(quote).join(',')]
    assignments.forEach((item) => {
      const itemState = state[item.review_item_id] as Record<string, string> || {}
      const output: Record<string, string> = { ...item }
      getCriteria(item).forEach((criterion) => { output[`criterion_score_${criterion.id}`] = itemState[`criterion_score_${criterion.id}`] || '' })
      const allScored = getCriteria(item).every((criterion) => itemState[`criterion_score_${criterion.id}`] !== undefined && itemState[`criterion_score_${criterion.id}`] !== '')
      output.human_score = allScored ? String(getCriteria(item).reduce((sum, criterion) => sum + Number(itemState[`criterion_score_${criterion.id}`]), 0)) : ''
      ;['human_notes', 'review_confidence', 'review_started_at', 'reviewed_at', 'review_status'].forEach((field) => { output[field] = itemState[field] || (field === 'review_status' ? 'pending' : '') })
      lines.push(headers.map((header) => quote(output[header])).join(','))
    })
    const url = URL.createObjectURL(new Blob([`\ufeff${lines.join('\n')}`], { type: 'text/csv;charset=utf-8' }))
    const anchor = document.createElement('a'); anchor.href = url; anchor.download = 'human_review_pilot50_vite_completed.csv'; anchor.click(); URL.revokeObjectURL(url)
  }
  const clearDraft = () => { if (window.confirm("Clear this browser's saved review draft?")) { localStorage.removeItem(storageKey); setState({}); setIndex(0) } }

  if (!row) return <main className="loading">Loading reviewer assignments…</main>
  const imageUrl = `/assets/questions/${row.question_asset.filename}`

  return <>
    <header className="app-header"><div className="header-inner"><div className="brand"><div className="brand-mark">KG</div><div><h1>KruGrade Human Review</h1><p>Visual question crops + readable math</p></div></div><div className="progress-block"><div><span>Completed {completed} / {assignments.length}</span><span>Autosaved {savedAt || 'locally'}</span></div><progress max={assignments.length} value={completed} /></div></div></header>
    <main className="app-shell">
      <section className="help-card"><h2>How to review</h2><p>Read the original question image first. Use the readable text and mathematical expressions below only as aids. Then score each rubric criterion independently.</p><kbd>←</kbd><kbd>→</kbd><span>Move between assignments</span></section>
      <nav className="toolbar" aria-label="Review navigation"><button className="ghost" disabled={index === 0} onClick={() => setIndex(index - 1)}>← Previous</button><button disabled={index === assignments.length - 1} onClick={() => setIndex(index + 1)}>Next →</button><button className="ghost" onClick={exportCsv}>Export CSV</button><button className="danger" onClick={clearDraft}>Clear draft</button><span>Saved {savedAt || 'locally'}</span></nav>
      <article className="review-card">
        <div className="review-heading"><div><span className="eyebrow">Review item {index + 1} of {assignments.length}</span><h2>{row.question_id}</h2><p>Review ID: {row.review_item_id} · Image: {row.question_asset.asset_kind}</p></div><span className={isComplete(row) ? 'badge complete' : 'badge pending'}>{isComplete(row) ? '✓ Completed' : '● Pending'}</span></div>
        <section className="question-hero"><span className="eyebrow">Original exam question</span><img className="question-image" src={imageUrl} alt={`${row.question_id} question crop`} onClick={() => setModalImage(imageUrl)} /><small>{row.question_asset.asset_kind === 'fallback_range' ? 'This is a supplied multi-question crop because an individual crop was unavailable.' : 'This is the original cropped image for this question.'} Click the image to enlarge.</small></section>
        {row.context_images.length > 0 && <section className="question-context"><div><span className="eyebrow">Question set context</span><h3>Original crop containing this question and nearby questions</h3><p>Use this when the wording, diagram, or shared information continues across the question set.</p></div><div className="context-images">{row.context_images.map((image) => <figure key={image.filename}><img src={`/assets/question-groups/${image.filename}`} alt={image.label} onClick={() => setModalImage(`/assets/question-groups/${image.filename}`)} /><figcaption>{image.label} · Click to enlarge</figcaption></figure>)}</div></section>}
        <TextPanel label="Readable question text" help="A text version of the question for searching and close reading. Refer to the original image if any wording differs." text={row.question_text} />
        <div className="content-grid"><TextPanel label="Reference solution" help="Use this to understand the intended correct result and valid reasoning." text={row.canonical_solution} /><TextPanel label="Student response" help="Score this response only against the rubric below." text={row.answer_text} answer /></div>
        <TextPanel label="How to award points" help="Award each listed criterion independently. The method may differ if the mathematical reasoning is valid." text={row.rubric_scoring_guide} />
        <section className="score-section"><span className="eyebrow">Enter criterion scores</span><div className="rubric">{criteria.map((criterion) => <div className="criterion" key={criterion.id}><div><strong>{criterion.id} <span>(maximum {criterion.max})</span></strong><p>{criterion.text}</p></div><select value={review[`criterion_score_${criterion.id}`] || ''} onChange={(event) => update(`criterion_score_${criterion.id}`, event.target.value)}><option value="">Choose score</option>{Array.from({ length: criterion.max + 1 }, (_, score) => <option value={score} key={score}>{score}</option>)}</select></div>)}</div><div className="total">Calculated total: <b>{total ?? '—'}</b> / {criteria.reduce((sum, criterion) => sum + criterion.max, 0)}</div></section>
        <section className="review-fields"><label>Review confidence<select value={review.review_confidence || ''} onChange={(event) => update('review_confidence', event.target.value)}><option value="">Choose confidence</option><option value="1">1 · Low</option><option value="2">2 · Medium</option><option value="3">3 · High</option></select></label><label>Review status<select value={review.review_status || 'pending'} onChange={(event) => update('review_status', event.target.value)}><option value="pending">Pending</option><option value="completed">Completed</option></select></label><label className="notes">Notes for reconciliation<textarea value={review.human_notes || ''} placeholder="Optional: ambiguity, assumption, or a decision to revisit" onChange={(event) => update('human_notes', event.target.value)} /></label></section>
        <footer><button className="ghost" disabled={index === 0} onClick={() => setIndex(index - 1)}>← Previous</button><button disabled={index === assignments.length - 1} onClick={() => setIndex(index + 1)}>Next →</button></footer>
      </article>
    </main>
    {modalImage && <div className="image-modal" role="dialog" aria-modal="true" onClick={() => setModalImage(null)}><button onClick={() => setModalImage(null)}>×</button><img src={modalImage} alt="Enlarged question crop" onClick={(event) => event.stopPropagation()} /></div>}
  </>
}

export default App
