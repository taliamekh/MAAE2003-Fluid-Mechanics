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
**3.1 Bernoulli's Equation I** — History (Daniel Bernoulli, Euler), derivation from the steady-flow Euler equation along a streamline (Newton's 2nd law on a fluid particle + FBD), integration → Bernoulli equation, pressure form (P + ½ρV² + ρgz = const) and two-point form, "same streamline only" restriction (unless irrotational), three interpretations (energy per unit mass J/kg, per unit volume = pressure form, per unit weight = head form), pressure/velocity/elevation heads, total head H, Energy Grade Line & Hydraulic Grade Line (HGL = EGL − velocity head V²/2g), static vs dynamic vs stagnation pressure (P₀ = P + ½ρV²), six limiting assumptions (steady, incompressible, frictionless/inviscid, along one streamline, no shaft work, no heat transfer), Example 1 (two-point Bernoulli → P₂ = 13.5 kPa), Example 2 (Torricelli tank drain, V₂ = √(2gz) = 9.9 m/s)

**3.2 Bernoulli's Equation II** — Flow-measurement devices (four devices, one idea = Bernoulli + continuity + a coefficient), stagnation recap (V = √(2(P₀−P)/ρ)), Pitot tube (piezometer reads static, Pitot reads stagnation, speed from the difference), Pitot-static tube (both pressures in one probe), Example 3 (piezometer + Pitot, V₁ = √(2g·h₃) = 1.53 m/s), Venturi meter (convergent–divergent, velocity coefficient C_v ≈ 0.98, nearly full pressure recovery, Q = C_v A₂√(2ΔP/[ρ(1−(A₂/A₁)²)])), Example 4 (air, BG units with 144 psi→lbf/ft² and g_c factors, (A₂/A₁)²=(d₂/d₁)⁴, Q = 4.48 ft³/s), orifice meter (sharp-edged plate, vena contracta, contraction coefficient C_c ≈ 0.6, discharge coefficient C_D = C_c C_v, larger permanent pressure loss), bell-mouth inlet (C_c = 1), Example 5 (wind tunnel, ½ρV² vs manometer, h = 2.67 in), continuity (A₁V₁ = A₂V₂), device trade-offs (Venturi vs orifice vs bell-mouth: cost vs pressure loss)

### Ch 4 — Introduction to Fluid Dynamics
**4.1 Introduction to Fluid Dynamics** — Fluid statics vs kinematics vs fluid dynamics (definitions), fluid kinematics (describes motion — velocity, acceleration — without reference to forces), Lagrangian vs Eulerian descriptions (Lagrangian follows an individual particle; Eulerian gives the velocity field V⃗(x,y,z,t) at fixed points in space — Eulerian used throughout), velocity field (V⃗ = u i + v j + w k), stagnation point (set V⃗ = 0; worked example → (−0.625, 1.875)), flow visualization (streamline = tangent to V⃗ at an instant, streamtube, pathline = actual track of one particle, streakline = dye trace through a fixed point, timeline = marked row of particles; streamline/pathline/streakline coincide in steady flow), steady vs unsteady flow (∂/∂t = 0 at a point), uniform vs non-uniform flow (no change in space along the flow), rate of flow — volume flow rate (Q = Av for uniform flow, Q = ∫vₙdA in general — only the normal velocity component carries flow), average velocity (Ū = Q/A), mass flow rate (ṁ = ρQ = ρŪA), Worked Example 1 (parabolic pipe profile: Q = ½V_max·πR², Ū = V_max/2, ṁ = ½ρV_max·πR²; doubling the diameter quadruples Q and ṁ while Ū is unchanged), Worked Example 2 (laminar pipe u = 3(1−25r²), R = 0.2 m → Q ≈ 0.188 m³/s, Ū ≈ 1.5 m/s), Worked Example 3 (flow between parallel plates u = u_max(1−2y/b) → Q = w·u_max·b/2, Ū = u_max/2)

### Ch 5 — Reynolds Transport Theorem
**5.1 RTT — Mass** — Motivation (system vs CV, Lagrangian vs Eulerian), system laws (mass/momentum/energy in Lagrangian form), system vs control volume definitions (fixed/moving/deforming CV), extensive B vs intensive β, generic property table (mass→1, momentum→V, energy→e), RTT derivation (coincident system+CV at time t, split at t+dt, three-region argument), general RTT: dB/dt|sys = ∂/∂t∫βρdV + ∫βρ(V·n)dA, steady-flow RTT (storage=0), conservation of mass from RTT (β=1): ∂/∂t∫ρdV + ∫ρ(V·n)dA = 0, steady incompressible continuity (ΣρVA = 0), volume conservation (ΣQ_in = ΣQ_out), worked examples (reservoir with multiple pipes, jet engine mass balance)

**5.2 RTT — Linear Momentum** — Motivation (hydrostatics = stationary fluid forces, momentum = moving fluid forces), B = mV (extensive), β = V (intensive), Newton's 2nd law for system (ΣF_ext = d(mV)/dt), linear momentum equation: ΣF_ext = ∂/∂t∫Vρ dV + ∫Vρ(V·n) dA (three terms: forces, storage, flux), steady-flow simplification (storage = 0), steady ideal flow discrete form: ΣF_ext = Σ Vρ(V·n)A, component decomposition (x and y separately), RHS sign convention (V·n < 0 at inlets, > 0 at outlets), LHS free-body diagram (F_pressure + F_weight + F_normal + F_shear), oversimplified 1-in/1-out form (ΣF = v_out·ṁ_out − v_in·ṁ_in), Example 1 (fire hose splitting flow: 3/4 to B, 1/4 to C, F_x=33.3 lb, F_y=9.92 lb, |F|=34.7 lb), moving CV at constant velocity (V_f/b = V_flow − V_b, replace all V with V_f/b), Example 2 (windshield: D=50mm, Q=8L/s, truck 5m/s, F_x=37.83N, F_y=103.9N, |F|=111N), Example 3 (concrete cart: T=918N tension, N=5190N scale), Example 4 (sluice gate: Bernoulli+continuity+momentum, F_G=6652 lb)

**5.3 RTT — Angular Momentum** — Angular momentum H_O = Σ(r⃗ × mV⃗) defined as moment of linear momentum about point O, Euler's law (rotational Newton's 2nd: ΣM = dH/dt), intensive property β = r⃗ × V⃗, general angular momentum equation via RTT: ΣM_ext = ∂/∂t∫(r⃗×V⃗)ρ dV + ∫(r⃗×V⃗)ρ(V⃗·n̂) dA (same 3-term structure as linear momentum with V⃗ replaced by r⃗×V⃗), steady ideal flow form: ΣM_ext = Σ(r⃗×V⃗)ṁ, when to use (moment/torque at a support, tipping), key strategy (choose moment point at support so unknown forces have zero arm), Example 1 (pipe elbow: Bernoulli p_A=363.354 lb/ft², continuity V_B=20 ft/s, linear momentum F_x=20.2 lb F_y=9.51 lb, angular momentum about A: M_A=6.34 lb·ft clockwise), Example 2 (fan tipping: Q=6000 ft³/min, V_B=31.83 ft/s, moment balance about base edge, d=0.7539 ft)

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
| 6 | 2026-06-10 | Ch 3 Bernoulli's Equation I & II | Added two per-lecture files from slide PDFs. **ch3-lec1** (Bernoulli I): derivation from steady-flow Euler, pressure & two-point forms, heads + EGL/HGL, static/dynamic/stagnation pressure, six assumptions, Examples 1–2 (P₂=13.5 kPa; Torricelli V=9.9 m/s). **ch3-lec2** (Bernoulli II): stagnation recap, Pitot & Pitot-static, Venturi (C_v), orifice (C_c≈0.6, C_D=C_cC_v), bell-mouth (C_c=1), continuity, Examples 3–5 (Pitot V=1.53 m/s; Venturi air Q=4.48 ft³/s; wind-tunnel h=2.67 in). All figures redrawn as Arctic Fox SVGs (no base64 bloat). Formula sheet: added Ch 3 chapter with 8 cards #14–#21 (Bernoulli energy/head forms, Euler, stagnation, continuity, Pitot, Venturi, orifice) with color-coded clickable variables. Summary: added Flow Measurement decision tree, full Ch 3 card (key ideas / when to use / traps), 5 quick-ref rows; stat bumps (refs 13→21, examples 4→9, chapters 0→1). **Structural:** converted Ch 3 from monolithic ch3-notes to per-lecture pattern — updated build.py CHAPTER_ORDER (ch3-lec1, ch3-lec2) and shell-head.html sidebar (per-lecture onclick, removed pending). All KaTeX validated (0 errors across lec1/lec2/formulas/summary). |
| 7 | 2026-06-10 | Ch 4 Introduction to Fluid Dynamics | Added single-lecture chapter (ch4-notes.html) from 28-slide PDF. Content: fluid statics/kinematics/dynamics definitions, Lagrangian vs Eulerian, velocity field V⃗=ui+vj+wk, stagnation-point worked example (−0.625, 1.875), flow visualization (streamline/streamtube/pathline/streakline/timeline, coincidence in steady flow), steady/unsteady & uniform/non-uniform, rate of flow (Q=Av, Q=∫vₙdA, Ū=Q/A, ṁ=ρQ=ρŪA), three worked examples (parabolic pipe Q=½V_max·πR² with doubling-diameter ×4 result; laminar pipe Q≈0.188 m³/s, Ū≈1.5 m/s; parallel plates Q=w·u_max·b/2). All diagrams authored as clean Arctic Fox SVGs (no base64 bloat). Formula sheet: added Ch 4 chapter with 4 cards #22–#25 (velocity field, volume flow rate, average velocity, mass flow rate) with color-coded clickable variables. Summary: added Fluid Kinematics & Rate of Flow decision tree, full Ch 4 card (key ideas / when to use / traps), 4 quick-ref rows; stat bumps (refs 21→25, examples 9→13, chapters 1→2). Sidebar: removed pending on Ch 4 item + 4.1 sub-link (prob-link still pending). Progress tracker already contained Ch 4 entries. All KaTeX validated (0 errors across ch4-notes/formulas/summary). |
| 8 | 2026-06-10 | Ch 5.2 RTT — Linear Momentum | Added ch5-lec2.html from 25-slide PDF. Content: motivation (hydrostatics→momentum), B=mV β=V, Newton's 2nd law for system, general linear momentum equation (ΣF=∂/∂t∫Vρ dV + ∫Vρ(V·n) dA), steady-flow simplification, discrete-port form, component decomposition with sign convention (V·n<0 inlets, >0 outlets), FBD approach (pressure+weight+normal+shear), oversimplified 1-in/1-out form, problem-solving checklist. Moving CV at constant velocity (V_f/b=V_flow−V_b). Four worked examples: (1) fire hose splitting flow Fx=33.3 lb Fy=9.92 lb |F|=34.7 lb, (2) windshield/moving truck Fx=37.83N Fy=103.9N |F|=111N, (3) concrete cart T=918N N=5190N, (4) sluice gate Bernoulli+continuity+momentum F_G=6652 lb. All diagrams SVG (FBD, fire hose CV, concrete cart, sluice gate). Formula sheet: added Ch 5 section with 4 cards #26–#29 (general momentum, steady ideal, simplified 1-in/1-out, moving CV). Summary: replaced Ch 5 pending with full card (key ideas/when-to-use/traps) + 5 quick-ref rows. Sidebar: removed pending from 5.1 (already had content) and 5.2. |
| 9 | 2026-06-10 | Ch 5.3 RTT — Angular Momentum | Added ch5-lec3.html from 12-slide PDF. Content: angular momentum definition (H_O = Σ r⃗×mV⃗), Euler's law (ΣM = dH/dt), intensive property β = r⃗×V⃗, general angular momentum equation via RTT (3-term structure same as linear momentum), steady ideal flow form ΣM = Σ(r⃗×V⃗)ṁ, problem-solving checklist (choose moment point at support), common mistakes. Two worked examples: (1) pipe elbow (Bernoulli→linear momentum→angular momentum: M_A=6.34 lb·ft), (2) fan tipping (moment balance: d=0.7539 ft). Six embedded slide images (compressed PNG, no SVGs per user request). Formula sheet: added 2 cards #30–#31 (general angular momentum, steady ideal flow). Summary: added angular momentum to Ch 5 key ideas/when-to-use/traps + 2 quick-ref rows; stat bumps (refs 25→31, examples 13→19). Sidebar: removed pending from 5.3. |
