# Reveal.js Presentation — AI Prompt Instructions

> **Purpose:** This document is a complete instruction set for an AI assistant generating Reveal.js HTML presentations. Follow every rule here. These instructions come from real mistakes and iterations — they exist for a reason. Do not skip or simplify them.

---

## TABLE OF CONTENTS

1. [Golden Rules (Read First)](#1-golden-rules-read-first)
2. [Project Setup & Boilerplate](#2-project-setup--boilerplate)
3. [Layout Architecture — The Div Box System](#3-layout-architecture--the-div-box-system)
4. [CSS Layout — Flexbox & Grid](#4-css-layout--flexbox--grid)
5. [Preventing Content Overflow](#5-preventing-content-overflow)
6. [Images — Sizing, Placement & Behavior](#6-images--sizing-placement--behavior)
7. [HTML Semantics — Use Proper Tags](#7-html-semantics--use-proper-tags)
8. [CSS Naming Conventions](#8-css-naming-conventions)
9. [Typography & Colors](#9-typography--colors)
10. [Reveal.js Configuration & Features](#10-revealjs-configuration--features)
11. [Animations & Fragments](#11-animations--fragments)
12. [Slide Navigation — Horizontal & Vertical](#12-slide-navigation--horizontal--vertical)
13. [Progress Bar, Controls & UI](#13-progress-bar-controls--ui)
14. [Speaker Notes](#14-speaker-notes)
15. [Plugins](#15-plugins)
16. [Common Mistakes — Do NOT Repeat These](#16-common-mistakes--do-not-repeat-these)
17. [Complete Slide Template](#17-complete-slide-template)
18. [Checklist Before Delivering](#18-checklist-before-delivering)

---

## 1. Golden Rules (Read First)

These are the most important rules. Violating any one of them will produce a broken presentation.

| # | Rule |
|---|------|
| 1 | **Everything must fit on ONE screen.** No scrolling. No overflow. Every slide must be fully visible within the Reveal.js viewport without any content being cut off or pushed below the visible area. |
| 2 | **Text beside images, NOT above/below.** Default layout is two-column: text on the left, image on the right. Never stack an image above a text block vertically unless the slide is a title/closing slide with no body content. |
| 3 | **Break everything into div boxes.** Every logical section of a slide is a `<div>`. Heading area = one div. Content area = another div. Inside content: text-column div + image-column div. |
| 4 | **Use semantic HTML tags INSIDE divs.** Divs are for layout. Content inside divs must use `<h1>`–`<h4>`, `<p>`, `<ul>`, `<ol>`, `<li>`, `<em>`, `<strong>`, `<blockquote>`, etc. Never use a bare `<div>` with raw text when a semantic tag exists. |
| 5 | **Test every slide mentally.** Before writing a slide, mentally calculate: heading height (~60px) + content height. If it exceeds ~620px (viewport minus margins), split into vertical sub-slides. |
| 6 | **NO fragments by default.** Do NOT add `class="fragment"` to bullet points or any elements. All slide content must appear immediately when the slide is navigated to. Fragments force the user to click multiple times per slide which is annoying. Only use fragments if the user explicitly requests step-by-step reveal for specific slides. |

---

## 2. Project Setup & Boilerplate

### CDN Links (Reveal.js 4.3.1)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Presentation Title</title>

  <!-- Reveal.js Core CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reset.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css" />

  <!-- Theme (pick ONE): night, moon, black, white, league, beige, sky, solarized, serif, simple, blood -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/night.min.css" />

  <!-- Google Fonts (optional but recommended) -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />

  <style>
    /* Custom CSS goes here — see sections below */
  </style>
</head>
<body>
  <div class="reveal">
    <div class="slides">

      <!-- ALL <section> slides go here -->

    </div>
  </div>

  <!-- Reveal.js Core JS -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>

  <!-- Plugins (load only what you need) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/notes/notes.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/markdown/markdown.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/highlight/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/math/math.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/zoom/zoom.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/search/search.min.js"></script>

  <script>
    Reveal.initialize({
      // See Section 10 for full config
    });
  </script>
</body>
</html>
```

---

## 3. Layout Architecture — The Div Box System

This is the **most critical** section. Every slide must follow this box model.

### 3.1 Mental Model

Think of every slide as a stack of boxes:

```
┌─────────────────────────────────────────┐
│  <section>  (the slide itself)          │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  HEADING BOX                    │    │
│  │  <h2>Slide Title</h2>          │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  CONTENT BOX  (.row)            │    │
│  │                                 │    │
│  │  ┌──────────┐  ┌────────────┐  │    │
│  │  │ TEXT COL  │  │ IMAGE COL  │  │    │
│  │  │.col-text  │  │ .col-img   │  │    │
│  │  │           │  │            │  │    │
│  │  │  <h3>     │  │  <img>     │  │    │
│  │  │  <ul>     │  │            │  │    │
│  │  │   <li>    │  │            │  │    │
│  │  │  </ul>    │  │            │  │    │
│  │  │           │  │            │  │    │
│  │  └──────────┘  └────────────┘  │    │
│  └─────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

### 3.2 Standard Content Slide HTML Structure

```html
<section>
  <!-- HEADING BOX -->
  <h2>Slide Title Here</h2>

  <!-- CONTENT BOX — always a .row for two-column -->
  <div class="row">

    <!-- TEXT COLUMN (left side) -->
    <div class="col-text">
      <h3>Sub-heading</h3>
      <ul>
        <li>Point one with <strong>emphasis</strong></li>
        <li>Point two with <em>italic term</em></li>
      </ul>

      <!-- Optional: callout box INSIDE the text column -->
      <div class="callout-box">
        <strong>Key Insight:</strong> Important takeaway here
      </div>
    </div>

    <!-- IMAGE COLUMN (right side) -->
    <div class="col-img">
      <img src="image-url.jpg" alt="Descriptive alt text" />
    </div>

  </div>
</section>
```

### 3.3 Rules for the Box System

1. **`<section>`** = the slide. Never put layout CSS directly on `<section>`. It's managed by Reveal.js.
2. **Heading** (`<h2>`) goes directly inside `<section>`, BEFORE the `.row` div.
3. **`.row`** = the flex container. It holds exactly 2 children: `.col-text` and `.col-img`.
4. **`.col-text`** = left column. Contains ALL text: `<h3>`, `<p>`, `<ul>`, callout boxes, etc.
5. **`.col-img`** = right column. Contains ONLY the `<img>` tag.
6. **Sub-sections within `.col-text`**: If you have multiple topics, use `<h3>` + `<ul>` blocks. Optionally separate them with an `<hr class="divider">`.
7. **Callout/practice boxes** go INSIDE `.col-text`, not outside the `.row`.

### 3.4 Variant Layouts

#### Full-width text (no image) — for takeaways/summary slides
```html
<section>
  <h2>Key Takeaways</h2>
  <div class="content-wrap">
    <ul>
      <li><strong>Point 1</strong> — explanation</li>
      <li><strong>Point 2</strong> — explanation</li>
    </ul>
  </div>
</section>
```

#### Title slide (centered, no columns)
```html
<section class="title-slide" data-background-image="url" data-background-opacity="0.3">
  <h1>Main Title</h1>
  <h3>Subtitle</h3>
  <div class="meta">
    <p>Course info</p>
    <p>Presenters</p>
    <p>Date</p>
  </div>
</section>
```

#### Full-background text overlay (no image column)
```html
<section data-background-image="url" data-background-opacity="0.15">
  <h2>Topic Title</h2>
  <div style="text-align:left; max-width:88%; margin:0 auto;">
    <h3>Section A</h3>
    <ul>
      <li>Point</li>
    </ul>
    <h3>Section B</h3>
    <ul>
      <li>Point</li>
    </ul>
  </div>
</section>
```

---

## 4. CSS Layout — Flexbox & Grid

### 4.1 The Core Flex Layout (REQUIRED)

```css
/* Two-column row — the backbone of every content slide */
.row {
  display: flex !important;   /* !important overrides Reveal.js defaults */
  align-items: center;        /* Vertically center text and image */
  gap: 1.6em;                 /* Space between columns */
  width: 100%;
  text-align: left;
}

.row .col-text {
  flex: 1 1 55%;    /* Takes 55% of width, can grow/shrink */
  min-width: 0;     /* Prevents flex item overflow */
}

.row .col-img {
  flex: 0 0 38%;    /* Fixed 38% width, does not grow/shrink */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Modifier: wider image column when image needs more space */
.row .col-img.wide {
  flex: 0 0 46%;
}
```

### 4.2 Why `!important` on `.row`

Reveal.js forces `display: block` and centering on `<section>` children. Without `!important`, your flex layout will be overridden. This is the ONE place `!important` is acceptable.

### 4.3 When to Use Grid Instead

Use CSS Grid for:
- **Image galleries** (2×2, 3×2 grids of thumbnails)
- **Stat dashboards** (multiple equal-sized stat cards)
- **Timeline layouts** (left column for dates, right for descriptions)

```css
/* Example: 2×2 image grid */
.image-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8em;
}
.image-grid img {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  border-radius: 6px;
}
```

### 4.4 Centering Cheat Sheet

| What to Center | Method |
|----------------|--------|
| Text horizontally | `text-align: center` |
| A block element horizontally | `margin: 0 auto` + set `max-width` |
| Flex children vertically | `align-items: center` on parent |
| Flex children horizontally | `justify-content: center` on parent |
| Single element dead-center | `display:flex; justify-content:center; align-items:center;` on parent |
| Absolute element dead-center | `position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)` |

---

## 5. Preventing Content Overflow

**This is the #1 most common mistake. Follow every rule here.**

### 5.1 Reveal.js Viewport

Reveal.js creates a virtual viewport. Content outside it is **invisible** — it doesn't scroll, it just disappears.

```js
Reveal.initialize({
  width: 1100,    // Virtual width in pixels
  height: 700,    // Virtual height in pixels
  margin: 0.07,   // 7% margin around slides
});
```

**Usable space:** ~1020px wide × ~610px tall (after margins).

### 5.2 Space Budget Per Slide

| Element | Approximate Height |
|---------|-------------------|
| `<h2>` heading | 50–70px |
| `<h3>` sub-heading | 25–35px |
| `<li>` bullet item | 28–35px |
| `<hr class="divider">` | 15px |
| Callout box | 45–60px |
| **TOTAL AVAILABLE** | **~610px** |

**Rule of thumb:** A slide with an `<h2>` + image can fit **6–8 bullet points** maximum. If you have more, split into vertical sub-slides.

### 5.3 Font Size Limits

```css
:root {
  --r-main-font-size: 20px;  /* Minimum: 18px, Maximum: 24px */
}
.reveal h2  { font-size: 1.4em; }   /* ~28–34px */
.reveal h3  { font-size: 0.95em; }  /* ~19–23px */
.reveal li  { font-size: 0.85em; }  /* ~17–20px */
```

**NEVER** set base font above 24px for content-heavy slides. If the user provides content text, you need to respect it by making it fit — not by truncating.

### 5.4 Image Size Limits

```css
.row .col-img img {
  max-width: 100%;
  max-height: 320px;    /* HARD CAP — never exceed this */
  object-fit: cover;    /* Crop gracefully instead of distorting */
}
```

### 5.5 The Overflow Test

For every slide, ask:
1. How many lines of text? (count `<li>`, `<p>`, `<h3>` items)
2. Each line ≈ 30px. Total text height = lines × 30.
3. Add heading height (~60px).
4. Is total < 610px? ✅ Ship it. ❌ Split into sub-slides.

---

## 6. Images — Sizing, Placement & Behavior

### 6.1 Rules

1. Images go in `.col-img` div, NEVER floating loose inside `<section>`.
2. Always set `alt` text on every `<img>`.
3. Always constrain with `max-height` (not just `max-width`).
4. Use `object-fit: cover` to prevent distortion.
5. Remove default Reveal.js image borders:

```css
.reveal section img {
  border: none;
  border-radius: 8px;
  box-shadow: 0 6px 24px rgba(0,0,0,0.5);
  margin: 0;    /* Reveal.js adds default margin — remove it */
}
```

### 6.2 Background Images

For atmospheric/full-bleed images, use Reveal.js data attributes instead of `<img>`:

```html
<section data-background-image="https://example.com/photo.jpg"
         data-background-opacity="0.15"
         data-background-size="cover"
         data-background-position="center">
  <!-- slide content here — text overlays the background -->
</section>
```

- `data-background-opacity`: 0.1–0.25 for text readability. Never above 0.3.
- Use this for title slides, closing slides, and accent slides where the image is mood-setting, not informational.

### 6.3 Image Column Width

| Scenario | Class | CSS |
|----------|-------|-----|
| Standard (text-heavy slide) | `.col-img` | `flex: 0 0 38%` |
| Image is a chart/diagram | `.col-img.wide` | `flex: 0 0 46%` |
| Small decorative image | `.col-img.narrow` | `flex: 0 0 28%` |

---

## 7. HTML Semantics — Use Proper Tags

**Divs are for LAYOUT. Semantic tags are for CONTENT.**

### 7.1 Required Tag Usage

| Content Type | Tag | WRONG |
|-------------|-----|-------|
| Slide main title | `<h2>` | `<div class="title">` |
| Sub-section heading | `<h3>` | `<div class="subtitle">` |
| Bullet list | `<ul><li>` | `<div>• text</div>` |
| Numbered list | `<ol><li>` | `<div>1. text</div>` |
| Paragraph text | `<p>` | `<div>text</div>` |
| Emphasis/term | `<em>` | `<span class="italic">` |
| Strong/keyword | `<strong>` | `<span class="bold">` |
| Thematic break | `<hr>` | `<div class="line">` |
| Quote/citation | `<blockquote>` | `<div class="quote">` |

### 7.2 Heading Hierarchy Per Slide

```
<section>
  <h2>  ← Main slide title (ONE per slide, ALWAYS present)
    <h3>  ← Sub-section headings (inside .col-text)
      <h4>  ← Rare: sub-sub-heading (avoid if possible)
```

- `<h1>` is reserved for the **title slide** and **thank-you slide** ONLY.
- Every content slide MUST have exactly one `<h2>`.
- Do NOT use `<h3>` as the main slide heading — the styling (color, border, size) is different and it will look inconsistent.

---

## 8. CSS Naming Conventions

### 8.1 Class Naming Rules

Use **descriptive, purpose-based** names. Format: `component-modifier`.

| Purpose | Good Name | Bad Name |
|---------|-----------|----------|
| Two-column container | `.row` | `.div1`, `.container` |
| Text column | `.col-text` | `.left`, `.div-left` |
| Image column | `.col-img` | `.right`, `.pic` |
| Wider image variant | `.col-img.wide` | `.col-img-2`, `.bigger` |
| Practice/tip callout | `.practice-box` | `.box1`, `.special` |
| Comparison callout | `.contrast-box` | `.box2`, `.other` |
| Title slide | `.title-slide` | `.slide1`, `.first` |
| Thank-you slide | `.thankyou-slide` | `.last-slide`, `.end` |
| Utility: small text | `.small` | `.s`, `.mini` |
| Utility: accent color | `.cream` | `.c1`, `.color2` |
| Section divider | `.divider` | `.line`, `.hr1` |

### 8.2 ID Usage

- IDs are for **unique one-off elements** only (e.g., a special kanji character `#kanji-big`).
- Never use IDs for reusable patterns. Use classes.

### 8.3 Comments in HTML

Label every slide with a block comment:

```html
<!-- ═══════ SLIDE 3 — TOPIC NAME ═══════ -->
<section>
```

---

## 9. Typography & Colors

### 9.1 Font Setup

```css
:root {
  --r-main-font: "Inter", "Noto Sans JP", Helvetica, sans-serif;
  --r-heading-font: "Inter", "Noto Sans JP", Helvetica, sans-serif;
}
```

- Always include a **fallback stack**: custom → system sans → generic.
- If the presentation includes non-Latin scripts (Japanese, Arabic, etc.), add a dedicated font family like `Noto Sans JP`.

### 9.2 Color Palette Pattern

Define a consistent palette with exactly these roles:

```css
:root {
  --color-primary: #f0b247;    /* Headings, links, accents */
  --color-bg: #1a1a2e;         /* Slide background */
  --color-accent: #e8dcc4;     /* Sub-headings, emphasis, markers */
  --color-text: #ffffff;       /* Body text */
  --color-text-secondary: #999;/* Footnotes, metadata */
}
```

Apply consistently:
- `<h1>`, `<h2>`: `--color-primary`
- `<h3>`: `--color-accent`
- `<strong>`, `<em>`, `li::marker`: `--color-accent`
- Body text, `<li>`: `--color-text`

---

## 10. Reveal.js Configuration & Features

### 10.1 Full Configuration Reference

```js
Reveal.initialize({
  // ─── Viewport ───
  width: 1100,           // Presentation width (px)
  height: 700,           // Presentation height (px)
  margin: 0.07,          // Margin around slides (0.0 – 0.5)
  minScale: 0.2,         // Minimum scale factor
  maxScale: 2.0,         // Maximum scale factor
  center: true,          // Vertically center slide content

  // ─── Navigation ───
  hash: true,            // Enable #/slide-number in URL
  history: false,        // Push slide changes to browser history
  keyboard: true,        // Enable keyboard navigation
  touch: true,           // Enable touch navigation
  loop: false,           // Loop back to first slide after last
  rtl: false,            // Right-to-left mode
  navigationMode: 'default',  // 'default' | 'linear' | 'grid'
  shuffle: false,        // Randomize slide order

  // ─── Behavior ───
  embedded: false,       // True if embedding in another page
  help: true,            // Show help overlay on ?
  pause: true,           // Allow pausing with 'b' or '.'
  showNotes: false,      // Show speaker notes to audience
  autoPlayMedia: null,   // null = only autoplay with data-autoplay
  preloadIframes: null,  // null = only preload with data-preload
  autoAnimate: true,     // Enable auto-animation
  autoAnimateEasing: 'ease',
  autoAnimateDuration: 1.0,

  // ─── Appearance ───
  transition: 'slide',         // 'none' | 'fade' | 'slide' | 'convex' | 'concave' | 'zoom'
  transitionSpeed: 'default',  // 'default' | 'fast' | 'slow'
  backgroundTransition: 'fade', // Background image transition

  // ─── Progress & Controls ───
  controls: true,              // Show arrow navigation controls
  controlsLayout: 'bottom-right',  // 'bottom-right' | 'edges'
  controlsBackArrows: 'faded',     // 'faded' | 'hidden' | 'visible'
  progress: true,              // Show progress bar at bottom
  slideNumber: false,          // false | true | 'h.v' | 'h/v' | 'c' | 'c/t'
  showSlideNumber: 'all',      // 'all' | 'speaker' | 'print'
  hashOneBasedIndex: false,    // Use 1-based index in URL hash
  respondToHashChanges: true,  // Update presentation on hash change

  // ─── Plugins ───
  plugins: [
    RevealNotes,       // Speaker notes (press 'S')
    // RevealMarkdown,  // Write slides in Markdown
    // RevealHighlight, // Code syntax highlighting
    // RevealMath,      // LaTeX math rendering
    // RevealZoom,      // Alt+click to zoom in
    // RevealSearch,    // Ctrl+Shift+F to search
  ],
});
```

### 10.2 Recommended Minimal Config

```js
Reveal.initialize({
  width: 1100,
  height: 700,
  margin: 0.07,
  center: true,
  hash: true,
  transition: 'slide',
  transitionSpeed: 'default',
  backgroundTransition: 'fade',
  controls: true,
  controlsLayout: 'bottom-right',
  controlsBackArrows: 'faded',
  progress: true,
  slideNumber: 'c/t',      // Shows "3/14" in corner
  plugins: [RevealNotes],
});
```

---

## 11. Animations & Fragments

> **⚠️ CRITICAL: Do NOT use fragments by default.** Fragments (`class="fragment"`) force the user to click/press arrow keys multiple times on a single slide to reveal each element one by one. This is extremely annoying for most presentations. All slide content must be fully visible the moment the slide appears.

### 11.1 Default Behavior: NO Fragments

All `<li>`, `<p>`, `<h3>`, `<div>`, and other elements should render immediately:

```html
<!-- ✅ CORRECT — everything visible on arrival -->
<ul>
  <li>Point one</li>
  <li>Point two</li>
  <li>Point three</li>
</ul>
```

```html
<!-- ❌ WRONG — requires 3 clicks to see all content -->
<ul>
  <li class="fragment fade-in">Point one</li>
  <li class="fragment fade-in">Point two</li>
  <li class="fragment fade-in">Point three</li>
</ul>
```

### 11.2 When Fragments ARE Allowed

Only add fragments if the user **explicitly asks** for step-by-step reveal (e.g., "I want bullet points to appear one at a time"). In that case, here are the available styles:

```html
<p class="fragment fade-in">Fades in (default)</p>
<p class="fragment fade-up">Slides up while fading in</p>
<p class="fragment fade-down">Slides down while fading in</p>
<p class="fragment highlight-red">Text turns red</p>
<p class="fragment highlight-blue">Text turns blue</p>
<p class="fragment grow">Grows slightly</p>
<p class="fragment shrink">Shrinks slightly</p>
<p class="fragment strike">Gets strikethrough</p>
```

Control order with `data-fragment-index`:

```html
<p class="fragment" data-fragment-index="2">I appear second</p>
<p class="fragment" data-fragment-index="1">I appear first</p>
```

### 11.5 Auto-Animate (Smooth Transitions Between Slides)

Add `data-auto-animate` to consecutive `<section>` tags. Reveal.js will automatically animate matching elements between them:

```html
<section data-auto-animate>
  <h2>Step One</h2>
  <div data-id="box" style="background: red; width: 100px; height: 100px;"></div>
</section>

<section data-auto-animate>
  <h2>Step Two</h2>
  <div data-id="box" style="background: blue; width: 300px; height: 100px;"></div>
</section>
```

- Elements are matched by `data-id` attribute.
- Works on any CSS property: position, size, color, opacity, transform.
- Headings with the same text auto-match without needing `data-id`.

### 11.6 Per-Slide Transitions

Override the global transition on a single slide:

```html
<section data-transition="zoom">
  <h2>This slide zooms in</h2>
</section>

<section data-transition="fade-in slide-out">
  <h2>Fades in, slides out</h2>
</section>

<section data-transition-speed="fast">
  <h2>Fast transition</h2>
</section>
```

---

## 12. Slide Navigation — Horizontal & Vertical

### 12.1 Horizontal Slides (Left ↔ Right)

Each top-level `<section>` is a horizontal slide:

```html
<section>Slide 1</section>  <!-- → →  -->
<section>Slide 2</section>  <!-- → →  -->
<section>Slide 3</section>
```

Navigate with: `←` `→` arrow keys.

### 12.2 Vertical Sub-Slides (Up ↕ Down)

Nest `<section>` inside a parent `<section>` to create vertical stacks:

```html
<section>
  <section>Slide 3a (press ↓)</section>
  <section>Slide 3b (press ↓)</section>
  <section>Slide 3c</section>
</section>
```

Navigate with: `↑` `↓` arrow keys.

### 12.3 When to Use Vertical Sub-Slides

Use them when:
- A topic has too much content for one screen
- You want to group related content under one "chapter"
- Content-heavy topics need 2–3 sub-views

**Pattern:**
```
Slide 1 (title)           → horizontal
Slide 2 (intro)           → horizontal
Slide 3a (topic A, part 1) → vertical stack
Slide 3b (topic A, part 2)
Slide 4a (topic B, part 1) → vertical stack
Slide 4b (topic B, part 2)
...
Slide 13 (takeaways)      → horizontal
Slide 14 (thank you)      → horizontal
```

### 12.4 Navigation Mode

```js
navigationMode: 'default'  // ← → navigates horizontally, ↑ ↓ vertically
navigationMode: 'linear'   // All slides in one flat sequence (← →  only)
navigationMode: 'grid'     // 2D grid navigation
```

### 12.5 Keyboard Shortcuts (Built-in)

| Key | Action |
|-----|--------|
| `→` or `Space` | Next slide |
| `←` | Previous slide |
| `↑` | Previous vertical slide |
| `↓` | Next vertical slide |
| `Home` | First slide |
| `End` | Last slide |
| `F` or `F11` | Toggle fullscreen |
| `S` | Open speaker notes window |
| `O` or `Esc` | Slide overview/grid |
| `B` or `.` | Pause (black screen) |
| `?` | Show keyboard shortcuts |
| `Alt + Click` | Zoom in (requires Zoom plugin) |
| `Ctrl+Shift+F` | Search (requires Search plugin) |

---

## 13. Progress Bar, Controls & UI

### 13.1 Progress Bar

```js
progress: true,   // Show thin progress bar at the bottom of the screen
```

Style it with CSS:

```css
.reveal .progress {
  height: 4px;              /* Thickness */
  color: #f0b247;           /* Bar color (uses your primary color) */
}
.reveal .progress span {
  background: #f0b247;      /* Fill color */
  transition: width 0.8s ease;
}
```

### 13.2 Slide Number

```js
slideNumber: true,          // Just shows number
slideNumber: 'c/t',         // Shows "current / total" (e.g., "5/14")
slideNumber: 'h.v',         // Shows "horizontal.vertical" (e.g., "3.2")
slideNumber: 'c',           // Sequential count only
```

Style it:

```css
.reveal .slide-number {
  font-size: 14px;
  color: rgba(255,255,255,0.5);
  background: transparent;
  right: auto;
  left: 16px;
  bottom: 10px;
}
```

### 13.3 Navigation Controls (Arrows)

```js
controls: true,
controlsLayout: 'bottom-right',   // 'bottom-right' or 'edges'
controlsBackArrows: 'faded',      // Back arrows dim when not applicable
controlsTutorial: true,           // Bounce arrows on first slide
```

Style:

```css
.reveal .controls {
  color: #f0b247;   /* Arrow color matches primary */
}
```

### 13.4 Hiding UI for Clean Slides

```html
<!-- Hide controls on a specific slide -->
<section data-state="no-controls">

<style>
  .no-controls .reveal .controls { display: none; }
</style>
```

---

## 14. Speaker Notes

### 14.1 Adding Notes

```html
<section>
  <h2>My Slide</h2>
  <p>Visible content</p>

  <aside class="notes">
    These notes are only visible in the speaker view.
    Press 'S' to open it. You can write full sentences here.
    Timing: spend about 45 seconds on this slide.
  </aside>
</section>
```

### 14.2 Speaker View

Press `S` to open a new window with:
- Current slide
- Next slide preview
- Your notes
- Timer
- Clock

### 14.3 Showing Notes to Audience

```js
showNotes: true,  // Notes visible on main display (rare use case)
```

---

## 15. Plugins

### 15.1 Available CDN Plugins

| Plugin | Purpose | CDN Path |
|--------|---------|----------|
| Notes | Speaker notes | `.../plugin/notes/notes.min.js` |
| Markdown | Write slides in MD | `.../plugin/markdown/markdown.min.js` |
| Highlight | Code syntax colors | `.../plugin/highlight/highlight.min.js` |
| Math | LaTeX equations | `.../plugin/math/math.min.js` |
| Zoom | Alt+click zoom | `.../plugin/zoom/zoom.min.js` |
| Search | Ctrl+Shift+F | `.../plugin/search/search.min.js` |

### 15.2 Loading Plugins

```html
<!-- Load BEFORE Reveal.initialize() -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/notes/notes.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/highlight/highlight.min.js"></script>

<script>
  Reveal.initialize({
    plugins: [RevealNotes, RevealHighlight],
  });
</script>
```

### 15.3 Code Highlighting (if presentation includes code)

```html
<section>
  <pre><code data-trim data-noescape data-line-numbers="1-3|5-7">
function hello() {
  console.log("Hello");
  return true;

  // This block highlights second
  const x = 42;
  return x;
}
  </code></pre>
</section>
```

Also load the Highlight.js theme CSS:
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/highlight/monokai.min.css" />
```

---

## 16. Common Mistakes — Do NOT Repeat These

These are real mistakes made during development. Every one caused a visible bug.

### ❌ Mistake 1: Stacking image above text vertically
```html
<!-- WRONG — image on top pushes text below the viewport -->
<section>
  <h2>Title</h2>
  <img src="photo.jpg" />
  <ul>
    <li>This gets pushed off-screen</li>
  </ul>
</section>
```
```html
<!-- CORRECT — side-by-side layout -->
<section>
  <h2>Title</h2>
  <div class="row">
    <div class="col-text"><ul><li>Visible</li></ul></div>
    <div class="col-img"><img src="photo.jpg" /></div>
  </div>
</section>
```

### ❌ Mistake 2: Using `<h3>` as the main slide heading
```html
<!-- WRONG — h3 has different color/size/no border, looks broken -->
<section>
  <h3>Patience Over Speed</h3>
</section>
```
```html
<!-- CORRECT — h2 for EVERY main slide heading -->
<section>
  <h2>Patience Over Speed</h2>
</section>
```

### ❌ Mistake 3: No max-height on images
```html
<!-- WRONG — tall image pushes content off-screen -->
<img src="photo.jpg" style="width: 100%;" />
```
```css
/* CORRECT — always constrain height */
.col-img img {
  max-width: 100%;
  max-height: 320px;
  object-fit: cover;
}
```

### ❌ Mistake 4: Too large base font size
```css
/* WRONG — 30px base causes overflow on every content-heavy slide */
:root { --r-main-font-size: 30px; }
```
```css
/* CORRECT — 20–24px range */
:root { --r-main-font-size: 22px; }
```

### ❌ Mistake 5: Forgetting `min-width: 0` on flex children
```css
/* WRONG — long words can force flex item to overflow container */
.col-text { flex: 1 1 55%; }
```
```css
/* CORRECT */
.col-text { flex: 1 1 55%; min-width: 0; }
```

### ❌ Mistake 6: Putting content outside `.row` structure
```html
<!-- WRONG — loose content outside layout system -->
<section>
  <h2>Title</h2>
  <h3>Subheading floating freely</h3>
  <p>Orphaned paragraph</p>
  <img src="photo.jpg" />
</section>
```
```html
<!-- CORRECT — everything inside the box system -->
<section>
  <h2>Title</h2>
  <div class="row">
    <div class="col-text">
      <h3>Subheading</h3>
      <p>Contained paragraph</p>
    </div>
    <div class="col-img">
      <img src="photo.jpg" />
    </div>
  </div>
</section>
```

### ❌ Mistake 7: Not removing Reveal.js default image margins
```css
/* Reveal.js adds margin: 20px 0; to images — ALWAYS reset */
.reveal section img { margin: 0; border: none; }
```

### ❌ Mistake 8: Using `create_file` when file already exists
When editing an existing presentation, **always read the file first**, then use edit/replace operations. Never try to recreate it from scratch without deleting the old one first.

---

## 17. Complete Slide Template

Copy this as your starting point for any new presentation:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>PRESENTATION TITLE</title>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reset.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/night.min.css" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />

  <style>
    :root {
      --r-background-color: #1a1a2e;
      --r-main-font: "Inter", Helvetica, sans-serif;
      --r-main-font-size: 22px;
      --r-main-color: #fff;
      --r-heading-font: "Inter", Helvetica, sans-serif;
      --r-heading-color: #f0b247;
      --r-heading-text-transform: none;
    }

    .reveal h1, .reveal h2, .reveal h3 {
      color: #f0b247;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
      margin-bottom: 0.4em;
    }
    .reveal h2 {
      font-size: 1.5em;
      border-bottom: 2px solid rgba(240,178,71,0.4);
      padding-bottom: 0.15em;
    }
    .reveal h3 {
      font-size: 0.95em;
      color: #e8dcc4;
    }
    .reveal em    { color: #e8dcc4; }
    .reveal strong { color: #e8dcc4; }
    .reveal li    { font-size: 0.85em; line-height: 1.4; }
    .reveal li::marker { color: #e8dcc4; }
    .reveal ul    { text-align: left; margin-left: 1em; }

    .reveal section img {
      border: none; border-radius: 8px; margin: 0;
      box-shadow: 0 6px 24px rgba(0,0,0,0.5);
    }

    .row {
      display: flex !important;
      align-items: center;
      gap: 1.5em;
      width: 100%;
      text-align: left;
    }
    .col-text { flex: 1 1 55%; min-width: 0; }
    .col-img  { flex: 0 0 38%; display: flex; justify-content: center; align-items: center; }
    .col-img img { max-width: 100%; max-height: 320px; object-fit: cover; }
    .col-img.wide { flex: 0 0 46%; }

    .title-slide { text-align: center !important; }
    .title-slide h1 {
      font-size: 2.8em; text-transform: uppercase; border-bottom: none;
    }

    .progress { color: #f0b247; }
  </style>
</head>
<body>
<div class="reveal">
<div class="slides">

  <!-- ═══════ SLIDE 1 — TITLE ═══════ -->
  <section class="title-slide" data-background-image="URL" data-background-opacity="0.3">
    <h1>Title</h1>
    <h3>Subtitle</h3>
    <div class="meta">
      <p>Course &bull; Date</p>
      <p>Presenters</p>
    </div>
  </section>

  <!-- ═══════ SLIDE 2 — CONTENT ═══════ -->
  <section>
    <h2>Slide Title</h2>
    <div class="row">
      <div class="col-text">
        <ul>
          <li>Point one</li>
          <li>Point two</li>
        </ul>
      </div>
      <div class="col-img">
        <img src="URL" alt="Description" />
      </div>
    </div>
  </section>

  <!-- ═══════ SLIDE 3 — WITH VERTICAL SUB-SLIDES ═══════ -->
  <section>
    <section>
      <h2>Topic Part 1</h2>
      <div class="row">
        <div class="col-text">
          <h3>Sub-heading</h3>
          <ul><li>Content</li></ul>
        </div>
        <div class="col-img"><img src="URL" alt="" /></div>
      </div>
    </section>
    <section>
      <h2>Topic Part 2</h2>
      <div class="row">
        <div class="col-text">
          <h3>Sub-heading</h3>
          <ul><li>Content</li></ul>
        </div>
        <div class="col-img"><img src="URL" alt="" /></div>
      </div>
    </section>
  </section>

  <!-- ═══════ LAST SLIDE — THANK YOU ═══════ -->
  <section class="title-slide" data-background-image="URL" data-background-opacity="0.25">
    <h1>Thank You</h1>
    <h3>Questions & Discussion</h3>
  </section>

</div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/plugin/notes/notes.min.js"></script>
<script>
Reveal.initialize({
  width: 1100,
  height: 700,
  margin: 0.07,
  center: true,
  hash: true,
  transition: 'slide',
  backgroundTransition: 'fade',
  controls: true,
  controlsLayout: 'bottom-right',
  controlsBackArrows: 'faded',
  progress: true,
  slideNumber: 'c/t',
  plugins: [RevealNotes],
});
</script>
</body>
</html>
```

---

## 18. Checklist Before Delivering

Run through this for **every slide** before considering the presentation done:

- [ ] Every slide has exactly ONE `<h2>` (except title/thankyou which use `<h1>`)
- [ ] Every content slide uses `.row` > `.col-text` + `.col-img` layout
- [ ] No raw text inside `<div>` — all content uses semantic tags (`<h3>`, `<p>`, `<ul>`, `<li>`, `<em>`, `<strong>`)
- [ ] All images have `alt` text
- [ ] All images are constrained by `max-height: 320px` and `object-fit: cover`
- [ ] No slide has more than ~8 bullet points (split to sub-slides if more)
- [ ] Font sizes: base ≤ 24px, h2 ≤ 1.5em, li ≤ 0.85em
- [ ] `margin: 0` is set on images to override Reveal.js defaults
- [ ] Background images use `data-background-opacity` ≤ 0.3
- [ ] Every HTML slide section has a descriptive comment above it
- [ ] CSS classes use descriptive names (`.col-text`, `.practice-box`, not `.div1`, `.box`)
- [ ] **No `class="fragment"` on any element** (unless user explicitly requested step-by-step reveals)
- [ ] Tested: open in browser, press `→` through every slide — each slide fully appears in ONE click, nothing overflows
- [ ] Progress bar and slide number are visible and styled
- [ ] Press `S` — speaker notes window opens correctly

---

*Generated from real production experience. Every rule here prevented or fixed an actual bug.*
