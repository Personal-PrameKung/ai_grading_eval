import {
  Combobox,
  ComboboxContent,
  ComboboxEmpty,
  ComboboxInput,
  ComboboxItem,
  ComboboxList,
} from '@/components/ui/combobox'
import type { Exam } from '@/features/review/lib/exam-loader'

type ReviewTopBarProps = {
  exams: Exam[]
  selectedIndex: number
  onSelectExam: (index: number) => void
  loading: boolean
  error: string | null
}

export function ReviewTopBar({
  exams,
  selectedIndex,
  onSelectExam,
  loading,
  error,
}: ReviewTopBarProps) {
  const selectedExam = exams[selectedIndex]
  const examOptions = exams.map((exam, index) => `${index + 1}. ${exam.question_id}`)

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
                  {item}
                </ComboboxItem>
              )}
            </ComboboxList>
          </ComboboxContent>
        </Combobox>
      </div>

      <div className="min-h-10 min-w-32 text-right text-sm text-muted-foreground sm:content-center">
        {error ? (
          <p role="status" className="text-destructive">{error}</p>
        ) : selectedExam ? (
          <p>
            <span className="font-medium text-foreground">{selectedIndex + 1}</span>
            {' '}of {exams.length}
          </p>
        ) : (
          <p>{loading ? 'Preparing review…' : 'Ready when exams are loaded'}</p>
        )}
      </div>
    </header>
  )
}
