import os
import sys

# We will write the full Python script that defines the story generator and compiles it directly.
print("Writing compile_complete_report.py...")

def generate_report_story(styles):
    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 4))
    
    # Official Logos Header Table
    logo_data = [
        [
            Image('report_assets/vtu_logo.jpeg', width=54, height=54),
            Paragraph(
                "<b>PKM EDUCATIONAL TRUST &reg;</b><br/>"
                "<font size='12' color='#881337'><b>R. R. INSTITUTE OF TECHNOLOGY</b></font><br/>"
                "<font size='8' color='#334155'><b>(An Autonomous Institution under VTU Belgaum)</b><br/>"
                "Approved by AICTE, New Delhi, Recognised by Govt. of Karnataka<br/>"
                "Accredited by NAAC with A+, NBA<br/>"
                "Raja Reddy Layout, Chikkabanavara, Bengaluru – 560 090</font>",
                styles['CoverCollegeHeader']
            ),
            Image('report_assets/rrit_logo.png', width=54, height=64)
        ]
    ]
    t_logo = Table(logo_data, colWidths=[65, 303, 65])
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
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#881337'), spaceAfter=10))
    
    story.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</b>", styles['CoverCollegeHeader']))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("<b>MAJOR PROJECT WORK RECORD (PHASE 1 & 2)</b>", ParagraphStyle('Rec', fontName='Times-Bold', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#475569'))))
    story.append(Paragraph("<b>BATCH NO: G-05 &nbsp;&nbsp;|&nbsp;&nbsp; ACADEMIC YEAR: 2025 – 2026</b>", ParagraphStyle('Rec2', fontName='Times-Bold', fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#1E293B'))))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("A PROJECT REPORT ON", ParagraphStyle('Sub', fontName='Times-Bold', fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor('#475569'))))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>CYBER THREAT DETECTION USING MACHINE LEARNING</b>", styles['ProjectCoverMainTitle']))
    story.append(Paragraph("<b>(Phishing URL & Android APK Malware Detection Platform)</b>", ParagraphStyle('Subtheme', fontName='Times-BoldItalic', fontSize=12, leading=16, alignment=TA_CENTER, textColor=colors.HexColor('#1E3A8A'))))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<i>Submitted in partial fulfillment of the requirements for the award of degree of</i>", ParagraphStyle('Sub2', fontName='Times-Italic', fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#334155'))))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>BACHELOR OF ENGINEERING IN COMPUTER SCIENCE AND ENGINEERING</b>", ParagraphStyle('Deg', fontName='Times-Bold', fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor('#0F172A'))))
    story.append(Spacer(1, 12))

    # Team Members Table
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
    story.append(Spacer(1, 14))
    
    story.append(Paragraph("<b>DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING</b>", ParagraphStyle('Dpt', fontName='Times-Bold', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.HexColor('#881337'))))
    story.append(Paragraph("<b>R. R. INSTITUTE OF TECHNOLOGY, BENGALURU – 560090</b>", ParagraphStyle('Yr', fontName='Times-Bold', fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#0F172A'))))
    story.append(Paragraph("<b>2025 – 2026</b>", ParagraphStyle('Yr2', fontName='Times-Bold', fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#0F172A'))))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE
    # =========================================================================
    story.append(Spacer(1, 6))
    
    cert_logo_data = [
        [
            Image('report_assets/vtu_logo.jpeg', width=45, height=45),
            Paragraph(
                "<b>R. R. INSTITUTE OF TECHNOLOGY</b><br/>"
                "<font size='8' color='#334155'><b>(An Autonomous Institution under VTU Belgaum)</b><br/>"
                "Raja Reddy Layout, Chikkabanavara, Bengaluru – 560 090<br/>"
                "<b>DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING</b></font>",
                styles['CoverCollegeHeader']
            ),
            Image('report_assets/rrit_logo.png', width=45, height=52)
        ]
    ]
    t_clogo = Table(cert_logo_data, colWidths=[55, 323, 55])
    t_clogo.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,0), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_clogo)
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#1E293B'), spaceAfter=10))
    story.append(Paragraph("CERTIFICATE", styles['FrontMatterTitle']))
    story.append(Spacer(1, 6))
    
    cert_text = (
        "This is to certify that the Project Work Phase-2 entitled <b>"CYBER THREAT DETECTION USING MACHINE LEARNING "
        "(Phishing URL & Android APK Malware Detection Platform)"</b> is a bonafide work carried out by "
        "<b>AMAN YADAV (1RI23CS007)</b>, <b>ASHRAF SAMI (1RI23CS013)</b>, <b>ASHUTOSH DAYAL CHOUDHARY (1RI23CS014)</b>, "
        "and <b>DUSHYANTH R (1RI23CS046)</b>, students of Sixth Semester Bachelor of Engineering in Computer Science & Engineering "
        "of <b>R. R. Institute of Technology</b>, in partial fulfillment for the award of Bachelor of Engineering in "
        "Computer Science and Engineering of <b>Visvesvaraya Technological University, Belagavi</b> during the academic year "
        "2025–2026. It is certified that all corrections and suggestions indicated during internal evaluations have been "
        "incorporated in the report deposited in the departmental library. The project report has been approved as it satisfies "
        "the academic requirements prescribed by VTU for Project Work."
    )
    story.append(Paragraph(cert_text, styles['BodyContent']))
    story.append(Spacer(1, 25))
    
    sig_data = [
        [
            Paragraph("<b>Prof. ASHA V</b><br/>Project Guide<br/>Assistant Professor<br/>Dept. of CSE, RRIT", styles['TableCellCenter']),
            Paragraph("<b>Dr. SWETHA G</b><br/>Project Coordinator<br/>Dept. of CSE, RRIT", styles['TableCellCenter']),
            Paragraph("<b>Dr. MANJUNATH R</b><br/>Professor & HOD<br/>Dept. of CSE, RRIT", styles['TableCellCenter']),
            Paragraph("<b>PRINCIPAL</b><br/>R. R. Institute of Technology<br/>Bengaluru", styles['TableCellCenter'])
        ]
    ]
    t_sig = Table(sig_data, colWidths=[108, 108, 108, 109])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sig)
    story.append(Spacer(1, 20))
    
    viva_data = [
        [Paragraph("<b>Name of the External Viva Examiners:</b>", styles['TableCell']), Paragraph("<b>Signature with Date:</b>", styles['TableCellCenter'])],
        [Paragraph("1. ____________________________________________", styles['TableCell']), Paragraph("1. ________________________", styles['TableCellCenter'])],
        [Paragraph("2. ____________________________________________", styles['TableCell']), Paragraph("2. ________________________", styles['TableCellCenter'])],
    ]
    t_viva = Table(viva_data, colWidths=[260, 173])
    t_viva.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_viva)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: DECLARATION
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("DECLARATION", styles['FrontMatterTitle']))
    story.append(Spacer(1, 14))
    
    decl_text = (
        "We, the students of Sixth Semester Bachelor of Engineering in Computer Science & Engineering, "
        "R. R. Institute of Technology, Bengaluru, hereby declare that the project work entitled <b>"CYBER THREAT "
        "DETECTION USING MACHINE LEARNING (Phishing URL & Android APK Malware Detection Platform)"</b> has been "
        "independently carried out by our project team under the guidance of <b>Prof. Asha V</b>, Assistant Professor, "
        "Department of Computer Science & Engineering, and the mentorship of <b>Dr. Manjunath R</b>, Professor & HOD, "
        "in partial fulfillment of the academic requirements for the award of the degree of <b>Bachelor of Engineering "
        "in Computer Science and Engineering</b> by <b>Visvesvaraya Technological University (VTU), Belagavi</b> during the "
        "academic year 2025–2026.<br/><br/>"
        "We further declare that the work embodied in this project report has been undertaken with academic integrity and "
        "has not been submitted previously to this or any other university or institution for the award of any degree, "
        "diploma, or fellowship."
    )
    story.append(Paragraph(decl_text, styles['BodyContent']))
    story.append(Spacer(1, 25))
    
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
    story.append(Spacer(1, 20))
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
        "and our respected <b>Principal</b>, R. R. Institute of Technology, for providing the necessary infrastructure, high-speed "
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
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Project Team — Batch G-05</b><br/>Aman Yadav (1RI23CS007)<br/>Ashraf Sami (1RI23CS013)<br/>Ashutosh Dayal Choudhary (1RI23CS014)<br/>Dushyanth R (1RI23CS046)", ParagraphStyle('Rt', fontName='Times-Bold', fontSize=10, leading=14, alignment=TA_RIGHT, textColor=colors.HexColor('#0F172A'))))
    story.append(PageBreak())
