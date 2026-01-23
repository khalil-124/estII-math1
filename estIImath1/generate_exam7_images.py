"""Generate Exam 7 images - 5 graph questions with NO ANSWER SPOILERS"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q1: Cubic function with 2 turning points (different from Exam 6)
fig, ax = plt.subplots(figsize=(10, 7))
x = np.linspace(-3, 4, 300)
y = 0.15 * (x + 2) * (x - 1) * (x - 3)
ax.plot(x, y, 'b-', linewidth=2.5)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 4)
ax.set_ylim(-3, 3)
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Graph of g(x)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex7_q1_cubic.png', dpi=150)
plt.close()
print("[OK] ex7_q1_cubic.png")

# Q12: Trapezoid with labeled sides (for area calculation)
fig, ax = plt.subplots(figsize=(8, 6))
trap = np.array([[0, 0], [8, 0], [6, 4], [2, 4], [0, 0]])
ax.plot(trap[:, 0], trap[:, 1], 'b-', linewidth=2.5)
ax.fill(trap[:, 0], trap[:, 1], alpha=0.1, color='blue')
# Labels
ax.annotate('8', (4, -0.5), ha='center', fontsize=12, fontweight='bold')
ax.annotate('4', (4, 4.5), ha='center', fontsize=12, fontweight='bold')
ax.annotate('h=4', (8.3, 2), fontsize=11)
ax.plot([8, 8], [0, 4], 'r--', linewidth=1.5)  # height line
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Trapezoid ABCD', fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex7_q12_trapezoid.png', dpi=150)
plt.close()
print("[OK] ex7_q12_trapezoid.png")

# Q19: Pie chart for statistics (student calculates percentage)
fig, ax = plt.subplots(figsize=(8, 8))
sizes = [30, 25, 20, 15, 10]  # Percentages
labels = ['Math', 'Science', 'English', 'History', 'Art']
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']
explode = (0.02, 0.02, 0.02, 0.02, 0.02)
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.0f%%',
       shadow=True, startangle=90, textprops={'fontsize': 12})
ax.set_title('Favorite Subjects (200 Students)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex7_q19_piechart.png', dpi=150)
plt.close()
print("[OK] ex7_q19_piechart.png")

# Q32: Box plot for statistics (IQR question)
fig, ax = plt.subplots(figsize=(10, 5))
data = [15, 18, 22, 25, 28, 30, 32, 35, 40, 45]  # Q1=20, Q3=36, IQR=16
bp = ax.boxplot(data, vert=False, patch_artist=True)
bp['boxes'][0].set_facecolor('steelblue')
bp['boxes'][0].set_alpha(0.7)
ax.set_xlabel('Values', fontsize=12, fontweight='bold')
ax.set_title('Data Distribution', fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('images/ex7_q32_boxplot.png', dpi=150)
plt.close()
print("[OK] ex7_q32_boxplot.png")

# Q38: Right triangle for cos θ (different from Exam 6)
fig, ax = plt.subplots(figsize=(8, 6))
A = np.array([0, 0])
B = np.array([5, 0])
C = np.array([5, 12])
triangle = plt.Polygon([A, B, C], fill=False, edgecolor='blue', linewidth=2.5)
ax.add_patch(triangle)
# Right angle
rect = patches.Rectangle((4.6, 0), 0.4, 0.4, fill=False, edgecolor='red', linewidth=1.5)
ax.add_patch(rect)
# Angle theta at A
arc = patches.Arc((0, 0), 2, 2, angle=0, theta1=0, theta2=67, color='green', linewidth=2)
ax.add_patch(arc)
ax.text(1.3, 0.6, 'θ', fontsize=14, color='green')
# Labels
ax.annotate('A', (-0.4, -0.4), fontsize=12, fontweight='bold')
ax.annotate('B', (5.2, -0.4), fontsize=12, fontweight='bold')
ax.annotate('C', (5.2, 12.2), fontsize=12, fontweight='bold')
ax.annotate('5', (2.5, -0.6), ha='center', fontsize=11)
ax.annotate('12', (5.5, 6), fontsize=11)
ax.annotate('13', (2, 6.5), fontsize=11, rotation=67)
ax.set_xlim(-1, 8)
ax.set_ylim(-1, 14)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Right Triangle (Find cos θ)', fontweight='bold')
plt.tight_layout()
plt.savefig('images/ex7_q38_triangle.png', dpi=150)
plt.close()
print("[OK] ex7_q38_triangle.png")

print("\n[OK] All Exam 7 images generated!")
