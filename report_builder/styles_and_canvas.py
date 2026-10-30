import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

OUTPUT_PDF = "CyberGuard_Project_Report.pdf"
ASSETS_DIR = "report_assets"

# Page Dimensions (A4: 595.27 x 841.89 points)
PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 90.0    # 1.25 inch
RIGHT_MARGIN = 72.0   # 1.0 inch
TOP_MARGIN = 54.0     # 0.75 inch
BOTTOM_MARGIN = 54.0  # 0.75 inch
USABLE_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN  # 433.27 pt

PAGE_BOOKMARKS = {}
CHAPTER_START_DOC_PAGE = 9

class PageMarker(Flowable):
    def __init__(self, key):
        super().__init__()
        self.key = key
    def draw(self):
        page = self.canv._pageNumber
        PAGE_BOOKMARKS[self.key] = page

class AcademicNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        global CHAPTER_START_DOC_PAGE
        total_pages = len(self.pages)
        start_page = CHAPTER_START_DOC_PAGE
        
        for page_data in self.pages:
            self.__dict__.update(page_data)
            page_num = self._pageNumber
            
            # 1. Page 1 to 5 Border requirement:
            # "All the pages should have border ( Page No. 1 to 5)"
            if 1 <= page_num <= 5:
                # Page 1 cream background
                if page_num == 1:
                    self.saveState()
                    self.setFillColor(colors.HexColor('#FAF8EE')) # Academic Cream
                    self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
                    self.restoreState()
                
                # Double border in Academic Navy
                self.saveState()
                self.setStrokeColor(colors.HexColor('#1B365D'))
                self.setLineWidth(1.8)
                self.rect(26, 26, PAGE_WIDTH - 52, PAGE_HEIGHT - 52, fill=0, stroke=1)
                self.setLineWidth(0.6)
                self.rect(30, 30, PAGE_WIDTH - 60, PAGE_HEIGHT - 60, fill=0, stroke=1)
                self.restoreState()
            
            # 2. Header and Footer for Chapter pages:
            # "Header – Title of the Project"
            # "Footer Department Of CSE,RRIT and Page No Font Size is 8"
            # "Page no starts from footer of Chapter 1 till end"
            if page_num >= start_page:
                self.saveState()
                self.setFont('Times-Italic', 8.5)
                self.setFillColor(colors.HexColor('#4A5568'))
                header_text = "Cyber Threat Detection Using Machine Learning"
                self.drawString(LEFT_MARGIN, PAGE_HEIGHT - 42, header_text)
                
                # Header rule
                self.setStrokeColor(colors.HexColor('#CBD5E1'))
                self.setLineWidth(0.6)
                self.line(LEFT_MARGIN, PAGE_HEIGHT - 46, PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 46)
                
                # Footer rule
                self.line(LEFT_MARGIN, 46, PAGE_WIDTH - RIGHT_MARGIN, 46)
                # Footer text
                self.setFont('Times-Roman', 8)
                self.setFillColor(colors.HexColor('#2D3748'))
                self.drawString(LEFT_MARGIN, 34, "Department Of CSE, RRIT")
                # Right footer: Page number starting at 1 on Chapter 1
                curr_ch_page = page_num - (start_page - 1)
                self.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 34, f"Page {curr_ch_page}")
                self.restoreState()
                
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

def setup_styles():
    styles = getSampleStyleSheet()
    
    # Custom Paragraph Styles according to guidelines:
    # Font Size: 18 - Chapter Name, 16 - Heading, 14 - Sub Heading, 12 - Contents / Paragraphs, 10 - Table Name / Figure Name
    # Font Type: Times new roman
    # Line spacing: 1.5 (leading = fontSize * 1.5)
    
    styles.add(ParagraphStyle(
        name='ProjectCoverMainTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=10
    ))
    styles.add(ParagraphStyle(
        name='CoverCollegeHeader',
        fontName='Times-Bold',
        fontSize=13.5,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#881337'),
        spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name='CoverSubHeader',
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#334155'),
        spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        name='FrontMatterTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=14
    ))
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=14,
        spaceAfter=14,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='SectionHeading',
        fontName='Times-Bold',
        fontSize=15,
        leading=21,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=13,
        spaceAfter=7,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='SubSectionHeading',
        fontName='Times-Bold',
        fontSize=13,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#334155'),
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='SubSubSectionHeading',
        fontName='Times-Bold',
        fontSize=12,
        leading=16,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#475569'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='BodyContent',
        fontName='Times-Roman',
        fontSize=12,
        leading=18, # 1.5 line spacing (12 * 1.5 = 18 pt)
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=7
    ))
    styles.add(ParagraphStyle(
        name='BodyBullet',
        fontName='Times-Roman',
        fontSize=12,
        leading=18,
        alignment=TA_JUSTIFY,
        leftIndent=18,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name='CaptionText',
        fontName='Times-Bold',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=5,
        spaceAfter=8,
        keepWithNext=False
    ))
    styles.add(ParagraphStyle(
        name='TableCell',
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0F172A')
    ))
    styles.add(ParagraphStyle(
        name='TableCellCenter',
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A')
    ))
    styles.add(ParagraphStyle(
        name='TableHeader',
        fontName='Times-Bold',
        fontSize=9,
        leading=12.5,
        alignment=TA_CENTER,
        textColor=colors.white
    ))
    styles.add(ParagraphStyle(
        name='CodeSnippet',
        fontName='Courier',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        name='EquationText',
        fontName='Times-Italic',
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=4,
        spaceAfter=6
    ))
    return styles

def get_page_str(key, default_val):
    if key in PAGE_BOOKMARKS and 'CH1' in PAGE_BOOKMARKS:
        offset = PAGE_BOOKMARKS['CH1'] - 1
        return str(max(1, PAGE_BOOKMARKS[key] - offset))
    return str(default_val)
