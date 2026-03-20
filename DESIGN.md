# Design System Specification: The Architectural Minimalist

## 1. Overview & Creative North Star
The creative North Star for this design system is **"The Digital Architect."**

We are moving away from the chaotic, "pasted-together" look of community portals and toward a sophisticated, high-end editorial experience. This system balances the technical rigor of the Python language with the precision of modern Tokyo architecture.

Rather than a standard grid, we utilize **intentional asymmetry** and **breathable tonal layering**. High-contrast typography scales create a clear path for the developer's eye, while the generous use of white space ensures that technical resources feel approachable rather than overwhelming. We treat every page as a canvas where "void" (empty space) is as important as the content itself.

---

## 2. Colors: Tonal Depth & The No-Line Rule
Our palette is anchored in the iconic Python Red (`#E4231E`) and technical Navy (`#33628B`), supported by a sophisticated range of warm grays.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders for sectioning. Boundaries must be defined solely through background color shifts.
- To separate the Hero from the Community Highlights, transition from `surface` (`#fcf9f8`) to `surface_container_low` (`#f6f3f2`).
- This creates a soft, architectural edge that feels native to the screen, rather than a forced "box."

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. Use the surface-container tiers to create depth:
* **Base:** `surface` (`#fcf9f8`) for the primary background.
* **Layer 1:** `surface_container_low` (`#f6f3f2`) for secondary content areas.
* **Layer 2 (The Inset):** `surface_container_highest` (`#e5e2e1`) for code blocks or technical snippets to provide high contrast against the body text.

### The "Glass & Gradient" Rule
For floating elements (like Navigation or Mobile Menus), use **Glassmorphism**. Use `surface` at 80% opacity with a `20px` backdrop-blur.
For primary CTAs, apply a subtle linear gradient from `primary` (`#bd000a`) to `primary_container` (`#e4231e`) at a 135-degree angle. This adds "soul" and prevents the vibrant red from feeling flat or "web 1.0."

---

## 3. Typography: Editorial Authority
We use a dual-font approach to balance personality with technical readability.

* **Display & Headlines (Manrope):** Chosen for its geometric precision. Use `display-lg` (3.5rem) for hero headers to command attention. The wide tracking and clean lines of Manrope reflect the "Tokyo" side of the identity—modern, clean, and structured.
* **Body & Labels (Inter):** The industry standard for a reason. Inter provides the highest level of legibility for documentation.
* **Body-lg (1rem):** Use for community updates.
* **Label-md (0.75rem):** Use for metadata, tags, and "Pythonic" technical details.

The hierarchy is intentionally steep. A `display-lg` headline should sit comfortably above `body-lg` text, using the **Spacing Scale (8 or 10)** to provide enough "air" between the two, conveying authority.

---

## 4. Elevation & Depth: Tonal Layering
Traditional drop shadows are forbidden unless specified. We achieve elevation through color science.

* **The Layering Principle:** Place a `surface_container_lowest` (`#ffffff`) card on top of a `surface_container_low` (`#f6f3f2`) background. The subtle difference in hex value provides a "natural lift" that mimics fine paper without the clutter of shadows.
* **Ambient Shadows:** If an element must float (e.g., a modal), use a shadow with a blur of `40px` and an opacity of `6%`. Use the `on_surface` color (`#1c1b1b`) as the shadow tint—never pure black.
* **The "Ghost Border":** For input fields or cards where a boundary is critical for accessibility, use the `outline_variant` (`#e7bdb7`) at **15% opacity**. This creates a suggestion of a container rather than a hard cage.

---

## 5. Components

### Buttons
* **Primary:** Background: Gradient `primary` to `primary_container`. Text: `on_primary` (`#ffffff`). Corner Radius: `md` (0.375rem).
* **Secondary:** Background: `secondary_container` (`#a4d0ff`). Text: `on_secondary_container` (`#295982`).
* **Tertiary:** No background. Text: `primary`. Use for "Read More" or "View Documentation."

### Cards (Community & Resources)
* **Style:** No borders. Use `surface_container_low`.
* **Padding:** Use Spacing Scale `6` (2rem) for internal padding to ensure content doesn't feel cramped.
* **Interaction:** On hover, shift the background to `surface_container_high` and apply an Ambient Shadow.

### Inputs & Search
* **Style:** Minimalist. Background: `surface_container_lowest`. Ghost Border at 15%.
* **Focus State:** Border becomes 100% `secondary` (`#33628b`) with a 2px outer glow of `secondary_container`.

### Technical Resources List
* **Style:** Do not use divider lines. Use Spacing Scale `4` (1.4rem) between list items. Use `label-md` for "Python Version" tags in `tertiary_fixed` colors.

---

## 6. Do's and Don'ts

### Do:
* **DO** use whitespace as a functional tool. If a section feels crowded, double the spacing token (e.g., move from `8` to `16`).
* **DO** use the Python Red sparingly as an "energy" color—save it for CTAs and critical branding elements.
* **DO** ensure all text on `surface_container` levels maintains a contrast ratio of 4.5:1.

### Don't:
* **DON'T** use 1px solid black borders. It breaks the architectural fluidity of the system.
* **DON'T** use the "Tokyo Python" logo at small sizes without adequate clear space (at least Spacing Scale `5`).
* **DON'T** use standard "Drop Shadows." If it looks like a default Photoshop style, it doesn't belong here.
* **DON'T** center-align long blocks of text. Stick to editorial left-alignment to maintain the "Architectural" grid.