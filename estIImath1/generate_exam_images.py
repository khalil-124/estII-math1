"""
Generate TRUE image-dependent questions for EST Practice Exams
Questions CANNOT be solved without looking at the image!
The image contains essential data not mentioned in text.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('images', exist_ok=True)

def set_style():
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14

# ============== EXAM 2: TRUE IMAGE-DEPENDENT ==============

def exam2_q1_graph_reading():
    """Q1: Must READ VALUE from graph - f(3) = ?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-2, 6, 100)
    y = -0.5*(x - 2)**2 + 4  # Parabola with vertex at (2, 4)
    ax.plot(x, y, 'b-', linewidth=2.5)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.4)
    ax.set_xlim(-3, 7)
    ax.set_ylim(-4, 6)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_title('Graph of y = f(x)', fontsize=16)
    # Mark key points that student must read
    ax.plot([0, 2, 4, -1, 3], [2, 4, 2, 1.5, 3.5], 'ko', markersize=4)
    # Add grid lines at integers
    ax.set_xticks(range(-3, 8))
    ax.set_yticks(range(-4, 7))
    plt.tight_layout()
    plt.savefig('images/ex2_q1_read_graph.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Answer: f(3) = 3.5

def exam2_q8_count_intersection():
    """Q8: Count intersection points of two curves"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-3, 4, 200)
    y1 = x**2 - 2  # Parabola
    y2 = 2*x + 1   # Line
    ax.plot(x, y1, 'b-', linewidth=2.5, label='f(x)')
    ax.plot(x, y2, 'r-', linewidth=2.5, label='g(x)')
    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=0, color='k', linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-4, 5)
    ax.set_ylim(-4, 10)
    ax.legend(fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graphs of f(x) and g(x)')
    plt.tight_layout()
    plt.savefig('images/ex2_q8_intersections.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Answer: 2 intersection points (at x = -1 and x = 3)

def exam2_q17_find_angle():
    """Q17: Measure angle from diagram - essential"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    
    # Two lines meeting at point
    ax.plot([1, 5, 9], [2, 5, 2], 'b-', linewidth=2.5)  # V shape
    ax.plot([5, 5], [5, 1], 'g--', linewidth=2)  # Height
    
    # Angle arc
    theta = np.linspace(np.pi - 0.93, np.pi, 20)  # ~53 degrees
    ax.plot(5 + 0.8*np.cos(theta), 5 + 0.8*np.sin(theta), 'r-', linewidth=2)
    
    # Labels
    ax.annotate('A', (1, 2), fontsize=14, xytext=(-10, -10), textcoords='offset points')
    ax.annotate('B', (5, 5), fontsize=14, xytext=(0, 10), textcoords='offset points')
    ax.annotate('C', (9, 2), fontsize=14, xytext=(5, -10), textcoords='offset points')
    ax.annotate('x', (4.3, 4.5), fontsize=14, color='red')
    ax.annotate('53', (3.5, 3), fontsize=12)  # One angle given
    
    ax.axis('off')
    ax.set_title('Triangle ABC')
    plt.tight_layout()
    plt.savefig('images/ex2_q17_find_angle.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: If angle at A = 53 degrees, find x (angle ABD where D is foot of altitude)

def exam2_q21_identify_transformation():
    """Q21: Identify which transformation - must see both graphs"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-4, 4, 100)
    y1 = x**2  # Original
    y2 = (x-2)**2  # Shifted right 2
    
    ax.plot(x, y1, 'b-', linewidth=2.5, label='f(x)')
    ax.plot(x, y2, 'r--', linewidth=2.5, label='g(x)')
    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=0, color='k', linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-5, 6)
    ax.set_ylim(-2, 10)
    ax.legend(fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graphs of f(x) and g(x)')
    # Mark vertices
    ax.plot(0, 0, 'bo', markersize=8)
    ax.plot(2, 0, 'ro', markersize=8)
    plt.tight_layout()
    plt.savefig('images/ex2_q21_transformation.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Answer: g(x) = f(x-2) - shifted right 2 units

def exam2_q28_read_piechart():
    """Q28: Read percentage from pie chart - MUST look at chart"""
    fig, ax = plt.subplots(figsize=(8, 8))
    # Don't show percentages - student must estimate!
    sizes = [35, 25, 20, 12, 8]
    labels = ['Math', 'Science', 'English', 'History', 'Art']
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7']
    
    wedges, texts = ax.pie(sizes, labels=labels, colors=colors, 
                           startangle=90, 
                           wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax.set_title('Student Subject Preferences\n(200 students surveyed)', fontsize=14)
    plt.tight_layout()
    plt.savefig('images/ex2_q28_piechart.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: What fraction of students prefer Math? (must estimate ~1/3)

def exam2_q32_read_histogram():
    """Q32: Read specific value from histogram bars"""
    fig, ax = plt.subplots(figsize=(8, 6))
    scores = ['60-69', '70-79', '80-89', '90-100']
    counts = [8, 15, 12, 5]  # Must read these from graph!
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#9b59b6']
    
    bars = ax.bar(scores, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Score Range', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.set_title('Test Score Distribution', fontsize=14)
    ax.set_ylim(0, 20)
    ax.grid(True, axis='y', alpha=0.3)
    # NO labels on bars - must read!
    plt.tight_layout()
    plt.savefig('images/ex2_q32_histogram.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: How many students scored 70-79? Answer: 15 (must read from graph)

def exam2_q38_triangle_find_side():
    """Q38: Right triangle - some values shown, find missing"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    
    # Triangle with only SOME measurements shown
    triangle = plt.Polygon([(0, 0), (10, 0), (10, 8)], fill=False, edgecolor='blue', linewidth=2.5)
    ax.add_patch(triangle)
    
    # Right angle marker
    rect = patches.Rectangle((9.5, 0), 0.5, 0.5, fill=False, edgecolor='blue', linewidth=1.5)
    ax.add_patch(rect)
    
    # Labels - only show ONE side and ask for another!
    ax.annotate('P', (0, 0), fontsize=14, xytext=(-15, -10), textcoords='offset points')
    ax.annotate('Q', (10, 0), fontsize=14, xytext=(10, -10), textcoords='offset points')
    ax.annotate('R', (10, 8), fontsize=14, xytext=(10, 5), textcoords='offset points')
    
    # Show hypotenuse length only!
    ax.text(4, 5, '?', fontsize=16, fontweight='bold', color='red')  # Hypotenuse PR = ?
    ax.text(5, -0.8, '6', fontsize=14, ha='center')  # PQ = 6
    ax.text(10.8, 4, '8', fontsize=14, ha='center')  # QR = 8
    
    ax.axis('off')
    ax.set_title('Right Triangle PQR')
    plt.tight_layout()
    plt.savefig('images/ex2_q38_triangle.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find PR (must use values from figure: 6 and 8 -> PR = 10)

# ============== EXAM 3 ==============

def exam3_q1_find_zeros():
    """Q1: Count x-intercepts from graph"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-3, 4, 200)
    y = (x + 2)*(x - 1)*(x - 3)  # Three zeros
    ax.plot(x, y, 'b-', linewidth=2.5)
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.4)
    ax.set_xlim(-4, 5)
    ax.set_ylim(-15, 15)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_title('Graph of y = f(x)', fontsize=16)
    ax.set_xticks(range(-4, 6))
    plt.tight_layout()
    plt.savefig('images/ex3_q1_zeros.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: How many x-intercepts does f have? Answer: 3 (must count from graph)

def exam3_q8_find_area_shaded():
    """Q8: Find area of shaded region"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    
    # Rectangle with triangle shaded
    ax.fill([2, 8, 8, 2], [1, 1, 5, 5], color='lightblue', alpha=0.5)  # Rectangle
    ax.fill([2, 8, 5], [1, 1, 5], color='yellow', alpha=0.8)  # Shaded triangle
    
    ax.plot([2, 8, 8, 2, 2], [1, 1, 5, 5, 1], 'b-', linewidth=2)  # Rectangle outline
    ax.plot([2, 8, 5, 2], [1, 1, 5, 1], 'r-', linewidth=2)  # Triangle outline
    
    # Grid markings
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 9))
    ax.set_xlabel('x (each square = 1 unit)', fontsize=12)
    
    ax.set_title('Shaded Triangle in Rectangle')
    plt.tight_layout()
    plt.savefig('images/ex3_q8_shaded.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: What is the area of the shaded triangle? 
    # Must read: base = 6, height = 4, Area = 12

def exam3_q17_circle_chord():
    """Q17: Circle with measurements to find"""
    fig, ax = plt.subplots(figsize=(8, 8))
    circle = plt.Circle((0, 0), 5, fill=False, color='blue', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    ax.set_aspect('equal')
    
    # Chord
    ax.plot([-4, 4], [3, 3], 'r-', linewidth=2.5)
    ax.plot(-4, 3, 'ro', markersize=8)
    ax.plot(4, 3, 'ro', markersize=8)
    ax.annotate('A', (-4, 3), fontsize=14, xytext=(-15, 5), textcoords='offset points')
    ax.annotate('B', (4, 3), fontsize=14, xytext=(10, 5), textcoords='offset points')
    
    # Center  
    ax.plot(0, 0, 'ko', markersize=6)
    ax.annotate('O', (0, 0), fontsize=14, xytext=(-15, -12), textcoords='offset points')
    
    # Radius shown
    ax.plot([0, 5], [0, 0], 'g--', linewidth=1.5)
    ax.text(2.5, -0.5, 'r = 5', fontsize=12, color='green')
    
    # Distance from center to chord - what we're finding
    ax.plot([0, 0], [0, 3], 'm--', linewidth=1.5)
    ax.text(0.3, 1.5, '?', fontsize=14, color='purple', fontweight='bold')
    
    ax.axis('off')
    ax.set_title('Circle O with Chord AB')
    plt.tight_layout()
    plt.savefig('images/ex3_q17_chord.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find distance from O to chord AB. Must see r=5 from figure.

def exam3_q21_compare_functions():
    """Q21: Which function is greater at x=2?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-2, 5, 100)
    y1 = 2*x - 1  # f(x)
    y2 = x**2 - 3  # g(x)
    
    ax.plot(x, y1, 'b-', linewidth=2.5, label='f(x)')
    ax.plot(x, y2, 'r--', linewidth=2.5, label='g(x)')
    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=0, color='k', linewidth=0.8)
    ax.axvline(x=2, color='gray', linewidth=1, linestyle=':')  # Mark x=2
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-3, 6)
    ax.set_ylim(-5, 10)
    ax.legend(fontsize=12)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Graphs of f(x) and g(x)')
    ax.annotate('x = 2', (2, -4), fontsize=11)
    plt.tight_layout()
    plt.savefig('images/ex3_q21_compare.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: At x=2, which is greater, f(2) or g(2)? By how much?
    # Must read from graph: f(2)=3, g(2)=1, so f(2) is greater by 2

def exam3_q28_bar_chart():
    """Q28: Which day had the most visitors?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    visitors = [45, 62, 38, 71, 55]  # NO labels - must read!
    
    bars = ax.bar(days, visitors, color=['#e74c3c', '#3498db', '#2ecc71', '#9b59b6', '#f39c12'],
                  edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Day', fontsize=12)
    ax.set_ylabel('Number of Visitors', fontsize=12)
    ax.set_title('Daily Museum Visitors', fontsize=14)
    ax.set_ylim(0, 80)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_yticks(range(0, 81, 10))
    # NO bar labels!
    plt.tight_layout()
    plt.savefig('images/ex3_q28_bar.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Which day had the most visitors? How many?
    # Answer: Thursday, ~71 (must read from bars)

def exam3_q32_scatter_trend():
    """Q32: Predict value from scatter plot trend"""
    fig, ax = plt.subplots(figsize=(8, 6))
    np.random.seed(42)
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([12, 18, 25, 32, 38, 45, 52])  # Clear linear trend
    
    ax.scatter(x, y, c='blue', s=100, edgecolors='black', linewidth=1.5)
    ax.set_xlabel('Study Hours', fontsize=12)
    ax.set_ylabel('Test Score', fontsize=12)
    ax.set_title('Study Hours vs Test Score', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 80)
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 81, 10))
    plt.tight_layout()
    plt.savefig('images/ex3_q32_scatter.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Based on the trend, predict score for 8 study hours
    # Must extrapolate from graph: ~59

def exam3_q38_parallel_lines():
    """Q38: Find missing angle with parallel lines"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    
    # Two parallel lines
    ax.plot([0, 10], [2, 2], 'b-', linewidth=2.5)
    ax.plot([0, 10], [6, 6], 'b-', linewidth=2.5)
    ax.text(0.3, 2.3, 'm', fontsize=14, color='blue')
    ax.text(0.3, 6.3, 'n', fontsize=14, color='blue')
    
    # Transversal
    ax.plot([2, 8], [0, 8], 'r-', linewidth=2)
    
    # Angles marked
    # Angle at bottom line (given)
    ax.annotate('65', (3.8, 2.5), fontsize=14, color='green', fontweight='bold')
    # Angle at top line (find)
    ax.annotate('x', (5.3, 5.3), fontsize=14, color='red', fontweight='bold')
    
    ax.annotate('Parallel lines m and n', (3, 0.5), fontsize=12)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('images/ex3_q38_angles.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find x. Must see 65 from figure -> x = 65 (alternate) or 115 (co-interior)

# ============== EXAM 4 ==============

def exam4_q1_domain_from_graph():
    """Q1: What is the domain from looking at graph?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(0, 6, 100)
    y = np.sqrt(x)
    ax.plot(x, y, 'b-', linewidth=2.5)
    # Show that graph starts at x=0
    ax.plot(0, 0, 'bo', markersize=10)  # Closed endpoint
    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=0, color='k', linewidth=0.8)
    ax.grid(True, alpha=0.4)
    ax.set_xlim(-2, 8)
    ax.set_ylim(-1, 4)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_title('Graph of y = f(x)', fontsize=16)
    ax.set_xticks(range(-2, 9))
    plt.tight_layout()
    plt.savefig('images/ex4_q1_domain.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: What is the domain of f? Must see graph starts at x=0

def exam4_q8_find_perimeter():
    """Q8: Find perimeter from coordinate grid"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.5)
    
    # Triangle on grid - no measurements given!
    triangle = plt.Polygon([(1, 1), (1, 5), (7, 1)], fill=False, 
                           edgecolor='blue', linewidth=2.5)
    ax.add_patch(triangle)
    ax.fill([1, 1, 7], [1, 5, 1], alpha=0.2, color='blue')
    
    ax.plot([1, 1, 7], [1, 5, 1], 'bo', markersize=8)
    ax.annotate('A', (1, 1), fontsize=14, xytext=(-15, -10), textcoords='offset points')
    ax.annotate('B', (1, 5), fontsize=14, xytext=(-15, 5), textcoords='offset points')
    ax.annotate('C', (7, 1), fontsize=14, xytext=(5, -10), textcoords='offset points')
    
    ax.set_xlabel('(each square = 1 unit)', fontsize=11)
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 9))
    ax.set_title('Triangle ABC on Coordinate Grid')
    plt.tight_layout()
    plt.savefig('images/ex4_q8_perimeter.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find the perimeter of triangle ABC
    # Must count from grid: AB=4, BC=sqrt(52), AC=6 -> P = 10 + sqrt(52)

def exam4_q17_tangent_length():
    """Q17: Find tangent length from diagram"""
    fig, ax = plt.subplots(figsize=(8, 8))
    circle = plt.Circle((0, 0), 3, fill=False, color='blue', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-6, 8)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    
    # External point
    P = (7, 0)
    ax.plot(*P, 'ro', markersize=10)
    ax.annotate('P', P, fontsize=14, xytext=(10, 5), textcoords='offset points')
    
    # Tangent point
    T = (3, 0)
    ax.plot(*T, 'go', markersize=8)
    ax.annotate('T', T, fontsize=14, xytext=(5, 10), textcoords='offset points')
    
    # Center
    ax.plot(0, 0, 'ko', markersize=6)
    ax.annotate('O', (0, 0), fontsize=14, xytext=(-12, 10), textcoords='offset points')
    
    # Lines
    ax.plot([0, 7], [0, 0], 'g--', linewidth=1.5)  # OP
    ax.plot([3, 7], [0, 0], 'r-', linewidth=2)  # PT (tangent)
    
    # Show radius value
    ax.text(1.5, 0.4, 'r = 3', fontsize=12, color='blue')
    # Show OP distance
    ax.text(3.5, -0.6, 'OP = 7', fontsize=12, color='green')
    # PT = ?
    ax.text(5.2, 0.5, 'PT = ?', fontsize=14, color='red', fontweight='bold')
    
    ax.axis('off')
    ax.set_title('Circle O with Tangent PT from External Point P')
    plt.tight_layout()
    plt.savefig('images/ex4_q17_tangent.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find PT (tangent length)
    # Must use: OP=7, r=3 -> PT = sqrt(49-9) = sqrt(40) = 2sqrt(10)

def exam4_q21_max_value():
    """Q21: What is maximum value of f from graph?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-3, 5, 200)
    y = -0.5*(x - 1)**2 + 4.5  # Max at (1, 4.5)
    ax.plot(x, y, 'b-', linewidth=2.5)
    ax.axhline(y=0, color='k', linewidth=0.8)
    ax.axvline(x=0, color='k', linewidth=0.8)
    ax.grid(True, alpha=0.4)
    ax.set_xlim(-4, 6)
    ax.set_ylim(-4, 6)
    ax.set_xlabel('x', fontsize=14)
    ax.set_ylabel('y', fontsize=14)
    ax.set_title('Graph of y = f(x)', fontsize=16)
    ax.set_xticks(range(-4, 7))
    ax.set_yticks(range(-4, 7))
    # Show vertex point
    ax.plot(1, 4.5, 'ro', markersize=8)
    plt.tight_layout()
    plt.savefig('images/ex4_q21_maximum.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: What is the maximum value of f(x)?
    # Must read from graph: approximately 4.5

def exam4_q28_boxplot():
    """Q28: Compare medians from boxplot"""
    fig, ax = plt.subplots(figsize=(8, 6))
    np.random.seed(123)
    data1 = [50, 55, 60, 62, 65, 68, 70, 72, 75, 80]  # Median ~66
    data2 = [55, 60, 65, 70, 73, 76, 78, 80, 85, 90]  # Median ~74
    
    bp = ax.boxplot([data1, data2], tick_labels=['Class A', 'Class B'], 
                    patch_artist=True, widths=0.6)
    colors = ['#3498db', '#e74c3c']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    
    ax.set_ylabel('Test Score', fontsize=12)
    ax.set_title('Test Scores by Class', fontsize=14)
    ax.grid(True, axis='y', alpha=0.3)
    ax.set_ylim(40, 100)
    ax.set_yticks(range(40, 101, 10))
    plt.tight_layout()
    plt.savefig('images/ex4_q28_boxplot.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: What is the difference between medians?
    # Must read from boxplot

def exam4_q32_line_compare():
    """Q32: At what month do sales equal?"""
    fig, ax = plt.subplots(figsize=(8, 6))
    months = range(1, 7)
    sales_A = [100, 120, 140, 160, 180, 200]
    sales_B = [180, 170, 160, 150, 140, 130]
    
    ax.plot(months, sales_A, 'b-o', linewidth=2, markersize=8, label='Product A')
    ax.plot(months, sales_B, 'r-s', linewidth=2, markersize=8, label='Product B')
    
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Sales ($)', fontsize=12)
    ax.set_title('Monthly Sales', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 6.5)
    ax.set_ylim(80, 220)
    ax.set_xticks(range(1, 7))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
    plt.tight_layout()
    plt.savefig('images/ex4_q32_lines.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: In which month are sales equal?
    # Must read from graph: Month 3 (March)

def exam4_q38_trig_triangle():
    """Q38: Find sin of angle from triangle measurements"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-1, 12)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    
    # Right triangle
    triangle = plt.Polygon([(0, 0), (9, 0), (9, 12)], fill=False, 
                           edgecolor='blue', linewidth=2.5)
    ax.add_patch(triangle)
    
    # Right angle marker
    rect = patches.Rectangle((8.5, 0), 0.5, 0.5, fill=False, edgecolor='blue')
    ax.add_patch(rect)
    
    # Labels
    ax.annotate('A', (0, 0), fontsize=14, xytext=(-15, -10), textcoords='offset points')
    ax.annotate('B', (9, 0), fontsize=14, xytext=(10, -10), textcoords='offset points')
    ax.annotate('C', (9, 12), fontsize=14, xytext=(10, 5), textcoords='offset points')
    
    # Show measurements
    ax.text(4.5, -0.8, '9', fontsize=14, ha='center')  # AB
    ax.text(9.8, 6, '12', fontsize=14, ha='center')  # BC
    
    # Angle theta at A
    theta = np.linspace(0, np.arctan(12/9), 30)
    ax.plot(1.5*np.cos(theta), 1.5*np.sin(theta), 'g-', linewidth=1.5)
    ax.text(1.8, 0.6, 'theta', fontsize=12, color='green')
    
    ax.axis('off')
    ax.set_title('Right Triangle ABC')
    plt.tight_layout()
    plt.savefig('images/ex4_q38_trig.png', dpi=150, bbox_inches='tight')
    plt.close()
    # Question: Find sin(theta)
    # Must use: opposite=12, adjacent=9 -> hyp=15, sin = 12/15 = 4/5

# Generate all
if __name__ == "__main__":
    set_style()
    
    print("Generating Exam 2 TRUE image-dependent questions...")
    exam2_q1_graph_reading()
    exam2_q8_count_intersection()
    exam2_q17_find_angle()
    exam2_q21_identify_transformation()
    exam2_q28_read_piechart()
    exam2_q32_read_histogram()
    exam2_q38_triangle_find_side()
    print("Exam 2: 7 images done!")
    
    print("Generating Exam 3...")
    exam3_q1_find_zeros()
    exam3_q8_find_area_shaded()
    exam3_q17_circle_chord()
    exam3_q21_compare_functions()
    exam3_q28_bar_chart()
    exam3_q32_scatter_trend()
    exam3_q38_parallel_lines()
    print("Exam 3: 7 images done!")
    
    print("Generating Exam 4...")
    exam4_q1_domain_from_graph()
    exam4_q8_find_perimeter()
    exam4_q17_tangent_length()
    exam4_q21_max_value()
    exam4_q28_boxplot()
    exam4_q32_line_compare()
    exam4_q38_trig_triangle()
    print("Exam 4: 7 images done!")
    
    print("Done! All 21 essential images created.")
