# Project Rules — MAAE 2300 Fluid Mechanics Notes

## Non-Negotiable
1. **No regression**: Never modify fragment files that aren't being actively worked on.
2. **Fragments only**: Edit fragment files, never the built `MAAE2300-notes.html` directly.
3. **Build script**: Always run `build.py` after editing fragments.
4. **Push via script**: Use `scripts/push_to_github.py` to push changes.

## Theme: Arctic Fox
- Light mode. Poppins font.
- All colors defined in `shell-head.html` `:root` block — never hardcode hex in fragments.
- Use CSS variables: `var(--eq)`, `var(--def)`, `var(--tip)`, `var(--deriv)`, `var(--example)`, `var(--unit)`.
- Chapter title colors: `var(--ch1-title)` through `var(--ch6-title)`.

## Content Organization
- Main categories = Textbook chapters (6 total)
- Sub-categories = Individual lecture topics within each chapter
- Each chapter file (`chN-notes.html`) contains all lectures for that chapter as `<h2>` sections
- Lecture anchors: `id="chN-lecM"` for sidebar deep-linking

## Engineering Notes Standards
- Every equation card has variable pills below the formula
- Every equation has "When to use / When NOT to use"
- Full algebraic step-by-step in all solutions
- SVG diagrams for any visual setup (flow diagrams, FBDs, control volumes)
- Tip labels prefixed with ★
- Unit analysis blocks where relevant
