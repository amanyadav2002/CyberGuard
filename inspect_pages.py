import pypdf

reader = pypdf.PdfReader('CyberGuard_Project_Report.pdf')
print(f"Total Pages in PDF: {len(reader.pages)}")
for i in range(min(15, len(reader.pages))):
    text = reader.pages[i].extract_text() or ""
    first_line = text.strip().split('\n')[0] if text.strip() else "[BLANK]"
    print(f"Page {i+1}: {first_line[:60]}")
