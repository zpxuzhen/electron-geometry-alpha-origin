# Copyright © 2026-4-23 [Xu, Zhen]. 
# Derived from Displacement Geometry Theory (DGT).
# This script calculates the inverse fine-structure constant through 
# topological path integration and relativistic self-consistency.

import math

def calculate_displacement_trace():
    # --- Fundamental Parameters ---
    n = 137.0  # Topological weaving base (discrete units)
    pi = math.pi
    
    # --- 1. Derivation of Discrete Geometric Components ---
    # d1: First-order correction (1D/Linear) - Helical intrinsic path increment
    d1 = (pi ** 2) / (2 * n)          
    
    # d2: Second-order correction (2D/Surface) - Discrete area overlap deficit
    d2 = -(1.0 / (2 * n**2))          
    
    # d3: Third-order correction (3D/Volume) - 4D projection dimensional tension
    d3 = (4 * pi - 1) / (n ** 3)      
    
    # Static Geometric Skeleton (L_static)
    l_static = n + d1 + d2 + d3       
    
    # Phase-Flip Compensation (Offset)
    # Represents the 0.5 rotation (180°) required for fermion topological closure
    offset = 0.5 / n                  
    
    # Experimental Reference Target: 
    # Weighted mean of Berkeley 2018 (Cs) and Paris 2020 (Rb)
    # Berkeley 2018: 137.035999046
    # Paris 2020:    137.035999206
    target = 137.035999126            
    
    current_val = l_static
    print(f"--- DGT Self-Consistent Iteration for alpha^-1 ---")
    print(f"Static Baseline (L_static): {l_static:.12f}")
    print(f"{'Iter':<4} | {'Converged Value':<18} | {'Delta':<15}")
    print("-" * 55)

    # --- 2. Lorentz Self-Consistent Iteration ---
    # Models the relativistic path contraction (Lorentz contraction) 
    # caused by the displacement flow rotating within its own induced field.
    for i in range(1, 11):
        prev_val = current_val
        
        # Beta represents the advancement efficiency ratio (c / v_total)
        # In DGT, v_total = L * c, thus beta = 1/L
        beta = 1.0 / current_val      
        
        # Inverse Lorentz Factor (gamma^-1)
        gamma_inv = math.sqrt(1.0 - beta**2)
        
        # Core Mapping Function: L = (Skeleton + Offset) * Contraction_Factor
        current_val = (l_static + offset) * gamma_inv
        
        # Calculate convergence delta
        diff = current_val - prev_val
        print(f"{i:<4} | {current_val:.12f} | {diff:.2e}")
        
    print("-" * 55)
    print(f"Steady-State Fixed Point: {current_val:.12f}")
    print(f"Theoretical Residual vs Target: {current_val - target:.12e}")

if __name__ == "__main__":
    calculate_displacement_trace()
