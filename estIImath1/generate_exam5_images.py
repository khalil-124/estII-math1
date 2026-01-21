import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create images directory path
import os
os.makedirs('images', exist_ok=True)

# ============================================
# Q1: Circle with Parallel Chords
# ============================================
fig, ax = plt.subplots(figsize=(8, 8))

# Draw circle
circle = plt.Circle((0, 0), 2, fill=False, color='blue', linewidth=2)
ax.add_patch(circle)

# Draw parallel chords AB and CD
# Chord AB (upper)
A = (-1.5, np.sqrt(4 - 1.5**2))
B = (1.5, np.sqrt(4 - 1.5**2))
ax.plot([A[0], B[0]], [A[1], B[1]], 'g-', linewidth=2)

# Chord CD (lower)
C = (-1.5, -np.sqrt(4 - 1.5**2))
D = (1.5, -np.sqrt(4 - 1.5**2))
ax.plot([C[0], D[0]], [C[1], D[1]], 'g-', linewidth=2)

# Mark points
for point, label in [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D')]:
    ax.plot(point[0], point[1], 'ro', markersize=8)
    offset = (0.2, 0.2) if label in ['A', 'B'] else (0.2, -0.3)
    ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=14, fontweight='bold')

# Mark center
ax.plot(0, 0, 'ko', markersize=6)
ax.text(0.15, 0.1, 'O', fontsize=12)

# Arc label
ax.annotate('40°', xy=(-1.8, 0.5), fontsize=12, color='red')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title('Circle with Parallel Chords', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex5_q1_circle_parallel.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q2: Isosceles Triangle on Coordinate Plane
# ============================================
fig, ax = plt.subplots(figsize=(8, 6))

# Triangle vertices
X = np.array([0, 0])
Y = np.array([3, 4])
Z = np.array([6, 0])

# Draw triangle
triangle = plt.Polygon([X, Y, Z], fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(triangle)

# Mark vertices
for point, label, offset in [(X, 'X(0,0)', (-0.5, -0.5)), 
                              (Y, 'Y(a,b)', (-0.3, 0.3)), 
                              (Z, 'Z(c,0)', (0.2, -0.5))]:
    ax.plot(point[0], point[1], 'ro', markersize=8)
    ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=12, fontweight='bold')

# Draw perpendicular bisector (dashed)
midpoint_x = 3
ax.axvline(x=midpoint_x, color='gray', linestyle='--', linewidth=1.5, label='Perpendicular Bisector')

ax.set_xlim(-1, 8)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Isosceles Triangle XYZ', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex5_q2_isosceles_coord.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q15: Right Triangle with Altitude
# ============================================
fig, ax = plt.subplots(figsize=(8, 6))

# Triangle vertices
A = np.array([0, 0])
B = np.array([8, 0])
C = np.array([0, 6])

# Draw triangle
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(triangle)

# Draw altitude from C to AB
H = np.array([0, 0])  # In this case, altitude is at A for right triangle
ax.plot([C[0], A[0]], [C[1], A[1]], 'g-', linewidth=2)

# Mark right angle
rect = patches.Rectangle((0, 0), 0.5, 0.5, fill=False, edgecolor='red', linewidth=1.5)
ax.add_patch(rect)

# Mark vertices
for point, label, offset in [(A, 'A', (-0.4, -0.4)), 
                              (B, 'B', (0.2, -0.4)), 
                              (C, 'C', (-0.4, 0.2))]:
    ax.plot(point[0], point[1], 'ro', markersize=8)
    ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=14, fontweight='bold')

# Add measurements
ax.text(4, -0.6, '8', fontsize=12, ha='center')
ax.text(-0.6, 3, '6', fontsize=12, ha='center')

ax.set_xlim(-1, 10)
ax.set_ylim(-1, 8)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Right Triangle ABC', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex5_q15_triangle.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q18: Regular Hexagon
# ============================================
fig, ax = plt.subplots(figsize=(8, 8))

# Hexagon vertices
n = 6
angles = np.linspace(0, 2*np.pi, n+1)
radius = 2
x = radius * np.cos(angles)
y = radius * np.sin(angles)

# Draw hexagon
ax.plot(x, y, 'b-', linewidth=2)
ax.fill(x, y, alpha=0.1, color='blue')

# Draw diagonals from vertex A
ax.plot([x[0], x[2]], [y[0], y[2]], 'r--', linewidth=1.5)
ax.plot([x[0], x[3]], [y[0], y[3]], 'r--', linewidth=1.5)
ax.plot([x[0], x[4]], [y[0], y[4]], 'r--', linewidth=1.5)

# Label vertices
labels = ['A', 'B', 'C', 'D', 'E', 'F']
for i in range(n):
    offset = 0.3
    ax.text(x[i] * 1.15, y[i] * 1.15, labels[i], fontsize=14, fontweight='bold', ha='center')
    ax.plot(x[i], y[i], 'ro', markersize=8)

# Mark angle at B
angle_arc = patches.Arc((x[1], y[1]), 0.6, 0.6, angle=0, theta1=180, theta2=240, color='green', linewidth=2)
ax.add_patch(angle_arc)
ax.text(x[1]-0.5, y[1]+0.3, '?°', fontsize=12, color='green')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Regular Hexagon ABCDEF', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex5_q18_hexagon.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q21: Function Graph (Polynomial)
# ============================================
fig, ax = plt.subplots(figsize=(10, 7))

x = np.linspace(-4, 4, 500)
# Cubic function with 3 roots
y = 0.3 * (x + 2) * (x) * (x - 2)

ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')

# Mark roots
roots = [-2, 0, 2]
for root in roots:
    ax.plot(root, 0, 'ro', markersize=10)
    ax.annotate(f'({root}, 0)', xy=(root, 0), xytext=(root, -1.5), 
                fontsize=10, ha='center', color='red')

# Mark local max and min
ax.plot(-1.15, 0.3*(-1.15+2)*(-1.15)*(-1.15-2), 'go', markersize=8)
ax.plot(1.15, 0.3*(1.15+2)*(1.15)*(1.15-2), 'go', markersize=8)

# Axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, alpha=0.3, linestyle='--')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('images/ex5_q21_function_graph.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q32: Histogram for Statistics
# ============================================
fig, ax = plt.subplots(figsize=(10, 6))

# Data
hours = ['0-10', '10-20', '20-30', '30-40', '40-50']
frequency = [4, 8, 12, 6, 5]
x_pos = np.arange(len(hours))

bars = ax.bar(x_pos, frequency, color='steelblue', edgecolor='black', alpha=0.8)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
            f'{int(height)}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_xticks(x_pos)
ax.set_xticklabels(hours, fontsize=11)
ax.set_xlabel('Study Hours per Week', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Students', fontsize=12, fontweight='bold')
ax.set_title('Weekly Study Hours Distribution', fontsize=14, fontweight='bold')
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('images/ex5_q32_histogram.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================
# Q38: Right Triangle Trigonometry
# ============================================
fig, ax = plt.subplots(figsize=(8, 6))

# Triangle vertices
A = np.array([0, 0])
B = np.array([5, 0])
C = np.array([5, 3])

# Draw triangle
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2)
ax.add_patch(triangle)

# Mark right angle at B
rect = patches.Rectangle((4.7, 0), 0.3, 0.3, fill=False, edgecolor='red', linewidth=1.5)
ax.add_patch(rect)

# Mark angle theta at A
angle_arc = patches.Arc((0, 0), 1.5, 1.5, angle=0, theta1=0, theta2=31, color='green', linewidth=2)
ax.add_patch(angle_arc)
ax.text(1, 0.3, 'θ', fontsize=14, color='green')

# Mark vertices
for point, label, offset in [(A, 'A', (-0.4, -0.4)), 
                              (B, 'B', (0.2, -0.4)), 
                              (C, 'C', (0.2, 0.2))]:
    ax.plot(point[0], point[1], 'ro', markersize=8)
    ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=14, fontweight='bold')

# Add measurements
ax.text(2.5, -0.5, '5', fontsize=12, ha='center', fontweight='bold')
ax.text(5.4, 1.5, '3', fontsize=12, ha='center', fontweight='bold')

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Right Triangle (Find tan θ)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex5_q38_trig_triangle.png', dpi=150, bbox_inches='tight')
plt.close()

print("[SUCCESS] All 7 images generated successfully!")
print("Images saved in 'images/' folder:")
print("  - ex5_q1_circle_parallel.png")
print("  - ex5_q2_isosceles_coord.png")
print("  - ex5_q15_triangle.png")
print("  - ex5_q18_hexagon.png")
print("  - ex5_q21_function_graph.png")
print("  - ex5_q32_histogram.png")
print("  - ex5_q38_trig_triangle.png")
