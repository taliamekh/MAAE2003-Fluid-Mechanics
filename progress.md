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

**1.3 Hydrostatics & Manometers** — Hydrostatic condition (V=0, shear=0), pressure as scalar (equal in all directions at a point), wedge element proof (px=pz=pn=p), Pascal's Law (pressure change transmitted throughout confined incompressible fluid), hydrostatic pressure gradient (dp/dz = -γ = -ρg, dp/dx=dp/dy=0), incompressible pressure-depth relation (p2-p1 = -γ(z2-z1), z+p/γ = const), pressure independent of container shape, same-horizontal-plane rule (same pressure only in same continuous fluid), absolute/gage/vacuum pressure definitions (p_gage = p_abs - p_atm), pressure head (h = p_gage/γ), specific weight table (air through mercury at 20°C), ocean/atmosphere pressure distribution (above: p ≈ pa - bγ_air, below: p ≈ pa + hγ_water), compressible fluid pressure (dp/p = -g/(RT)dz), troposphere formula (p = p0(1-Bz/T0)^5.26, B=0.00650 K/m), isothermal atmosphere (p = p0·e^(-gz/RT)), U.S. Standard Atmosphere (T0=288.16K, B=0.00650K/m), hydraulic machinery (F1/A1=F2/A2, mechanical advantage=A2/A1), barometer (p_atm = γh), manometry general rule (down: +γh, up: -γh, jump across at same level), U-tube/inclined-tube/differential manometers, differential manometer result (pa-pb = (ρ2-ρ1)gh — don't forget ρ1), Examples: 2.1 (lake depth pressure), pipe AB (force on cap), 2.2 (altitude pressure comparison), 2.4 (multi-fluid manometer)

### Ch 2 — Hydrostatic Forces & Buoyancy
Pending

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
| 5 | 2026-06-09 | Midterm 2 Prep | Added full Midterm 2 Prep page from Sample Midterm II PDF. Scope banner (Ch 3–5), past exam card, exam format table, 3-tier study priority (high: linear momentum/Bernoulli/continuity/manometry, medium: angular momentum/hydrostatic pressure/flow types, low: energy eq/unsteady/boundary layer), skip list, insider tips, problem-type→strategy table, topic checklist with localStorage persistence. Fully solved all 5 exam questions: Q1a (angular momentum MCQ → b), Q1b (streamline velocity MCQ → a), Q1c (tank mass conservation → 0.012 kg/s), Q2 (sluice gate momentum — 5-step Bernoulli+continuity+momentum derivation), Q3 (pipe flow with manometer — 5-step Bernoulli+continuity+manometry → Q=3.24 m³/s). All solutions include embedded exam images, thought process, formulas-needed block, step-by-step work, boxed answers, tips, and concept bridges. Exam debrief with topic map, patterns, time allocation. Common traps section. Updated progress tracker with expanded MT2 sub-items. |
| 6 | 2026-06-09 | Midterm 2 Prep page | Built full MT2 prep page from Brightspace announcement: scope banner (Ch 3 Bernoulli I+II, Ch 4 Intro to Fluid Dynamics, Ch 5 RTT Mass/LinMom/AngMom — NOT Energy), exam logistics (June 11, 11:35 AM, 90 min, ME 3380, MCQ + numerical, equation sheet provided), 3-tier study priority (high: linear momentum/Bernoulli+continuity/mass conservation/flow measurement; medium: angular momentum/streamlines/heads/CV selection; low: boundary layer/flow classification/shear), skip list (RTT-Energy, pipe flow, derivations, hydrostatics, compressible), 8 insider tips, 9-row problem-type→strategy table, 24-item topic checklist with localStorage, 6 common trap cards. Added prep CSS to shell-head. Expanded progress tracker MT2 sub-items. |
| 6 | 2026-06-10 | Structural: MT2 sub-page | Split m2prep.html into prep overview (scope/priorities/tips/strategy/checklist/traps) and m2prep-sample.html (Sample Midterm II fully solved). Midterm 2 sidebar item now expandable with "Practice Midterm" sub-link. Back-link in sample page returns to prep overview. Updated build.py fragment order (25 total). |
| 7 | 2026-06-10 | Ch 1.3 Hydrostatics & Manometers | Full lecture notes from 35-slide PDF: hydrostatic condition, pressure as scalar (wedge element proof), Pascal's Law, hydrostatic pressure gradient derivation (dp/dz = -γ), incompressible pressure-depth relation, same-fluid horizontal-plane rule, absolute/gage/vacuum pressure, pressure head, specific weight table, ocean/atmosphere distribution, compressible fluid (troposphere p = p0(1-Bz/T0)^5.26 and isothermal p = p0·e^(-gz/RT)), U.S. Standard Atmosphere, hydraulic machinery (Pascal's Law application), manometry (barometer, multi-fluid, U-tube, inclined, differential), 4 worked examples (2.1, pipe AB, 2.2, 2.4). 10 embedded slide images. 9 new formulas (#10–#18). 4 summary clusters + 7 quick-ref entries. Fixed build.py to resolve fragments from both root and chapters/. |
