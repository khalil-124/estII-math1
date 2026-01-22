"""Generate graph images for Practice Exam 2 - NO ANSWER SPOILERS"""
import matplotlib.pyplot as plt
import numpy as np
import os
os.makedirs('images', exist_ok=True)

# Q17: Histogram - shows data, student must add values
def create_histogram():
    fig, ax = plt.subplots(figsize=(8, 6))
    ranges = ['50-60', '60-70', '70-80', '80-90', '90-100']
    frequencies = [4, 7, 12, 9, 5]
    colors = ['#3498db', '#3498db', '#e74c3c', '#e74c3c', '#3498db']
    bars = ax.bar(ranges, frequencies, color=colors, edgecolor='black', linewidth=1.2)
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
    print("[OK] ex2_q17_histogram.png")

# Q21: Piecewise function - NO LABELS showing f(2) or f(-1) values!
def create_piecewise_graph():
    fig, ax = plt.subplots(figsize=(8, 6))
    x1 = np.linspace(-4, 0, 100)
    y1 = x1 + 3
    x2 = np.linspace(0, 4, 100)
    y2 = -x2 + 3
    ax.plot(x1, y1, 'b-', linewidth=2.5, label='f(x)')
    ax.plot(x2, y2, 'b-', linewidth=2.5)
    # NO point labels! Student must read from graph
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-2, 5)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title('Graph of f(x)', fontsize=14, fontweight='bold')
    ax.set_xticks(range(-4, 5))
    ax.set_yticks(range(-2, 6))
    plt.tight_layout()
    plt.savefig('images/ex2_q21_piecewise.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex2_q21_piecewise.png")

# Q32: Scatter plot - show x=6 line but NOT the y value!
def create_scatter_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    x_data = [1, 2, 3, 4, 5, 7, 8]
    y_data = [3, 5, 6, 9, 11, 15, 17]
    ax.scatter(x_data, y_data, s=100, c='#e74c3c', edgecolors='black', linewidth=1.5, zorder=5)
    x_line = np.array([0, 9])
    y_line = 2 * x_line + 1
    ax.plot(x_line, y_line, 'b--', linewidth=2, alpha=0.7, label='Trend line')
    # Only mark x=6, NOT the y value
    ax.axvline(x=6, color='green', linestyle=':', linewidth=2, alpha=0.7)
    ax.annotate('x = 6\ny = ?', (6.2, 3), fontsize=11, color='green')
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 20)
    ax.set_xlabel('x', fontsize=12, fontweight='bold')
    ax.set_ylabel('y', fontsize=12, fontweight='bold')
    ax.set_title('Estimate y when x = 6', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(loc='upper left')
    ax.set_xticks(range(0, 10))
    ax.set_yticks(range(0, 21, 2))
    plt.tight_layout()
    plt.savefig('images/ex2_q32_scatter.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] ex2_q32_scatter.png")

if __name__ == "__main__":
    print("Generating Exam 2 images (NO SPOILERS)...")
    create_histogram()
    create_piecewise_graph()
    create_scatter_plot()
    print("\n[OK] All Exam 2 images done!")
