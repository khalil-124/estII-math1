"""
Generate graph images for Practice Exam 3
Questions that REQUIRE visual analysis
"""

import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('images', exist_ok=True)

# ===== Q1: Composite function graph =====
def create_composite_function():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    x = np.linspace(-3, 5, 200)
    y = 3*x + 2
    
    ax.plot(x, y, 'b-', linewidth=2.5, label='h(x) = 3x + 2')
    
    # Mark key points
    ax.plot(1, 5, 'ro', markersize=10, zorder=5)
    ax.annotate('(1, 5)', (1.2, 5.3), fontsize=11)
    ax.plot(5, 17, 'go', markersize=10, zorder=5)  
    ax.annotate('(5, 17)', (5.2, 17.3), fontsize=11)
    
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-3, 7)
    ax.set_ylim(-5, 20)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graph of h(x)', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('images/ex3_q1_composite.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q1_composite.png")

# ===== Q8: Linear equation graph =====
def create_linear_graph():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Line: 6x - 3 = 5x + 4 => x = 7
    x = np.linspace(-2, 10, 200)
    y1 = 6*x - 3  # y = 3(2x-1)
    y2 = 5*x + 4
    
    ax.plot(x, y1, 'b-', linewidth=2.5, label='y = 6x - 3')
    ax.plot(x, y2, 'r-', linewidth=2.5, label='y = 5x + 4')
    
    # Intersection point
    ax.plot(7, 39, 'go', markersize=12, zorder=5)
    ax.annotate('Intersection\n(7, 39)', (7.3, 35), fontsize=10)
    
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-2, 10)
    ax.set_ylim(-10, 60)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graph showing intersection point', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('images/ex3_q8_intersection.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q8_intersection.png")

# ===== Q17: Rhombus with diagonals =====
def create_rhombus():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Rhombus vertices (diagonals 12 and 16)
    d1, d2 = 12, 16
    vertices = [(0, d2/2), (d1/2, 0), (0, -d2/2), (-d1/2, 0), (0, d2/2)]
    x_vals = [v[0] for v in vertices]
    y_vals = [v[1] for v in vertices]
    
    ax.plot(x_vals, y_vals, 'b-', linewidth=2.5)
    ax.fill(x_vals, y_vals, alpha=0.3, color='blue')
    
    # Diagonals
    ax.plot([0, 0], [-d2/2, d2/2], 'r--', linewidth=2, label=f'd2 = {d2}')
    ax.plot([-d1/2, d1/2], [0, 0], 'g--', linewidth=2, label=f'd1 = {d1}')
    
    # Labels
    ax.annotate('16', (0.5, 4), fontsize=12, color='red')
    ax.annotate('12', (3, 0.5), fontsize=12, color='green')
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Rhombus with diagonals', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('images/ex3_q17_rhombus.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q17_rhombus.png")

# ===== Q21: Parallel lines =====
def create_parallel_lines():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    x = np.linspace(-5, 5, 200)
    y1 = -3*x + 7  # Original
    y2 = -3*x + 2  # Parallel
    y3 = -3*x - 3  # Parallel
    
    ax.plot(x, y1, 'b-', linewidth=2.5, label='y = -3x + 7')
    ax.plot(x, y2, 'r--', linewidth=2, label='y = -3x + 2')  
    ax.plot(x, y3, 'g--', linewidth=2, label='y = -3x - 3')
    
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-3, 5)
    ax.set_ylim(-10, 15)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Parallel Lines (same slope = -3)', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('images/ex3_q21_parallel.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q21_parallel.png")

# ===== Q32: Coin toss tree diagram =====
def create_probability_tree():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Tree diagram for 2 coin tosses
    # Level 0: Start
    ax.plot(0, 0, 'ko', markersize=10)
    ax.annotate('Start', (-0.3, 0.2), fontsize=10)
    
    # Level 1: First toss
    ax.plot([-2, 2], [1, 1], 'ko', markersize=10)
    ax.plot([0, -2], [0, 1], 'b-', linewidth=2)
    ax.plot([0, 2], [0, 1], 'b-', linewidth=2)
    ax.annotate('H', (-2.3, 1), fontsize=12, fontweight='bold')
    ax.annotate('T', (2.1, 1), fontsize=12, fontweight='bold')
    ax.annotate('1/2', (-1.2, 0.3), fontsize=10)
    ax.annotate('1/2', (0.8, 0.3), fontsize=10)
    
    # Level 2: Second toss
    positions = [(-3, 2), (-1, 2), (1, 2), (3, 2)]
    outcomes = ['HH', 'HT', 'TH', 'TT']
    
    for i, (pos, outcome) in enumerate(zip(positions, outcomes)):
        ax.plot(pos[0], pos[1], 'ro' if 'H' in outcome else 'go', markersize=10)
        ax.annotate(outcome, (pos[0]-0.2, pos[1]+0.3), fontsize=11, fontweight='bold')
    
    # Lines from level 1 to level 2
    ax.plot([-2, -3], [1, 2], 'b-', linewidth=1.5)
    ax.plot([-2, -1], [1, 2], 'b-', linewidth=1.5)
    ax.plot([2, 1], [1, 2], 'b-', linewidth=1.5)
    ax.plot([2, 3], [1, 2], 'b-', linewidth=1.5)
    
    # Highlight "at least one H" outcomes
    ax.annotate('At least 1 H: HH, HT, TH = 3 outcomes', (0, 3), fontsize=12, 
                ha='center', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    ax.annotate('P(at least 1 H) = 3/4', (0, 2.6), fontsize=11, ha='center')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-0.5, 3.5)
    ax.axis('off')
    ax.set_title('Tree Diagram: 2 Coin Tosses', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('images/ex3_q32_tree.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q32_tree.png")

# ===== Q40: Circle with chord =====
def create_circle_chord():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Circle
    theta = np.linspace(0, 2*np.pi, 100)
    r = 10
    x_circle = r * np.cos(theta)
    y_circle = r * np.sin(theta)
    ax.plot(x_circle, y_circle, 'b-', linewidth=2)
    
    # Center O
    ax.plot(0, 0, 'ro', markersize=8)
    ax.annotate('O', (0.5, 0.5), fontsize=12, fontweight='bold')
    
    # Chord AB (length 12, so AM = 6)
    # If OM = 8, then chord is at height 8, with half-length = sqrt(100-64) = 6
    ax.plot([-6, 6], [8, 8], 'g-', linewidth=3)
    ax.plot(-6, 8, 'go', markersize=8)
    ax.plot(6, 8, 'go', markersize=8)
    ax.annotate('A', (-6.5, 8.5), fontsize=12, fontweight='bold')
    ax.annotate('B', (6.2, 8.5), fontsize=12, fontweight='bold')
    
    # Midpoint M
    ax.plot(0, 8, 'mo', markersize=8)
    ax.annotate('M', (0.3, 8.5), fontsize=12, fontweight='bold')
    
    # OM line
    ax.plot([0, 0], [0, 8], 'r-', linewidth=2)
    ax.annotate('OM = 8', (0.5, 4), fontsize=11, color='red')
    
    # Radius OA
    ax.plot([0, -6], [0, 8], 'b--', linewidth=1.5)
    ax.annotate('r = 10', (-4, 3), fontsize=11, color='blue')
    
    # Right angle at M
    ax.plot([-0.8, -0.8, 0], [8, 7.2, 7.2], 'k-', linewidth=1)
    
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Circle with Chord AB, Midpoint M', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('images/ex3_q40_chord.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex3_q40_chord.png")

if __name__ == "__main__":
    print("Generating images for Exam 3...")
    create_composite_function()
    create_linear_graph()
    create_rhombus()
    create_parallel_lines()
    create_probability_tree()
    create_circle_chord()
    print("\n[OK] All Exam 3 images generated!")
