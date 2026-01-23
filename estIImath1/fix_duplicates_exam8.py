"""Remove all duplicate questions from Exam 8"""
import re

with open('est-practice-exam8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove duplicate Q6 entries (keep last one which is correct)
# The pattern is to find the questions array and clean it up

# Find Questions 6 with the problems and remove them
# Q6 attempt 1 - remove
content = content.replace('''            {
                id: 6,
                question: "If \\\\(|3x - 6| = |x + 2|\\\\), what is the sum of all solutions?",
                options: ["1", "2", "4", "6", "8"],
                answer: 1,
                explanation: ["Case 1: 3x - 6 = x + 2 → 2x = 8, x = 4.", "Case 2: 3x - 6 = -(x + 2) → 3x - 6 = -x - 2.", "4x = 4, x = 1.", "Sum = 4 + 1... Wait, let me check: 4x = 4, x = 1. But also -2 case.", "Actually: Case 2: 3x-6 = -x-2, 4x = 4, x = 1. Sum = 4 + 1 = 5. Hmm not in options. Let me recalc."]
            },
            {''', '''            {''')

content = content.replace('''            {
                id: 6,
                question: "If \\\\(|2x - 4| = |x + 1|\\\\), what is the sum of all solutions?",
                options: ["1", "2", "3", "4", "5"],
                answer: 2,
                explanation: ["Case 1: 2x - 4 = x + 1 → x = 5.", "Case 2: 2x - 4 = -(x + 1) = -x - 1.", "3x = 3, x = 1.", "Sum = 5 + 1 = 6. Hmm. Let me use x = 5, 1. Sum = 6? Not matching. Actually: 2(5)-4=6, 5+1=6 ✓. 2(1)-4=-2, |−2|=2, 1+1=2 ✓. Sum = 6. Let me fix options."]
            },
            {''', '''            {''')

content = content.replace('''            {
                id: 6,
                question: "If \\\\(|2x - 4| = |x - 1|\\\\), what is the sum of all solutions?",
                options: ["1", "2", "3", "5/3", "8/3"],
                answer: 2,
                explanation: ["Case 1: 2x - 4 = x - 1 → x = 3.", "Case 2: 2x - 4 = -(x - 1) = -x + 1.", "3x = 5, x = 5/3.", "Sum = 3 + 5/3 = 14/3. Hmm still not matching. Let me just use different question."]
            },
            {''', '''            {''')

# Remove duplicate Q23
content = content.replace('''            {
                id: 23,
                question: "The line 2x - 3y = 6 is perpendicular to ax + 2y = 5. What is a?",
                options: ["-3", "-2", "2", "3", "4"],
                answer: 2,
                explanation: ["Line 1 slope: 2x - 3y = 6 → y = (2/3)x - 2, m₁ = 2/3.", "For perpendicular: m₁ × m₂ = -1.", "(2/3) × m₂ = -1, m₂ = -3/2.", "Line 2: ax + 2y = 5 → y = (-a/2)x + 5/2.", "-a/2 = -3/2, a = 3. Hmm not matching options."]
            },
            {''', '''            {''')

# Remove duplicate Q28
content = content.replace('''            {
                id: 28,
                question: "How many ways can 8 people sit in a row if 3 specific people must sit together?",
                options: ["720", "4320", "5040", "21600", "40320"],
                answer: 3,
                explanation: ["Treat 3 people as 1 unit: 6 units.", "Arrange 6 units: 6! = 720.", "The 3 people can arrange among themselves: 3! = 6.", "Total = 720 × 6 = 4320. Hmm. Wait: 6 units arranged in 6! ways, times 3! internal = 720 × 6 = 4320."]
            },
            {''', '''            {''')

# Remove duplicate Q30
content = content.replace('''            {
                id: 30,
                question: "Data set: {3, 5, 7, 9, x} has mean equal to median. What is x?",
                options: ["5", "6", "7", "8", "11"],
                answer: 1,
                explanation: ["Median = 7 (middle value, assuming x ≥ 9 or sorted).", "If x ≤ 9: median is 7.", "Mean = (3+5+7+9+x)/5 = (24+x)/5.", "(24+x)/5 = 7 → 24 + x = 35 → x = 11.", "Wait: if x = 11, sorted: 3,5,7,9,11, median = 7. Mean = 35/5 = 7 ✓", "The answer is E: 11."]
            },
            {''', '''            {''')

content = content.replace('''            {
                id: 30,
                question: "Data: {2, 5, 8, 10, x} has mean = median. What is x?",
                options: ["5", "7", "8", "10", "15"],
                answer: 0,
                explanation: ["If sorted with x, find when mean = median.", "Try x = 5: sorted {2,5,5,8,10}, median = 5, mean = 30/5 = 6 ≠ 5.", "Try x = 10: {2,5,8,10,10}, median = 8, mean = 35/5 = 7 ≠ 8.", "Try finding: median depends on x position. This is tricky - let me use simpler version."]
            },
            {''', '''            {''')

with open('est-practice-exam8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Removed duplicate questions from Exam 8")
