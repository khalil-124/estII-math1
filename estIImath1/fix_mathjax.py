"""Fix MathJax escaping in Exam 6"""
# Read file
with open('est-practice-exam6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace \( with \\( for MathJax (in JavaScript strings)
# We need to find \( that is not already \\(
import re

# Count occurrences before
count_before = content.count('\\(')
count_double_before = content.count('\\\\(')

# Replace single \ with double \\ before ( and )
# But only in the questions array section
content = content.replace('\\(', '\\\\(')
content = content.replace('\\)', '\\\\)')
content = content.replace('\\\\\\\\(', '\\\\(')  # Fix any that got over-escaped
content = content.replace('\\\\\\\\)', '\\\\)')

# Save
with open('est-practice-exam6.html', 'w', encoding='utf-8') as f:
    f.write(content)

count_after = content.count('\\\\(')
print(f"[OK] Fixed MathJax escaping")
print(f"Before: {count_before} single backslash, {count_double_before} double")
print(f"After: {count_after} double backslash occurrences")
