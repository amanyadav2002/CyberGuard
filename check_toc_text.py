import pypdf

reader = pypdf.PdfReader('CyberGuard_Project_Report.pdf')
print("=== PAGE 5: TOC PART 1 ===")
print(reader.pages[4].extract_text())
print("\n=== PAGE 6: TOC PART 2 ===")
print(reader.pages[5].extract_text())
print("\n=== PAGE 7: LIST OF FIGURES ===")
print(reader.pages[6].extract_text())
print("\n=== PAGE 8: LIST OF TABLES ===")
print(reader.pages[7].extract_text())
