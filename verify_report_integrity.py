import pypdf
import re

reader = pypdf.PdfReader('CyberGuard_Project_Report.pdf')
total = len(reader.pages)
print(f"Total Pages: {total}")

# Extract TOC text from page 5 & 6
toc_text = reader.pages[4].extract_text() + "\n" + reader.pages[5].extract_text()
print("\n--- EXTRACTED TOC SAMPLE ---")
for line in toc_text.split('\n')[:25]:
    print(line)

print("\n--- CHAPTER START PAGES IN PDF ---")
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    m = re.search(r'CHAPTER\s+([1-9])', text)
    if m:
        ch_num = m.group(1)
        # Check if it's the chapter title at the top
        if f"CHAPTER {ch_num}" in text[:150]:
            ch_page = i + 1 - 8  # Chapter page number
            print(f"Chapter {ch_num}: PDF Page {i+1} (Chapter Page {ch_page})")

    if "REFERENCES" in text[:150] and i > 50:
        ref_page = i + 1 - 8
        print(f"REFERENCES: PDF Page {i+1} (Chapter Page {ref_page})")

print("\n--- VERIFYING FOOTER NUMBERING ---")
for p in [8, 9, 13, 17, 30, 40, 50, 60, 63]:
    if p < total:
        text = reader.pages[p].extract_text() or ""
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        footer_line = lines[-1] if lines else ""
        header_line = lines[0] if lines else ""
        print(f"PDF Page {p+1}: Header: '{header_line[:45]}' | Footer: '{footer_line}'")
