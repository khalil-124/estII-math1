"""Fix Exam 8: MathJax escaping and remove duplicates"""
import re

with open('est-practice-exam8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix MathJax
content = content.replace('\\frac', '\\\\frac')
content = content.replace('\\sqrt', '\\\\sqrt')
content = content.replace('\\log', '\\\\log')
content = content.replace('\\lim', '\\\\lim')
content = content.replace('\\to', '\\\\to')
content = content.replace('\\\\\\\\frac', '\\\\frac')
content = content.replace('\\\\\\\\sqrt', '\\\\sqrt')
content = content.replace('\\\\\\\\log', '\\\\log')
content = content.replace('\\\\\\\\lim', '\\\\lim')
content = content.replace('\\\\\\\\to', '\\\\to')

with open('est-practice-exam8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Fixed MathJax escaping")
