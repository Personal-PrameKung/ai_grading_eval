# Repository Guidelines

## Product and Rebuild Scope

This repository contains a React 19, TypeScript, and Vite application for human review of grading assignments. The new frontend must keep the existing framework and review behavior while adopting Tailwind CSS, shadcn/ui, and Lucide icons.

Preserve these behaviors during the rebuild:

- Load and sort assignments from `public/data/assignments.json`.
- Review one assignment at a time and jump directly to another item.
- Display question crops, grouped context images, question text, reference solutions, student responses, rubrics, and rendered mathematical expressions.
- Record criterion scores, confidence, status, and reconciliation notes.
- Calculate totals and completion progress from the rubric data.
- Autosave review state and the current item in `localStorage`.
- Support Previous/Next buttons and Left/Right keyboard navigation when the user is not editing a field.
- Enlarge question images in an accessible dialog.
- Export the completed dataset as CSV and clear saved work only after confirmation.
- Support persistent light and dark themes, using the system preference for first-time visitors.

Do not change the assignment schema, asset paths, storage key, completion rules, or CSV columns without an explicit requirement.

## Target Architecture

Keep `src/App.tsx` as a small composition root. Organize implementation by responsibility:

```text
src/
  components/
    ui/                    # shadcn/ui primitives only
  features/
    review/
      components/          # review-specific presentation components
      hooks/               # session, persistence, keyboard, and theme hooks
      lib/                 # pure scoring, sorting, CSV, and math helpers
      types.ts             # assignment and review domain types
  lib/
    utils.ts               # shared helpers such as cn()
  App.tsx
  index.css                # Tailwind import, tokens, and minimal global styles
  main.tsx
```

Recommended review components include `ReviewHeader`, `ProgressSummary`, `EvidencePanel`, `TextPanel`, `MathPreview`, `ScoringPanel`, `CriterionScore`, `ImageViewerDialog`, and `ClearDraftDialog`. Split by clear ownership rather than making a separate file for every small element.

Stateful hooks may coordinate browser behavior, but scoring, sorting, completion checks, math extraction, and CSV serialization must remain pure functions. Keep the dataset immutable after loading. Derive totals and completion instead of storing duplicate values in React state.

## UI System

- Use Tailwind CSS utilities for layout, spacing, typography, responsive behavior, and visual states.
- Keep design tokens and theme colors in `src/index.css` using Tailwind v4 conventions and CSS variables.
- Do not recreate a large global stylesheet or add component-specific selectors when utilities and variants are sufficient.
- Use `cn()` when classes are conditional or composed by a reusable component.
- Use shadcn/ui primitives for common interactive surfaces such as buttons, selects, dialogs, alert dialogs, badges, progress, textareas, tooltips, and skeletons.
- Add shadcn components through the configured CLI when practical. Keep generated primitives in `src/components/ui/`; put product-specific composition elsewhere.
- Use Lucide React for interface icons. Import icons individually, include visible text or an accessible name, and mark decorative icons with `aria-hidden="true"`.
- Do not add a second component library, icon set, CSS-in-JS system, or state-management package unless the requirement clearly justifies it.
- Preserve the calm, focused review experience. The evidence and scoring workflow should dominate; export, theme, and destructive actions should remain secondary.

## Data and Domain Rules

`public/data/assignments.json` is the source dataset. Question crops live in `public/assets/questions/`, while grouped context images live in `public/assets/question-groups/`. `public/vendor/katex/` is vendored third-party code and must not be hand-edited.

Define explicit types for `Assignment`, `Criterion`, `QuestionAsset`, `ContextImage`, `ReviewEntry`, and persisted session data. Avoid `any`, unsafe casts, and UI code that reaches into unknown JSON without validation or normalization.

An item is complete only when every non-blank criterion has a score, confidence is selected, and its status is `completed`. Scores of `0` are valid and must not be treated as missing. Preserve timestamps when editing an existing review and set completion time only when status becomes completed.

CSV values must be safely quoted, including quotes, commas, newlines, arrays, and objects. Keep browser-only download code separate from the pure CSV serializer.

## Accessibility and Responsive Behavior

- Use semantic landmarks, headings, labels, and native controls where possible.
- Every icon-only action needs an `aria-label` and a tooltip or title.
- Maintain visible keyboard focus, sufficient contrast, and logical tab order in both themes.
- Dialogs must trap focus, close with Escape, restore focus, and provide an accessible title.
- Do not trigger item navigation while focus is in an input, textarea, select, or other editable element.
- Respect `prefers-reduced-motion`; motion should clarify state rather than decorate it.
- Keep the scoring panel easy to reach on small screens. Avoid layouts that require horizontal page scrolling at 320px width.

## Coding Conventions

Follow the established TypeScript style: two-space indentation, single quotes, no semicolons, and trailing commas in multiline constructs. Use `PascalCase` for components and types and `camelCase` for functions, hooks, and variables.

Keep components focused and props explicit. Prefer early returns and named helpers over deeply nested JSX. Do not suppress ESLint or TypeScript errors unless a narrow comment explains a genuine external limitation. Avoid premature memoization; use it only when a measured or structurally clear benefit exists.

Use the `@/` alias for source imports. Import types with `import type`. Keep shadcn/ui primitives generic and free from review-domain knowledge.

## Commands and Validation

Install the locked dependency set with `npm ci`.

- `npm run dev` starts the Vite development server.
- `npm run lint` runs ESLint.
- `npm run build` runs TypeScript project checks and creates the production bundle.
- `npm run preview` serves the production build locally.

There is currently no automated test command. Before handing off a change, run `npm run lint` and `npm run build`. Manually verify any affected workflow, including:

1. Initial loading and failure states.
2. Item selection and keyboard navigation.
3. Scoring, zero scores, totals, confidence, status, and completion progress.
4. Autosave and restoration after a page refresh.
5. Theme persistence and system-theme fallback.
6. Question and context image enlargement.
7. CSV content and escaping.
8. Clear-draft confirmation.
9. Layout and keyboard access at desktop and mobile widths.

If tests are introduced, colocate them with the review feature using `*.test.ts` or `*.test.tsx`. Prioritize pure data helpers, persistence migration, score calculation, completion rules, and CSV serialization before snapshot tests.

## Change Discipline

Refactor incrementally and keep the application usable between steps. Preserve user data when changing persisted-state structure by adding a migration or backward-compatible reader. Do not edit generated `dist/` output, vendored KaTeX assets, or the review dataset unless the task explicitly requires it.

Keep commits focused and use short imperative summaries, such as `Restructure review workspace`. Pull requests should describe user-visible changes, architectural changes, validation performed, and any data or asset updates. Include screenshots for visual changes.
