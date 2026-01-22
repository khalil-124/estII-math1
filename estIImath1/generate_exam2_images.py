"""
Generate additional graph images for Practice Exam 2
These images are designed for questions that REQUIRE visual analysis
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure images directory exists
os.makedirs('images', exist_ok=True)

# ===== IMAGE 1: Histogram for Q17 replacement =====
# Question: "Based on the histogram, how many students scored between 70-90?"
def create_histogram():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Score ranges and frequencies
    ranges = ['50-60', '60-70', '70-80', '80-90', '90-100']
    frequencies = [4, 7, 12, 9, 5]  # Students in each range
    
    colors = ['#3498db', '#3498db', '#e74c3c', '#e74c3c', '#3498db']
    bars = ax.bar(ranges, frequencies, color=colors, edgecolor='black', linewidth=1.2)
    
    # Add value labels on bars
    for bar, freq in zip(bars, frequencies):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                str(freq), ha='center', fontsize=12, fontweight='bold')
    
    ax.set_xlabel('Score Range', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Students', fontsize=12, fontweight='bold')
    ax.set_title('Math Test Score Distribution', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 15)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('images/ex2_q17_histogram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex2_q17_histogram.png")

# ===== IMAGE 2: Piecewise function graph for Q21 replacement =====
# Question: "Based on the graph, what is f(2) + f(-1)?"
def create_piecewise_graph():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Piecewise function:
    # f(x) = x + 3 for x < 0
    # f(x) = -x + 3 for x >= 0
    
    x1 = np.linspace(-4, 0, 100)
    y1 = x1 + 3
    
    x2 = np.linspace(0, 4, 100)
    y2 = -x2 + 3
    
    ax.plot(x1, y1, 'b-', linewidth=2.5, label='f(x)')
    ax.plot(x2, y2, 'b-', linewidth=2.5)
    
    # Mark key points
    ax.plot(0, 3, 'ro', markersize=10, zorder=5)  # Vertex
    ax.plot(2, 1, 'go', markersize=8, zorder=5)   # f(2) = 1
    ax.plot(-1, 2, 'go', markersize=8, zorder=5)  # f(-1) = 2
    
    # Add labels for key points
    ax.annotate('(0, 3)', (0.2, 3.2), fontsize=10)
    ax.annotate('(2, 1)', (2.2, 1.2), fontsize=10)
    ax.annotate('(-1, 2)', (-0.8, 2.3), fontsize=10)
    
    # Axes
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2, 5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')
    
    # Set integer ticks
    ax.set_xticks(range(-4, 5))
    ax.set_yticks(range(-2, 6))
    
    plt.tight_layout()
    plt.savefig('images/ex2_q21_piecewise.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex2_q21_piecewise.png")

# ===== IMAGE 3: Scatter plot with trend for Q32 replacement =====
# Question: "Based on the scatter plot, what is the best estimate for y when x = 6?"
def create_scatter_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Data points that follow y ≈ 2x + 1 trend
    x_data = [1, 2, 3, 4, 5, 7, 8]
    y_data = [3, 5, 6, 9, 11, 15, 17]  # Roughly y = 2x + 1
    
    ax.scatter(x_data, y_data, s=100, c='#e74c3c', edgecolors='black', linewidth=1.5, zorder=5)
    
    # Draw trend line
    x_line = np.array([0, 9])
    y_line = 2 * x_line + 1
    ax.plot(x_line, y_line, 'b--', linewidth=2, alpha=0.7, label='Trend line')
    
    # Mark the question point
    ax.axvline(x=6, color='green', linestyle=':', linewidth=2, alpha=0.7)
    ax.plot(6, 13, 'g^', markersize=12, zorder=5)  # Expected y when x=6
    ax.annotate('x = 6', (6.2, 1), fontsize=11, color='green')
    
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 20)
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title('Scatter Plot with Trend Line', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper left')
    
    # Integer ticks
    ax.set_xticks(range(0, 10))
    ax.set_yticks(range(0, 21, 2))
    
    plt.tight_layout()
    plt.savefig('images/ex2_q32_scatter.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex2_q32_scatter.png")

# ===== IMAGE 4: Circle with tangent for Q18 =====
# Question: "In the circle with center O, if AB is tangent at point P and OP = 5, what is the length of OP?"
def create_circle_tangent():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Circle
    theta = np.linspace(0, 2*np.pi, 100)
    r = 5
    x_circle = r * np.cos(theta)
    y_circle = r * np.sin(theta)
    ax.plot(x_circle, y_circle, 'b-', linewidth=2)
    
    # Center O
    ax.plot(0, 0, 'ro', markersize=8)
    ax.annotate('O', (0.3, 0.3), fontsize=12, fontweight='bold')
    
    # Tangent point P at (5, 0)
    ax.plot(5, 0, 'go', markersize=8)
    ax.annotate('P', (5.3, 0.3), fontsize=12, fontweight='bold')
    
    # Tangent line (vertical at x=5)
    ax.axvline(x=5, color='purple', linewidth=2, linestyle='-')
    
    # Points A and B on tangent
    ax.plot(5, 4, 'ko', markersize=8)
    ax.annotate('A', (5.3, 4), fontsize=12, fontweight='bold')
    ax.plot(5, -4, 'ko', markersize=8)
    ax.annotate('B', (5.3, -4), fontsize=12, fontweight='bold')
    
    # Radius OP
    ax.plot([0, 5], [0, 0], 'r-', linewidth=2)
    ax.annotate('r = 5', (2.5, 0.5), fontsize=11, color='red')
    
    # Right angle symbol at P
    rect_size = 0.5
    ax.plot([5-rect_size, 5-rect_size, 5], [0, rect_size, rect_size], 'k-', linewidth=1)
    
    ax.set_xlim(-7, 8)
    ax.set_ylim(-7, 7)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_title('Circle with Tangent Line AB', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('images/ex2_q18_tangent.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created: ex2_q18_tangent.png")

if __name__ == "__main__":
    print("Generating additional images for Exam 2...")
    create_histogram()
    create_piecewise_graph()
    create_scatter_plot()
    create_circle_tangent()
    print("\n[OK] All images generated successfully!")
