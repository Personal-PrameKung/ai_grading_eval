import { useEffect, useMemo, useRef } from 'react'
import { mathCandidates } from '@/features/review/lib/math'

type KatexRenderer = {
  render: (
    formula: string,
    element: HTMLElement,
    options: { displayMode: boolean; throwOnError: boolean; trust: boolean },
  ) => void
}

declare global {
  interface Window {
    katex?: KatexRenderer
  }
}

export function MathPreview({ text }: { text: string }) {
  const formulas = useMemo(() => mathCandidates(text), [text])
  const elements = useRef<(HTMLDivElement | null)[]>([])

  useEffect(() => {
    formulas.forEach((formula, index) => {
      const element = elements.current[index]
      if (!element) return

      element.replaceChildren()
      try {
        if (window.katex) {
          window.katex.render(formula, element, {
            displayMode: true,
            throwOnError: false,
            trust: false,
          })
        } else {
          element.textContent = formula
        }
      } catch {
        element.textContent = formula
      }
    })
  }, [formulas])

  if (formulas.length === 0) {
    return <p className="text-xs text-muted-foreground">No mathematical expressions found.</p>
  }

  return (
    <div className="space-y-2" aria-label="Rendered mathematical expressions">
      <p className="text-xs font-medium text-muted-foreground">Mathematical expressions</p>
      {formulas.map((formula, index) => (
        <div
          key={`${formula}-${index}`}
          ref={(element) => { elements.current[index] = element }}
          className="overflow-x-auto rounded-md border bg-card px-3 py-2 text-sm"
        />
      ))}
    </div>
  )
}
