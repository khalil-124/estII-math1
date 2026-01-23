"""Fix Exam 7: remove duplicates and fix MathJax escaping"""
import re

with open('est-practice-exam7.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix MathJax escaping: \( → \\(
content = content.replace('\\(', '\\\\(')
content = content.replace('\\)', '\\\\)')
content = content.replace('\\\\\\\\(', '\\\\(')  # Fix over-escaped
content = content.replace('\\\\\\\\)', '\\\\)')

# Save
with open('est-practice-exam7.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Fixed MathJax escaping in Exam 7")
