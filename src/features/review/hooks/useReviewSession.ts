import { useCallback, useEffect, useState } from 'react'
import type { Exam } from '@/features/review/lib/exam-loader'
import { canCompleteReview, criterionScore, isReviewComplete } from '@/features/review/lib/scoring'
import type {
  PersistedReviewSession,
  ReviewConfidence,
  ReviewEntry,
  ReviewSession,
} from '@/features/review/types'

const storageKey = 'krugrade-vite-human-review-v1'

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

function readSavedSession(): ReviewSession {
  try {
    const saved = localStorage.getItem(storageKey)
    if (!saved) return { reviews: {}, currentIndex: 0 }

    const parsed: unknown = JSON.parse(saved)
    if (!isRecord(parsed)) return { reviews: {}, currentIndex: 0 }

    const reviews: Record<string, ReviewEntry> = {}
    for (const [reviewItemId, value] of Object.entries(parsed)) {
      if (reviewItemId === '__index' || !isRecord(value)) continue

      reviews[reviewItemId] = Object.fromEntries(
        Object.entries(value).filter((entry): entry is [string, string] => typeof entry[1] === 'string'),
      )
    }

    const currentIndex = Number.isInteger(parsed.__index) && Number(parsed.__index) >= 0
      ? Number(parsed.__index)
      : 0

    return { reviews, currentIndex }
  } catch {
    return { reviews: {}, currentIndex: 0 }
  }
}

export function useReviewSession() {
  const [session, setSession] = useState<ReviewSession>(readSavedSession)

  useEffect(() => {
    const saved: PersistedReviewSession = {
      ...session.reviews,
      __index: session.currentIndex,
    }

    try {
      localStorage.setItem(storageKey, JSON.stringify(saved))
    } catch {
      // The review remains usable if browser storage is unavailable.
    }
  }, [session])

  const selectIndex = useCallback((index: number) => {
    setSession((current) => ({ ...current, currentIndex: index }))
  }, [])

  const clampIndex = useCallback((count: number) => {
    setSession((current) => {
      const currentIndex = Math.min(current.currentIndex, Math.max(0, count - 1))
      return currentIndex === current.currentIndex ? current : { ...current, currentIndex }
    })
  }, [])

  const updateField = useCallback((reviewItemId: string, field: string, value: string) => {
    setSession((current) => {
      const review = current.reviews[reviewItemId] || {}
      return {
        ...current,
        reviews: {
          ...current.reviews,
          [reviewItemId]: {
            ...review,
            [field]: value,
            review_started_at: review.review_started_at || new Date().toISOString(),
          },
        },
      }
    })
  }, [])

  const updateScore = useCallback((reviewItemId: string, criterionId: string, score: number) => {
    updateField(reviewItemId, `criterion_score_${criterionId}`, String(score))
  }, [updateField])

  const updateConfidence = useCallback((reviewItemId: string, confidence: ReviewConfidence) => {
    updateField(reviewItemId, 'review_confidence', confidence)
  }, [updateField])

  const updateFeedback = useCallback((reviewItemId: string, feedback: string) => {
    updateField(reviewItemId, 'feedback_to_student', feedback)
  }, [updateField])

  const completeReview = useCallback((exam: Exam) => {
    setSession((current) => {
      const review = current.reviews[exam.review_item_id] || {}
      if (isReviewComplete(exam.criteria, review) || !canCompleteReview(exam.criteria, review)) {
        return current
      }

      const now = new Date().toISOString()
      const scores = Object.fromEntries(
        exam.criteria.map((criterion) => [
          `criterion_score_${criterion.id}`,
          String(criterionScore(criterion, review)),
        ]),
      )

      return {
        ...current,
        reviews: {
          ...current.reviews,
          [exam.review_item_id]: {
            ...review,
            ...scores,
            review_started_at: review.review_started_at || now,
            review_status: 'completed',
            reviewed_at: now,
          },
        },
      }
    })
  }, [])

  return {
    reviews: session.reviews,
    selectedIndex: session.currentIndex,
    selectIndex,
    clampIndex,
    updateScore,
    updateConfidence,
    updateFeedback,
    completeReview,
  }
}
