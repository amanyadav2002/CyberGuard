import os
import sys
import pypdf
from reportlab.platypus import SimpleDocTemplate
from report_builder.styles_and_canvas import (
    A4, LEFT_MARGIN, RIGHT_MARGIN, TOP_MARGIN, BOTTOM_MARGIN,
    AcademicNumberedCanvas, setup_styles, OUTPUT_PDF, PAGE_BOOKMARKS, CHAPTER_START_DOC_PAGE
)
from report_builder.front_matter import get_front_matter_story
from report_builder.ch1_and_ch2 import get_ch1_and_ch2_story
from report_builder.ch3_literature import get_ch3_literature_story
from report_builder.ch4_requirements import get_ch4_requirements_story
from report_builder.ch5_design import get_ch5_design_story
from report_builder.ch6_implementation import get_ch6_implementation_story
from report_builder.ch7_testing import get_ch7_testing_story
from report_builder.ch8_results import get_ch8_results_story
from report_builder.ch9_and_refs import get_ch9_and_refs_story

def assemble_full_story(styles):
    story = []
    # Front Matter (Cover, Cert, Decl, Ack, TOC 1&2, LOF, LOT) -> 8 pages
    story.extend(get_front_matter_story(styles))
    # Chapter 1 & Chapter 2
    story.extend(get_ch1_and_ch2_story(styles))
    # Chapter 3 (Literature Review - 20 Papers + Tables)
    story.extend(get_ch3_literature_story(styles))
    # Chapter 4 (System Requirements)
    story.extend(get_ch4_requirements_story(styles))
    # Chapter 5 (System Design - Architecture, UML, DFD, ER, Flowchart)
    story.extend(get_ch5_design_story(styles))
    # Chapter 6 (System Implementation - Formulas, Walkthrough, Algorithms)
    story.extend(get_ch6_implementation_story(styles))
    # Chapter 7 (System Testing - 20 Test Cases & Traceability Matrix)
    story.extend(get_ch7_testing_story(styles))
    # Chapter 8 (Results & Discussion - HUD, Benchmarks, ROC, Confusion Matrix)
    story.extend(get_ch8_results_story(styles))
    # Chapter 9 (Conclusion & Future Scope) + References
    story.extend(get_ch9_and_refs_story(styles))
    return story

def main():
    print("=" * 70)
    print("CYBERGUARD ACADEMIC PROJECT REPORT BUILDER (VTU / RRIT CIRCLUAR)")
    print("=" * 70)
    
    styles = setup_styles()

    # Pass 1: Build to capture exact page bookmarks
    print("\n[Pass 1/2] Compiling document to calculate exact page positions...")
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )
    story_pass1 = assemble_full_story(styles)
    doc.build(story_pass1, canvasmaker=AcademicNumberedCanvas)
    
    print(f"Captured {len(PAGE_BOOKMARKS)} bookmark markers.")
    ch1_page = PAGE_BOOKMARKS.get('CH1', CHAPTER_START_DOC_PAGE)
    print(f"Chapter 1 begins on PDF document page: {ch1_page}")

    # Pass 2: Re-compile with resolved Table of Contents & Lists
    print("\n[Pass 2/2] Re-compiling document with accurate dynamic Table of Contents...")
    doc2 = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN
    )
    story_pass2 = assemble_full_story(styles)
    doc2.build(story_pass2, canvasmaker=AcademicNumberedCanvas)
    
    reader = pypdf.PdfReader(OUTPUT_PDF)
    total_pages = len(reader.pages)
    file_size_mb = os.path.getsize(OUTPUT_PDF) / (1024 * 1024)

    print("\n" + "=" * 70)
    print(f"SUCCESS: Report compiled successfully to {OUTPUT_PDF}")
    print(f"Total Page Count: {total_pages} pages")
    print(f"File Size: {file_size_mb:.2f} MB")
    print("=" * 70)

    if 60 <= total_pages <= 65:
        print(f"[VERIFIED] Page count ({total_pages}) is strictly within requested range 60 to 65 pages!")
    else:
        print(f"[ATTENTION] Page count is {total_pages}. Target is strictly 60 to 65 pages.")

if __name__ == '__main__':
    main()
