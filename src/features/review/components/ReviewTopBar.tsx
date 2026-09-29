import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from '@/components/ui/combobox'
import { ClearDraftDialog } from '@/features/review/components/ClearDraftDialog'
import type { Exam } from '@/features/review/lib/exam-loader'
import { isReviewComplete } from '@/features/review/lib/scoring'
import type { ReviewEntry } from '@/features/review/types'

type ReviewTopBarProps = {
  exams: Exam[]
  reviews: Record<string, ReviewEntry>
  selectedIndex: number
  onSelectExam: (index: number) => void
  onClearProgress: () => void
  loading: boolean
  error: string | null
}

export function ReviewTopBar({
  exams,
  reviews,
  selectedIndex,
  onSelectExam,
  onClearProgress,
  loading,
  error,
}: ReviewTopBarProps) {
  const selectedExam = exams[selectedIndex]
  const examOptions = exams.map((exam, index) => `${index + 1}. ${exam.question_id}`)
  const completedOptions = new Set(
    exams.flatMap((exam, index) => (
      isReviewComplete(exam.criteria, reviews[exam.review_item_id]) ? [examOptions[index]] : []
    )),
  )
  const selectedCompleted = selectedExam && completedOptions.has(examOptions[selectedIndex])

  return (
    <header className="mx-auto flex w-full max-w-7xl flex-col gap-4 rounded-xl border bg-card px-5 py-4 shadow-sm sm:flex-row sm:items-center sm:justify-between sm:gap-6">
      <div className="min-w-0">
        <p className="text-xs font-semibold tracking-[0.16em] text-muted-foreground uppercase">
          Human grading
        </p>
        <h1 className="mt-1 text-xl font-semibold tracking-tight text-foreground">
          Review
        </h1>
      </div>

      <div className="flex min-w-0 flex-col gap-1.5 sm:w-80">
        <label htmlFor="exam-jump" className="text-xs font-medium text-muted-foreground">
          Exam question
        </label>
        <Combobox
          items={examOptions}
          value={selectedExam ? examOptions[selectedIndex] : null}
          disabled={loading || exams.length === 0}
          onValueChange={(value) => {
            if (typeof value !== 'string') return
            const index = examOptions.indexOf(value)
            if (index !== -1) onSelectExam(index)
          }}
        >
          <ComboboxInput
            id="exam-jump"
            className="w-full bg-background"
            placeholder={loading ? 'Loading exams…' : exams.length ? 'Search exam questions…' : 'No exams available'}
          />
          <ComboboxContent>
            <ComboboxEmpty>No matching questions.</ComboboxEmpty>
            <ComboboxList>
              {(item: string) => (
                <ComboboxItem key={item} value={item}>
                  <span className="min-w-0 flex-1 truncate">{item}</span>
                  <span className={completedOptions.has(item)
                    ? 'mr-4 shrink-0 text-xs font-medium text-emerald-700 dark:text-emerald-400'
                    : 'mr-4 shrink-0 text-xs text-muted-foreground'}>
                    {completedOptions.has(item) ? 'Completed' : 'Not completed'}
                  </span>
                </ComboboxItem>
              )}
            </ComboboxList>
          </ComboboxContent>
        </Combobox>
      </div>

      <div className="flex min-h-10 min-w-32 items-center justify-end gap-3 text-right text-sm text-muted-foreground">
        <ClearDraftDialog
          disabled={Object.keys(reviews).length === 0 && selectedIndex === 0}
          onConfirm={onClearProgress}
        />
        {error ? (
          <p role="status" className="text-destructive">{error}</p>
        ) : selectedExam ? (
          <div>
            <p>
              <span className="font-medium text-foreground">{selectedIndex + 1}</span>
              {' '}of {exams.length}
            </p>
            <p className={selectedCompleted
              ? 'text-xs font-medium text-emerald-700 dark:text-emerald-400'
              : 'text-xs text-muted-foreground'}>
              {selectedCompleted ? 'Completed' : 'Not completed'}
            </p>
          </div>
        ) : (
          <p>{loading ? 'Preparing review…' : 'Ready when exams are loaded'}</p>
        )}
      </div>
    </header>
  )
}
