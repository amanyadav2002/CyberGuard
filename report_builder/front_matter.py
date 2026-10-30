import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from report_builder.styles_and_canvas import PageMarker, get_page_str

def get_front_matter_story(styles):
    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 4))
    
    # Official Logos Header Table
    logo_data = [
        [
            Image('report_assets/vtu_logo.jpeg', width=52, height=52),
            Paragraph(
                "<b>PKM EDUCATIONAL TRUST &reg;</b><br/>"
                "<font size='12' color='#881337'><b>R. R. INSTITUTE OF TECHNOLOGY</b></font><br/>"
                "<font size='8' color='#334155'><b>(An Autonomous Institution under VTU Belgaum)</b><br/>"
                "Approved by AICTE, New Delhi, Recognised by Govt. of Karnataka<br/>"
                "Accredited by NAAC with A+, NBA<br/>"
                "Raja Reddy Layout, Chikkabanavara, Bengaluru – 560 090</font>",
                styles['CoverCollegeHeader']
            ),
            Image('report_assets/rrit_logo.png', width=52, height=62)
        ]
    ]
    t_logo = Table(logo_data, colWidths=[60, 313, 60])
    t_logo.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (0,0), 'LEFT'),
        ('ALIGN', (1,0), (1,0), 'CENTER'),
        ('ALIGN', (2,0), (2,0), 'RIGHT'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_logo)
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#881337'), spaceAfter=8))
    
    story.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</b>", styles['CoverCollegeHeader']))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>MAJOR PROJECT WORK RECORD (PHASE 1 & 2)</b>", ParagraphStyle('Rec', fontName='Times-Bold', fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#475569'))))
    story.append(Paragraph("<b>BATCH NO: G-05 &nbsp;&nbsp;|&nbsp;&nbsp; ACADEMIC YEAR: 2025 – 2026</b>", ParagraphStyle('Rec2', fontName='Times-Bold', fontSize=9, leading=12, alignment=TA_CENTER, textColor=colors.HexColor('#1E293B'))))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("A PROJECT REPORT ON", ParagraphStyle('Sub', fontName='Times-Bold', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#475569'))))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>CYBER THREAT DETECTION USING MACHINE LEARNING</b>", styles['ProjectCoverMainTitle']))
    story.append(Paragraph("<b>(Phishing URL & Android APK Malware Detection Platform)</b>", ParagraphStyle('Subtheme', fontName='Times-BoldItalic', fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor('#1E3A8A'))))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("<i>Submitted in partial fulfillment of the requirements for the award of degree of</i>", ParagraphStyle('Sub2', fontName='Times-Italic', fontSize=9, leading=12, alignment=TA_CENTER, textColor=colors.HexColor('#334155'))))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>BACHELOR OF ENGINEERING IN COMPUTER SCIENCE AND ENGINEERING</b>", ParagraphStyle('Deg', fontName='Times-Bold', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#0F172A'))))
    story.append(Spacer(1, 10))

    # Team Members & Guides Table
    team_data = [
        [Paragraph("<b>Submitted by:</b>", styles['TableCell']), Paragraph("<b>Under the Guidance of:</b>", styles['TableCell'])],
        [
            Paragraph(
                "<b>1. AMAN YADAV</b> (USN: <b>1RI23CS007</b>)<br/>"
                "<b>2. ASHRAF SAMI</b> (USN: <b>1RI23CS013</b>) [Team Leader]<br/>"
                "<b>3. ASHUTOSH DAYAL CHOUDHARY</b> (USN: <b>1RI23CS014</b>)<br/>"
                "<b>4. DUSHYANTH R</b> (USN: <b>1RI23CS046</b>)<br/>"
                "<i>6th Semester B.E., Section B, Dept. of CSE, RRIT</i>",
                styles['TableCell']
            ),
            Paragraph(
                "<b>Prof. ASHA V</b><br/>"
                "Assistant Professor<br/>"
                "Department of Computer Science & Engg.<br/>"
                "R. R. Institute of Technology, Bengaluru<br/><br/>"
                "<b>Under the Leadership of:</b><br/>"
                "<b>Dr. MANJUNATH R</b><br/>"
                "Professor & Head of Department<br/>"
                "Department of Computer Science & Engg., RRIT",
                styles['TableCell']
            )
        ]
    ]
    t_team = Table(team_data, colWidths=[220, 213])
    t_team.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_team)
    story.append(Spacer(1, 10))
    story.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</b><br/><b>R. R. INSTITUTE OF TECHNOLOGY</b><br/>Raja Reddy Layout, Chikkabanavara, Bengaluru – 560 090<br/><b>2025 – 2026</b>", ParagraphStyle('FootC', fontName='Times-Bold', fontSize=9, leading=12, alignment=TA_CENTER, textColor=colors.HexColor('#0F172A'))))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("PKM EDUCATIONAL TRUST &reg;", styles['CoverSubHeader']))
    story.append(Paragraph("R. R. INSTITUTE OF TECHNOLOGY", styles['CoverCollegeHeader']))
    story.append(Paragraph("<b>(An Autonomous Institution under VTU Belgaum)</b>", styles['CoverSubHeader']))
    story.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING", styles['CoverCollegeHeader']))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#881337'), spaceAfter=10))
    story.append(Paragraph("CERTIFICATE", styles['FrontMatterTitle']))
    story.append(Spacer(1, 8))
    
    cert_text = (
        "This is to certify that the Major Project Work entitled <b>\"CYBER THREAT DETECTION USING MACHINE LEARNING\" "
        "(Phishing URL & Android APK Malware Detection Platform)</b> is a bonafide work carried out by "
        "<b>AMAN YADAV (1RI23CS007)</b>, <b>ASHRAF SAMI (1RI23CS013)</b>, <b>ASHUTOSH DAYAL CHOUDHARY (1RI23CS014)</b>, "
        "and <b>DUSHYANTH R (1RI23CS046)</b>, students of 6th Semester B.E., Department of Computer Science & Engineering, "
        "in partial fulfillment of the requirements for the award of degree of <b>Bachelor of Engineering in Computer Science & Engineering</b> "
        "of Visvesvaraya Technological University (VTU), Belagavi, during the academic year 2025–2026.<br/><br/>"
        "It is certified that all suggestions indicated during internal and continuous reviews have been incorporated into this report. "
        "The project report has been approved as it satisfies the academic requirements prescribed by the University for Major Project Work."
    )
    story.append(Paragraph(cert_text, styles['BodyContent']))
    story.append(Spacer(1, 16))

    sig_data = [
        [
            Paragraph("<b>Prof. ASHA V</b><br/>Project Guide<br/>Assistant Professor, CSE", styles['TableCellCenter']),
            Paragraph("<b>Dr. SWETHA G</b><br/>Project Coordinator<br/>Associate Professor, CSE", styles['TableCellCenter']),
            Paragraph("<b>Dr. MANJUNATH R</b><br/>Professor & HOD<br/>Dept. of CSE, RRIT", styles['TableCellCenter']),
            Paragraph("<b>Dr. MAHENDRA K V</b><br/>Principal<br/>RRIT, Bengaluru", styles['TableCellCenter'])
        ]
    ]
    t_sig = Table(sig_data, colWidths=[108, 108, 108, 109])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'BOTTOM'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sig)
    story.append(Spacer(1, 16))

    viva_data = [
        [Paragraph("<b>Name of Examiners</b>", styles['TableHeader']), Paragraph("<b>Signature with Date</b>", styles['TableHeader'])],
        [Paragraph("1. ________________________________________", styles['TableCell']), Paragraph("_______________________", styles['TableCellCenter'])],
        [Paragraph("2. ________________________________________", styles['TableCell']), Paragraph("_______________________", styles['TableCellCenter'])],
    ]
    t_viva = Table(viva_data, colWidths=[240, 193])
    t_viva.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_viva)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: DECLARATION
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("DECLARATION", styles['FrontMatterTitle']))
    story.append(Spacer(1, 12))
    
    decl_text = (
        "We, the undersigned students of the 6th Semester Bachelor of Engineering in Computer Science & Engineering "
        "at <b>R. R. Institute of Technology, Bengaluru</b>, hereby declare that the project work entitled "
        "<b>\"CYBER THREAT DETECTION USING MACHINE LEARNING\"</b> has been independently executed by our team "
        "under the esteemed guidance of <b>Prof. Asha V</b>, Assistant Professor, Department of Computer Science & Engineering.<br/><br/>"
        "We certify that this report presents our authentic design, implementation, and empirical testing. "
        "All software source code, architectural flowcharts, database schemas, feature extraction pipelines, "
        "and user interface components documented herein represent the work performed by our team. "
        "All external algorithms, libraries, reference research papers, and software tools have been duly and formally "
        "acknowledged in accordance with standard academic citation standards.<br/><br/>"
        "We further declare that the work embodied in this project report has been undertaken with academic integrity and "
        "has not been submitted previously to this or any other university or institution for the award of any degree, "
        "diploma, or fellowship."
    )
    story.append(Paragraph(decl_text, styles['BodyContent']))
    story.append(Spacer(1, 20))
    
    decl_team_data = [
        [Paragraph("<b>Candidate Name</b>", styles['TableHeader']), Paragraph("<b>USN</b>", styles['TableHeader']), Paragraph("<b>Signature</b>", styles['TableHeader'])],
        [Paragraph("AMAN YADAV", styles['TableCell']), Paragraph("1RI23CS007", styles['TableCellCenter']), Paragraph("_______________________", styles['TableCellCenter'])],
        [Paragraph("ASHRAF SAMI", styles['TableCell']), Paragraph("1RI23CS013", styles['TableCellCenter']), Paragraph("_______________________", styles['TableCellCenter'])],
        [Paragraph("ASHUTOSH DAYAL CHOUDHARY", styles['TableCell']), Paragraph("1RI23CS014", styles['TableCellCenter']), Paragraph("_______________________", styles['TableCellCenter'])],
        [Paragraph("DUSHYANTH R", styles['TableCell']), Paragraph("1RI23CS046", styles['TableCellCenter']), Paragraph("_______________________", styles['TableCellCenter'])],
    ]
    t_dt = Table(decl_team_data, colWidths=[150, 130, 153])
    t_dt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_dt)
    story.append(Spacer(1, 16))
    story.append(Paragraph("<b>Date:</b> 06/10/2026 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Place:</b> Bengaluru", styles['BodyContent']))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("ACKNOWLEDGEMENT", styles['FrontMatterTitle']))
    story.append(Spacer(1, 14))
    
    ack_text = (
        "The completion of any comprehensive engineering project is never the effort of an individual alone; it represents "
        "the encouragement, academic resources, and generous guidance of many individuals who supported us at every turn.<br/><br/>"
        "We take this opportunity to express our heartfelt gratitude to the management of <b>PKM Educational Trust &reg;</b> "
        "and our respected <b>Principal, Dr. Mahendra K V</b>, R. R. Institute of Technology, for providing the necessary infrastructure, high-speed "
        "computational laboratory facilities, and an encouraging academic atmosphere that made this project possible.<br/><br/>"
        "We are profoundly indebted to <b>Dr. Manjunath R</b>, Professor & Head of the Department of Computer Science & Engineering, "
        "for his inspirational leadership, steady encouragement, and constructive critique throughout the project lifecycle.<br/><br/>"
        "We convey our sincere and deepest gratitude to our project guide, <b>Prof. Asha V</b>, Assistant Professor, Department of "
        "Computer Science & Engineering. Her patient guidance, technical insights in machine learning, and constant feedback on our "
        "feature extraction pipelines were invaluable in helping us overcome complex technical hurdles.<br/><br/>"
        "We also sincerely thank our project coordinator, <b>Dr. Swetha G</b>, and all faculty and technical staff of the CSE Department "
        "for their timely suggestions, evaluations, and logistical support during our Phase 1 and Phase 2 reviews.<br/><br/>"
        "Finally, we wish to express our warmest appreciation to our <b>parents and family members</b> whose unconditional love, sacrifices, "
        "and moral support kept us motivated throughout our engineering education, as well as our <b>friends and classmates</b> who "
        "offered feedback and helpful discussions."
    )
    story.append(Paragraph(ack_text, styles['BodyContent']))
    story.append(Spacer(1, 18))
    story.append(Paragraph("<b>Project Team — Batch G-05</b><br/>Aman Yadav (1RI23CS007)<br/>Ashraf Sami (1RI23CS013)<br/>Ashutosh Dayal Choudhary (1RI23CS014)<br/>Dushyanth R (1RI23CS046)", ParagraphStyle('Rt', fontName='Times-Bold', fontSize=10, leading=14, alignment=TA_RIGHT, textColor=colors.HexColor('#0F172A'))))
    story.append(PageBreak())

    # =========================================================================
    # PAGES 5 & 6: TABLE OF CONTENTS (2 Pages)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("TABLE OF CONTENTS", styles['FrontMatterTitle']))
    story.append(Spacer(1, 6))
    
    toc_data_p1 = [
        [Paragraph("<b>Chapter No.</b>", styles['TableHeader']), Paragraph("<b>Title</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>Certificate</b>", styles['TableCell']), Paragraph("ii", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>Declaration</b>", styles['TableCell']), Paragraph("iii", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>Acknowledgement</b>", styles['TableCell']), Paragraph("iv", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>List of Figures</b>", styles['TableCell']), Paragraph("vii", styles['TableCellCenter'])],
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>List of Tables</b>", styles['TableCell']), Paragraph("viii", styles['TableCellCenter'])],
        
        [Paragraph("<b>1</b>", styles['TableCellCenter']), Paragraph("<b>INTRODUCTION</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH1', 1)}</b>", styles['TableCellCenter'])],
        [Paragraph("1.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Overview", styles['TableCell']), Paragraph(get_page_str('S1_1', 1), styles['TableCellCenter'])],
        [Paragraph("1.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Objectives", styles['TableCell']), Paragraph(get_page_str('S1_2', 2), styles['TableCellCenter'])],
        [Paragraph("1.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Scope of the Project", styles['TableCell']), Paragraph(get_page_str('S1_3', 2), styles['TableCellCenter'])],
        [Paragraph("1.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Applications", styles['TableCell']), Paragraph(get_page_str('S1_4', 3), styles['TableCellCenter'])],
        [Paragraph("1.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Organization of Report", styles['TableCell']), Paragraph(get_page_str('S1_5', 3), styles['TableCellCenter'])],
        [Paragraph("1.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S1_6', 4), styles['TableCellCenter'])],
        
        [Paragraph("<b>2</b>", styles['TableCellCenter']), Paragraph("<b>PROBLEM IDENTIFICATION</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH2', 5)}</b>", styles['TableCellCenter'])],
        [Paragraph("2.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Problem Overview", styles['TableCell']), Paragraph(get_page_str('S2_1', 5), styles['TableCellCenter'])],
        [Paragraph("2.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Existing System", styles['TableCell']), Paragraph(get_page_str('S2_2', 6), styles['TableCellCenter'])],
        [Paragraph("2.2.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Drawbacks of Existing System", styles['TableCell']), Paragraph(get_page_str('S2_2_1', 6), styles['TableCellCenter'])],
        [Paragraph("2.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Proposed System", styles['TableCell']), Paragraph(get_page_str('S2_3', 7), styles['TableCellCenter'])],
        [Paragraph("2.3.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;Advantages of Proposed System", styles['TableCell']), Paragraph(get_page_str('S2_3_1', 7), styles['TableCellCenter'])],
        [Paragraph("2.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S2_4', 8), styles['TableCellCenter'])],
        
        [Paragraph("<b>3</b>", styles['TableCellCenter']), Paragraph("<b>LITERATURE REVIEW</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH3', 9)}</b>", styles['TableCellCenter'])],
        [Paragraph("3.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Introduction", styles['TableCell']), Paragraph(get_page_str('S3_1', 9), styles['TableCellCenter'])],
        [Paragraph("3.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Review of Existing Research (20 Papers from Presentation)", styles['TableCell']), Paragraph(get_page_str('S3_2', 9), styles['TableCellCenter'])],
        [Paragraph("3.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Comparative Taxonomy of Attack Indicators", styles['TableCell']), Paragraph(get_page_str('S3_3', 20), styles['TableCellCenter'])],
        [Paragraph("3.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Research Gap", styles['TableCell']), Paragraph(get_page_str('S3_4', 23), styles['TableCellCenter'])],
        [Paragraph("3.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S3_5', 24), styles['TableCellCenter'])],
        
        [Paragraph("<b>4</b>", styles['TableCellCenter']), Paragraph("<b>SYSTEM REQUIREMENTS</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH4', 25)}</b>", styles['TableCellCenter'])],
        [Paragraph("4.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;System Overview", styles['TableCell']), Paragraph(get_page_str('S4_1', 25), styles['TableCellCenter'])],
        [Paragraph("4.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Functional Requirements", styles['TableCell']), Paragraph(get_page_str('S4_2', 25), styles['TableCellCenter'])],
        [Paragraph("4.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Non-Functional Requirements", styles['TableCell']), Paragraph(get_page_str('S4_3', 27), styles['TableCellCenter'])],
        [Paragraph("4.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Hardware Requirements", styles['TableCell']), Paragraph(get_page_str('S4_4', 28), styles['TableCellCenter'])],
        [Paragraph("4.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Software Requirements", styles['TableCell']), Paragraph(get_page_str('S4_5', 29), styles['TableCellCenter'])],
        [Paragraph("4.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S4_6', 29), styles['TableCellCenter'])],
    ]
    t_toc_p1 = Table(toc_data_p1, colWidths=[70, 303, 60])
    t_toc_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
        ('TOPPADDING', (0,0), (-1,-1), 2.0),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ]))
    story.append(t_toc_p1)
    story.append(PageBreak())

    # TOC Page 2
    story.append(Spacer(1, 8))
    story.append(Paragraph("TABLE OF CONTENTS (Continued)", styles['FrontMatterTitle']))
    story.append(Spacer(1, 4))
    
    toc_data_p2 = [
        [Paragraph("<b>Chapter No.</b>", styles['TableHeader']), Paragraph("<b>Title</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("<b>5</b>", styles['TableCellCenter']), Paragraph("<b>SYSTEM DESIGN</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH5', 30)}</b>", styles['TableCellCenter'])],
        [Paragraph("5.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;System Design Overview", styles['TableCell']), Paragraph(get_page_str('S5_1', 30), styles['TableCellCenter'])],
        [Paragraph("5.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;System Architecture", styles['TableCell']), Paragraph(get_page_str('S5_2', 30), styles['TableCellCenter'])],
        [Paragraph("5.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;System Modules (6 Core Modules)", styles['TableCell']), Paragraph(get_page_str('S5_3', 31), styles['TableCellCenter'])],
        [Paragraph("5.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;UML Diagrams (Use Case, Sequence, Class, Activity)", styles['TableCell']), Paragraph(get_page_str('S5_4', 32), styles['TableCellCenter'])],
        [Paragraph("5.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Data Flow Diagrams (Level 0, Level 1)", styles['TableCell']), Paragraph(get_page_str('S5_5', 35), styles['TableCellCenter'])],
        [Paragraph("5.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Database Design & Entity Relationship", styles['TableCell']), Paragraph(get_page_str('S5_6', 36), styles['TableCellCenter'])],
        [Paragraph("5.7", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Flowchart of Threat Analysis", styles['TableCell']), Paragraph(get_page_str('S5_7', 37), styles['TableCellCenter'])],
        [Paragraph("5.8", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S5_8', 38), styles['TableCellCenter'])],
        
        [Paragraph("<b>6</b>", styles['TableCellCenter']), Paragraph("<b>SYSTEM IMPLEMENTATION</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH6', 39)}</b>", styles['TableCellCenter'])],
        [Paragraph("6.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Implementation Environment", styles['TableCell']), Paragraph(get_page_str('S6_1', 39), styles['TableCellCenter'])],
        [Paragraph("6.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Project Directory Structure", styles['TableCell']), Paragraph(get_page_str('S6_2', 39), styles['TableCellCenter'])],
        [Paragraph("6.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Core Backend Modules & File Walkthrough", styles['TableCell']), Paragraph(get_page_str('S6_3', 40), styles['TableCellCenter'])],
        [Paragraph("6.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Machine Learning Classification Formulations", styles['TableCell']), Paragraph(get_page_str('S6_4', 42), styles['TableCellCenter'])],
        [Paragraph("6.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Frontend HUD Implementation", styles['TableCell']), Paragraph(get_page_str('S6_5', 44), styles['TableCellCenter'])],
        [Paragraph("6.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Core Algorithmic Pseudocode", styles['TableCell']), Paragraph(get_page_str('S6_6', 45), styles['TableCellCenter'])],
        [Paragraph("6.7", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S6_7', 46), styles['TableCellCenter'])],
        
        [Paragraph("<b>7</b>", styles['TableCellCenter']), Paragraph("<b>SYSTEM TESTING</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH7', 47)}</b>", styles['TableCellCenter'])],
        [Paragraph("7.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Testing Methodology", styles['TableCell']), Paragraph(get_page_str('S7_1', 47), styles['TableCellCenter'])],
        [Paragraph("7.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Verification and Validation", styles['TableCell']), Paragraph(get_page_str('S7_2', 47), styles['TableCellCenter'])],
        [Paragraph("7.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Comprehensive Test Cases Suite (20 Test Cases)", styles['TableCell']), Paragraph(get_page_str('S7_3', 48), styles['TableCellCenter'])],
        [Paragraph("7.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Traceability Matrix", styles['TableCell']), Paragraph(get_page_str('S7_4', 50), styles['TableCellCenter'])],
        [Paragraph("7.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S7_5', 50), styles['TableCellCenter'])],
        
        [Paragraph("<b>8</b>", styles['TableCellCenter']), Paragraph("<b>RESULTS AND DISCUSSION</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH8', 51)}</b>", styles['TableCellCenter'])],
        [Paragraph("8.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;User Interface and Telemetry HUD", styles['TableCell']), Paragraph(get_page_str('S8_1', 51), styles['TableCellCenter'])],
        [Paragraph("8.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Model Performance Benchmarks", styles['TableCell']), Paragraph(get_page_str('S8_2', 51), styles['TableCellCenter'])],
        [Paragraph("8.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Inference Speed and Resource Profiling", styles['TableCell']), Paragraph(get_page_str('S8_3', 52), styles['TableCellCenter'])],
        [Paragraph("8.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;ROC Curves and Confusion Matrix Analysis", styles['TableCell']), Paragraph(get_page_str('S8_4', 53), styles['TableCellCenter'])],
        [Paragraph("8.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Feature Importance and Discriminative Power", styles['TableCell']), Paragraph(get_page_str('S8_5', 54), styles['TableCellCenter'])],
        [Paragraph("8.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Comparative Analysis with Existing Solutions", styles['TableCell']), Paragraph(get_page_str('S8_6', 54), styles['TableCellCenter'])],
        [Paragraph("8.7", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S8_7', 54), styles['TableCellCenter'])],
        
        [Paragraph("<b>9</b>", styles['TableCellCenter']), Paragraph("<b>CONCLUSION AND FUTURE SCOPE</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH9', 55)}</b>", styles['TableCellCenter'])],
        [Paragraph("9.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Conclusion", styles['TableCell']), Paragraph(get_page_str('S9_1', 55), styles['TableCellCenter'])],
        [Paragraph("9.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Core Contributions", styles['TableCell']), Paragraph(get_page_str('S9_2', 55), styles['TableCellCenter'])],
        [Paragraph("9.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Limitations Encountered", styles['TableCell']), Paragraph(get_page_str('S9_3', 56), styles['TableCellCenter'])],
        [Paragraph("9.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Future Scope", styles['TableCell']), Paragraph(get_page_str('S9_4', 56), styles['TableCellCenter'])],
        [Paragraph("9.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S9_5', 56), styles['TableCellCenter'])],
        
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>REFERENCES</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('REFS', 57)}</b>", styles['TableCellCenter'])],
    ]
    t_toc_p2 = Table(toc_data_p2, colWidths=[70, 303, 60])
    t_toc_p2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.0),
        ('TOPPADDING', (0,0), (-1,-1), 2.0),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ]))
    story.append(t_toc_p2)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: LIST OF FIGURES
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("LIST OF FIGURES", styles['FrontMatterTitle']))
    story.append(Spacer(1, 8))
    
    figures_data = [
        [Paragraph("<b>Figure No.</b>", styles['TableHeader']), Paragraph("<b>Figure Name</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("Figure 5.1", styles['TableCellCenter']), Paragraph("CyberGuard High-Level Modular System Architecture", styles['TableCell']), Paragraph(get_page_str('FIG_5_1', 30), styles['TableCellCenter'])],
        [Paragraph("Figure 5.2", styles['TableCellCenter']), Paragraph("Use Case Diagram of Multi-Role Threat Analysis", styles['TableCell']), Paragraph(get_page_str('FIG_5_2', 32), styles['TableCellCenter'])],
        [Paragraph("Figure 5.3", styles['TableCellCenter']), Paragraph("Sequence Diagram of Live Threat Inspection Lifecycle", styles['TableCell']), Paragraph(get_page_str('FIG_5_3', 33), styles['TableCellCenter'])],
        [Paragraph("Figure 5.4", styles['TableCellCenter']), Paragraph("UML Class Hierarchy of Model Zoo and Feature Engines", styles['TableCell']), Paragraph(get_page_str('FIG_5_4', 34), styles['TableCellCenter'])],
        [Paragraph("Figure 5.5", styles['TableCellCenter']), Paragraph("Data Flow Diagram (Level 0 - Context Diagram)", styles['TableCell']), Paragraph(get_page_str('FIG_5_5', 35), styles['TableCellCenter'])],
        [Paragraph("Figure 5.6", styles['TableCellCenter']), Paragraph("Data Flow Diagram (Level 1 - Detailed Threat Pipeline)", styles['TableCell']), Paragraph(get_page_str('FIG_5_6', 35), styles['TableCellCenter'])],
        [Paragraph("Figure 5.7", styles['TableCellCenter']), Paragraph("Entity Relationship Diagram of Dual-Persistence Schema", styles['TableCell']), Paragraph(get_page_str('FIG_5_7', 36), styles['TableCellCenter'])],
        [Paragraph("Figure 5.8", styles['TableCellCenter']), Paragraph("UML Activity Diagram of Threat Inspection Workflow", styles['TableCell']), Paragraph(get_page_str('FIG_5_8', 37), styles['TableCellCenter'])],
        [Paragraph("Figure 5.9", styles['TableCellCenter']), Paragraph("System Flowchart of Threat Decision Pipeline", styles['TableCell']), Paragraph(get_page_str('FIG_5_9', 37), styles['TableCellCenter'])],
        [Paragraph("Figure 8.1", styles['TableCellCenter']), Paragraph("Comparative Machine Learning Model Accuracy & F1-Score", styles['TableCell']), Paragraph(get_page_str('FIG_8_1', 51), styles['TableCellCenter'])],
        [Paragraph("Figure 8.2", styles['TableCellCenter']), Paragraph("Inference Latency Benchmark Across Evaluated Models", styles['TableCell']), Paragraph(get_page_str('FIG_8_2', 52), styles['TableCellCenter'])],
        [Paragraph("Figure 8.3", styles['TableCellCenter']), Paragraph("Receiver Operating Characteristic (ROC) Benchmark Curves", styles['TableCell']), Paragraph(get_page_str('FIG_8_3', 53), styles['TableCellCenter'])],
        [Paragraph("Figure 8.4", styles['TableCellCenter']), Paragraph("Confusion Matrix of Optimized Random Forest Ensemble", styles['TableCell']), Paragraph(get_page_str('FIG_8_4', 53), styles['TableCellCenter'])],
        [Paragraph("Figure 8.5", styles['TableCellCenter']), Paragraph("Cyberpunk HUD Dashboard Telemetry and Live Threat Gauge", styles['TableCell']), Paragraph(get_page_str('FIG_8_5', 54), styles['TableCellCenter'])],
    ]
    t_lof = Table(figures_data, colWidths=[70, 303, 60])
    t_lof.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_lof)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: LIST OF TABLES
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("LIST OF TABLES", styles['FrontMatterTitle']))
    story.append(Spacer(1, 8))
    
    tables_data = [
        [Paragraph("<b>Table No.</b>", styles['TableHeader']), Paragraph("<b>Table Name</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("Table 3.1", styles['TableCellCenter']), Paragraph("Summary of 20 Reviewed Literature Papers from Presentation", styles['TableCell']), Paragraph(get_page_str('TAB_3_1', 20), styles['TableCellCenter'])],
        [Paragraph("Table 3.2", styles['TableCellCenter']), Paragraph("Public Dataset Comparison for URL and APK Malware Research", styles['TableCell']), Paragraph(get_page_str('TAB_3_2', 22), styles['TableCellCenter'])],
        [Paragraph("Table 4.1", styles['TableCellCenter']), Paragraph("Minimum & Recommended Hardware Specifications", styles['TableCell']), Paragraph(get_page_str('TAB_4_1', 28), styles['TableCellCenter'])],
        [Paragraph("Table 4.2", styles['TableCellCenter']), Paragraph("Software Specifications and Development Stack", styles['TableCell']), Paragraph(get_page_str('TAB_4_2', 29), styles['TableCellCenter'])],
        [Paragraph("Table 5.1", styles['TableCellCenter']), Paragraph("Core Functional Modules of the CyberGuard Platform", styles['TableCell']), Paragraph(get_page_str('TAB_5_1', 31), styles['TableCellCenter'])],
        [Paragraph("Table 5.2", styles['TableCellCenter']), Paragraph("Dual-Persistence Database Relational / Document Schema", styles['TableCell']), Paragraph(get_page_str('TAB_5_2', 36), styles['TableCellCenter'])],
        [Paragraph("Table 7.1", styles['TableCellCenter']), Paragraph("Comprehensive Verification & Validation Test Suite (20 Test Cases)", styles['TableCell']), Paragraph(get_page_str('TAB_7_1', 48), styles['TableCellCenter'])],
        [Paragraph("Table 7.2", styles['TableCellCenter']), Paragraph("Traceability Matrix: Requirements to Verification Test Cases", styles['TableCell']), Paragraph(get_page_str('TAB_7_2', 50), styles['TableCellCenter'])],
        [Paragraph("Table 8.1", styles['TableCellCenter']), Paragraph("Model Performance Metrics on Phishing URL & APK Datasets", styles['TableCell']), Paragraph(get_page_str('TAB_8_1', 51), styles['TableCellCenter'])],
        [Paragraph("Table 8.2", styles['TableCellCenter']), Paragraph("Inference Latency and Resource Utilization Profile", styles['TableCell']), Paragraph(get_page_str('TAB_8_2', 52), styles['TableCellCenter'])],
        [Paragraph("Table 8.3", styles['TableCellCenter']), Paragraph("Top 10 Most Informative Features Derived via Gini Impurity", styles['TableCell']), Paragraph(get_page_str('TAB_8_3', 54), styles['TableCellCenter'])],
        [Paragraph("Table 8.4", styles['TableCellCenter']), Paragraph("Comparison of CyberGuard with Industry Solutions (VirusTotal, Hybrid)", styles['TableCell']), Paragraph(get_page_str('TAB_8_4', 54), styles['TableCellCenter'])],
    ]
    t_lot = Table(tables_data, colWidths=[70, 303, 60])
    t_lot.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_lot)
    story.append(PageBreak())

    return story
