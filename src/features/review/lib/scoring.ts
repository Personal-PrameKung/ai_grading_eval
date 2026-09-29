import type { Criterion } from '@/features/review/lib/exam-loader'
import type { ReviewEntry } from '@/features/review/types'

export function criterionScore(criterion: Criterion, review: ReviewEntry | undefined): number {
  const saved = review?.[`criterion_score_${criterion.id}`]
  if (saved === undefined || saved === '') return criterion.max

  const score = Number(saved)
  return Number.isInteger(score) && score >= 0 && score <= criterion.max
    ? score
    : criterion.max
}

export function scoreTotal(criteria: Criterion[], review: ReviewEntry | undefined): number {
  return criteria.reduce((total, criterion) => total + criterionScore(criterion, review), 0)
}

export function maximumScore(criteria: Criterion[]): number {
  return criteria.reduce((total, criterion) => total + criterion.max, 0)
}

export function canCompleteReview(criteria: Criterion[], review: ReviewEntry | undefined): boolean {
  const confidence = review?.review_confidence
  const confidenceSelected = confidence === '1' || confidence === '2' || confidence === '3'
  const criteriaScored = criteria.every((criterion) => {
    const score = criterionScore(criterion, review)
    return Number.isInteger(score) && score >= 0 && score <= criterion.max
  })

  return criteriaScored && confidenceSelected
}
