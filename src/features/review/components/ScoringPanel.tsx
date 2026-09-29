import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import type { Exam } from '@/features/review/lib/exam-loader'
import { canCompleteReview, criterionScore, maximumScore, scoreTotal } from '@/features/review/lib/scoring'
import type { ReviewConfidence, ReviewEntry } from '@/features/review/types'

const confidenceOptions = [
  { value: '1', label: 'Low' },
  { value: '2', label: 'Medium' },
  { value: '3', label: 'High' },
] as const

type ScoringPanelProps = {
  exam: Exam
  review: ReviewEntry | undefined
  onScoreChange: (criterionId: string, score: number) => void
  onConfidenceChange: (confidence: ReviewConfidence) => void
  onFeedbackChange: (feedback: string) => void
  hasPrevious: boolean
  hasNext: boolean
  onPrevious: () => void
  onComplete: () => void
  onNext: () => void
}

export function ScoringPanel({
  exam,
  review,
  onScoreChange,
  onConfidenceChange,
  onFeedbackChange,
  hasPrevious,
  hasNext,
  onPrevious,
  onComplete,
  onNext,
}: ScoringPanelProps) {
  const [completionAttempted, setCompletionAttempted] = useState(false)
  const total = scoreTotal(exam.criteria, review)
  const maximum = maximumScore(exam.criteria)
  const completed = review?.review_status === 'completed'
  const canComplete = canCompleteReview(exam.criteria, review)

  const handleComplete = () => {
    if (!canComplete) {
      setCompletionAttempted(true)
      return
    }

    onComplete()
  }

  return (
    <aside aria-labelledby="scoring-title" className="min-w-0 self-start rounded-xl border bg-card p-4 shadow-sm sm:p-6 md:sticky md:top-4 md:flex md:max-h-[calc(100dvh-2rem)] md:flex-col md:overflow-hidden">
      <div className="md:min-h-0 md:flex-1 md:overflow-y-auto">
        <div className="flex items-center justify-between gap-3">
          <h2 id="scoring-title" className="text-sm font-semibold">
            Score response
          </h2>
          <div className="shrink-0 text-right" aria-label={`Total score: ${total} out of ${maximum}`}>
            <span className="text-2xl font-semibold text-primary">{total}</span>
            <span className="text-sm text-muted-foreground"> / {maximum}</span>
          </div>
        </div>

        <div className="mt-5 space-y-4">
          {exam.criteria.map((criterion) => {
            const selectedScore = criterionScore(criterion, review)

            return (
              <section key={criterion.id} className="rounded-lg border bg-muted/20 p-3">
                <div className="flex items-baseline gap-1.5">
                  <h3 className="text-sm font-semibold">{criterion.id}</h3>
                  <span className="text-xs text-muted-foreground">
                    {criterion.max} max
                  </span>
                </div>
                <p className="mt-2 break-words text-sm leading-6 text-foreground/85">
                  {criterion.text}
                </p>
                <div
                  role="group"
                  aria-label={`Score for ${criterion.id}, maximum ${criterion.max}`}
                  className="mt-3 flex flex-wrap gap-2"
                >
                  {Array.from({ length: criterion.max + 1 }, (_, score) => (
                    <Button
                      key={score}
                      type="button"
                      size="icon-sm"
                      variant={score === selectedScore ? 'default' : 'outline'}
                      className="text-xs"
                      aria-pressed={score === selectedScore}
                      aria-label={`${score} points for ${criterion.id}`}
                      onClick={() => onScoreChange(criterion.id, score)}
                    >
                      {score}
                    </Button>
                  ))}
                </div>
              </section>
            )
          })}
        </div>

        <section aria-labelledby="confidence-title" className="mt-6">
          <h3 id="confidence-title" className="text-sm font-semibold">Confidence</h3>
          <div
            role="group"
            aria-label="Review confidence"
            aria-invalid={completionAttempted && !canComplete}
            className="mt-3 flex flex-wrap gap-2"
          >
            {confidenceOptions.map((option) => {
              const selected = review?.review_confidence === option.value

              return (
                <Button
                  key={option.value}
                  type="button"
                  size="sm"
                  variant={selected ? 'default' : 'outline'}
                  aria-pressed={selected}
                  onClick={() => onConfidenceChange(option.value)}
                >
                  {option.label}
                </Button>
              )
            })}
          </div>
          {completionAttempted && !canComplete && (
            <p role="alert" className="mt-2 text-xs text-destructive">
              Choose a confidence level before completing this review.
            </p>
          )}
        </section>

        <div className="mt-6">
          <label htmlFor="feedback-to-student" className="text-sm font-semibold">
            Feedback to student
          </label>
          <Textarea
            id="feedback-to-student"
            value={review?.feedback_to_student || ''}
            onChange={(event) => onFeedbackChange(event.target.value)}
            placeholder="Write feedback for the student…"
            className="mt-3 min-h-20 resize-y"
          />
        </div>
      </div>

      <footer className="mt-6 flex shrink-0 gap-2">
        <Button
          type="button"
          variant="outline"
          size="sm"
          className="h-9 w-14 px-0"
          disabled={!hasPrevious}
          onClick={onPrevious}
        >
          Prev
        </Button>
        <Button
          type="button"
          variant="default"
          size="sm"
          className="h-9 min-w-0 flex-1 px-2"
          disabled={completed}
          onClick={handleComplete}
        >
          {completed ? 'Completed' : 'Complete'}
        </Button>
        <Button
          type="button"
          variant="outline"
          size="sm"
          className="h-9 w-14 px-0"
          disabled={!hasNext}
          onClick={onNext}
        >
          Next
        </Button>
      </footer>
    </aside>
  )
}
