function normalizeLatex(value: string): string {
  return value.trim()
    .replaceAll('≥', '\\ge')
    .replaceAll('>=', '\\ge')
    .replaceAll('≤', '\\le')
    .replaceAll('<=', '\\le')
    .replace(/\s+/g, ' ')
}

/** Extracts mathematical expressions from the dataset's mixed prose and notation. */
export function mathCandidates(text: string): string[] {
  const formulas = new Set<string>()
  const add = (value: string, isLatex = false) => {
    const clean = value.trim().replace(/[,.!?;:]$/, '')
    if (clean.length < 2 || clean.length > 120) return
    if (
      !isLatex
      && (!/^[0-9A-Za-z_+*/^=<>(),.\s-]+$/.test(clean)
        || /\b(?:gives|hence|and|so|this|feasible|solution|profit|value)\b/i.test(clean))
    ) return

    formulas.add(isLatex ? clean : normalizeLatex(clean))
  }

  const clean = text.replaceAll('≥', '>=').replaceAll('≤', '<=')
  const linearProgram = clean.match(/\b(max|min)\s+z\s*=\s*(.+?)\s+subject\s+to\s+(.+?)(?:[.!?]|$)/i)
  if (linearProgram) {
    const objective = normalizeLatex(linearProgram[2])
    const pieces = linearProgram[3].split(/,\s*(?=[+-]?(?:(?:\d+)?x_\d|x_\d|\d))/)
    const constraints: string[] = []
    let pending = ''

    for (const piece of pieces) {
      const candidate = `${pending}${piece}`.trim()
      if (/(?:>=|<=|=)/.test(candidate)) {
        constraints.push(normalizeLatex(candidate))
        pending = ''
      } else {
        pending = `${candidate}, `
      }
    }

    if (constraints.length) {
      const rows = constraints
        .map((constraint, index) => `${index === 0 ? '\\text{subject to}\\quad &' : '&'} ${constraint}`)
        .join(' \\\\ ')
      return [`\\begin{aligned}\\${linearProgram[1].toLowerCase()}\\quad & z = ${objective} \\\\ ${rows}\\end{aligned}`]
    }
  }

  for (const match of clean.matchAll(/\\\(([^)]+)\\\)|\$\$?([^$]+)\$\$?/g)) {
    add(match[1] || match[2], true)
  }

  const variable = '(?:\\d+|\\([^)]*\\))?(?:x_\\d|z)'
  const term = `(?:${variable}|\\d+(?:,\\d+)?(?:\\([^)]*\\))?|\\([^)]*\\))`
  const expression = `${term}(?:\\s*[+*/-]\\s*${term})*`
  const patterns = [
    /\([^)]*x_\d[^)]*\)\s*=\s*\([^)]*\)/g,
    new RegExp(`[-+]?\\s*${expression}(?:\\s*(?:=|>=|<=)\\s*${expression})+`, 'g'),
  ]

  for (const pattern of patterns) {
    for (const match of clean.matchAll(pattern)) add(match[0])
  }

  return [...formulas].slice(0, 8)
}
