import { useEffect, useState } from 'react'
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

  return (
    <main className="min-h-screen bg-muted/40 px-4 py-5 sm:px-6 sm:py-8">
      <ReviewTopBar
        exams={exams}
        selectedIndex={selectedIndex}
        onSelectExam={setSelectedIndex}
        loading={loading}
        error={error}
      />
    </main>
  )
}

export default App
