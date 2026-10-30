import os
import sys
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable, Flowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
import pypdf

OUTPUT_PDF = "CyberGuard_Project_Report.pdf"
ASSETS_DIR = "report_assets"

PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 90.0    # 1.25 inch (90 pt)
RIGHT_MARGIN = 72.0   # 1.0 inch (72 pt)
TOP_MARGIN = 54.0     # 0.75 inch (54 pt)
BOTTOM_MARGIN = 54.0  # 0.75 inch (54 pt)
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
            
            # 1. Border on Page 1 to 5 (as required by circular)
            if 1 <= page_num <= 5:
                if page_num == 1:
                    self.saveState()
                    self.setFillColor(colors.HexColor('#FAF8EE')) # Cream covering sheet
                    self.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
                    self.restoreState()
                
                self.saveState()
                self.setStrokeColor(colors.HexColor('#1B365D')) # Academic Navy border
                self.setLineWidth(1.8)
                self.rect(26, 26, PAGE_WIDTH - 52, PAGE_HEIGHT - 52, fill=0, stroke=1)
                self.setLineWidth(0.6)
                self.rect(30, 30, PAGE_WIDTH - 60, PAGE_HEIGHT - 60, fill=0, stroke=1)
                self.restoreState()
            
            # 2. Header and Footer for Chapters (from Chapter 1 onwards)
            if page_num >= start_page:
                self.saveState()
                self.setFont('Times-Italic', 8.5)
                self.setFillColor(colors.HexColor('#4A5568'))
                header_text = "Cyber Threat Detection Using Machine Learning"
                self.drawString(LEFT_MARGIN, PAGE_HEIGHT - 42, header_text)
                
                self.setStrokeColor(colors.HexColor('#CBD5E1'))
                self.setLineWidth(0.6)
                self.line(LEFT_MARGIN, PAGE_HEIGHT - 46, PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 46)
                
                self.line(LEFT_MARGIN, 46, PAGE_WIDTH - RIGHT_MARGIN, 46)
                self.setFont('Times-Roman', 8)
                self.setFillColor(colors.HexColor('#2D3748'))
                self.drawString(LEFT_MARGIN, 34, "Department Of CSE, RRIT")
                curr_ch_page = page_num - (start_page - 1)
                self.drawRightString(PAGE_WIDTH - RIGHT_MARGIN, 34, f"Page {curr_ch_page}")
                self.restoreState()
                
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

def setup_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name='CoverCollegeHeader',
        fontName='Times-Bold',
        fontSize=12,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#881337'),
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name='CoverSubHeader',
        fontName='Times-Roman',
        fontSize=8.5,
        leading=11.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#334155'),
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        name='ProjectCoverMainTitle',
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='FrontMatterTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=12
    ))
    styles.add(ParagraphStyle(
        name='ChapterTitle',
        fontName='Times-Bold',
        fontSize=18,
        leading=24,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=14,
        spaceAfter=12,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='SectionHeading',
        fontName='Times-Bold',
        fontSize=16,
        leading=22,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='SubSectionHeading',
        fontName='Times-Bold',
        fontSize=14,
        leading=19,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#334155'),
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name='BodyContent',
        fontName='Times-Roman',
        fontSize=12,
        leading=18, # 1.5 line spacing
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
        leftIndent=16,
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
    return styles

def get_page_str(key, default_val):
    if key in PAGE_BOOKMARKS and 'CH1' in PAGE_BOOKMARKS:
        offset = PAGE_BOOKMARKS['CH1'] - 1
        return str(max(1, PAGE_BOOKMARKS[key] - offset))
    return str(default_val)
