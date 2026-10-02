import { Download } from 'lucide-react'
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

type ExportCsvDialogProps = {
  count: number
  onConfirm: () => void
}

export function ExportCsvDialog({ count, onConfirm }: ExportCsvDialogProps) {
  const disabled = count === 0

  return (
    <AlertDialog>
      <Tooltip>
        <TooltipTrigger
          disabled={disabled}
          render={
            <AlertDialogTrigger
              render={<Button type="button" variant="outline" size="sm" disabled={disabled} />}
            />
          }
        >
          <Download aria-hidden="true" />
          Export CSV
        </TooltipTrigger>
        <TooltipContent side="bottom">Download review data as CSV</TooltipContent>
      </Tooltip>
      <AlertDialogContent>
        <AlertDialogTitle>Export review data?</AlertDialogTitle>
        <AlertDialogDescription>
          Download all {count} questions as a CSV file. Saved scores and completed reviews will be included;
          unfinished questions will remain pending.
        </AlertDialogDescription>
        <div className="mt-6 flex flex-col-reverse gap-2 sm:flex-row sm:justify-end">
          <AlertDialogClose render={<Button type="button" variant="outline" />}>
            Cancel
          </AlertDialogClose>
          <AlertDialogClose render={<Button type="button" onClick={onConfirm} />}>
            Export CSV
          </AlertDialogClose>
        </div>
      </AlertDialogContent>
    </AlertDialog>
  )
}
