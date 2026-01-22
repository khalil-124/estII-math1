"""Generate Exam 6 images - 6 graph questions with NO ANSWER SPOILERS"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q1: Polynomial with 3 roots (student must count)
fig, ax = plt.subplots(figsize=(10, 7))
x = np.linspace(-4, 5, 300)
y = 0.1 * (x + 2) * x * (x - 3)
ax.plot(x, y, 'b-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, alpha=0.3)
ax.set_xlim(-4, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex6_q1_polynomial.png', dpi=150)
plt.close()
print("[OK] ex6_q1_polynomial.png")

# Q12: Triangle with sides (for perimeter calculation)
fig, ax = plt.subplots(figsize=(8, 6))
P = np.array([0, 0])
Q = np.array([7, 0])
R = np.array([3, 4.5])
triangle = plt.Polygon([P, Q, R], fill=False, edgecolor='blue', linewidth=2.5)
ax.add_patch(triangle)
ax.fill([P[0], Q[0], R[0]], [P[1], Q[1], R[1]], alpha=0.1, color='blue')
# Labels with just side names, not lengths
ax.annotate('P', (-0.3, -0.3), fontsize=12, fontweight='bold')
ax.annotate('Q', (7.2, -0.3), fontsize=12, fontweight='bold')
ax.annotate('R', (3, 5), fontsize=12, fontweight='bold')
ax.annotate('5', (-0.3, 2.5), fontsize=11)
ax.annotate('6', (5.3, 2.7), fontsize=11)
ax.annotate('7', (3.5, -0.5), fontsize=11)
ax.set_xlim(-1, 9)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Triangle PQR', fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex6_q12_triangle.png', dpi=150)
plt.close()
print("[OK] ex6_q12_triangle.png")

# Q19: Bar chart for statistics (student reads and sums)
fig, ax = plt.subplots(figsize=(10, 6))
scores = ['60', '70', '80', '90', '100']
students = [5, 10, 8, 5, 2]  # 80+ = 8+5+2 = 15
colors = ['#3498db', '#3498db', '#e74c3c', '#e74c3c', '#e74c3c']
bars = ax.bar(scores, students, color=colors, edgecolor='black')
for bar, s in zip(bars, students):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(s), ha='center', fontsize=12, fontweight='bold')
ax.set_xlabel('Test Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Students', fontsize=12, fontweight='bold')
ax.set_title('Test Score Distribution', fontsize=14, fontweight='bold')
ax.set_ylim(0, 15)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('images/ex6_q19_barchart.png', dpi=150)
plt.close()
print("[OK] ex6_q19_barchart.png")

# Q32: Histogram (median class question)
fig, ax = plt.subplots(figsize=(10, 6))
hours = ['0-5', '5-10', '10-15', '15-20', '20-25']
freq = [3, 7, 12, 5, 3]  # Total=30, median at 15th, in 10-15
bars = ax.bar(hours, freq, color='steelblue', edgecolor='black')
for bar, f in zip(bars, freq):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            str(f), ha='center', fontsize=12, fontweight='bold')
ax.set_xlabel('Hours Studied', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Study Hours Distribution (30 students)', fontsize=14, fontweight='bold')
ax.set_ylim(0, 16)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('images/ex6_q32_histogram.png', dpi=150)
plt.close()
print("[OK] ex6_q32_histogram.png")

# Q38: Right triangle for sin θ (3-4-5 triangle, no labels for values to find)
fig, ax = plt.subplots(figsize=(8, 6))
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([4, 3])
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2.5)
ax.add_patch(triangle)
# Right angle
rect = patches.Rectangle((3.7, 0), 0.3, 0.3, fill=False, edgecolor='red', linewidth=1.5)
ax.add_patch(rect)
# Angle theta at A
arc = patches.Arc((0, 0), 1.2, 1.2, angle=0, theta1=0, theta2=37, color='green', linewidth=2)
ax.add_patch(arc)
ax.text(0.8, 0.25, 'θ', fontsize=14, color='green')
# Labels
ax.annotate('A', (-0.3, -0.3), fontsize=12, fontweight='bold')
ax.annotate('B', (4.2, -0.3), fontsize=12, fontweight='bold')
ax.annotate('C', (4.2, 3.2), fontsize=12, fontweight='bold')
ax.annotate('4', (2, -0.4), ha='center', fontsize=11)
ax.annotate('3', (4.3, 1.5), fontsize=11)
ax.annotate('5', (1.8, 1.8), fontsize=11, rotation=37)
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Right Triangle (Find sin θ)', fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex6_q38_triangle.png', dpi=150)
plt.close()
print("[OK] ex6_q38_triangle.png")

print("\n[OK] All Exam 6 images generated!")
