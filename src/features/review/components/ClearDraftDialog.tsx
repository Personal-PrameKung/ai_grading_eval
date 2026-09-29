import { Trash2 } from 'lucide-react'
import {
  AlertDialog,
  AlertDialogClose,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'
import { Button } from '@/components/ui/button'
import { Tooltip, TooltipContent, TooltipTrigger } from '@/components/ui/tooltip'

type ClearDraftDialogProps = {
  disabled: boolean
  onConfirm: () => void
}

export function ClearDraftDialog({ disabled, onConfirm }: ClearDraftDialogProps) {
  return (
    <AlertDialog>
      <Tooltip>
        <TooltipTrigger
          disabled={disabled}
          render={
            <AlertDialogTrigger
              render={
                <Button
                  type="button"
                  variant="destructive"
                  size="icon-sm"
                  className="bg-destructive/20 hover:bg-destructive/30 dark:bg-destructive/25 dark:hover:bg-destructive/35"
                  disabled={disabled}
                  aria-label="Clear progress"
                />
              }
            />
          }
        >
          <Trash2 aria-hidden="true" />
        </TooltipTrigger>
        <TooltipContent side="bottom">Clear progress</TooltipContent>
      </Tooltip>
      <AlertDialogContent>
        <AlertDialogTitle>Clear all review progress?</AlertDialogTitle>
        <AlertDialogDescription>
          This removes every saved score, confidence selection, note, and completion status from this browser.
          Your review will return to the first question. This cannot be undone.
        </AlertDialogDescription>
        <div className="mt-6 flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
          <AlertDialogClose render={<Button type="button" variant="outline" />}>
            Cancel
          </AlertDialogClose>
          <AlertDialogClose render={<Button type="button" variant="destructive" onClick={onConfirm} />}>
            Clear progress
          </AlertDialogClose>
        </div>
      </AlertDialogContent>
    </AlertDialog>
  )
}
