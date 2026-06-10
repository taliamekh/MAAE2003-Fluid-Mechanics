# MAAE 2300 — Fluid Mechanics I — Progress

## Config

```
Course: MAAE 2300 — Fluid Mechanics I
Section: A — Summer 2026
Instructor: Dr. Nafisa Bano
Subject: Engineering
Content org: Chapters (main) → Lectures (sub)
Theme: Arctic Fox (custom Arctic Sunrise variant)
  Mode: Light
  Background: #F8F6F1 (soft ivory)
  Surface: #FFFFFF
  Sidebar BG: #0B2E48
  Sidebar Text: #8A9DB0
  Menu Active: #FF6B35
  eq: #FF6B35 (vivid orange)
  def: #2A6B7C (deep teal)
  tip: #1AAA96 / bright: #5DF8D8 (mint)
  der: #093C5D (navy)
  ex: #F4A261 (sand orange)
  unit: #7A8FA6 (greyish blue)
  Font: Poppins
Textbook: Fluid Mechanics 9e — White & Xue (McGraw Hill, ISBN 9781260575545)
Assessments:
  - Midterm 1: May 21 (15%) — covers Ch 1-2
  - Midterm 2: June 11 (15%) — covers Ch 3-5
  - Final: TBA (55%) — cumulative
  - Labs: 3 × 5% = 15% (Venturi, Jet Pump, Flow Measurement)
Repo: https://github.com/taliamekh/MAAE2003-Fluid-Mechanics
```

## Fetch Guide

| Task | Files to fetch |
|---|---|
| Lec N.M notes | `chapters/chN-lecM.html`, `chapters/formulas.html`, `chapters/summary.html`, `chapters/progress.html`, `shell-head.html`, `progress.md` |
| Ch N problems | `chapters/chN-prob.html`, `progress.md` |
| Formula sheet edit | `chapters/formulas.html`, `shell-head.html` |
| Midterm/Final prep | `chapters/m{N}prep.html` or `chapters/final.html`, `progress.md` |
| Lab report | `chapters/lab{N}.html` |
| Theme/CSS fix | `shell-head.html` |
| JS fix | `shell-foot.html` |
| Summary update | `chapters/summary.html` |
| Progress update | `chapters/progress.html` |

**Structure note:** Each lecture is its own fragment file (`ch1-lec1.html`, `ch1-lec2.html`, etc.) and its own sidebar page. This prevents regression — editing one lecture never touches another's file.

## Chapter Structure

| Ch | Title | Text Sections | Lectures |
|---|---|---|---|
| 1 | Fluid Properties & Pressure | 1.1-1.7, 2.1-2.4, 2.10 | Introduction; Units, DA & Fluid Properties; Hydrostatics & Manometers; Pressure |
| 2 | Hydrostatic Forces & Buoyancy | 2.5-2.8 | Forces on Plane Surfaces; Forces on Curved Surfaces; Buoyancy |
| 3 | Bernoulli's Equation | 2.9, 3.5 | Bernoulli's Equation I; Bernoulli's Equation II |
| 4 | Introduction to Fluid Dynamics | 1.5, 3.1, 6.1-6.2, 1.9, 3.2 | Introduction to Fluid Dynamics |
| 5 | Reynolds Transport Theorem | 3.2-3.6 | RTT — Mass; RTT — Linear Momentum; RTT — Angular Momentum; RTT — Energy |
| 6 | Pipe Flow & Losses | 3.7, 6.3-6.4, 6.6-6.7 | Pipe Flow Losses I; Pipe Flow Losses II; Pipe Flow Losses III |

## Concepts Index

*(Populated as chapters are added)*

### Ch 1 — Fluid Properties & Pressure
**1.1 Introduction** — Fluid definition (substance that deforms continuously under shear), classification of matter (solid/liquid/gas/plasma), solid vs fluid distinction (solids resist shear by deforming, fluids cannot), continuum assumption (δV* ~ 10⁻⁹ mm³), density continuum definition (ρ = lim δm/δV), branches of fluid mechanics (hydrostatics, kinematics, fluid dynamics)

**1.2 Units, Dimensional Analysis & Fluid Properties** — Primary dimensions {M,L,T,Θ}, SI vs BG unit systems (1 slug = 14.5939 kg, 1 ft = 0.3048 m), CGS & English Engineering systems, SI prefixes, consistency/homogeneity rules (never mix systems, never add different dimensions), dimensional homogeneity check (Bernoulli example), extensive vs intensive properties, pressure (p = dF/dA, Pascal's law), density (ρ = m/V), specific weight (γ = ρg), specific gravity (SG = ρ/ρ_W, ref water at 4°C), bulk modulus (E_V = -dp/(dV/V)), temperature conversions (K↔°C, °R↔°F), viscosity concept (resistance to shear deformation), Newton's law of viscosity (τ = μ du/dy), no-slip condition, Newtonian vs non-Newtonian fluids (dilatant, pseudoplastic, Bingham plastic), viscosity-temperature relations (Andrade for liquids: μ = Be^{C/T}, Sutherland for gases: μ = BT^{3/2}/(T+C)), kinematic viscosity (ν = μ/ρ), inviscid fluid (μ=0), ideal fluid (inviscid + incompressible), surface tension (Υ = F/L, cohesion vs adhesion), droplet pressure (Δp = 2Υ/R), bubble pressure (Δp = 4Υ/R), capillary height (h = 2Υcosθ/γR, wetting vs non-wetting), ideal gas law (p = ρRT)

### Ch 2 — Hydrostatic Forces & Buoyancy
**2.1 Forces on Plane Surfaces** — Why hydrostatic forces matter (dam/gate/tank design), force on horizontal surface (F = pA, uniform pressure), force on inclined plane surface (pressure varies linearly along surface), resultant force (F_R = γh̄A, pressure at centroid × area), center of pressure (y_cp = ȳ + I_xx/(ȳA), always below centroid), gage pressure simplification (set p_a=0, h̄ from liquid surface), area moments of inertia for common shapes (rectangle bh³/12, triangle bh³/36, circle πR⁴/4), worked examples (vertical gate with hinge, inclined gate with stop)

### Ch 3 — Bernoulli's Equation
Pending

### Ch 4 — Introduction to Fluid Dynamics
Pending

### Ch 5 — Reynolds Transport Theorem
Pending

### Ch 6 — Pipe Flow & Losses
Pending

## Session Log

| # | Date | Task | What was done |
|---|---|---|---|
| 1 | 2026-06-09 | Course setup | Initial scaffolding: Arctic Fox theme, 6-chapter structure with 17 lectures, sidebar, placeholders, summary, progress tracker, equation sheet, 3 labs, 2 midterms + final prep. Pushed to GitHub. |
| 2 | 2026-06-09 | Ch 1.1 Introduction | Added Lec 1.1 notes from slides: applications overview, classification of matter (solid/liquid/gas/plasma), shear stress distinction, continuum assumption + density definition, branches of fluid mechanics. SVG diagrams: classification tree, ρ-vs-δV plot, branches tree. Updated sidebar, summary (clusters), formula sheet (density eq), concepts index. |
| 3 | 2026-06-09 | Ch 1.2 Units, DA & Fluid Properties | Full lecture notes from 44-slide PDF: primary/secondary dimensions, SI/BG/CGS unit systems with conversion tables, SI prefixes table, consistency & homogeneity rules, dimensional homogeneity check (Bernoulli), extensive vs intensive properties, pressure definition (p = dF/dA), density/specific weight/specific gravity/bulk modulus/temperature equations, viscosity (Newton's law τ = μ du/dy, Newtonian vs non-Newtonian classification, temperature effects, Andrade & Sutherland empirical equations, kinematic viscosity), inviscid & ideal fluid definitions, surface tension (cohesion/adhesion, droplet Δp = 2Υ/R, bubble 4Υ/R), capillarity (h = 2Υcosθ/γR with numerical examples), ideal gas law (p = ρRT with worked example). 5 embedded slide images (Newton's viscosity diagram, non-Newtonian chart, viscosity-vs-T chart, droplet FBD, capillarity diagram). 8 new formulas added to equation sheet (#2–#9). 5 new summary clusters + 8 quick-ref table entries. |
| 4 | 2026-06-09 | Structural: per-lecture files | Split ch1-notes.html → ch1-lec1.html, ch1-lec2.html, ch1-lec3.html, ch1-lec4.html. Each lecture is its own fragment file and its own sidebar page. Updated build.py fragment order, sidebar onclick handlers, fetch guide in progress.md. Prevents regression — editing one lecture never touches another file. |
| 5 | 2026-06-10 | Fix misplaced files + formula sheet reformat + summary update | Found ch1-lec4 (1.2MB) and m2prep (864KB) pushed to repo root instead of chapters/ — copied into chapters/ and re-pushed. Rewrote formula sheet: all 13 formulas now have color-coded clickable variables (6-category palette: forces/areas/properties/angles/dimensions/moments), side-by-side ✓ Use when / ✗ Not for bubbles, search bar, color legend. Added Ch 1.4 formulas (#9 absolute/gage, #10 hydrostatic p=pa+γh, #11 manometer). Added Ch 2.1 formulas (#12 F_R=γh̄A, #13 center of pressure y_cp). Summary: completed Ch 1 card (added pressure/manometry content), added Ch 2 card (forces/center of pressure), added 2 new decision trees (Pressure & Manometry, Hydrostatic Forces), updated quick-ref table with 11 rows, fixed stat card labels per spec. |
