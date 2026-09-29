export type ReviewEntry = Record<string, string>

export type ReviewConfidence = '1' | '2' | '3'

export type PersistedReviewSession = {
  __index?: number
  [reviewItemId: string]: ReviewEntry | number | undefined
}

export type ReviewSession = {
  reviews: Record<string, ReviewEntry>
  currentIndex: number
}
