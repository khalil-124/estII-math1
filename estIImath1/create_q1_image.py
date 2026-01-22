"""Generate new Q1 image for Exam 5 - Quadratic function graph"""
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs('images', exist_ok=True)

fig, ax = plt.subplots(figsize=(10, 7))

# Quadratic: f(x) = -(x-1)^2 + 5 so vertex at (1, 5)
# f(-1) = -((-1)-1)^2 + 5 = -4 + 5 = 1... wait that doesn't work
# Let's use f(x) = (x-1)^2 so f(-1) = 4 and f(3) = 4
x = np.linspace(-3, 5, 300)
y = (x - 1)**2

ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')
ax.fill_between(x, y, alpha=0.1, color='blue')

# Mark key points but NOT the y-values (student must read)
ax.plot(-1, 4, 'ro', markersize=10, zorder=5)
ax.plot(3, 4, 'ro', markersize=10, zorder=5)
ax.plot(1, 0, 'go', markersize=10, zorder=5)  # vertex

# Add x-labels only (not y)
ax.annotate('x = -1', (-1, 4.5), ha='center', fontsize=11)
ax.annotate('x = 3', (3, 4.5), ha='center', fontsize=11)
ax.annotate('vertex', (1.5, 0.5), fontsize=10, color='green')

# Axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, alpha=0.3, linestyle='--')

ax.set_xlim(-3, 5)
ax.set_ylim(-1, 10)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')
ax.set_xticks(range(-3, 6))
ax.set_yticks(range(0, 11))

plt.tight_layout()
plt.savefig('images/ex5_q1_quadratic.png', dpi=150, bbox_inches='tight')
plt.close()
print("[OK] Created: ex5_q1_quadratic.png")
