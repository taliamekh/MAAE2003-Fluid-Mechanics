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

**2.2 Forces on Curved Surfaces** — Why curved surfaces differ (pressure ⊥ at every point but its direction swings along the surface, so one pressure×area no longer works), resolve-into-components strategy (split resultant into horizontal F_H + vertical F_V, solve each as a known problem, recombine), horizontal component (F_H = (γh_CG+p_a)A_proj = flat-plate force on the vertical projection; keep p_a in a pressurised chamber), vertical component (F_V = γ∀_above (+ p_aA) = weight of fluid above the surface, split into simple sub-volumes), real-vs-imaginary fluid subtlety (fluid physically above ⇒ F_V down; fluid below ⇒ imaginary column, F_V up = buoyancy preview), line of action (z_CP = h_CG + I_xx/(h_CG·A_proj) locates F_H; x_CP = ΣW_ix_i/F_V locates F_V via moment balance), resultant (F = √(F_H²+F_V²), θ = tan⁻¹(F_V/F_H)), circular-arc check (resultant passes through the centre), quarter-circle centroid 4r/3π, worked examples (2-D circular arc → F=146.9 kN @ 48°, x_CP=0.957 m, z_CP=5.067 m; 3-D hemisphere in 35 kPa chamber → F_x=163.9 kN, F_z=15.0 kN ↑, F_y=0 by symmetry)

**2.3 Buoyancy** — Archimedes' principle (immersed body: buoyant force = weight of displaced fluid; floating body: displaces its own weight; force always upward, independent of body material/shape/depth), two derivations (forces on upper vs lower surface F_B=F_V(2)−F_V(1); summation of elemental pressure forces F_B=∫(p₂−p₁)dA_H=γ·volume), **buoyant force** F_B=γ_fluid∀_displaced (whole body if fully submerged, submerged part if floating), centre of buoyancy (centroid of the displaced volume, ≠ centre of gravity in general — sets stability), floating-body equilibrium (F_B=W ⇒ γ_f∀_sub=γ_b∀_body), submerged fraction (∀_sub/∀_body=ρ_b/ρ_f=SG_b/SG_f; ice ≈ 92% submerged), float/sink/hover test (compare fully-submerged F_B with W, equivalently ρ_body with ρ_fluid), solution recipe (FBD with F_B up / W down / cable, ΣF_V=0, apparent weight = W−F_B, watch tether direction), worked examples (tethered instrument package → T=556 N; steel pipe in glycerin → F_B=274 N < W=277 N, sinks; floating wooden cone → h=H·SG^{1/3}=27 cm, 3 cm protrudes)

### Ch 3 — Bernoulli's Equation
Pending

### Ch 4 — Introduction to Fluid Dynamics
Pending

### Ch 5 — Reynolds Transport Theorem
**5.1 RTT — Mass** — System (Lagrangian, fixed mass) vs control volume (Eulerian, fixed region) + control surface (CS); the four system laws (dm/dt=0, F=d(mV)/dt, M=d/dt∫(r×V)dm, Q̇−Ẇ=dE/dt); three CV types (fixed/moving/deforming); extensive B vs intensive β=dB/dm (mass→β=1, momentum→β=V, energy→β=e); flow rate & flux through a surface (Q=∫(V·n)dA, ṁ=∫ρ(V·n)dA, swept-volume d∀=(V·n)dA dt); outward-normal sign convention (V·n>0 out, <0 in, =0 wall); average velocity (V̄=(1/A)∫u dA ⇒ Q=V̄A, ṁ=ρV̄A); net flow through a CS (Q=ΣVᵢ·Aᵢ=∫V·dA, Ḃ_out=∫βρV·dA); RTT derivation (fixed CV + coincident moving system, ΔM_in/ΔM_out slivers, limit → storage + flux); **RTT** dB_sys/dt = d/dt∫_CV βρ d∀ + ∫_CS βρ(V·n)dA; steady-flow simplification (storage→0); continuity (β=1): general d/dt∫ρd∀+∫ρ(V·n)dA=0, steady Σṁ_out=Σṁ_in, steady-uniform Σ(ρAV)_out=Σ(ρAV)_in, incompressible ΣQ_out=ΣQ_in; moving CV (relative velocity Vᵣ=V−Vs); material-derivative analogy (D/Dt=∂/∂t+V·∇); worked examples (reservoir rise rate → 13.9 cm/hr unsteady; jet-engine exit velocity → 85.1 m/s steady compressible)

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
| 6 | 2026-06-10 | Ch 5.1 RTT — Mass | Added new chapter: created `chapters/ch5-lec1.html` (RTT — Conservation of Mass) from 38-slide PDF. Content: system vs CV + control surface, the four system laws, three CV types, extensive/intensive B & β, flow rate/flux through a surface with sign convention, average velocity, net flow through a CS, full RTT derivation (coincident moving system + fixed CV, ΔM_in/ΔM_out limit), steady-flow simplification, continuity equation (general → steady → incompressible forms), moving CV (relative velocity), material-derivative analogy, problem-solving strategy + recap. 6 hand-built theme SVGs (flux patch, control-surface signs, RTT derivation 2-panel, branching-duct continuity, reservoir, jet engine). 2 worked examples (reservoir → 13.9 cm/hr; engine → 85.1 m/s). Formula sheet: added Ch 5 section with #14 RTT, #15 continuity (general), #16 steady-flow mass balance, #17 ṁ=ρAV, #18 Q=V̄A, #19 RTT moving CV — all with color-coded clickable variables. Summary: added Continuity/RTT decision tree, replaced Ch 5 pending placeholder with full chapter card (key ideas / when-to-use / traps), added 5 Ch 5 quick-ref rows, stat cards 13→19 references & 4→6 examples. Sidebar: converted Ch 5 to per-lecture pattern (un-pended 5.1). build.py: Ch 5 per-lecture ordering (ch5-lec1..lec4). Rebuilt MAAE2300-notes.html (27 fragments). |
| 7 | 2026-06-10 | Ch 5.1 — replace SVGs with slide figures | Per request, replaced all 6 hand-built SVGs in ch5-lec1.html with the corresponding actual figures from the lecture PDF (slides 10, 15, 19, 33, 34, 36 → Figures 5.1.1–5.1.6). Rendered pages at 250 DPI, cropped each figure tightly (excluding titles/footers/body text), and encoded as lossless WebP (pixel-identical to source, verified AE=0). WebP chosen over PNG for ~43% smaller base64 with zero quality loss (~1.0 MB total vs ~1.76 MB PNG). Embedded as `data:image/webp;base64` in the existing figure-box wrappers; captions and per-figure widths preserved. Rebuilt MAAE2300-notes.html. |
| 8 | 2026-06-10 | Ch 5.1 — add 3 concept figures | Added three figures to ch5-lec1.html (insert-only; verified no regression via normalized diff against original — every existing card/equation/figure byte-identical). (1) Fig 5.1.A: a new themed SVG comparing a system (fixed mass, boundary drifts with the flow, no flux) vs a control volume (fixed region, mass crosses the control surface) — placed after the "Two Ways to Define Your Stuff" card; built per diagram-rules with label-collision checks, uses live Arctic Fox CSS vars. (2) Fig 5.1.B: uploaded "Types of Control Volume" slide image (fixed/moving/deforming) — placed at the end of the System-vs-CV section. (3) Fig 5.1.C: uploaded "Moving System and fixed Control Volume" slide image — placed leading the Derivation section, ahead of Fig 5.1.3. Both uploads trimmed + lossless WebP (AE=0). Used letter labels (A/B/C) to avoid renumbering the existing 5.1.1–5.1.6 sequence and an internal "Figure 5.1.2" prose reference. Rebuilt MAAE2300-notes.html. |
| 9 | 2026-06-20 | Ch 2.2 Forces on Curved Surfaces | Replaced ch2-lec2 stub with full lecture from 18-slide PDF. Content: why curved surfaces differ (pressure ⊥ but direction varies along the wall), resolve-into-components strategy, horizontal force = flat-plate force on the vertical projection (F_H=(γh_CG+p_a)A_proj) + z_CP location, vertical force = weight of fluid above real/imaginary (F_V=γ∀+p_aA) + x_CP location via moment balance, real-vs-imaginary fluid subtlety (buoyancy preview), resultant F=√(F_H²+F_V²) & θ=tan⁻¹(F_V/F_H), circular-arc sanity check. 8 figures extracted from PDF (pdftoppm 200 DPI, cropped; lossless WebP for line diagrams AE=0, lossy q82 for 2 textured illustration panels; ~707 KB total). 2 worked examples (2-D circular arc → F=146.9 kN @ 48°, x_CP=0.957 m, z_CP=5.067 m; 3-D hemisphere in 35 kPa chamber → F_x=163.9 kN, F_z=15.0 kN ↑, F_y=0). Formula sheet: 6 new Ch 2 cards #32 resultant, #33 angle, #34 horizontal component, #35 vertical component, #36 x_CP, #37 z_CP — color-coded clickable variables, data-vars keys ordered most-specific-first so the popup matcher resolves subscripts correctly (verified via real KaTeX render + faithful wireUpVarPopups DOM replica: 0 mismatches across all 6 cards). Summary: 4 curved-surface decision rules, 3 traps, 3 quick-ref rows, stats 31→37 refs & 19→21 examples. Sidebar: un-pended 2.2 (2.3 Buoyancy still pending). Validation: 281/281 KaTeX expressions render clean, all HTML tags balanced, 8 valid image data-URIs. Rebuilt MAAE2300-notes.html (33 fragments) after fetching all fragments fresh per rebuild rule. Verified all 5 pushed files via GitHub API size match (incl. 19.57 MB monolith, no truncation). |
| 10 | 2026-06-22 | Ch 2.3 Buoyancy | Replaced ch2-lec3 stub (179 B) with full lecture from 15-slide PDF. Content: Archimedes' principle (immersed + floating statements), two derivations of the buoyant force (upper/lower surface forces F_B=F_V(2)−F_V(1); elemental pressure-force integral F_B=γ·volume), buoyant force F_B=γ_fluid∀_displaced, centre of buoyancy (centroid of displaced volume vs CG), floating-body equilibrium F_B=W ⇒ γ_f∀_sub=γ_b∀_body, submerged fraction ∀_sub/∀_body=SG_b/SG_f, float/sink/hover density test, solution recipe (FBD + ΣF_V=0, apparent weight = W−F_B, tether direction). 6 figures from PDF (pdftoppm 220 DPI, cropped; lossless WebP for line art AE=0, lossy q82 for textured panels) + 1 hand-built cone-geometry SVG (similar-triangles derivation, label-collision checked). 3 worked examples (tethered instrument package → T=556 N; steel pipe in glycerin → F_B=274 N < W=277 N, sinks; floating wooden cone → h=H·SG^{1/3}=27 cm, 3 cm protrudes). Formula sheet: 3 new Ch 2 cards #38 buoyant force, #39 floating body F_B=W, #40 submerged fraction — color-coded clickable variables, data-vars most-specific-first (verified via live wireUpVarPopups on real Chromium: 0 unresolved across all 3 cards). Summary: new Buoyancy & Floating Bodies decision tree, Ch 2 card +1 key idea / +4 when-to-use / +2 traps, 4 quick-ref rows, stats 37→40 refs & 21→24 examples. Sidebar: un-pended 2.3 (Ch 2 now complete). Validation: real headless Chromium — 159/159 KaTeX in 2.3 render clean (0 errors), 6/6 images loaded, cone SVG labels clean, all variable popups wired; summary 195 KaTeX clean; 0 console/page errors. Rebuilt MAAE2300-notes.html (33 fragments) after fetching all fragments fresh per rebuild rule. Verified all 5 pushed files via GitHub API size match (incl. 20.63 MB monolith, no truncation). Commit 029b98ba60. |
