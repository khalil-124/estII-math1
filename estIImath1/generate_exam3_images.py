"""Generate graph images for Practice Exam 3 - NO ANSWER SPOILERS"""
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q1: Composite function - show graph, student reads values
def create_composite_function():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-3, 7, 200)
    y = 3*x + 2
    ax.plot(x, y, 'b-', linewidth=2.5, label='h(x) = 3x + 2')
    # Only mark points WITHOUT y-values - student must read them
    ax.plot(1, 5, 'ro', markersize=8, zorder=5)
    ax.plot(5, 17, 'go', markersize=8, zorder=5)
    # NO annotations showing y-values
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-3, 7)
    ax.set_ylim(-5, 20)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graph of h(x) = 3x + 2', fontsize=14, fontweight='bold')
    ax.legend()
    plt.tight_layout()
    plt.savefig('images/ex3_q1_composite.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q1_composite.png")

# Q8: Linear equation - show graphs, student finds intersection
def create_linear_graph():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-2, 10, 200)
    y1 = 6*x - 3
    y2 = 5*x + 4
    ax.plot(x, y1, 'b-', linewidth=2.5, label='y = 6x - 3')
    ax.plot(x, y2, 'r-', linewidth=2.5, label='y = 5x + 4')
    # Intersection point shown but NOT labeled with coordinates
    ax.plot(7, 39, 'go', markersize=12, zorder=5)
    ax.annotate('Intersection', (7.3, 35), fontsize=10)
    # NO (7, 39) label!
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-2, 10)
    ax.set_ylim(-10, 60)
    ax.legend()
    ax.set_title('Find x-value of intersection', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex3_q8_intersection.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q8_intersection.png")

# Q17: Rhombus - show diagonals with labels (needed to solve)
def create_rhombus():
    fig, ax = plt.subplots(figsize=(8, 8))
    d1, d2 = 12, 16
    vertices = [(0, d2/2), (d1/2, 0), (0, -d2/2), (-d1/2, 0), (0, d2/2)]
    x_vals = [v[0] for v in vertices]
    y_vals = [v[1] for v in vertices]
    ax.plot(x_vals, y_vals, 'b-', linewidth=2.5)
    ax.fill(x_vals, y_vals, alpha=0.3, color='blue')
    # Diagonals with measurements (needed for area calculation)
    ax.plot([0, 0], [-d2/2, d2/2], 'r--', linewidth=2)
    ax.plot([-d1/2, d1/2], [0, 0], 'g--', linewidth=2)
    ax.annotate('d2 = 16', (0.5, 4), fontsize=12, color='red')
    ax.annotate('d1 = 12', (3, 0.5), fontsize=12, color='green')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Rhombus with diagonals', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex3_q17_rhombus.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q17_rhombus.png")

# Q21: Parallel lines - show lines but don't label slope
def create_parallel_lines():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-5, 5, 200)
    y1 = -3*x + 7
    y2 = -3*x + 2
    y3 = -3*x - 3
    ax.plot(x, y1, 'b-', linewidth=2.5, label='y = -3x + 7')
    ax.plot(x, y2, 'r--', linewidth=2, label='Line 2 (parallel)')  
    ax.plot(x, y3, 'g--', linewidth=2, label='Line 3 (parallel)')
    # NO slope labels - that's what the question asks!
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-3, 5)
    ax.set_ylim(-10, 15)
    ax.legend()
    ax.set_title('Parallel Lines - What is their slope?', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex3_q21_parallel.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q21_parallel.png")

# Q32: Coin toss tree - show outcomes but NOT probability
def create_probability_tree():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(0, 0, 'ko', markersize=10)
    ax.annotate('Start', (-0.3, 0.2), fontsize=10)
    ax.plot([-2, 2], [1, 1], 'ko', markersize=10)
    ax.plot([0, -2], [0, 1], 'b-', linewidth=2)
    ax.plot([0, 2], [0, 1], 'b-', linewidth=2)
    ax.annotate('H', (-2.3, 1), fontsize=12, fontweight='bold')
    ax.annotate('T', (2.1, 1), fontsize=12, fontweight='bold')
    ax.annotate('1/2', (-1.2, 0.3), fontsize=10)
    ax.annotate('1/2', (0.8, 0.3), fontsize=10)
    positions = [(-3, 2), (-1, 2), (1, 2), (3, 2)]
    outcomes = ['HH', 'HT', 'TH', 'TT']
    for i, (pos, outcome) in enumerate(zip(positions, outcomes)):
        ax.plot(pos[0], pos[1], 'ro' if 'H' in outcome else 'go', markersize=10)
        ax.annotate(outcome, (pos[0]-0.2, pos[1]+0.3), fontsize=11, fontweight='bold')
    ax.plot([-2, -3], [1, 2], 'b-', linewidth=1.5)
    ax.plot([-2, -1], [1, 2], 'b-', linewidth=1.5)
    ax.plot([2, 1], [1, 2], 'b-', linewidth=1.5)
    ax.plot([2, 3], [1, 2], 'b-', linewidth=1.5)
    # NO probability answer shown!
    ax.annotate('Find: P(at least one H) = ?', (0, 3), fontsize=12, 
                ha='center', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
    ax.set_xlim(-4, 4)
    ax.set_ylim(-0.5, 3.5)
    ax.axis('off')
    ax.set_title('Tree Diagram: 2 Coin Tosses', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex3_q32_tree.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q32_tree.png")

# Q40: Circle with chord - show setup, NOT answers
def create_circle_chord():
    fig, ax = plt.subplots(figsize=(8, 8))
    theta = np.linspace(0, 2*np.pi, 100)
    r = 10
    ax.plot(r * np.cos(theta), r * np.sin(theta), 'b-', linewidth=2)
    ax.plot(0, 0, 'ro', markersize=8)
    ax.annotate('O', (0.5, 0.5), fontsize=12, fontweight='bold')
    # Chord AB at height sqrt(100-36) = 8
    ax.plot([-6, 6], [8, 8], 'g-', linewidth=3)
    ax.plot(-6, 8, 'go', markersize=8)
    ax.plot(6, 8, 'go', markersize=8)
    ax.annotate('A', (-6.5, 8.5), fontsize=12, fontweight='bold')
    ax.annotate('B', (6.2, 8.5), fontsize=12, fontweight='bold')
    ax.plot(0, 8, 'mo', markersize=8)
    ax.annotate('M', (0.3, 8.5), fontsize=12, fontweight='bold')
    # OM line drawn but NOT labeled with 8
    ax.plot([0, 0], [0, 8], 'r-', linewidth=2)
    ax.annotate('OM = ?', (0.5, 4), fontsize=11, color='red')
    # Radius - given info
    ax.annotate('radius = 10', (-5, -8), fontsize=11)
    ax.annotate('AB = 12', (0, 9), ha='center', fontsize=11)
    ax.plot([-0.8, -0.8, 0], [8, 7.2, 7.2], 'k-', linewidth=1)  # Right angle
    ax.set_xlim(-12, 12)
    ax.set_ylim(-12, 12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Circle with Chord AB, M is midpoint', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex3_q40_chord.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex3_q40_chord.png")

if __name__ == "__main__":
    print("Generating Exam 3 images (NO SPOILERS)...")
    create_composite_function()
    create_linear_graph()
    create_rhombus()
    create_parallel_lines()
    create_probability_tree()
    create_circle_chord()
    print("\n[OK] All Exam 3 images done!")
