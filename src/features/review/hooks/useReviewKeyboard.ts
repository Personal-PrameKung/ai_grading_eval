import { useEffect } from 'react'

const interactiveSelector = 'input, textarea, select, [contenteditable], [role="combobox"], [role="listbox"], [role="dialog"]'

export function useReviewKeyboard(
  selectedIndex: number,
  itemCount: number,
  onSelectItem: (index: number) => void,
) {
  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (
        event.defaultPrevented
        || event.altKey
        || event.ctrlKey
        || event.metaKey
        || event.shiftKey
        || (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight')
      ) return

      const target = event.target
      if (target instanceof HTMLElement && target.closest(interactiveSelector)) return

      const nextIndex = event.key === 'ArrowLeft'
        ? Math.max(0, selectedIndex - 1)
        : Math.min(itemCount - 1, selectedIndex + 1)

      if (nextIndex === selectedIndex || nextIndex < 0) return
      event.preventDefault()
      onSelectItem(nextIndex)
    }

    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [selectedIndex, itemCount, onSelectItem])
}
