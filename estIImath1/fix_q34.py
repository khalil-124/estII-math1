import re

with open('est-practice-exam8.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Q34: \\sqrt should become \\\\sqrt
# The current text has: \\(\sqrt{2x + 3} = x\\)
# Which in the file is stored as: \\\\(\\sqrt{2x + 3} = x\\\\)
# But \\sqrt needs to be \\\\sqrt for MathJax to work

# Replace the specific pattern for Q34
old_text = 'question: "If \\\\(\\sqrt{2x + 3} = x\\\\), what is x?"'
new_text = 'question: "If \\\\(\\\\sqrt{2x + 3} = x\\\\), what is x?"'

if old_text in content:
    content = content.replace(old_text, new_text)
    print("Fixed Q34 sqrt - found exact match")
else:
    print("Exact match not found, trying regex...")
    # Try to find and fix any \sqrt patterns that aren't properly escaped
    # In JS string: \\sqrt should be \\\\sqrt
    pattern = r'\\\\sqrt\{'
    matches = re.findall(pattern, content)
    print(f"Found {len(matches)} instances of \\\\sqrt")
    
    # Look for patterns like \\( followed by \sqrt
    content = re.sub(r'\\\\\\(\\\\sqrt\{', r'\\\\(\\\\\\\\sqrt{', content)
    print("Applied regex fix")

with open('est-practice-exam8.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
