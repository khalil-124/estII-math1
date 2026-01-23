"""Create cleaner Q1 graph - simple parabola with a twist"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 7))

# Simple transformed parabola: f(x) = -(x-2)² + 4
x = np.linspace(-2, 6, 300)
y = -(x - 2)**2 + 4

ax.plot(x, y, 'b-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Mark intersection points with x-axis (zeros)
ax.plot(0, 0, 'ro', markersize=8)
ax.plot(4, 0, 'ro', markersize=8)

# Mark vertex
ax.plot(2, 4, 'go', markersize=8)
ax.annotate('Vertex', (2.2, 4.2), fontsize=11, color='green')

ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 7)
ax.set_ylim(-8, 6)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')

# Draw horizontal line y = -5 to ask about intersections
ax.axhline(-5, color='red', linewidth=1.5, linestyle='--', alpha=0.6)
ax.annotate('y = -5', (5.5, -4.5), fontsize=10, color='red')

plt.tight_layout()
plt.savefig('images/ex7_q1_parabola.png', dpi=150)
plt.close()
print("[OK] Created clean Q1 parabola graph")
