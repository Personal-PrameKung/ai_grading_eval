import { useEffect, useState } from 'react'
import { EvidencePanel } from '@/features/review/components/EvidencePanel'
import { ReviewTopBar } from '@/features/review/components/ReviewTopBar'
import { loadExams, type Exam } from '@/features/review/lib/exam-loader'

function App() {
  const [exams, setExams] = useState<Exam[]>([])
  const [selectedIndex, setSelectedIndex] = useState(0)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let active = true

    loadExams()
      .then((loadedExams) => {
        if (active) setExams(loadedExams)
      })
      .catch((loadError: unknown) => {
        if (!active) return
        setError(loadError instanceof Error ? loadError.message : 'Could not load exam data')
      })
      .finally(() => {
        if (active) setLoading(false)
      })

    return () => {
      active = false
    }
  }, [])

  const selectedExam = exams[selectedIndex]

  return (
    <main className="min-h-screen bg-muted/40 px-4 py-5 sm:px-6 sm:py-8">
      <ReviewTopBar
        exams={exams}
        selectedIndex={selectedIndex}
        onSelectExam={setSelectedIndex}
        loading={loading}
        error={error}
      />
      <div className="mx-auto mt-5 grid w-full max-w-7xl gap-5 md:grid-cols-[minmax(0,1fr)_minmax(15rem,20rem)]">
        {selectedExam ? (
          <EvidencePanel key={selectedExam.review_item_id} exam={selectedExam} />
        ) : (
          <section aria-live="polite" className="rounded-xl border bg-card p-6 shadow-sm">
            <h2 className="text-lg font-semibold">{loading ? 'Loading assignment…' : 'No assignment available'}</h2>
            <p className="mt-2 text-sm text-muted-foreground">
              {error || (loading ? 'Preparing the review content.' : 'There are no assignments to review.')}
            </p>
          </section>
        )}
        <aside aria-hidden="true" className="hidden min-h-[35rem] rounded-xl border bg-card shadow-sm md:block" />
      </div>
    </main>
  )
}

export default App
