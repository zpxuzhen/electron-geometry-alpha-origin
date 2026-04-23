# Copyright © 2026-4-23 [Xu, Zhen]. 
# Derived from Displacement Geometry Theory (DGT).
# This script calculates the electron g-factor through holographic 
# geometric projections and topological corrections.

import math

def calculate_g_factor():
    # --- Constant Definitions ---
    # zeta: Path Abundance (Inverse Fine-Structure Constant)
    zeta = 137.035999125536  
    
    # Experimental Reference Value (Northwestern University 2023)
    g_experimental = 2.00231930436118
    
    # x: Phase Perturbation Factor (Topological Torsion Density)
    x = 1 / (math.pi * zeta)
    
    # --- Order-by-Order Geometric Corrections ---
    
    # d1: First-order correction (Linear/Helical Path Overflow)
    d1 = 1 / (2 * math.pi * zeta)
    
    # d2: Second-order correction (Planar/Centripetal Compression)
    d2 = -3 / (8 * (math.pi**2) * (zeta**2))
    
    # d3: Third-order (Volumetric) components
    # d3_base: Intrinsic Lattice Volume contribution
    d3_base = 5 / (16 * (zeta**3))
    
    # delta_bend: Toroidal Bending Work (Overcoming Vacuum Impedance)
    delta_bend = (4 * math.pi - 1) / ((math.pi * zeta)**3)
    
    # d3_eff: Effective Volumetric term after applying Stitching Efficiency (1-x)
    d3_sum = (d3_base + delta_bend)
    d3_final = d3_sum * (1 - x)
    
    # d4: Fourth-order correction (4D Spacetime Projection Tension)
    d4 = -35 / 128 * (x**4)
    
    # d5: Fifth-order correction (Topological Granularity / Pixel Limit)
    # Note: This term is external noise and does not undergo spin-flip (no factor of 2)
    d5 = -1 / (zeta**5)
    
    # --- Cumulative Calculation Stages ---
    # Format: (Stage Name, Delta Value, Noise Term)
    steps = [
        ("Baseline (g=2)", 0, 0),
        ("m=1 (Helical Path)", d1, 0),
        ("m=2 (Planar Comp.)", d2, 0),
        ("m=3.1 (Lattice Vol.)", d3_base, 0),
        ("m=3.2 (Bending Work)", delta_bend, 0),
        ("m=3.3 (Stitch Eff.)", d3_final - (d3_base + delta_bend), 0),
        ("m=4 (4D Tension)", d4, 0),
        ("m=5 (Pixel Limit)", 0, d5)
    ]
    
    current_g = 2.0
    print(f"{'Correction Stage':<22} | {'Cumulative g':<18} | {'Residual':<12}")
    print("-" * 65)
    
    for name, delta, noise in steps:
        if name == "m=3.3 (Stitch Eff.)":
            # Apply the (1-x) efficiency factor to the cumulative d3 sum
            diff = (d3_sum * (1 - x)) - (d3_sum)
            current_g += 2 * diff
        elif noise == 0:
            # Standard spin-flip related geometric corrections (multiplied by 2)
            current_g += 2 * delta
        else:
            # External granularity noise (not multiplied by 2)
            current_g += noise
            
        residual = current_g - g_experimental
        print(f"{name:<22} | {current_g:.14f} | {residual:.2e}")

if __name__ == "__main__":
    calculate_g_factor()