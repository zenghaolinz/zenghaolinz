# nlin GitHub Profile README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a bilingual GitHub profile README in the approved Field Notes × Creative OS visual direction.

**Architecture:** Use a self-hosted SVG for the editorial hero and semantic Markdown/limited GitHub HTML for all essential content. A small Python unittest suite validates repository links, bilingual sections, accessibility metadata, asset paths, and the absence of third-party dynamic image services.

**Tech Stack:** GitHub Flavored Markdown, SVG 1.1, Python `unittest`, GitHub CLI

---

### Task 1: Create failing profile contract tests

**Files:**
- Create: `tests/test_profile.py`

- [ ] **Step 1: Write tests for required files and content**

```python
def test_profile_contains_bilingual_sections(self):
    readme = self.readme()
    for heading in ("Selected Works / 代表项目", "Interests / 兴趣坐标", "Currently Exploring / 最近在探索"):
        self.assertIn(heading, readme)
```

- [ ] **Step 2: Add tests for the four canonical repository links, local hero asset, SVG accessibility metadata, and forbidden third-party stat image hosts**

- [ ] **Step 3: Run the test suite**

Run: `python -m unittest discover -s tests -v`
Expected: FAIL because `README.md` and `assets/profile-hero.svg` do not exist.

### Task 2: Build the self-hosted editorial hero

**Files:**
- Create: `assets/profile-hero.svg`

- [ ] **Step 1: Create a 1000×360 warm-paper SVG**

The SVG contains `<title>` and `<desc>`, the label `NLIN / FIELD NOTES — BUILD 2026`, the statement `Software as an experimental medium.`, bilingual supporting copy, a restrained conic-like color wheel built from solid arcs, and the four topic labels AI AGENTS, LOCAL MODELS, MINECRAFT MODDING, and MULTIMODAL.

- [ ] **Step 2: Parse the SVG as XML**

Run: `python -c "import xml.etree.ElementTree as E; E.parse('assets/profile-hero.svg')"`
Expected: exit code 0.

### Task 3: Write the bilingual profile README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Add the local hero with descriptive alt text**

```markdown
![nlin — software as an experimental medium](./assets/profile-hero.svg)
```

- [ ] **Step 2: Add a concise bilingual introduction and Selected Works table**

The table links Ultra Studio, Quiz Studio, Minecraft Speed Force Mod, and Canvas Design Studio to their canonical `zenghaolinz` repository URLs and includes verified stacks from their current READMEs.

- [ ] **Step 3: Add Interests, Currently Exploring, Toolbox, and footer sections**

- [ ] **Step 4: Run profile tests**

Run: `python -m unittest discover -s tests -v`
Expected: all tests pass.

### Task 4: Render and visually verify

**Files:**
- Create: `preview/profile.html` only as an ignored/local verification artifact if needed.

- [ ] **Step 1: Render the README with GitHub-compatible Markdown**
- [ ] **Step 2: Inspect desktop and narrow layouts in the in-app browser**
- [ ] **Step 3: Fix broken hierarchy, overflow, contrast, or malformed links and rerun tests**

### Task 5: Publish the profile repository

**Files:**
- Modify: `.gitignore` only if preview artifacts need exclusion.

- [ ] **Step 1: Commit implementation**

```bash
git add README.md assets/profile-hero.svg tests/test_profile.py
git commit -m "feat: create bilingual GitHub profile"
```

- [ ] **Step 2: Create the public `zenghaolinz/zenghaolinz` repository and push `main`**

Run: `gh repo create zenghaolinz --public --source=. --remote=origin --push`
Expected: repository URL `https://github.com/zenghaolinz/zenghaolinz`.

- [ ] **Step 3: Verify the remote branch, rendered profile URL, repository links, and clean local worktree**
