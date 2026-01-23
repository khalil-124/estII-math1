"""Generate Exam 8 images - creative geometry focus"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q1: Absolute value function |x-2| + 1
fig, ax = plt.subplots(figsize=(10, 7))
x = np.linspace(-2, 6, 300)
y = np.abs(x - 2) + 1
ax.plot(x, y, 'b-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.plot(2, 1, 'ro', markersize=8)  # Vertex
ax.annotate('V(2, 1)', (2.2, 1.3), fontsize=11, color='red')
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 7)
ax.set_ylim(-1, 6)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex8_q1_absvalue.png', dpi=150)
plt.close()
print("[OK] ex8_q1_absvalue.png")

# Q12: Triangle with INSCRIBED circle (inradius question)
fig, ax = plt.subplots(figsize=(9, 7))
# Triangle 3-4-5 scaled by 2 = 6-8-10
A = np.array([0, 0])
B = np.array([8, 0])
C = np.array([0, 6])
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2.5)
ax.add_patch(triangle)
# Inscribed circle: inradius r = Area/s = 24/12 = 2, center at (r, r) = (2, 2)
circle = plt.Circle((2, 2), 2, fill=False, edgecolor='red', linewidth=2)
ax.add_patch(circle)
ax.plot(2, 2, 'ro', markersize=5)  # Incenter
# Labels
ax.annotate('A', (-0.5, -0.5), fontsize=12, fontweight='bold')
ax.annotate('B', (8.2, -0.5), fontsize=12, fontweight='bold')
ax.annotate('C', (-0.5, 6.2), fontsize=12, fontweight='bold')
ax.annotate('6', (-0.6, 3), fontsize=11)
ax.annotate('8', (4, -0.6), fontsize=11)
ax.annotate('10', (4.5, 3.5), fontsize=11, rotation=-37)
ax.annotate('r = ?', (2.5, 2), fontsize=11, color='red')
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 8)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Triangle with Inscribed Circle', fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex8_q12_inscribed.png', dpi=150)
plt.close()
print("[OK] ex8_q12_inscribed.png")

# Q19: Scatter plot with correlation
np.random.seed(42)
x_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_data = 2 * x_data + 3 + np.random.normal(0, 1.5, 10)
fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(x_data, y_data, s=80, c='blue', alpha=0.7)
# Best fit line
m, b = np.polyfit(x_data, y_data, 1)
ax.plot(x_data, m*x_data + b, 'r--', linewidth=2, label=f'Best fit: y ≈ {m:.1f}x + {b:.1f}')
ax.set_xlabel('Study Hours', fontsize=12)
ax.set_ylabel('Test Score', fontsize=12)
ax.set_title('Study Hours vs Test Score', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('images/ex8_q19_scatter.png', dpi=150)
plt.close()
print("[OK] ex8_q19_scatter.png")

# Q32: Cumulative frequency (Ogive)
fig, ax = plt.subplots(figsize=(10, 6))
class_bounds = [0, 10, 20, 30, 40, 50]
cumulative = [0, 5, 15, 30, 42, 50]
ax.plot(class_bounds, cumulative, 'b-o', linewidth=2, markersize=8)
ax.fill_between(class_bounds, cumulative, alpha=0.2)
ax.axhline(25, color='red', linestyle='--', linewidth=1.5)
ax.annotate('Median class?', (35, 27), fontsize=11, color='red')
ax.set_xlabel('Score', fontsize=12)
ax.set_ylabel('Cumulative Frequency', fontsize=12)
ax.set_title('Cumulative Frequency Graph (Ogive)', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 55)
ax.set_ylim(0, 55)
plt.tight_layout()
plt.savefig('images/ex8_q32_ogive.png', dpi=150)
plt.close()
print("[OK] ex8_q32_ogive.png")

# Q38: Unit circle with angle 5π/6
fig, ax = plt.subplots(figsize=(8, 8))
circle = plt.Circle((0, 0), 1, fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(circle)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
# Angle 5π/6 = 150°
angle_rad = 5 * np.pi / 6
x_pt = np.cos(angle_rad)
y_pt = np.sin(angle_rad)
ax.plot([0, x_pt], [0, y_pt], 'r-', linewidth=2)
ax.plot(x_pt, y_pt, 'ro', markersize=10)
ax.annotate(f'P', (x_pt - 0.15, y_pt + 0.1), fontsize=12, fontweight='bold')
# Draw arc for angle
arc = patches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0, theta2=150, color='green', linewidth=2)
ax.add_patch(arc)
ax.annotate('θ = 5π/6', (0.1, 0.25), fontsize=11, color='green')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Unit Circle', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex8_q38_unitcircle.png', dpi=150)
plt.close()
print("[OK] ex8_q38_unitcircle.png")

print("\n[OK] All Exam 8 images generated!")
