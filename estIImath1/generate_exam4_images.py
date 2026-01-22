"""Generate graph images for Practice Exam 4 - NO ANSWER SPOILERS"""
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q1: Composite function - show graphs WITHOUT answer annotations
def create_q1():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-2, 6, 200)
    f = x**2 - 4*x + 3
    g = x + 1
    ax.plot(x, f, 'b-', linewidth=2.5, label='f(x) = x^2 - 4x + 3')
    ax.plot(x, g, 'r--', linewidth=2, label='g(x) = x + 1')
    # NO answer points marked
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2, 6)
    ax.set_ylim(-2, 8)
    ax.legend()
    ax.set_title('Graphs of f(x) and g(x)', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex4_q1_functions.png', dpi=150)
    plt.close()
    print("[OK] ex4_q1_functions.png")

# Q17: Trapezoid - show figure with measurements (needed to solve)
def create_q17():
    fig, ax = plt.subplots(figsize=(8, 6))
    vertices = [(0, 0), (10, 0), (8, 4), (2, 4), (0, 0)]
    x_vals = [v[0] for v in vertices]
    y_vals = [v[1] for v in vertices]
    ax.fill(x_vals, y_vals, alpha=0.3, color='blue')
    ax.plot(x_vals, y_vals, 'b-', linewidth=2)
    ax.annotate('b1 = 10', (5, -0.5), ha='center', fontsize=12)
    ax.annotate('b2 = 6', (5, 4.5), ha='center', fontsize=12)
    ax.plot([0, 0], [0, 4], 'r--', linewidth=2)
    ax.annotate('h = 4', (-0.8, 2), fontsize=12, color='red')
    ax.set_xlim(-2, 12)
    ax.set_ylim(-1, 6)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Trapezoid', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex4_q17_trapezoid.png', dpi=150)
    plt.close()
    print("[OK] ex4_q17_trapezoid.png")

# Q21: Perpendicular lines - show only original line, NOT the perpendicular
def create_q21():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-3, 5, 200)
    original = -0.5*x + 2  # 2x + 4y = 8 -> y = -x/2 + 2
    ax.plot(x, original, 'b-', linewidth=2.5, label='Line: 2x + 4y = 8')
    # NO perpendicular line shown - that's what the question asks!
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(-3, 5)
    ax.set_ylim(-3, 6)
    ax.set_title('Find the slope of a perpendicular line', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex4_q21_perpendicular.png', dpi=150)
    plt.close()
    print("[OK] ex4_q21_perpendicular.png")

# Q32: Normal distribution - show curve WITHOUT z-score labels
def create_q32():
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(-4, 4, 1000)
    y = (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)
    ax.plot(x, y, 'b-', linewidth=2)
    # Show shaded region but ask student to find z-score
    x_fill = np.linspace(-1.96, 1.96, 500)
    y_fill = (1/np.sqrt(2*np.pi)) * np.exp(-x_fill**2/2)
    ax.fill_between(x_fill, y_fill, alpha=0.4, color='green')
    ax.axvline(-1.96, color='red', linestyle='--', linewidth=2)
    ax.axvline(1.96, color='red', linestyle='--', linewidth=2)
    # Only label 95% - the z-score is NOT labeled (that's the answer!)
    ax.annotate('95%', (0, 0.15), ha='center', fontsize=14, fontweight='bold')
    ax.annotate('z = ?', (-1.96, 0.42), ha='center', fontsize=11)
    ax.annotate('z = ?', (1.96, 0.42), ha='center', fontsize=11)
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.5)
    ax.set_title('Normal Distribution: What z-score for 95% CI?', fontweight='bold')
    ax.set_xlabel('z-score')
    plt.tight_layout()
    plt.savefig('images/ex4_q32_normal.png', dpi=150)
    plt.close()
    print("[OK] ex4_q32_normal.png")

# Q40: Right triangle - only show given info (AC, BC), NOT AB
def create_q40():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot([0, 8, 0, 0], [0, 0, 6, 0], 'b-', linewidth=2.5)
    ax.fill([0, 8, 0], [0, 0, 6], alpha=0.2, color='blue')
    ax.plot([0, 0.5, 0.5, 0], [0.5, 0.5, 0, 0], 'k-', linewidth=1)  # Right angle
    ax.annotate('C (90 deg)', (-0.5, 0.3), fontsize=12, fontweight='bold')
    ax.annotate('A', (8.2, 0), fontsize=12, fontweight='bold')
    ax.annotate('B', (0, 6.3), fontsize=12, fontweight='bold')
    ax.annotate('AC = 8', (4, -0.5), ha='center', fontsize=11)
    ax.annotate('BC = 6', (-0.7, 3), fontsize=11)
    # AB is NOT labeled - student must calculate it!
    ax.annotate('AB = ?', (4.5, 3.5), fontsize=11, rotation=-37, color='gray')
    ax.set_xlim(-1.5, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title('Right Triangle ABC', fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/ex4_q40_triangle.png', dpi=150)
    plt.close()
    print("[OK] ex4_q40_triangle.png")

if __name__ == "__main__":
    print("Generating images for Exam 4 (NO SPOILERS)...")
    create_q1()
    create_q17()
    create_q21()
    create_q32()
    create_q40()
    print("\n[OK] All Exam 4 images done!")
