"""Fix ALL MathJax escaping in Exam 7 - frac, sqrt, and all backslash commands"""
with open('est-practice-exam7.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all backslash commands
content = content.replace('\\frac', '\\\\frac')
content = content.replace('\\sqrt', '\\\\sqrt')
content = content.replace('\\\\\\\\frac', '\\\\frac')  # Fix over-escaped
content = content.replace('\\\\\\\\sqrt', '\\\\sqrt')

with open('est-practice-exam7.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("[OK] Fixed all MathJax (frac, sqrt) escaping in Exam 7")
