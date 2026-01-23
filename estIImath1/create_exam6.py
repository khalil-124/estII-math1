"""Replace Exam 6 questions properly"""
import re

# Read template
with open('est-practice-exam6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles
content = content.replace('Practice Exam 5', 'Practice Exam 6')
content = content.replace('Exam 5', 'Exam 6')

# New questions array (clean, with proper IDs 1-40)
new_questions = '''        const questions = [
            // ===== Q1-11: ALGEBRA & FUNCTIONS (27.5%) =====
            {
                id: 1,
                question: "Based on the graph above, at how many points does f(x) cross the x-axis?",
                hasGraph: true,
                graphImage: "images/ex6_q1_polynomial.png",
                options: ["1", "2", "3", "4", "5"],
                answer: 2,
                explanation: ["Count where the graph crosses the x-axis.", "The curve crosses at exactly 3 points.", "These are the real zeros of f(x).", "Read carefully from the graph.", "The answer is C: 3."]
            },
            {
                id: 2,
                question: "If \\\\\\\\(f(x) = x^2 - 5x + 6\\\\), for what values of x is f(x) = 0?",
                options: ["1 and 6", "2 and 3", "-2 and -3", "-1 and -6", "1 and 5"],
                answer: 1,
                explanation: ["Factor: x² - 5x + 6 = (x-2)(x-3).", "Set equal to 0: (x-2)(x-3) = 0.", "x = 2 or x = 3.", "Verify: 2² - 5(2) + 6 = 0 ✓", "The answer is B: 2 and 3."]
            },
            {
                id: 3,
                question: "Solve: \\\\\\\\(4(x - 3) = 2x + 6\\\\)",
                options: ["6", "9", "12", "15", "18"],
                answer: 1,
                explanation: ["Distribute: 4x - 12 = 2x + 6.", "Subtract 2x: 2x - 12 = 6.", "Add 12: 2x = 18.", "Divide: x = 9.", "The answer is B: 9."]
            },
            {
                id: 4,
                question: "If \\\\\\\\(2^{3x} = 64\\\\), what is x?",
                options: ["1", "2", "3", "4", "6"],
                answer: 1,
                explanation: ["64 = 2⁶.", "So 2^(3x) = 2⁶.", "3x = 6.", "x = 2.", "The answer is B: 2."]
            },
            {
                id: 5,
                question: "What is the y-intercept of \\\\\\\\(y = 3x^2 - 6x + 9\\\\)?",
                options: ["3", "6", "9", "-6", "-9"],
                answer: 2,
                explanation: ["Y-intercept occurs when x = 0.", "y = 3(0)² - 6(0) + 9 = 9.", "The constant term is the y-intercept.", "Point: (0, 9).", "The answer is C: 9."]
            },
            {
                id: 6,
                question: "If \\\\\\\\(h(x) = 2x + 1\\\\), what is \\\\\\\\(h(h(2))\\\\)?",
                options: ["5", "7", "9", "11", "13"],
                answer: 3,
                explanation: ["First: h(2) = 2(2) + 1 = 5.", "Then: h(h(2)) = h(5) = 2(5) + 1.", "= 10 + 1 = 11.", "Function composition applied twice.", "The answer is D: 11."]
            },
            {
                id: 7,
                question: "Simplify: \\\\\\\\(\\\\frac{x^2 - 25}{x + 5}\\\\) for \\\\\\\\(x \\\\neq -5\\\\)",
                options: ["x + 5", "x - 5", "x + 25", "x - 25", "5"],
                answer: 1,
                explanation: ["Factor: x² - 25 = (x+5)(x-5).", "Expression = (x+5)(x-5)/(x+5).", "Cancel (x+5).", "= x - 5.", "The answer is B: x - 5."]
            },
            {
                id: 8,
                question: "If \\\\\\\\(|x + 4| = 9\\\\), what is the sum of all solutions?",
                options: ["-8", "-4", "0", "4", "8"],
                answer: 0,
                explanation: ["Case 1: x + 4 = 9, so x = 5.", "Case 2: x + 4 = -9, so x = -13.", "Sum: 5 + (-13) = -8.", "Both values satisfy the equation.", "The answer is A: -8."]
            },
            {
                id: 9,
                question: "The quadratic \\\\\\\\(x^2 - 8x + k = 0\\\\) has roots that differ by 2. What is k?",
                options: ["12", "15", "16", "18", "20"],
                answer: 1,
                explanation: ["Let roots be r and r+2.", "Sum: r + (r+2) = 2r + 2 = 8, so r = 3.", "Roots: 3 and 5.", "Product: k = 3 × 5 = 15.", "The answer is B: 15."]
            },
            {
                id: 10,
                question: "Which equation has no real solutions?",
                options: ["x² + 4 = 0", "x² - 4 = 0", "x² = 4", "x² + 4x + 4 = 0", "x² - 4x + 4 = 0"],
                answer: 0,
                explanation: ["A: x² = -4, no real solution (negative).", "B: x² = 4, x = ±2 ✓", "C: same as B ✓", "D: (x+2)² = 0, x = -2 ✓", "The answer is A: x² + 4 = 0."]
            },
            {
                id: 11,
                question: "If \\\\\\\\(f(x) = \\\\frac{x+3}{2}\\\\), what is \\\\\\\\(f^{-1}(5)\\\\)?",
                options: ["4", "7", "8", "10", "13"],
                answer: 1,
                explanation: ["Find x where f(x) = 5.", "(x+3)/2 = 5.", "x + 3 = 10.", "x = 7.", "The answer is B: 7."]
            },
            // ===== Q12-20: GEOMETRY (22.5%) =====
            {
                id: 12,
                question: "What is the perimeter of the triangle shown in the figure?",
                hasGraph: true,
                graphImage: "images/ex6_q12_triangle.png",
                options: ["15", "16", "17", "18", "19"],
                answer: 3,
                explanation: ["Read side lengths from figure: 5, 6, 7.", "Perimeter = 5 + 6 + 7 = 18.", "Sum of all sides.", "Simple addition.", "The answer is D: 18."]
            },
            {
                id: 13,
                question: "In a right triangle, the legs are 9 and 12. What is the hypotenuse?",
                options: ["13", "15", "17", "21", "108"],
                answer: 1,
                explanation: ["Use Pythagorean theorem: c² = a² + b².", "c² = 81 + 144 = 225.", "c = √225 = 15.", "This is a 3-4-5 triangle ×3.", "The answer is B: 15."]
            },
            {
                id: 14,
                question: "What is the sum of interior angles of a pentagon?",
                options: ["360°", "450°", "540°", "720°", "900°"],
                answer: 2,
                explanation: ["Formula: (n-2) × 180°.", "For pentagon n = 5.", "(5-2) × 180° = 3 × 180°.", "= 540°.", "The answer is C: 540°."]
            },
            {
                id: 15,
                question: "A square has diagonal 10. What is its area?",
                options: ["25", "50", "100", "200", "400"],
                answer: 1,
                explanation: ["For a square: d² = 2s².", "100 = 2s², so s² = 50.", "Area = s² = 50.", "Or: Area = d²/2 = 100/2 = 50.", "The answer is B: 50."]
            },
            {
                id: 16,
                question: "In triangle ABC, ∠A = 50° and ∠B = 70°. What is ∠C?",
                options: ["40°", "50°", "60°", "70°", "80°"],
                answer: 2,
                explanation: ["Sum of angles = 180°.", "∠C = 180° - 50° - 70°.", "= 180° - 120° = 60°.", "Basic triangle property.", "The answer is C: 60°."]
            },
            {
                id: 17,
                question: "A circle has diameter 14. What is its circumference?",
                options: ["7π", "14π", "28π", "49π", "196π"],
                answer: 1,
                explanation: ["C = πd.", "C = π × 14 = 14π.", "Or: r = 7, C = 2πr = 14π.", "Simple formula application.", "The answer is B: 14π."]
            },
            {
                id: 18,
                question: "In a rhombus, the diagonals are 10 and 24. What is the area?",
                options: ["60", "120", "240", "480", "960"],
                answer: 1,
                explanation: ["Area of rhombus = (d₁ × d₂)/2.", "= (10 × 24)/2.", "= 240/2 = 120.", "Diagonals bisect each other at 90°.", "The answer is B: 120."]
            },
            {
                id: 19,
                question: "Based on the bar chart, how many students scored 80 or above?",
                hasGraph: true,
                graphImage: "images/ex6_q19_barchart.png",
                options: ["10", "13", "15", "18", "20"],
                answer: 2,
                explanation: ["Read bars for 80, 90, 100.", "80: 8 students, 90: 5 students, 100: 2 students.", "Total = 8 + 5 + 2 = 15.", "Count from the chart.", "The answer is C: 15."]
            },
            {
                id: 20,
                question: "A sector has central angle 60° and radius 6. What is the arc length?",
                options: ["π", "2π", "3π", "6π", "12π"],
                answer: 1,
                explanation: ["Arc length = (θ/360°) × 2πr.", "= (60/360) × 2π × 6.", "= (1/6) × 12π = 2π.", "Proportional to angle.", "The answer is B: 2π."]
            },
            // ===== Q21-25: COORDINATE GEOMETRY (12.5%) =====
            {
                id: 21,
                question: "What is the slope of the line 2x + 3y = 12?",
                options: ["-3/2", "-2/3", "2/3", "3/2", "4"],
                answer: 1,
                explanation: ["Solve for y: 3y = -2x + 12.", "y = (-2/3)x + 4.", "Slope = -2/3.", "Coefficient of x in slope-intercept form.", "The answer is B: -2/3."]
            },
            {
                id: 22,
                question: "Line passes through (2, 5) with slope 3. What is the y-intercept?",
                options: ["-1", "0", "1", "5", "11"],
                answer: 0,
                explanation: ["y - y₁ = m(x - x₁).", "y - 5 = 3(x - 2).", "y = 3x - 6 + 5 = 3x - 1.", "Y-intercept = -1.", "The answer is A: -1."]
            },
            {
                id: 23,
                question: "What is the equation of a circle centered at origin with radius 4?",
                options: ["x² + y² = 4", "x² + y² = 8", "x² + y² = 16", "(x-4)² + (y-4)² = 16", "x² + y² = 64"],
                answer: 2,
                explanation: ["Standard form: x² + y² = r².", "r = 4, so r² = 16.", "Equation: x² + y² = 16.", "Center at origin means no shifts.", "The answer is C: x² + y² = 16."]
            },
            {
                id: 24,
                question: "Points A(1, 2) and B(7, 10). What is the length of AB?",
                options: ["8", "10", "12", "14", "100"],
                answer: 1,
                explanation: ["d = √[(7-1)² + (10-2)²].", "= √[36 + 64] = √100.", "= 10.", "Distance formula.", "The answer is B: 10."]
            },
            {
                id: 25,
                question: "The vertex of \\\\\\\\(y = (x - 4)^2 - 9\\\\) is at:",
                options: ["(4, 9)", "(4, -9)", "(-4, 9)", "(-4, -9)", "(9, 4)"],
                answer: 1,
                explanation: ["Vertex form: y = (x-h)² + k.", "Vertex at (h, k).", "Here h = 4, k = -9.", "Vertex: (4, -9).", "The answer is B: (4, -9)."]
            },
            // ===== Q26-32: STATISTICS & PROBABILITY (17.5%) =====
            {
                id: 26,
                question: "For data {5, 7, 7, 9, 12}, which is/are true?<br>I. Mean = 8<br>II. Median = 7<br>III. Mode = 7",
                options: ["I only", "II only", "III only", "II and III only", "I, II, and III"],
                answer: 4,
                explanation: ["Mean = (5+7+7+9+12)/5 = 40/5 = 8. I: TRUE.", "Median = 7 (middle value). II: TRUE.", "Mode = 7 (appears twice). III: TRUE.", "All three statements are true.", "The answer is E: I, II, and III."]
            },
            {
                id: 27,
                question: "A bag has 3 red and 5 blue balls. P(red) = ?",
                options: ["3/8", "5/8", "3/5", "5/3", "8/3"],
                answer: 0,
                explanation: ["Total balls = 3 + 5 = 8.", "P(red) = 3/8.", "Favorable over total.", "Simple probability.", "The answer is A: 3/8."]
            },
            {
                id: 28,
                question: "How many 3-letter codes from A, B, C, D, E with no repetition?",
                options: ["15", "60", "120", "125", "243"],
                answer: 1,
                explanation: ["P(5,3) = 5 × 4 × 3.", "= 60.", "Order matters, no repetition.", "Permutation formula.", "The answer is B: 60."]
            },
            {
                id: 29,
                question: "A coin is flipped 3 times. P(exactly 2 heads) = ?",
                options: ["1/8", "1/4", "3/8", "1/2", "5/8"],
                answer: 2,
                explanation: ["Favorable: HHT, HTH, THH = 3 outcomes.", "Total: 2³ = 8 outcomes.", "P = 3/8.", "Or: C(3,2) × (1/2)³ = 3/8.", "The answer is C: 3/8."]
            },
            {
                id: 30,
                question: "The IQR of {2, 5, 7, 9, 12, 15, 18} is:",
                options: ["7", "10", "13", "16", "18"],
                answer: 1,
                explanation: ["Q1 = 5 (median of lower half).", "Q3 = 15 (median of upper half).", "IQR = Q3 - Q1 = 15 - 5 = 10.", "Interquartile range.", "The answer is B: 10."]
            },
            {
                id: 31,
                question: "C(6, 2) = ?",
                options: ["12", "15", "30", "36", "720"],
                answer: 1,
                explanation: ["C(6,2) = 6!/(2! × 4!).", "= (6 × 5)/(2 × 1).", "= 30/2 = 15.", "Combinations formula.", "The answer is B: 15."]
            },
            {
                id: 32,
                question: "Based on the histogram, what is the median class interval?",
                hasGraph: true,
                graphImage: "images/ex6_q32_histogram.png",
                options: ["0-5", "5-10", "10-15", "15-20", "20-25"],
                answer: 2,
                explanation: ["Count total frequency from all bars.", "Find middle position.", "Median falls in 10-15 class.", "Cumulative frequency method.", "The answer is C: 10-15."]
            },
            // ===== Q33-37: NUMERATIONS & OPERATIONS (12.5%) =====
            {
                id: 33,
                question: "What is the 8th term of 5, 9, 13, 17, ...?",
                options: ["29", "33", "37", "41", "45"],
                answer: 1,
                explanation: ["a₁ = 5, d = 4.", "aₙ = a₁ + (n-1)d.", "a₈ = 5 + 7(4) = 5 + 28 = 33.", "Arithmetic sequence.", "The answer is B: 33."]
            },
            {
                id: 34,
                question: "If x/y = 2/3 and y/z = 4/5, what is x/z?",
                options: ["8/15", "6/15", "2/5", "10/12", "3/4"],
                answer: 0,
                explanation: ["x/z = (x/y) × (y/z).", "= (2/3) × (4/5).", "= 8/15.", "Chain multiplication.", "The answer is A: 8/15."]
            },
            {
                id: 35,
                question: "Simplify: \\\\\\\\(\\\\frac{4^5}{4^2}\\\\)",
                options: ["4", "16", "64", "256", "1024"],
                answer: 2,
                explanation: ["Same base: subtract exponents.", "4^(5-2) = 4³ = 64.", "Quotient rule.", "Verify: 1024/16 = 64.", "The answer is C: 64."]
            },
            {
                id: 36,
                question: "In geometric sequence, a₂ = 6 and a₅ = 162. What is r?",
                options: ["2", "3", "4", "5", "6"],
                answer: 1,
                explanation: ["a₅/a₂ = r³.", "162/6 = 27 = r³.", "r = 3.", "Using aₙ = a₁ × r^(n-1).", "The answer is B: 3."]
            },
            {
                id: 37,
                question: "What is 40% of 75?",
                options: ["25", "30", "35", "40", "45"],
                answer: 1,
                explanation: ["40% = 0.40.", "0.40 × 75 = 30.", "Or: (40/100) × 75 = 30.", "Simple percentage.", "The answer is B: 30."]
            },
            // ===== Q38-40: TRIGONOMETRY (7.5%) =====
            {
                id: 38,
                question: "In the right triangle shown, what is sin θ?",
                hasGraph: true,
                graphImage: "images/ex6_q38_triangle.png",
                options: ["3/5", "4/5", "3/4", "4/3", "5/3"],
                answer: 0,
                explanation: ["sin θ = opposite/hypotenuse.", "From triangle: opposite = 3, hypotenuse = 5.", "sin θ = 3/5.", "SOH-CAH-TOA.", "The answer is A: 3/5."]
            },
            {
                id: 39,
                question: "If tan θ = 3/4 (θ acute), what is cos θ?",
                options: ["3/5", "4/5", "3/4", "5/4", "5/3"],
                answer: 1,
                explanation: ["tan θ = opp/adj = 3/4.", "Hypotenuse = √(9+16) = 5.", "cos θ = adj/hyp = 4/5.", "Using Pythagorean theorem.", "The answer is B: 4/5."]
            },
            {
                id: 40,
                question: "For which is sin²θ + cos²θ = 1 directly verified?<br>I. sin 30° = 1/2, cos 30° = √3/2<br>II. sin 45° = cos 45°<br>III. tan θ = sin θ/cos θ",
                options: ["I only", "II only", "I and II only", "III only", "I, II, and III"],
                answer: 0,
                explanation: ["I: (1/2)² + (√3/2)² = 1/4 + 3/4 = 1 ✓ TRUE", "II: True but not directly from identity.", "III: Definition, not from Pythagorean identity.", "Only I directly satisfies the identity.", "The answer is A: I only."]
            }
        ];'''

# Find and replace the questions array
pattern = r'const questions = \[.*?\];'
content = re.sub(pattern, new_questions, content, flags=re.DOTALL)

# Write the file
with open('est-practice-exam6.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Exam 6 created with 40 unique questions!")
