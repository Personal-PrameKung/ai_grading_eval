export type QuestionAsset = {
  asset_kind: 'exact' | 'fallback_range'
  filename: string
}

export type ContextImage = {
  filename: string
  label: string
}

export type Criterion = {
  id: string
  text: string
  max: number
}

export type Exam = Record<string, unknown> & {
  review_item_id: string
  question_id: string
  question_text: string
  canonical_solution: string
  answer_text: string
  rubric_scoring_guide: string
  question_asset: QuestionAsset
  context_images: ContextImage[]
  criteria: Criterion[]
}

const defaultExamDataUrl = '/data/assignments.json'

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

function requiredText(value: Record<string, unknown>, field: string, rowIndex: number): string {
  const text = value[field]
  if (typeof text !== 'string') {
    throw new Error(`Exam row ${rowIndex + 1} has an invalid ${field}`)
  }

  return text
}

function parseQuestionAsset(value: unknown, rowIndex: number): QuestionAsset {
  if (!isRecord(value)) {
    throw new Error(`Exam row ${rowIndex + 1} has an invalid question_asset`)
  }

  const { asset_kind: assetKind, filename } = value
  if ((assetKind !== 'exact' && assetKind !== 'fallback_range') || typeof filename !== 'string') {
    throw new Error(`Exam row ${rowIndex + 1} has an invalid question_asset`)
  }

  return { asset_kind: assetKind, filename }
}

function parseContextImages(value: unknown, rowIndex: number): ContextImage[] {
  if (!Array.isArray(value)) {
    throw new Error(`Exam row ${rowIndex + 1} has invalid context_images`)
  }

  return value.map((image, imageIndex) => {
    if (!isRecord(image) || typeof image.filename !== 'string' || typeof image.label !== 'string') {
      throw new Error(`Exam row ${rowIndex + 1} has invalid context image ${imageIndex + 1}`)
    }

    return { filename: image.filename, label: image.label }
  })
}

function parseCriteria(value: Record<string, unknown>, rowIndex: number): Criterion[] {
  const criteria: Criterion[] = []

  for (let number = 1; number <= 5; number += 1) {
    const id = requiredText(value, `criterion_id_${number}`, rowIndex)
    const text = requiredText(value, `criterion_text_${number}`, rowIndex)
    const rawMax = requiredText(value, `criterion_max_${number}`, rowIndex)
    if (!id.trim()) continue

    const max = Number(rawMax)
    if (!Number.isInteger(max) || max < 0) {
      throw new Error(`Exam row ${rowIndex + 1} has an invalid criterion_max_${number}`)
    }

    criteria.push({ id, text, max })
  }

  return criteria
}

function parseExam(value: unknown, rowIndex: number): Exam {
  if (
    !isRecord(value)
    || typeof value.review_item_id !== 'string'
    || typeof value.question_id !== 'string'
  ) {
    throw new Error(`Exam row ${rowIndex + 1} is missing its review_item_id or question_id`)
  }

  return {
    ...value,
    review_item_id: value.review_item_id,
    question_id: value.question_id,
    question_text: requiredText(value, 'question_text', rowIndex),
    canonical_solution: requiredText(value, 'canonical_solution', rowIndex),
    answer_text: requiredText(value, 'answer_text', rowIndex),
    rubric_scoring_guide: requiredText(value, 'rubric_scoring_guide', rowIndex),
    question_asset: parseQuestionAsset(value.question_asset, rowIndex),
    context_images: parseContextImages(value.context_images, rowIndex),
    criteria: parseCriteria(value, rowIndex),
  }
}

function questionOrder(exam: Exam): [number, number] {
  const match = exam.question_id.match(/^EXAM_(\d{4})_Q(\d+)$/)
  return match
    ? [Number(match[1]), Number(match[2])]
    : [Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER]
}

function compareExams(left: Exam, right: Exam): number {
  const [leftYear, leftQuestion] = questionOrder(left)
  const [rightYear, rightQuestion] = questionOrder(right)

  return leftYear - rightYear
    || leftQuestion - rightQuestion
    || left.review_item_id.localeCompare(right.review_item_id)
}

/** Fetches, validates, and sorts the exam assignments used by the review app. */
export async function loadExams(dataUrl = defaultExamDataUrl): Promise<Exam[]> {
  const response = await fetch(dataUrl)
  if (!response.ok) {
    throw new Error(`Unable to load exam data (${response.status} ${response.statusText})`)
  }

  const payload: unknown = await response.json()
  if (!Array.isArray(payload)) {
    throw new Error('Exam data must be a JSON array')
  }

  return payload.map(parseExam).sort(compareExams)
}
