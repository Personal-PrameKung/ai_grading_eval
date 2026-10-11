import type { Criterion, Exam } from '@/features/review/lib/exam-loader'
import { isReviewComplete } from '@/features/review/lib/scoring'
import type { ReviewEntry } from '@/features/review/types'

function savedScore(criterion: Criterion, review: ReviewEntry | undefined): string {
  const value = review?.[`criterion_score_${criterion.id}`]
  if (value === undefined || value === '') return ''

  const score = Number(value)
  return Number.isInteger(score) && score >= 0 && score <= criterion.max ? String(score) : ''
}

function csvCell(value: unknown): string {
  const text = value === null || value === undefined
    ? ''
    : typeof value === 'object' ? JSON.stringify(value) : String(value)

  return `"${text.replaceAll('"', '""')}"`
}

/** Keeps the source dataset's CSV columns and fills them with saved review values. */
export function serializeReviewsCsv(exams: Exam[], reviews: Record<string, ReviewEntry>): string {
  if (exams.length === 0) return ''

  const columns = Object.keys(exams[0]).filter((column) => column !== 'question_asset' && column !== 'criteria')
  const lines = [columns.map(csvCell).join(',')]

  for (const exam of exams) {
    const review = reviews[exam.review_item_id]
    const row: Record<string, unknown> = { ...exam }
    const scores = exam.criteria.map((criterion) => savedScore(criterion, review))

    for (let slot = 1; slot <= 5; slot += 1) {
      const criterionId = exam[`criterion_id_${slot}`]
      const criterion = exam.criteria.find((item) => item.id === criterionId)
      if (criterion) row[`criterion_score_${slot}`] = savedScore(criterion, review)
    }

    row.human_score = scores.every((score) => score !== '')
      ? String(scores.reduce((total, score) => total + Number(score), 0))
      : ''
    row.human_notes = review?.human_notes || review?.feedback_to_student || exam.human_notes || ''
    row.review_confidence = review?.review_confidence || exam.review_confidence || ''
    row.review_started_at = review?.review_started_at || exam.review_started_at || ''
    row.reviewed_at = review?.reviewed_at || exam.reviewed_at || ''
    row.review_status = isReviewComplete(exam.criteria, review) ? 'completed' : 'pending'

    lines.push(columns.map((column) => csvCell(row[column])).join(','))
  }

  return lines.join('\n')
}
