import { useState } from 'react'
import { FileText, Image as ImageIcon, Sigma } from 'lucide-react'
import { Button } from '@/components/ui/button'
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import { MathPreview } from '@/features/review/components/MathPreview'
import type { Exam } from '@/features/review/lib/exam-loader'

type EvidencePanelProps = {
  exam: Exam
}

type ImageViewerProps = {
  src: string
  alt: string
}

function ImageViewer({ src, alt }: ImageViewerProps) {
  return (
    <Dialog>
      <DialogTrigger
        render={
          <button
            type="button"
            className="block w-full overflow-hidden rounded-lg border bg-muted/30 outline-none transition hover:border-primary/50 focus-visible:ring-3 focus-visible:ring-ring/50"
            aria-label={`Enlarge ${alt}`}
            title={`Enlarge ${alt}`}
          />
        }
      >
        <img src={src} alt={alt} className="block h-auto w-full" />
      </DialogTrigger>
      <DialogContent className="max-h-[90vh] w-auto max-w-[min(90vw,72rem)] overflow-auto sm:max-w-[min(90vw,72rem)]">
        <DialogTitle className="sr-only">{alt}</DialogTitle>
        <img src={src} alt={alt} className="mx-auto max-h-[80vh] max-w-full object-contain" />
      </DialogContent>
    </Dialog>
  )
}

function TextBlock({
  title,
  text,
  latexToggle = false,
}: {
  title: string
  text: string
  latexToggle?: boolean
}) {
  const [showLatex, setShowLatex] = useState(latexToggle)

  return (
    <section className="min-w-0 rounded-lg border bg-muted/20 p-4 sm:p-5">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h3 className="text-sm font-semibold text-foreground">{title}</h3>
        {latexToggle && (
          <Button
            type="button"
            variant="outline"
            size="sm"
            aria-pressed={showLatex}
            onClick={() => setShowLatex((current) => !current)}
          >
            <Sigma aria-hidden="true" />
            {showLatex ? 'View text' : 'View LaTeX'}
          </Button>
        )}
      </div>
      <p className="mt-3 whitespace-pre-wrap break-words text-sm leading-7 text-foreground/85">
        {text || 'No text provided.'}
      </p>
      {latexToggle && showLatex && (
        <div className="mt-4">
          <MathPreview text={text} />
        </div>
      )}
    </section>
  )
}

function QuestionDisplay({ exam }: { exam: Exam }) {
  const [showText, setShowText] = useState(false)
  const questionImage = `/assets/questions/${exam.question_asset.filename}`

  return (
    <section aria-labelledby="question-image-title">
      <h3 id="question-image-title" className="mb-3 text-sm font-semibold">Question</h3>
      <div className="relative">
        {showText ? (
          <div className="min-h-48 rounded-lg border bg-muted/20 px-4 pb-4 pt-16 sm:px-5">
            <p className="whitespace-pre-wrap break-words text-sm leading-7 text-foreground/85">
              {exam.question_text || 'No question text provided.'}
            </p>
          </div>
        ) : (
          <ImageViewer src={questionImage} alt={`${exam.question_id} question image`} />
        )}
        <Button
          type="button"
          variant="secondary"
          size="sm"
          aria-pressed={showText}
          onClick={() => setShowText((current) => !current)}
          className="absolute right-3 top-3 z-10 border border-border bg-card shadow-sm"
        >
          {showText ? <ImageIcon aria-hidden="true" /> : <FileText aria-hidden="true" />}
          {showText ? 'View image' : 'View as text'}
        </Button>
      </div>
      {exam.question_asset.asset_kind === 'fallback_range' && !showText && (
        <p className="mt-2 text-xs text-muted-foreground">
          This image includes multiple questions. Use the relevant question shown.
        </p>
      )}
    </section>
  )
}

export function EvidencePanel({ exam }: EvidencePanelProps) {
  return (
    <section aria-labelledby="review-question-title" className="min-w-0 rounded-xl border bg-card p-4 shadow-sm sm:p-6">
      <h2 id="review-question-title" className="sr-only">Evidence for {exam.question_id}</h2>

      <div className="space-y-6">
        {exam.context_images.length > 0 && (
          <section aria-labelledby="question-context-title">
            <h3 id="question-context-title" className="mb-3 text-sm font-semibold">
              Question context <span className="font-normal text-muted-foreground">· {exam.context_images[0].label}</span>
            </h3>
            <div className="grid gap-4">
              {exam.context_images.map((image, index) => (
                <figure key={image.filename} className="min-w-0">
                  {index > 0 && (
                    <figcaption className="mb-3 text-sm font-semibold text-muted-foreground">
                      {image.label}
                    </figcaption>
                  )}
                  <ImageViewer
                    src={`/assets/question-groups/${image.filename}`}
                    alt={image.label}
                  />
                </figure>
              ))}
            </div>
          </section>
        )}

        <QuestionDisplay exam={exam} />
        <section aria-labelledby="grading-title">
          <h3 id="grading-title" className="mb-3 text-sm font-semibold">Grading</h3>
          <div className="grid min-w-0 gap-4 lg:grid-cols-2">
            <TextBlock title="Reference solution" text={exam.canonical_solution} latexToggle />
            <TextBlock title="Student response" text={exam.answer_text} latexToggle />
          </div>
        </section>
        <TextBlock title="Scoring guide" text={exam.rubric_scoring_guide} />
      </div>
    </section>
  )
}
