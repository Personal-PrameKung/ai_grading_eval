export type ReviewEntry = Record<string, string>

export type PersistedReviewSession = {
  __index?: number
  [reviewItemId: string]: ReviewEntry | number | undefined
}

export type ReviewSession = {
  reviews: Record<string, ReviewEntry>
  currentIndex: number
}
