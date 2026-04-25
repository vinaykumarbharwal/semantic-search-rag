# Design PRD — HackerRank B2B SaaS Landing Page

> **Document Type:** Product Requirements Document (Design)
> **Product:** HackerRank for Work — Enterprise Landing Page
> **Design Reference:** Ramotion × HackerRank (Dribbble Shot #26414267)
> **Version:** 1.0 | April 2026
> **Status:** Draft — For Design Review

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Design System](#2-design-system)
3. [Page Architecture](#3-page-architecture)
4. [Component Specifications](#4-component-specifications)
5. [UX Flows & Interaction Design](#5-ux-flows--interaction-design)
6. [Accessibility & Performance](#6-accessibility--performance)
7. [Responsive Design Spec](#7-responsive-design-spec)
8. [Implementation Guidance](#8-implementation-guidance)
9. [Acceptance Criteria](#9-acceptance-criteria)

---

## 1. Executive Summary

### 1.1 Project Overview

This Product Requirements Document defines the UI/UX architecture for the HackerRank B2B SaaS enterprise landing page, based on the Dribbble design concept by Ramotion (Shot #26414267). The document translates visual design intent into actionable engineering and design specifications for production implementation.

### 1.2 Product Context

HackerRank for Work is an enterprise technical hiring platform targeting engineering leaders, talent acquisition teams, and HR departments at mid-to-large technology companies. The landing page serves as the primary acquisition touchpoint for B2B prospects arriving from paid media, referrals, and organic search.

### 1.3 Design Philosophy

The design concept embodies three core pillars derived from the Ramotion approach:

| Pillar | Design Expression | Business Goal |
|--------|------------------|---------------|
| Developer Credibility | Terminal aesthetics, monospace typography, code motifs | Trust with technical decision-makers |
| Enterprise Authority | Dark theme, geometric precision, generous whitespace | Signal maturity and scalability |
| Conversion Clarity | Single-focus CTAs, progressive disclosure, social proof | Drive demo and trial sign-ups |

### 1.4 Scope

- **Hero Section** — above-the-fold value proposition and primary CTA
- **Social Proof Bar** — trusted-by logos and key metrics
- **Problem/Solution Narrative** — pain-point storytelling section
- **Feature Showcase** — interactive product capability highlights
- **Testimonials & Case Studies** — enterprise customer validation
- **Pricing Overview** — plan structure and CTA
- **Final CTA Section** — conversion-focused footer zone
- **Navigation & Footer** — global UI shell components

---

## 2. Design System

### 2.1 Brand Identity Analysis

The Ramotion design for HackerRank employs a **"developer-native"** visual vocabulary — borrowing from terminal interfaces, code editors, and technical documentation to create an interface that resonates with engineering audiences while maintaining enterprise-grade polish.

---

### 2.2 Colour Palette

| Swatch | Token Name | Hex Value | Usage |
|--------|-----------|-----------|-------|
| 🟢 | `--color-brand-primary` | `#00EA64` | Primary CTAs, hover states, active indicators, brand marks |
| ⬛ | `--color-bg-base` | `#0D1117` | Page background, primary surface |
| 🟦 | `--color-bg-elevated` | `#1A2233` | Card backgrounds, section containers |
| 🔷 | `--color-bg-card` | `#2D3A4A` | Feature tiles, hover overlays |
| ⬜ | `--color-text-primary` | `#F8FAFC` | Primary heading text on dark backgrounds |
| 🔘 | `--color-text-secondary` | `#94A3B8` | Body copy, supporting text, captions |
| ⬜ | `--color-text-inverse` | `#FFFFFF` | Text on green CTA buttons |

---

### 2.3 Typography System

Typography follows a dual-font strategy: a geometric sans-serif for marketing headlines and UI chrome, paired with a monospace face for code-adjacent content to reinforce developer credibility.

| Token | Font Family | Weight | Size | Line Height | Use Case |
|-------|------------|--------|------|-------------|----------|
| `--text-display-xl` | Sora / Neue Haas Grotesk | 800 | 72–96px | 1.05 | Hero headline |
| `--text-display-lg` | Sora | 700 | 48–64px | 1.1 | Section headlines |
| `--text-display-md` | Sora | 600 | 32–40px | 1.2 | Card headings |
| `--text-body-lg` | Inter | 400 | 18–20px | 1.6 | Lead paragraphs |
| `--text-body-md` | Inter | 400 | 16px | 1.65 | Body copy |
| `--text-code` | JetBrains Mono | 400 | 14–16px | 1.5 | Code snippets, badges |
| `--text-label` | Inter | 600 | 12–13px | 1.4 | Form labels, tags |
| `--text-nav` | Inter | 500 | 15px | 1.0 | Navigation items |

---

### 2.4 Spacing & Grid

The layout uses an **8px base unit system** on a 12-column grid with responsive breakpoints.

| Breakpoint | Viewport Width | Columns | Gutter | Margin | Max Content Width |
|-----------|---------------|---------|--------|--------|------------------|
| Mobile (sm) | < 768px | 4 | 16px | 20px | 100% |
| Tablet (md) | 768–1023px | 8 | 24px | 40px | 100% |
| Desktop (lg) | 1024–1279px | 12 | 32px | 64px | 1280px |
| Wide (xl) | 1280–1535px | 12 | 40px | 80px | 1440px |
| Ultrawide (2xl) | ≥ 1536px | 12 | 48px | Auto | 1536px |

---

### 2.5 Motion & Animation Principles

- **Entrance animations:** fade-up with 24px translate, 400–600ms ease-out
- **Stagger delay:** 80–120ms between sequential elements in lists/grids
- **Hover micro-interactions:** 200ms ease-in-out on interactive elements
- **Page scroll:** section reveal triggered at 15% viewport intersection
- **CTA pulse:** subtle glow ring animation at 2s interval to draw attention
- **Reduce motion:** all animations disabled via `prefers-reduced-motion`

---

## 3. Page Architecture

### 3.1 Page Section Hierarchy

The page follows a **"problem → solution → proof → action"** narrative arc, proven for B2B SaaS conversion.

| # | Section Name | Primary Goal | Key Elements | Viewport Height |
|---|-------------|-------------|-------------|----------------|
| 01 | Global Navigation | Wayfinding + CTA | Logo, nav links, Demo CTA, mobile hamburger | Fixed 72px |
| 02 | Hero | Value proposition + primary CTA | Headline, subhead, CTA pair, product screenshot/animation | 100vh |
| 03 | Trust Bar | Social proof | Company logos (Fortune 500 clients), metrics strip | 120–180px |
| 04 | Problem Statement | Pain amplification | Headline, pain-point cards (3–4 items) | 60–80vh |
| 05 | Solution Showcase | Feature education | Tabbed interface, animated product demos | 80–100vh |
| 06 | Feature Grid | Feature depth | 6-tile feature grid with icons and descriptions | 70–90vh |
| 07 | Testimonials | Trust + FOMO | Quote carousel, headshots, company logos | 60vh |
| 08 | Case Study Highlight | ROI evidence | Stat callouts, customer story card | 50–70vh |
| 09 | Pricing Overview | Qualification | Plan cards (3 tiers), feature comparison | 80–100vh |
| 10 | Final CTA | Conversion | Headline, subhead, dual CTA, background gradient | 50–60vh |
| 11 | Footer | Navigation + compliance | Links, social icons, legal text, newsletter input | 300–400px |

---

### 3.2 Navigation Architecture

#### Primary Navigation Structure

| Nav Item | Type | Destination | Hover State | Mobile |
|----------|------|------------|------------|--------|
| HackerRank Logo | Brand mark | `/` | Subtle scale 1.02 | Visible in hamburger bar |
| Products | Dropdown trigger | Mega menu | Expand mega menu at 300ms | Accordion expand |
| Solutions | Dropdown trigger | Mega menu | Expand mega menu | Accordion expand |
| Resources | Link | `/resources` | Green underline slide-in | Link item |
| Pricing | Link | `/pricing` | Green underline slide-in | Link item |
| Sign In | Ghost button | `/login` | Border turns green | Full-width button |
| Get a Demo | Primary CTA | `/demo` | Glow + slight lift | Full-width green button |

#### Navigation Scroll Behaviour

- **Default:** Transparent background over hero section, white logo mark
- **On scroll > 80px:** Background transitions to `#0D1117` with `blur(12px)` backdrop filter
- **Scrolled state:** `border-bottom: 1px solid rgba(255,255,255,0.08)`
- **CTA button** remains consistently visible in both states

---

## 4. Component Specifications

### 4.1 Hero Section

The hero is the highest-stakes section. It must communicate the core value proposition in under 5 seconds and drive a single clear action. The design uses an **asymmetric layout** with a dominant headline left-aligned and a product UI screenshot or animated code demo on the right.

#### Layout Specification

| Element | Column Span | Content Spec | Responsive Behaviour |
|---------|------------|-------------|---------------------|
| Eyebrow tag | Full (12) | `#1 Technical Hiring Platform` — green badge with icon | Centered on mobile |
| Headline | 7 of 12 | 72px Sora 800, 2–3 lines max, white on dark | Full-width, 40–48px mobile |
| Sub-headline | 7 of 12 | 20px Inter 400, 2 lines, `--color-text-secondary` | Full-width mobile |
| CTA Group | 7 of 12 | Primary: "Get a Demo" + Secondary: "View Pricing" | Stacked full-width on mobile |
| Social proof line | 7 of 12 | "Trusted by 3,000+ companies" with avatar stack | Below CTA on mobile |
| Product visual | 5 of 12 | Elevated screenshot with shadow + hexagon grid bg | Below fold on mobile |

#### CTA Button Specifications

| Variant | Background | Text | Border | Height | Padding | Border Radius |
|---------|-----------|------|--------|--------|---------|--------------|
| Primary (Get Demo) | `#00EA64` | `#0D1117` bold | None | 52px | 16px 32px | 8px |
| Secondary (View Pricing) | Transparent | `#F8FAFC` | `1px #F8FAFC` at 30% opacity | 52px | 16px 32px | 8px |
| Ghost | Transparent | `#00EA64` | `1px #00EA64` | 44px | 12px 24px | 6px |
| Danger/Outline | Transparent | `#F87171` | `1px #F87171` at 60% | 44px | 12px 24px | 6px |

---

### 4.2 Social Proof Trust Bar

Horizontally scrolling ticker of client logos. Two rows on desktop: a metrics strip above, logo carousel below. Logos displayed in **monochrome (white, 40% opacity)** to maintain visual hierarchy and avoid brand conflicts.

#### Metrics Strip — Key Stats

| Metric | Value | Supporting Label | Display Format |
|--------|-------|-----------------|---------------|
| Active Developers | 23M+ | in HackerRank network | Large number + small label |
| Hiring Companies | 3,000+ | enterprise customers | Large number + small label |
| Tests Administered | 100M+ | coding assessments given | Large number + small label |
| Time-to-Hire Reduction | 40% | average across customers | Large number + small label |

---

### 4.3 Feature Showcase — Tabbed Interface

A horizontally tabbed interface allows prospects to self-select their role and see contextually relevant feature demonstrations.

| Tab ID | Persona | Feature Highlighted | Product Screenshot | Key Benefit Statement |
|--------|---------|--------------------|--------------------|----------------------|
| T1 | Technical Recruiter | Code Screening & Assessments | Assessment builder UI | Screen 5x more candidates in less time |
| T2 | Engineering Manager | Interview Intelligence | Live interview session UI | Standardize your hiring signal |
| T3 | HR / CHRO | Analytics Dashboard | Reporting & insights view | Prove hiring ROI with data |
| T4 | Developer | Candidate Experience | Problem-solving interface | Give developers a fair, engaging process |

---

### 4.4 Feature Grid (6-Tile)

A **3×2 grid** on desktop (2×3 on tablet, 1×6 on mobile). Each tile has an icon, headline, 1–2 sentence description, and an optional "Learn more" link. Background uses subtle card elevation with border glow on hover.

| Tile | Icon Style | Feature Name | Description | Link Target |
|------|-----------|-------------|-------------|------------|
| F1 | Code bracket | Technical Assessments | Role-specific coding tests across 40+ languages with anti-cheat detection | `/features/assessments` |
| F2 | Video camera | Live Coding Interviews | Real-time collaborative coding environment with built-in interview guides | `/features/interviews` |
| F3 | Chart bar | Hiring Analytics | Funnel metrics, bias detection, and hiring velocity dashboards | `/features/analytics` |
| F4 | Person check | Candidate Screening | AI-powered resume screening and automated shortlisting workflows | `/features/screening` |
| F5 | Puzzle piece | ATS Integrations | Native connectors for Greenhouse, Lever, Workday, and 40+ more | `/integrations` |
| F6 | Shield check | Enterprise Security | SOC 2 Type II, GDPR, and SSO-ready infrastructure | `/security` |

---

### 4.5 Testimonial Component

#### Carousel Card Anatomy

| Element | Specification | Notes |
|---------|-------------|-------|
| Quote mark | Oversized decorative, `#00EA64`, 120px | Positioned top-left of card |
| Quote text | Inter 400, 20–22px, max 180 characters, italic | Two lines max on desktop |
| Attribution name | Inter 700, 16px, white | Full name of reviewer |
| Attribution title | Inter 400, 14px, `--color-text-secondary` | Job title and company |
| Avatar | 48×48px circle, 2px border `#00EA64` | Real photo preferred |
| Company logo | 120×40px max, monochrome white | Positioned right of attribution |
| Card background | `#1A2233` with `border: 1px solid #2D3A4A` | 16px border radius |

---

## 5. UX Flows & Interaction Design

### 5.1 Primary Conversion Flow

The critical path from landing to demo request must be frictionless.

| Step | Touchpoint | User Action | System Response | Drop-off Risk |
|------|-----------|------------|----------------|--------------|
| 1 | Page Load | Arrives from paid ad / referral | Hero renders <1s LCP | High — first impression |
| 2 | Hero scan | Reads headline + subheadline | Eyebrow tag reinforces role match | Medium |
| 3 | Social proof | Sees logos of known companies | Trust bar auto-scrolls | Low |
| 4 | Feature exploration | Clicks persona tab | Animated demo loads | Medium — must be fast |
| 5 | CTA click | Clicks "Get a Demo" | Modal or page transition to form | High — form friction |
| 6 | Form fill | Enters work email + name | Real-time validation, role suggestions | High — fields |
| 7 | Submission | Submits form | Success state + calendar link | Low |
| 8 | Confirmation | Receives email confirmation | Automated nurture sequence begins | Very Low |

---

### 5.2 Demo Request Modal

The demo request form appears as a modal dialog triggered by any CTA click. Intentionally minimal — **4 fields maximum** — to reduce friction.

#### Form Fields Specification

| Field | Type | Placeholder | Validation Rule | Error Message |
|-------|------|------------|----------------|--------------|
| Work Email | Email input | `you@company.com` | Valid email, no personal domains (gmail, yahoo etc.) | "Please use your work email" |
| Full Name | Text input | `Jane Smith` | Min 2 chars, max 80 chars | "Please enter your full name" |
| Company Size | Select dropdown | `Select team size` | 1–50 / 51–500 / 501–5000 / 5000+ | Required selection |
| Phone (optional) | Tel input | `+1 (555) 000-0000` | International format, optional | Format hint only |

> **Progressive disclosure:** Show only Email + Name initially. Reveal Company Size and Phone after email validation to reduce perceived effort.

---

### 5.3 Scroll-Triggered Sticky CTA

After the user scrolls past the hero section (> 100vh), a sticky bottom bar appears on **mobile only** with a persistent "Get a Demo" CTA.

| Property | Value | Notes |
|----------|-------|-------|
| Trigger | `scrollY > window.innerHeight` | Fires once, persists unless form opened |
| Position | `fixed bottom-0`, full width on mobile | `z-index: 9000` |
| Height | 72px | Includes `safe-area-inset-bottom` for iOS |
| Background | `#0D1117` with `top border #00EA64 2px` | Matches page bg for seamless feel |
| Animation in | `translateY(0)` from `translateY(100%)`, 300ms ease-out | Smooth slide-up |
| Desktop | Not shown — nav CTA is sufficient | `display: none` at `lg` breakpoint |

---

## 6. Accessibility & Performance

### 6.1 Colour Contrast Requirements

All colour pairings must meet **WCAG 2.1 AA** as a minimum.

| Text Pairing | Foreground | Background | Contrast Ratio | WCAG AA Pass? |
|-------------|-----------|-----------|---------------|--------------|
| Body copy on dark bg | `#94A3B8` | `#0D1117` | 5.2:1 | ✅ Pass |
| Primary heading on dark | `#F8FAFC` | `#0D1117` | 19.6:1 | ✅ Pass (AAA) |
| CTA text on green | `#0D1117` | `#00EA64` | 9.1:1 | ✅ Pass (AAA) |
| Green on dark card | `#00EA64` | `#1A2233` | 6.8:1 | ✅ Pass |
| Secondary text on card | `#94A3B8` | `#1A2233` | 4.5:1 | ✅ Pass (minimum) |
| Badge text | `#F8FAFC` | `#2D3A4A` | 7.8:1 | ✅ Pass (AAA) |

---

### 6.2 ARIA & Semantic HTML Requirements

- Navigation: `<nav aria-label="Main navigation">` with skip-link to main content
- Hero CTA: `aria-describedby` pointing to value proposition text
- Tabbed feature section: `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`
- Testimonial carousel: `aria-live="polite"` on the active quote region
- Modal form: `role="dialog"`, `aria-modal="true"`, focus trap on open, Esc to close
- Animated counters: `aria-label` with final value (not animated) for screen readers
- Logo images: `alt=""` (decorative) with `aria-label` on the containing section
- All interactive elements: minimum **44×44px** touch target

---

### 6.3 Core Web Vitals Targets

| Metric | Target | Measurement Tool | Priority |
|--------|--------|-----------------|---------|
| Largest Contentful Paint (LCP) | < 1.8s | Lighthouse / CrUX | Critical |
| First Input Delay (FID) | < 50ms | CrUX field data | High |
| Cumulative Layout Shift (CLS) | < 0.05 | Lighthouse | High |
| Time to Interactive (TTI) | < 3.0s | Lighthouse | High |
| Total Blocking Time (TBT) | < 150ms | Lighthouse | Medium |
| Page Weight (initial load) | < 500KB gzipped | Webpack Bundle Analyzer | High |
| Image optimisation | WebP/AVIF, responsive srcset | Manual audit | High |
| Font loading | `font-display: swap`, subset for Latin | Lighthouse | Medium |

---

## 7. Responsive Design Spec

### 7.1 Breakpoint Behaviour Matrix

| Section | Desktop (lg+) | Tablet (md) | Mobile (sm) |
|---------|--------------|------------|------------|
| Navigation | 2-col flex: logo \| links + CTA | Logo + hamburger menu | Fullscreen overlay menu |
| Hero | 50/50 split: text \| visual | 60/40 split, visual below fold | Stacked: text → CTA → visual |
| Trust Bar | Horizontal marquee, 2 rows | Horizontal marquee, 1 row | Horizontal marquee, smaller logos |
| Problem Section | 3-col card grid | 2-col card grid | 1-col stacked cards |
| Feature Tabs | Horizontal tabs + right panel | Top tabs + below panel | Accordion-style expansion |
| Feature Grid | 3×2 tile grid | 2×3 tile grid | 1×6 stacked list |
| Testimonials | 3-up carousel (visible) | 2-up carousel | Single card, swipe enabled |
| Pricing | 3-col plan cards | 3-col compressed or 1-col | 1-col stacked, scrollable |
| Final CTA | Centered block, 60% width | 80% width | Full width, stacked buttons |
| Footer | 5-col link grid + logo | 3-col grid + logo | 2-col grid + logo above |

---

### 7.2 Touch Interaction Patterns

- **Swipe left/right:** Testimonial carousel and pricing plan cards
- **Tap targets:** Minimum 44×44px, recommended 48×48px for primary actions
- **Long press:** Disabled — no context menus on interactive elements
- **Pinch-zoom:** Allowed — do not override viewport meta with `user-scalable=no`

---

## 8. Implementation Guidance

### 8.1 Tech Stack Recommendation

| Layer | Recommended Technology | Rationale |
|-------|----------------------|-----------|
| Framework | Next.js 14+ (App Router) | SSR for SEO + RSC for performance |
| Styling | Tailwind CSS + CSS Variables | Design token alignment, purging |
| Animation | Framer Motion | Scroll triggers, layout animation, gesture |
| Icons | Heroicons / Phosphor Icons | Consistent with clean SaaS aesthetic |
| Form handling | React Hook Form + Zod | Validation, TypeScript integration |
| Analytics | Segment + Google Analytics 4 | Funnel tracking, A/B test support |
| A/B Testing | Vercel Edge Config / LaunchDarkly | Hero headline and CTA testing |
| CMS (copy) | Contentful / Sanity | Enables non-dev copy iteration |
| Deployment | Vercel | Edge functions, analytics, preview URLs |

---

### 8.2 Asset Specifications

| Asset Type | Format | Max Size | Notes |
|-----------|--------|---------|-------|
| Hero product screenshot | WebP + PNG fallback | < 200KB | Retina @2x, lazy-load below initial viewport |
| Client logos (trust bar) | SVG | < 8KB each | Monochrome, white fill for dark bg |
| Testimonial avatars | WebP, 96×96px @2x | < 20KB each | Circular crop via CSS |
| Feature tab animations | Lottie JSON or CSS animation | < 100KB per animation | Prefer CSS for simple demos |
| Background hexagon pattern | SVG inline or CSS | < 4KB | GPU-composited, opacity 0.04 |
| OG image (social share) | PNG, 1200×630px | < 100KB | Separate design asset |

---

### 8.3 SEO Metadata Requirements

| Meta Tag | Content | Notes |
|----------|---------|-------|
| `<title>` | HackerRank for Work \| Technical Hiring Platform for Enterprise | < 60 chars |
| `<meta description>` | Screen, interview, and hire top technical talent with HackerRank. Trusted by 3,000+ enterprises. | < 160 chars |
| `og:title` | HackerRank — Hire Better Engineers, Faster | Social-optimised variant |
| `og:image` | `https://cdn.hackerrank.com/og/enterprise-landing.png` | 1200×630px social card |
| Canonical | `https://www.hackerrank.com/work/` | Prevent duplicate indexing |
| robots | `index, follow` | Default, no noindex |
| Schema (JSON-LD) | SoftwareApplication + Organization | Structured data for SERP rich results |

---

### 8.4 Analytics Event Taxonomy

| Event Name | Trigger | Properties | Priority |
|-----------|---------|-----------|---------|
| `page_view` | Page load | `utm_source`, `utm_medium`, `utm_campaign`, `referrer` | Critical |
| `hero_cta_click` | Primary CTA click | `cta_text`, `cta_position` | Critical |
| `demo_form_started` | First field focused | `form_id` | High |
| `demo_form_submitted` | Successful form submission | `company_size`, `email_domain` | Critical |
| `feature_tab_click` | Tab selection | `tab_name`, `persona` | Medium |
| `pricing_plan_click` | Plan CTA click | `plan_name` | High |
| `testimonial_viewed` | 80% of component visible | `testimonial_company` | Low |
| `scroll_depth` | 25%, 50%, 75%, 100% | `depth_percentage` | Medium |
| `exit_intent` | Mouse leaves viewport (desktop) | `current_section` | Medium |

---

## 9. Acceptance Criteria

### 9.1 Design QA Checklist

All design deliverables must pass the following criteria before handoff to engineering. Priority: **P0** = launch blocker, **P1** = pre-launch, **P2** = post-launch iteration.

| ID | Criteria | Test Method | Priority |
|----|---------|------------|---------|
| AC-01 | All colour pairings meet WCAG 2.1 AA contrast ratios | Figma A11y plugin + manual check | P0 |
| AC-02 | Page LCP < 1.8s on 4G mobile | Lighthouse CI in staging | P0 |
| AC-03 | CLS score < 0.05 (no layout shift from fonts or images) | Lighthouse CI + WebPageTest | P0 |
| AC-04 | Demo form submits successfully with valid data | Manual QA across 3 browsers | P0 |
| AC-05 | All interactive elements keyboard-navigable (Tab + Enter/Space) | Manual keyboard walkthrough | P0 |
| AC-06 | Page renders correctly at 375px, 768px, 1280px, 1440px | BrowserStack cross-device | P0 |
| AC-07 | All animations respect `prefers-reduced-motion` | Browser DevTools emulation | P0 |
| AC-08 | Feature tab content loads within 300ms of click | Manual QA + network throttle | P1 |
| AC-09 | Sticky CTA appears on mobile after scrolling past hero | Manual mobile device test | P1 |
| AC-10 | OG image renders correctly in Slack, LinkedIn, Twitter previews | Social share debug tools | P1 |
| AC-11 | Analytics events fire correctly as per event taxonomy | GA4 DebugView + Segment Debugger | P1 |
| AC-12 | Form validation shows appropriate error messages | Manual QA with edge cases | P1 |
| AC-13 | Trust bar logo marquee pauses on hover/focus | Manual accessibility check | P2 |
| AC-14 | Testimonial carousel is swipeable on iOS Safari and Android Chrome | Physical device test | P2 |
| AC-15 | Page TBT < 150ms (no render-blocking scripts) | Lighthouse CI | P2 |

---

### 9.2 Open Design Decisions

The following items require stakeholder alignment before design finalization:

| Item | Options | Recommended | Decision Owner | Deadline |
|------|---------|------------|---------------|---------|
| Pricing page strategy | Show prices vs. "Contact Sales" gating | Show pricing (self-serve signals) | Product + Revenue | Pre-launch |
| Video in hero | Static screenshot vs. autoplay looping product video | Looping video (muted, poster fallback) | Marketing | Week 2 |
| CTA copy test | "Get a Demo" vs "Start Free Trial" vs "See It In Action" | A/B test all three | Growth team | Post-launch |
| Chat widget | Intercom or Drift live chat overlay on scroll | Defer to V2 (adds weight) | CS + Product | V2 scope |

---

*Document prepared following UI/UX analysis of Ramotion × HackerRank B2B SaaS Landing Page (Dribbble Shot #26414267)*
*Version 1.0 | April 2026 | For Design Review*