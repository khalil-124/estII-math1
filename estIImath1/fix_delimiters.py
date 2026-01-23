"""Fix MathJax delimiters in Exam 8 - need \\\\( for JavaScript strings"""
with open('est-practice-exam8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The script wrote \\( which becomes \( in the file
# We need \\\\( in the source to get \\( in HTML
content = content.replace('\\(', '\\\\(')
content = content.replace('\\)', '\\\\)')
# Fix any over-escaping
content = content.replace('\\\\\\\\(', '\\\\(')
content = content.replace('\\\\\\\\)', '\\\\)')

with open('est-practice-exam8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Fixed MathJax delimiters in Exam 8")
