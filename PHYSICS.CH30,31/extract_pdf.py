import sys
import subprocess

try:
    from pypdf import PdfReader
except ImportError:
    # Should be installed by previous run, but just in case
    print("pypdf missing?")
    sys.exit(1)

try:
    reader = PdfReader("30_LectureOutline.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open("pdf_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction complete. Written to pdf_content.txt")
except Exception as e:
    print(f"Error: {e}")
