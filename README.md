# Geometric Structure of the Electron and the Topological Origin of the Fine-Structure Constant

This repository contains the theoretical framework and numerical verification for the **Displacement Geometry Theory (DGT)**. 

## Overview

Displacement Geometry Theory (DGT) proposes that space is not a void background but a "displacement flow" advancing at the speed of light $c$. This project demonstrates that the electron's fundamental properties—charge, mass, and the fine-structure constant—are geometric necessities arising from the "topological closure" of this flow.

### Key Discoveries
- **Fine-Structure Constant ($\alpha^{-1}$):** Derived from a Lorentz self-consistent iteration of a nested helical torus.
- **Electron $g$-factor:** Explained as a holographic geometric projection across different dimensions.
- **Origin of Mass and Charge:** Identified as the geometric pressure and dimensional exchange rate of the topological knot.

## Mathematical Foundation

The core postulate defines the displacement flow as:
$$ \vec{r}(t) = a \cos(\omega t)\mathbf{i} + a \sin(\omega t)\mathbf{j} + ct\mathbf{k} $$

The inverse fine-structure constant is calculated through a recursive fixed-point iteration:
$$ L = (L_{\text{static}} + \text{Offset}) \cdot \sqrt{1 - \frac{1}{L^2}} $$

## Code Verification

The repository includes Python scripts to verify the theoretical derivations:

1. `alpha_iteration.py`: Calculates $\alpha^{-1}$ with a precision of $10^{-9}$.
2. `g_factor_holography.py`: Demonstrates the $g$-factor convergence to $10^{-14}$.
3. `mass_charge_origin.py`: Verifies the consistency between the Field Pressure Model and the Path Topology Model.

## How to Run

Ensure you have Python 3.x installed. Clone the repo and run:

```bash
python alpha_iteration.py
