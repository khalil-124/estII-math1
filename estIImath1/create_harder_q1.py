"""Create harder Q1 graph for Exam 7"""
import matplotlib.pyplot as plt
import numpy as np
import os

# Create a piecewise function with interesting features
fig, ax = plt.subplots(figsize=(10, 7))

# Create a more complex function: f(x) with specific features for harder question
x1 = np.linspace(-4, -1, 100)
y1 = -0.5 * (x1 + 2.5)**2 + 2  # Parabola opening down, max at x=-2.5

x2 = np.linspace(-1, 2, 100)
y2 = np.sin(np.pi * (x2 + 1) / 1.5)  # Sine wave

x3 = np.linspace(2, 5, 100)
y3 = 0.3 * (x3 - 3.5)**2 - 1  # Parabola opening up, min at x=3.5

# Combine
x = np.concatenate([x1, x2, x3])
y = np.concatenate([y1, y2, y3])

ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Mark key points for reference
ax.plot(-2.5, 2, 'ro', markersize=8)  # Local max
ax.plot(0.5, 1, 'go', markersize=8)   # Local max of sine  
ax.plot(3.5, -1, 'ro', markersize=8)  # Local min

# Add annotations
ax.annotate('A(-2.5, 2)', (-2.5, 2.2), ha='center', fontsize=10)
ax.annotate('B', (0.5, 1.2), ha='center', fontsize=10)
ax.annotate('C(3.5, -1)', (3.5, -1.3), ha='center', fontsize=10)

ax.grid(True, alpha=0.3)
ax.set_xlim(-4.5, 5.5)
ax.set_ylim(-2.5, 3)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')

# Add horizontal line at y=0 for reference (to count zeros)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')

plt.tight_layout()
plt.savefig('images/ex7_q1_complex.png', dpi=150)
plt.close()
print("[OK] Created harder Q1 graph: ex7_q1_complex.png")
