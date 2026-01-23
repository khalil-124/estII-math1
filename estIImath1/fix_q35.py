"""Remove duplicate Q35 from Exam 7"""
with open('est-practice-exam7.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove first Q35 (with answer: 2)
old_text = '''            {
                id: 35,
                question: "If \\\\(2^a = 3\\\\) and \\\\(2^b = 5\\\\), what is \\\\(2^{2a+b}\\\\)?",
                options: ["8", "15", "30", "45", "225"],
                answer: 2,
                explanation: ["2^(2a+b) = 2^(2a) × 2^b.", "= (2^a)² × 2^b.", "= 3² × 5 = 9 × 5 = 45. Wait.", "Actually = 9 × 5 = 45. Answer D.", "The answer is D: 45."]
            },
            {'''

new_text = '''            {'''

content = content.replace(old_text, new_text)

with open('est-practice-exam7.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Removed duplicate Q35")
