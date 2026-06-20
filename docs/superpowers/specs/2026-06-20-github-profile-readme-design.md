# nlin GitHub Profile README Design

## Purpose

Create a bilingual GitHub profile README for `zenghaolinz` that presents nlin
as a curious software builder working across AI agents, local models, creative
tools, and game mechanics. The profile should feel personal and mature rather
than like a badge collection or generic developer template.

## Visual Direction

Use the approved **Field Notes × Creative OS** direction:

- Editorial field-notebook structure on a warm paper background.
- One restrained multicolor visual anchor in the hero banner.
- Serif-led typography rendered inside a repository-owned SVG banner.
- Numbered project entries and small technical labels inspired by a personal
  workspace or operating system.
- Stable Markdown and simple HTML tables below the banner so the page remains
  legible in GitHub light and dark themes.

The design must not depend on third-party GitHub statistics, contribution
streak images, visitor counters, typing services, or remote badge generators.

## Content Structure

1. **Hero banner**
   - `NLIN / FIELD NOTES — BUILD 2026`
   - “Software as an experimental medium.”
   - A short English and Chinese introduction.
2. **Selected Works / 代表项目**
   - Ultra Studio — agent conversations, memory, images, and 3D workflows.
   - Quiz Studio — local-first question bank, OCR, AI explanations, and grading.
   - Speed Force Mod — NeoForge gameplay mechanics and time-system experiments.
   - Canvas Design Studio — local creative AI built around ComfyUI.
3. **Interests / 兴趣坐标**
   - AI Agents, Local LLMs, Open Source, Minecraft Modding, Game Development,
     Multimodal AI, Creative Software, and Biology.
4. **Currently Exploring / 最近在探索**
   - Consumer-hardware model inference.
   - More reliable agent behavior.
   - Minecraft mechanics.
   - Lightweight desktop AI applications.
5. **Toolbox / 技术栈**
   - C/C++, Python, JavaScript/TypeScript, Rust, and Java.
6. **Footer**
   - Link to `github.com/zenghaolinz` and the line “ideas → systems → tools”.

## Repository Data

All project links and descriptions are grounded in the current public GitHub
repositories. `CanvasDesignStudio` is presented publicly as “Canvas Design
Studio”, matching its repository README rather than inventing a separate repo.

## Files

- `README.md`: the complete bilingual profile page.
- `assets/profile-hero.svg`: self-hosted editorial hero artwork.
- `assets/project-*.svg`: optional self-hosted compact project labels only when
  they improve hierarchy; no decorative asset is required without a purpose.

## Accessibility and Compatibility

- The SVG includes accessible title and description metadata.
- Text essential to navigation and project understanding remains in Markdown,
  not only inside images.
- Every image has useful alt text.
- Layout must remain readable on narrow screens; two-column HTML tables may
  stack conceptually but must not contain tiny body copy.
- Links use canonical GitHub repository URLs.

## Acceptance Criteria

- The profile is bilingual without duplicating every paragraph mechanically.
- All four featured projects link to real public repositories.
- The result is visually recognizable as the approved hybrid direction.
- No third-party runtime image service is required.
- Markdown and SVG render without broken links or malformed HTML.
