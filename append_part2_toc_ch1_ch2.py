# append_part2_toc_ch1_ch2.py

with open("compile_complete_report.py", "a", encoding="utf-8") as f:
    f.write('''
    # =========================================================================
    # PAGES 5 & 6: TABLE OF CONTENTS (2 Pages)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("TABLE OF CONTENTS", styles['FrontMatterTitle']))
    story.append(Spacer(1, 6))
    
    toc_data = [
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
        [Paragraph("6.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Overview", styles['TableCell']), Paragraph(get_page_str('S6_1', 39), styles['TableCellCenter'])],
        [Paragraph("6.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Implementation Environment", styles['TableCell']), Paragraph(get_page_str('S6_2', 39), styles['TableCellCenter'])],
        [Paragraph("6.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Module-wise Implementation", styles['TableCell']), Paragraph(get_page_str('S6_3', 40), styles['TableCellCenter'])],
        [Paragraph("6.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Algorithm / Methodology & Formulations", styles['TableCell']), Paragraph(get_page_str('S6_4', 44), styles['TableCellCenter'])],
        [Paragraph("6.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Pseudocode Algorithms", styles['TableCell']), Paragraph(get_page_str('S6_5', 47), styles['TableCellCenter'])],
        [Paragraph("6.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Key Implementation Code Snippets", styles['TableCell']), Paragraph(get_page_str('S6_6', 49), styles['TableCellCenter'])],
        [Paragraph("6.7", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S6_7', 50), styles['TableCellCenter'])],
        
        [Paragraph("<b>7</b>", styles['TableCellCenter']), Paragraph("<b>SYSTEM TESTING</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH7', 51)}</b>", styles['TableCellCenter'])],
        [Paragraph("7.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Overview & V&V Strategy", styles['TableCell']), Paragraph(get_page_str('S7_1', 51), styles['TableCellCenter'])],
        [Paragraph("7.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Types of Testing (6 Categories)", styles['TableCell']), Paragraph(get_page_str('S7_2', 51), styles['TableCellCenter'])],
        [Paragraph("7.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Test Cases (20 Comprehensive Scenarios)", styles['TableCell']), Paragraph(get_page_str('S7_3', 53), styles['TableCellCenter'])],
        [Paragraph("7.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S7_4', 58), styles['TableCellCenter'])],
        
        [Paragraph("<b>8</b>", styles['TableCellCenter']), Paragraph("<b>RESULTS AND DISCUSSION</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH8', 59)}</b>", styles['TableCellCenter'])],
        [Paragraph("8.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Overview", styles['TableCell']), Paragraph(get_page_str('S8_1', 59), styles['TableCellCenter'])],
        [Paragraph("8.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Results Screen Shots and discussion", styles['TableCell']), Paragraph(get_page_str('S8_2', 59), styles['TableCellCenter'])],
        [Paragraph("8.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Experimental Results & Benchmarks", styles['TableCell']), Paragraph(get_page_str('S8_3', 60), styles['TableCellCenter'])],
        [Paragraph("8.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Comparison with Existing System", styles['TableCell']), Paragraph(get_page_str('S8_4', 63), styles['TableCellCenter'])],
        [Paragraph("8.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Discussion & Observations", styles['TableCell']), Paragraph(get_page_str('S8_5', 64), styles['TableCellCenter'])],
        [Paragraph("8.6", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S8_6', 64), styles['TableCellCenter'])],
        
        [Paragraph("<b>9</b>", styles['TableCellCenter']), Paragraph("<b>CONCLUSION AND FUTURE SCOPE</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('CH9', 65)}</b>", styles['TableCellCenter'])],
        [Paragraph("9.1", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Conclusion", styles['TableCell']), Paragraph(get_page_str('S9_1', 65), styles['TableCellCenter'])],
        [Paragraph("9.2", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Contributions of the Project", styles['TableCell']), Paragraph(get_page_str('S9_2', 65), styles['TableCellCenter'])],
        [Paragraph("9.3", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Limitations", styles['TableCell']), Paragraph(get_page_str('S9_3', 66), styles['TableCellCenter'])],
        [Paragraph("9.4", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Future Scope", styles['TableCell']), Paragraph(get_page_str('S9_4', 66), styles['TableCellCenter'])],
        [Paragraph("9.5", styles['TableCellCenter']), Paragraph("&nbsp;&nbsp;Summary", styles['TableCell']), Paragraph(get_page_str('S9_5', 67), styles['TableCellCenter'])],
        
        [Paragraph("", styles['TableCellCenter']), Paragraph("<b>REFERENCES</b>", styles['TableCell']), Paragraph(f"<b>{get_page_str('REFS', 68)}</b>", styles['TableCellCenter'])],
    ]
    
    t_toc = Table(toc_data, colWidths=[70, 305, 55])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_toc)
    story.append(PageBreak())

    # Page 7: List of Figures
    story.append(Spacer(1, 15))
    story.append(Paragraph("LIST OF FIGURES", styles['FrontMatterTitle']))
    story.append(Spacer(1, 12))
    
    lof_data = [
        [Paragraph("<b>Figure No.</b>", styles['TableHeader']), Paragraph("<b>Figure Title</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("Figure 5.1", styles['TableCellCenter']), Paragraph("CyberGuard End-to-End System Architecture", styles['TableCell']), Paragraph(get_page_str('FIG_5_1', 30), styles['TableCellCenter'])],
        [Paragraph("Figure 5.2", styles['TableCellCenter']), Paragraph("UML Use Case Diagram for Security Analyst Workflows", styles['TableCell']), Paragraph(get_page_str('FIG_5_2', 32), styles['TableCellCenter'])],
        [Paragraph("Figure 5.3", styles['TableCellCenter']), Paragraph("UML Sequence Diagram for Threat Analysis Lifecycle", styles['TableCell']), Paragraph(get_page_str('FIG_5_3', 33), styles['TableCellCenter'])],
        [Paragraph("Figure 5.4", styles['TableCellCenter']), Paragraph("UML Class Diagram of Backend Subsystems and Managers", styles['TableCell']), Paragraph(get_page_str('FIG_5_4', 34), styles['TableCellCenter'])],
        [Paragraph("Figure 5.5", styles['TableCellCenter']), Paragraph("Data Flow Diagram (DFD Level 0 - Context Diagram)", styles['TableCell']), Paragraph(get_page_str('FIG_5_5', 35), styles['TableCellCenter'])],
        [Paragraph("Figure 5.6", styles['TableCellCenter']), Paragraph("Data Flow Diagram (DFD Level 1) for Threat Processing", styles['TableCell']), Paragraph(get_page_str('FIG_5_6', 35), styles['TableCellCenter'])],
        [Paragraph("Figure 5.7", styles['TableCellCenter']), Paragraph("Entity-Relationship (ER) Diagram for Persistence Layer", styles['TableCell']), Paragraph(get_page_str('FIG_5_7', 36), styles['TableCellCenter'])],
        [Paragraph("Figure 5.8", styles['TableCellCenter']), Paragraph("UML Activity Diagram for Threat Evaluation Workflow", styles['TableCell']), Paragraph(get_page_str('FIG_5_8', 37), styles['TableCellCenter'])],
        [Paragraph("Figure 5.9", styles['TableCellCenter']), Paragraph("Overall System Threat Scanning and Classification Flowchart", styles['TableCell']), Paragraph(get_page_str('FIG_5_9', 38), styles['TableCellCenter'])],
        [Paragraph("Figure 8.1", styles['TableCellCenter']), Paragraph("Classifier Performance Benchmarks Across Evaluation Metrics", styles['TableCell']), Paragraph(get_page_str('FIG_8_1', 60), styles['TableCellCenter'])],
        [Paragraph("Figure 8.2", styles['TableCellCenter']), Paragraph("Inference Latency Benchmark across Machine Learning Models", styles['TableCell']), Paragraph(get_page_str('FIG_8_2', 61), styles['TableCellCenter'])],
        [Paragraph("Figure 8.3", styles['TableCellCenter']), Paragraph("Receiver Operating Characteristic (ROC) Curves", styles['TableCell']), Paragraph(get_page_str('FIG_8_3', 61), styles['TableCellCenter'])],
        [Paragraph("Figure 8.4", styles['TableCellCenter']), Paragraph("Random Forest Confusion Matrix Heatmap (N=1500)", styles['TableCell']), Paragraph(get_page_str('FIG_8_4', 62), styles['TableCellCenter'])],
        [Paragraph("Figure 8.5", styles['TableCellCenter']), Paragraph("CyberGuard Futuristic Cyberpunk Telemetry HUD Dashboard", styles['TableCell']), Paragraph(get_page_str('FIG_8_5', 59), styles['TableCellCenter'])],
    ]
    t_lof = Table(lof_data, colWidths=[80, 295, 55])
    t_lof.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_lof)
    story.append(PageBreak())

    # Page 8: List of Tables
    story.append(Spacer(1, 15))
    story.append(Paragraph("LIST OF TABLES", styles['FrontMatterTitle']))
    story.append(Spacer(1, 12))
    
    lot_data = [
        [Paragraph("<b>Table No.</b>", styles['TableHeader']), Paragraph("<b>Table Title</b>", styles['TableHeader']), Paragraph("<b>Page No.</b>", styles['TableHeader'])],
        [Paragraph("Table 3.1", styles['TableCellCenter']), Paragraph("Summary of Literature Review Papers (20 Research Studies from Presentation)", styles['TableCell']), Paragraph(get_page_str('TAB_3_1', 19), styles['TableCellCenter'])],
        [Paragraph("Table 3.2", styles['TableCellCenter']), Paragraph("Comparative Evaluation of Cybersecurity Threat Datasets", styles['TableCell']), Paragraph(get_page_str('TAB_3_2', 21), styles['TableCellCenter'])],
        [Paragraph("Table 4.1", styles['TableCellCenter']), Paragraph("Hardware Requirements Specification (Laboratory Benchmarks)", styles['TableCell']), Paragraph(get_page_str('TAB_4_1', 28), styles['TableCellCenter'])],
        [Paragraph("Table 4.2", styles['TableCellCenter']), Paragraph("Software Requirements & Dependency Matrix", styles['TableCell']), Paragraph(get_page_str('TAB_4_2', 29), styles['TableCellCenter'])],
        [Paragraph("Table 5.1", styles['TableCellCenter']), Paragraph("Relational Schema Definition for 'users' Table", styles['TableCell']), Paragraph(get_page_str('TAB_5_1', 36), styles['TableCellCenter'])],
        [Paragraph("Table 5.2", styles['TableCellCenter']), Paragraph("Relational Schema Definition for 'scans' Table", styles['TableCell']), Paragraph(get_page_str('TAB_5_2', 37), styles['TableCellCenter'])],
        [Paragraph("Table 6.1", styles['TableCellCenter']), Paragraph("Lexical URL Feature Extraction Vector Specification", styles['TableCell']), Paragraph(get_page_str('TAB_6_1', 41), styles['TableCellCenter'])],
        [Paragraph("Table 6.2", styles['TableCellCenter']), Paragraph("Android APK Static Manifest Feature Vector Specification", styles['TableCell']), Paragraph(get_page_str('TAB_6_2', 42), styles['TableCellCenter'])],
        [Paragraph("Table 6.3", styles['TableCellCenter']), Paragraph("Hyperparameter Configurations for Machine Learning Zoo", styles['TableCell']), Paragraph(get_page_str('TAB_6_3', 45), styles['TableCellCenter'])],
        [Paragraph("Table 7.1", styles['TableCellCenter']), Paragraph("Comprehensive System Verification & Validation Test Cases (20 Cases)", styles['TableCell']), Paragraph(get_page_str('TAB_7_1', 53), styles['TableCellCenter'])],
        [Paragraph("Table 8.1", styles['TableCellCenter']), Paragraph("Classifier Performance Benchmarks Across 6 Machine Learning Models", styles['TableCell']), Paragraph(get_page_str('TAB_8_1', 60), styles['TableCellCenter'])],
        [Paragraph("Table 8.2", styles['TableCellCenter']), Paragraph("System Runtime Latency and Resource Utilization Metrics", styles['TableCell']), Paragraph(get_page_str('TAB_8_2', 62), styles['TableCellCenter'])],
        [Paragraph("Table 8.3", styles['TableCellCenter']), Paragraph("Feature Importance Weightings Derived from Random Forest Model", styles['TableCell']), Paragraph(get_page_str('TAB_8_3', 63), styles['TableCellCenter'])],
        [Paragraph("Table 8.4", styles['TableCellCenter']), Paragraph("Technical Comparison Matrix: CyberGuard vs Existing Systems", styles['TableCell']), Paragraph(get_page_str('TAB_8_4', 63), styles['TableCellCenter'])],
    ]
    t_lot = Table(lot_data, colWidths=[80, 295, 55])
    t_lot.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_lot)
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 1: INTRODUCTION (Doc Page 9 -> Page 1)
    # =========================================================================
    story.append(PageMarker('CH1'))
    story.append(Paragraph("CHAPTER 1", styles['ChapterTitle']))
    story.append(Paragraph("INTRODUCTION", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))
    
    story.append(PageMarker('S1_1'))
    story.append(Paragraph("1.1 Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "Over the last decade, internet usage and mobile smartphone adoption have grown exponentially across every sphere of personal, "
        "academic, and commercial life. While this digital expansion has made banking, education, and commerce accessible from anywhere, "
        "it has simultaneously created a massive and fertile attack surface for cybercriminals. In our daily observations as students and "
        "technology users, we regularly encounter deceptive phishing links distributed through messaging apps, spam SMS messages (smishing), "
        "and untrusted links on social platforms. At the same time, Android operating systems, which power the overwhelming majority of mobile "
        "devices in India and worldwide, have become primary targets for malicious application packages (APKs).",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "Phishing attacks are designed to mimic legitimate institutions—such as popular commercial banks, e-commerce stores, college student portals, "
        "or social media services. Unsuspecting users are tricked into clicking a spoofed link and entering confidential credentials, one-time passwords "
        "(OTPs), and credit card details. On the mobile front, rogue Android applications often disguise themselves as harmless utility tools, such as "
        "document scanners, PDF readers, flashlights, or system cleaners. However, behind the scenes, these trojanized binaries quietly request elevated "
        "privileges—such as intercepting SMS messages to harvest two-factor authentication codes, or setting persistent broadcast receivers that boot "
        "automatically whenever the phone restarts.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "Historically, computer defense systems have relied almost exclusively on static blacklists and signature-matching databases. "
        "Well-known security tools maintain lists of previously reported phishing domains and MD5 or SHA-256 cryptographic hashes of identified malware. "
        "While this approach works well for known, unchanging threats, it fundamentally fails against modern cyber campaigns. Today, attackers can register "
        "a new domain name in minutes, distribute malicious links for a few hours, and abandon the domain before any security blacklist updates its records. "
        "Similarly, Android malware developers employ polymorphic code obfuscation and dynamic package repackaging to produce completely different cryptographic "
        "hashes for the exact same malicious payload.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "To solve these real-world challenges, our project team developed <b>CyberGuard</b>, an intelligent cyber threat detection platform. "
        "Rather than relying on outdated lists or slow dynamic sandboxes that take several minutes to detonate a file in a virtual emulator, "
        "our system extracts static lexical patterns and Android manifest structures in milliseconds. These features are then fed into trained "
        "Machine Learning algorithms—including Random Forest, XGBoost, Support Vector Machines, and Neural Networks—allowing our platform to evaluate "
        "whether a URL or APK is safe or malicious with high accuracy and wire-speed response times.",
        styles['BodyContent']
    ))

    story.append(PageMarker('S1_2'))
    story.append(Paragraph("1.2 Objectives", styles['SectionHeading']))
    story.append(Paragraph(
        "The primary objectives of our project work, as approved in our project synopsis by the Department of Computer Science & Engineering, "
        "are outlined as follows:",
        styles['BodyContent']
    ))
    objectives = [
        "<b>To develop an automated, user-friendly security system</b> that rapidly detects whether a given web URL or Android APK is safe or malicious using machine learning.",
        "<b>To engineer a static feature extraction pipeline</b> that analyzes URL lexical patterns and decompiles AndroidManifest.xml bytecode without requiring slow and resource-heavy dynamic sandbox execution.",
        "<b>To evaluate and benchmark multiple supervised classifiers</b> (Random Forest, XGBoost, Decision Tree, Logistic Regression, SVM, and MLP) to determine which algorithm offers the best trade-off between detection accuracy and execution latency.",
        "<b>To enable dynamic runtime model switching</b>, allowing an operator to switch the active classification model on the fly through an API without having to restart the backend server process.",
        "<b>To provide a resilient dual-database persistence engine</b> that automatically routes scan records to MongoDB and seamlessly falls back to local SQLite storage if the remote database is offline.",
        "<b>To build an intuitive, cyberpunk-themed web dashboard (HUD)</b> that displays real-time risk scores (0.0% to 100.0%), detailed parameter breakdowns, and historical telemetry for security analysts."
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_3'))
    story.append(Paragraph("1.3 Scope of the Project", styles['SectionHeading']))
    story.append(Paragraph(
        "The scope of CyberGuard encompasses both web-based and mobile application threat surfaces. The system is intentionally designed "
        "for practical, real-world deployment in collegiate laboratories, small-to-medium enterprise Security Operations Centers (SOCs), "
        "and individual user workflows:",
        styles['BodyContent']
    ))
    scopes = [
        "<b>Threat Surface Coverage:</b> The system analyzes full HTTP and HTTPS web URLs, as well as compiled Android Application Packages (.apk) and compressed archives (.zip).",
        "<b>Target Users:</b> Security analysts, network administrators, academic researchers, and end users seeking quick verification of suspicious links or unknown mobile packages.",
        "<b>Major Functionalities:</b> Token-based user authentication (JWT), static lexical parsing, Android bytecode decompilation via Androguard, multi-model probability scoring, dual-database audit logging, and interactive telemetry visualization.",
        "<b>Application Areas:</b> Email gateway filtering, automated ticket triage in SOC environments, corporate app-store pre-screening, and browser extension security engines.",
        "<b>Future Extensions:</b> Potential future extensions include live browser extension integration, automated dynamic hooking with Frida to inspect runtime encrypted payloads, and cloud Kubernetes containerization for large-scale enterprise deployments."
    ]
    for sc in scopes:
        story.append(Paragraph(f"• {sc}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_4'))
    story.append(Paragraph("1.4 Applications", styles['SectionHeading']))
    story.append(Paragraph(
        "The proposed platform can be deployed across multiple defensive environments, as outlined in our project presentation:",
        styles['BodyContent']
    ))
    story.append(Paragraph("1. <b>Web Browser Extension Integration:</b> Performing instant pre-navigation URL checks before a page loads, alerting users if an address exhibits suspicious brand spoofing or delimiter manipulation.", styles['BodyBullet']))
    story.append(Paragraph("2. <b>Enterprise Corporate Network Gateways:</b> Acting as an automated filter on corporate proxies to audit external links in employee emails and prevent credential harvesting.", styles['BodyBullet']))
    story.append(Paragraph("3. <b>App Store & MDM Pre-Screening:</b> Serving as an automated verification checkpoint for enterprise Mobile Device Management (MDM) platforms before sideloading APKs onto employee smartphones.", styles['BodyBullet']))
    story.append(Paragraph("4. <b>Academic Cybersecurity Research:</b> Serving as a testbench for comparing classification algorithms, observing confusion matrices, and testing feature engineering techniques under controlled laboratory conditions.", styles['BodyBullet']))

    story.append(PageMarker('S1_5'))
    story.append(Paragraph("1.5 Organization of Report", styles['SectionHeading']))
    story.append(Paragraph(
        "This project report is organized into nine structured chapters in accordance with the departmental guidelines:",
        styles['BodyContent']
    ))
    story.append(Paragraph("• <b>Chapter 1 – Introduction:</b> Establishes domain background, project objectives, operational scope, and practical applications.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 2 – Problem Identification:</b> Details current security challenges, analyzes existing signature systems, and articulates the proposed solution's advantages.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 3 – Literature Review:</b> Surveys twenty relevant peer-reviewed research papers from our project presentation, establishing the research gap.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 4 – System Requirements:</b> Defines functional, non-functional, hardware, and software requirements.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 5 – System Design:</b> Presents the overall architecture, module decomposition, UML diagrams, DFDs, database schema, and system flowchart.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 6 – System Implementation:</b> Walks through the implementation environment, module code logic, mathematical formulations, and pseudocode.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 7 – System Testing:</b> Details our verification and validation strategy along with twenty comprehensive, documented test cases.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 8 – Results and Discussion:</b> Presents interface screenshots, experimental benchmark metrics, ROC curves, confusion matrices, and comparative analyses.", styles['BodyBullet']))
    story.append(Paragraph("• <b>Chapter 9 – Conclusion and Future Scope:</b> Concludes the report, summarizes our contributions, discusses limitations, and outlines future enhancements.", styles['BodyBullet']))

    story.append(PageMarker('S1_6'))
    story.append(Paragraph("1.6 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 1 introduced the growing menace of phishing URLs and mobile Android malware, establishing why automated machine learning "
        "is necessary to replace slow blacklists. It outlined our project objectives, operational scope, real-world applications, "
        "and the overall structure of this report.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: PROBLEM IDENTIFICATION (3 Pages)
    # =========================================================================
    story.append(PageMarker('CH2'))
    story.append(Paragraph("CHAPTER 2", styles['ChapterTitle']))
    story.append(Paragraph("PROBLEM IDENTIFICATION", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S2_1'))
    story.append(Paragraph("2.1 Problem Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "Modern cybersecurity threats are constantly evolving to bypass traditional defensive perimeters. "
        "In our project analysis, we focused on two high-risk threat vectors: deceptive phishing URLs and malicious Android application packages (APKs). "
        "Phishing attacks rely heavily on social engineering, creating a sense of urgency through fake security alerts, bank account suspension warnings, "
        "or courier delivery notifications. Attackers craft web addresses that closely mimic legitimate institutions by using domain spoofing, "
        "adding excessive subdomains, inserting hyphens and sensitive keywords (such as 'secure-login-bank-update.com'), or using direct IP addresses "
        "instead of registered domain names to evade reputation filters.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "In the mobile Android domain, malware threats have become increasingly stealthy. Rather than overtly damaging device firmware, "
        "contemporary trojans masquerade as ordinary utilities—such as PDF readers, simple games, or calculator apps. "
        "Once installed by an unsuspecting user, these applications abuse permissions defined in their <code>AndroidManifest.xml</code>. "
        "For example, an app requesting <code>RECEIVE_BOOT_COMPLETED</code> can automatically trigger background malicious services whenever the smartphone "
        "is powered on. Similarly, an application requesting <code>SEND_SMS</code> can stealthily subscribe the user to premium-rate messaging services, "
        "while <code>SYSTEM_ALERT_WINDOW</code> allows malware to draw transparent overlays over authentic banking apps to steal login credentials.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "The major engineering challenges we identified in existing security pipelines include: (1) high classification latency that frustrates users, "
        "(2) excessive computational overhead of dynamic sandboxes, (3) static model obsolescence where security systems cannot adapt to new evasion "
        "patterns without complex redeployments, and (4) single points of failure where logging systems fail completely if a remote database goes offline.",
        styles['BodyContent']
    ))

    story.append(PageMarker('S2_2'))
    story.append(Paragraph("2.2 Existing System", styles['SectionHeading']))
    story.append(Paragraph(
        "Traditional defensive mechanisms rely primarily on three methodologies:",
        styles['BodyContent']
    ))
    story.append(Paragraph("1. <b>Signature-Based Antivirus and Blacklisting:</b> Security tools query centralized repositories of known malicious URLs (such as Google Safe Browsing or PhishTank) and databases of known file hashes (MD5, SHA-256).", styles['BodyBullet']))
    story.append(Paragraph("2. <b>Dynamic Virtual Machine Sandboxes:</b> Automated appliances boot guest virtual machines or Android emulators, detonate the suspicious sample, and record system call activity over a 5 to 15 minute window.", styles['BodyBullet']))
    story.append(Paragraph("3. <b>Static Rule-Based String Matching:</b> Regular expression engines scan files for static text signatures and predefined patterns.", styles['BodyBullet']))

    story.append(PageMarker('S2_2_1'))
    story.append(Paragraph("2.2.1 Drawbacks of Existing System", styles['SubSectionHeading']))
    story.append(Paragraph(
        "Through our research and hands-on experimentation, we identified several major drawbacks in the existing system:",
        styles['BodyContent']
    ))
    drawbacks = [
        "<b>Inability to Detect Zero-Day Threats:</b> Blacklists and hash registries can only flag threats after they have already been discovered, analyzed, and added to the database. Newly created phishing domains and freshly compiled malware easily slip through during this critical delay window.",
        "<b>Severe Computational Latency:</b> Running a dynamic sandbox requires spinning up an entire operating system emulator, simulating user touches, and waiting for network calls, taking anywhere from 3 to 15 minutes per file. This is far too slow for real-time browsing or rapid mobile triage.",
        "<b>Anti-Analysis and Evasion Tactics:</b> Modern malware binaries contain checks that detect the presence of emulators, debuggers, or missing hardware sensors (such as gyroscopes). When these indicators are detected, the malware remains dormant, tricking the sandbox into labeling it as benign.",
        "<b>Vendor Lock-in and Static Architectures:</b> Existing appliances lock administrators into a single proprietary algorithm. If an attacker discovers a blind spot in that specific classifier, the defense system cannot be easily reconfigured.",
        "<b>Database Failure Vulnerability:</b> When cloud-connected scanners lose connection to their centralized logging servers, scan records are often lost or unhandled exceptions crash the service."
    ]
    for db in drawbacks:
        story.append(Paragraph(f"• {db}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S2_3'))
    story.append(Paragraph("2.3 Proposed System", styles['SectionHeading']))
    story.append(Paragraph(
        "To overcome the fatal shortcomings of existing solutions, our team designed and implemented <b>CyberGuard</b>—an intelligent, "
        "hybrid static analysis platform powered by a flexible Machine Learning Model Zoo and a resilient dual-database persistence engine. "
        "Instead of waiting minutes for an emulator to boot or relying on outdated blacklists, CyberGuard inspects structural and lexical features "
        "within milliseconds. For web addresses, our extractor calculates lexical densities (dots, slashes, hyphens), checks for IP-based hostnames, "
        "verifies HTTPS encryption, and checks for credential-harvesting keywords. For Android APKs, our system decompresses the package and uses "
        "Androguard bytecode parsing to audit declared permissions, boot-time broadcast receivers, and background services.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "These extracted numerical vectors are fed into our dynamic Model Manager singleton. Security operators can select among six trained "
        "algorithms (Random Forest, XGBoost, Support Vector Machine, Decision Tree, Logistic Regression, and MLP Neural Network) on the fly without "
        "restarting the server. Every scan transaction is logged to our dual-persistence engine, which dynamically routes data to MongoDB and seamlessly "
        "falls back to local SQLite if MongoDB is offline.",
        styles['BodyContent']
    ))

    story.append(PageMarker('S2_3_1'))
    story.append(Paragraph("2.3.1 Advantages of Proposed System", styles['SubSectionHeading']))
    story.append(Paragraph("The key technical advantages of our proposed system include:", styles['BodyContent']))
    advantages = [
        "<b>Wire-Speed Real-Time Inference:</b> Evaluates URLs in under 20 milliseconds and APK packages in under 200 milliseconds, completely eliminating sandbox boot delays.",
        "<b>Proactive Zero-Day Detection:</b> Recognizes structural patterns and permission abuse in never-before-seen threats rather than relying on historical hashes.",
        "<b>Dynamic Multi-Model Agility:</b> Enables live switching between 6 distinct classifiers with zero server downtime, allowing operators to compare model performance in real time.",
        "<b>Fault-Tolerant Dual Persistence:</b> Seamlessly switches between MongoDB and SQLite to guarantee 100% audit log retention during network or database outages.",
        "<b>Intuitive Cyberpunk HUD:</b> Delivers an engaging, responsive user interface featuring circular threat gauges, comparative model matrices, and searchable telemetry archives."
    ]
    for adv in advantages:
        story.append(Paragraph(f"• {adv}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S2_4'))
    story.append(Paragraph("2.4 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 2 identified the fundamental weaknesses of traditional blacklists and dynamic sandboxes, highlighting zero-day blind spots "
        "and execution latency. It detailed the architecture of our proposed CyberGuard platform, demonstrating its superior speed, "
        "multi-model agility, and persistence resilience.",
        styles['BodyContent']
    ))
    story.append(PageBreak())
''')
print("Part 2 appended.")
