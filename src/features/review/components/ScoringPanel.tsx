import { Button } from '@/components/ui/button'
import type { Exam } from '@/features/review/lib/exam-loader'
import { criterionScore, maximumScore, scoreTotal } from '@/features/review/lib/scoring'
import type { ReviewEntry } from '@/features/review/types'

type ScoringPanelProps = {
  exam: Exam
  review: ReviewEntry | undefined
  onScoreChange: (criterionId: string, score: number) => void
}

export function ScoringPanel({ exam, review, onScoreChange }: ScoringPanelProps) {
  const total = scoreTotal(exam.criteria, review)
  const maximum = maximumScore(exam.criteria)

  return (
    <aside aria-labelledby="scoring-title" className="min-w-0 self-start rounded-xl border bg-card p-4 shadow-sm sm:p-6">
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
    </aside>
  )
}
