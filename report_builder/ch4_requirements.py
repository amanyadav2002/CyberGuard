import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from report_builder.styles_and_canvas import PageMarker

def get_ch4_requirements_story(styles):
    story = []

    # =========================================================================
    # CHAPTER 4: SYSTEM REQUIREMENTS
    # =========================================================================
    story.append(PageMarker('CH4'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 4", styles['ChapterTitle']))
    story.append(Paragraph("SYSTEM REQUIREMENTS", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S4_1'))
    story.append(Paragraph("4.1 System Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "A rigorous requirements engineering process is paramount to translating high-level cybersecurity goals into a robust, "
        "production-grade software system. The CyberGuard platform was designed from the ground up to address the complex operational "
        "demands of modern Security Operations Centers (SOCs) and autonomous malware triage pipelines. The system operates as a hybrid, "
        "asynchronous client-server architecture comprising a high-performance Python FastAPI backend, a scikit-learn/XGBoost machine learning "
        "inference engine, an Androguard static bytecode parsing pipeline, a dual-persistence database layer, and a reactive cyberpunk-themed HUD.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "Our requirements definition process involved analyzing the threat workflows of SOC analysts, reverse engineers, and system administrators. "
        "Three distinct user roles were established to govern system interactions: <b>Security Analysts</b> (who submit scan requests, inspect "
        "detailed telemetry, and export threat reports), <b>Threat Hunters / Data Scientists</b> (who evaluate comparative model benchmarks and "
        "switch active classifier backends), and <b>System Administrators</b> (who manage user authentication, API token quotas, and database "
        "failover configurations).",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S4_2'))
    story.append(Paragraph("4.2 Functional Requirements", styles['SectionHeading']))
    story.append(Paragraph(
        "Functional requirements specify the concrete actions, algorithmic computations, and data transformations that the system must "
        "execute. We formally defined eight primary functional requirements (FR-01 through FR-08):",
        styles['BodyContent']
    ))

    func_reqs = [
        ("FR-01: User Authentication & Role-Based Access Control (RBAC)",
         "The system shall authenticate operators using industry-standard JSON Web Tokens (JWT) signed with HMAC-SHA256. User credentials shall be salted and hashed using bcrypt (cost factor 12). The system must enforce granular access controls distinguishing between Analysts, Threat Hunters, and Administrators across all protected REST endpoints."),
        ("FR-02: Real-Time URL Heuristic Ingestion and Parsing",
         "The system shall ingest arbitrary Uniform Resource Identifier (URI) strings via HTTP POST requests, validate syntax against RFC 3986, and extract sixteen distinct lexical and structural features—including character counts, delimiter frequencies, presence of raw IP hostnames, Shannon entropy, and security-sensitive keywords—in under 10 milliseconds without making outbound network connections."),
        ("FR-03: Static Android APK Binary Decompression and Bytecode Extraction",
         "The system shall accept uploaded Android Application Package (APK) binaries up to 100 megabytes in size, verify ZIP archive integrity headers, parse the binary AndroidManifest.xml and classes.dex files using in-memory Androguard routines, and generate a standardized binary feature vector capturing dangerous permissions, boot broadcast receivers, and background service declarations in under 200 milliseconds."),
        ("FR-04: Multi-Model Machine Learning Zoo & Live Switching",
         "The system shall maintain a pre-loaded, thread-safe Model Zoo singleton capable of hosting six trained supervised classifiers: Random Forest, XGBoost, Support Vector Machines (SVM), Decision Trees, Logistic Regression, and Multi-Layer Perceptron (MLP). The platform must provide an administrative endpoint allowing operators to switch the active global classifier on the fly with zero server restarts and zero dropped connections."),
        ("FR-05: Real-Time Threat Scoring & Human-Readable Categorization",
         "Upon receiving an extracted feature vector, the active classifier shall compute a continuous threat confidence score (0.00 to 1.00) and assign a discrete triage verdict: 'Benign' (score &lt; 0.40), 'Suspicious' (0.40 &le; score &le; 0.70), or 'Malicious' (score &gt; 0.70). The response payload must include a detailed breakdown of the top contributing risk indicators."),
        ("FR-06: Resilient Dual-Persistence Telemetry Archival",
         "The system shall automatically record every scan event—including client IP, timestamp, target artifact, extracted features, active model, verdict, confidence, and inference latency—to a primary MongoDB database. If the primary database is unreachable, the system must transparently fall back to an embedded SQLite database without throwing 500 errors to the client, synchronizing pending records once connectivity is restored."),
        ("FR-07: Historical Telemetry Querying and Search Filtering",
         "The platform shall provide indexed search endpoints allowing security analysts to query historical scan records using flexible filters (artifact type, threat verdict, date range, minimum confidence threshold, and keyword search) with paginated JSON responses executing in under 50 milliseconds."),
        ("FR-08: Cyberpunk HUD Telemetry Dashboard Rendering",
         "The frontend web interface shall dynamically render scan results using a futuristic cyberpunk Heads-Up Display (HUD) theme. The interface must feature real-time circular SVG threat gauges, color-coded risk badges (Crimson Red for Malicious, Amber Yellow for Suspicious, Emerald Green for Benign), interactive model-switching dropdowns, and live-updating telemetry feed tables.")
    ]

    for title, desc in func_reqs:
        story.append(Paragraph(f"<b>{title}:</b> {desc}", styles['BodyContent']))
        story.append(Spacer(1, 2))

    # =========================================================================
    # SECTION 4.3: NON-FUNCTIONAL REQUIREMENTS
    # =========================================================================
    story.append(PageMarker('S4_3'))
    story.append(Paragraph("4.3 Non-Functional Requirements", styles['SectionHeading']))
    story.append(Paragraph(
        "Non-functional requirements define the systemic quality attributes, operational constraints, and performance benchmarks "
        "that ensure enterprise-grade dependability:",
        styles['BodyContent']
    ))
    nfrs = [
        "<b>Performance & Latency:</b> The system must evaluate URL threats in under 20 milliseconds and APK packages in under 200 milliseconds under single-request conditions. The API layer must sustain a throughput of at least 100 concurrent requests per second with 95th percentile response times remaining below 300 milliseconds on quad-core hardware.",
        "<b>Security & Robustness:</b> The platform must conform to OWASP Top 10 security standards. All input parameters must be strictly sanitized to eliminate Server-Side Request Forgery (SSRF), Cross-Site Scripting (XSS), and SQL/NoSQL injection vulnerabilities. Uploaded APKs must be inspected strictly in memory or in isolated temporary directories with immediate post-scan shredding.",
        "<b>Availability & Fault Tolerance:</b> The backend service must achieve 99.9% operational availability. The dual-database persistence engine must execute automatic failover from MongoDB to SQLite in less than 50 milliseconds without losing a single telemetry record or interrupting ongoing scans.",
        "<b>Maintainability & Extensibility:</b> The codebase must strictly adhere to PEP-8 coding standards, with modular separation between API routing, feature extractors, model managers, and database adapters. Adding a new machine learning algorithm to the Model Zoo must require fewer than 20 lines of configuration code.",
        "<b>Usability & Accessibility:</b> The user interface must provide a modern, responsive layout that adapts seamlessly to desktop monitors and field tablet displays. Visual indicators must maintain high contrast ratios compliant with WCAG 2.1 AA standards to prevent analyst fatigue during extended monitoring shifts."
    ]
    for nfr in nfrs:
        story.append(Paragraph(f"• {nfr}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # TABLE 4.1: HARDWARE REQUIREMENTS
    # =========================================================================
    story.append(PageMarker('TAB_4_1'))
    story.append(Paragraph("4.4 Hardware Requirements", styles['SectionHeading']))
    story.append(Paragraph(
        "To ensure optimal execution during both training and real-time inference phases, our team formulated minimum and recommended "
        "hardware specifications as shown in Table 4.1:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<b>Table 4.1: Minimum & Recommended Hardware Specifications</b>", styles['CaptionText']))

    t41_data = [
        [Paragraph("<b>Hardware Component</b>", styles['TableHeader']), Paragraph("<b>Minimum Specification (Triage Node)</b>", styles['TableHeader']), Paragraph("<b>Recommended Specification (SOC Cluster)</b>", styles['TableHeader'])],
        [Paragraph("Processor (CPU)", styles['TableCell']), Paragraph("Intel Core i3 / AMD Ryzen 3 (4 Cores, 2.5 GHz)", styles['TableCell']), Paragraph("Intel Core i7 / AMD Ryzen 7 (8 Cores, 3.8 GHz+)", styles['TableCell'])],
        [Paragraph("System Memory (RAM)", styles['TableCell']), Paragraph("8 GB DDR4", styles['TableCell']), Paragraph("16 GB – 32 GB DDR4/DDR5", styles['TableCell'])],
        [Paragraph("Persistent Storage", styles['TableCell']), Paragraph("256 GB SATA SSD", styles['TableCell']), Paragraph("512 GB NVMe M.2 SSD (High IOPS)", styles['TableCell'])],
        [Paragraph("Network Interface", styles['TableCell']), Paragraph("100 Mbps Fast Ethernet", styles['TableCell']), Paragraph("1 Gbps / 10 Gbps Full Duplex Ethernet", styles['TableCell'])],
        [Paragraph("Display Resolution", styles['TableCell']), Paragraph("1366 &times; 768 pixels", styles['TableCell']), Paragraph("1920 &times; 1080 pixels (Full HD) or higher", styles['TableCell'])],
        [Paragraph("Dedicated GPU", styles['TableCell']), Paragraph("Not required for CPU inference", styles['TableCell']), Paragraph("NVIDIA RTX 3060+ (for model retraining)", styles['TableCell'])],
    ]
    t41 = Table(t41_data, colWidths=[110, 160, 163])
    t41.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t41)
    story.append(Spacer(1, 6))

    # =========================================================================
    # TABLE 4.2: SOFTWARE REQUIREMENTS
    # =========================================================================
    story.append(PageMarker('TAB_4_2'))
    story.append(Paragraph("4.5 Software Requirements", styles['SectionHeading']))
    story.append(Paragraph(
        "The complete software development stack, runtimes, operating environments, and foundational libraries utilized in CyberGuard "
        "are enumerated in Table 4.2:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<b>Table 4.2: Software Specifications and Development Stack</b>", styles['CaptionText']))

    t42_data = [
        [Paragraph("<b>Layer / Category</b>", styles['TableHeader']), Paragraph("<b>Software / Tool Name</b>", styles['TableHeader']), Paragraph("<b>Version</b>", styles['TableHeader']), Paragraph("<b>Operational Role & Justification</b>", styles['TableHeader'])],
        [Paragraph("Operating System", styles['TableCell']), Paragraph("Ubuntu Linux / Windows 11", styles['TableCell']), Paragraph("22.04 LTS / 64-bit", styles['TableCell']), Paragraph("Cross-platform host environment for services.", styles['TableCell'])],
        [Paragraph("Backend Runtime", styles['TableCell']), Paragraph("Python", styles['TableCell']), Paragraph("3.10.12", styles['TableCell']), Paragraph("Primary programming language for ML and API.", styles['TableCell'])],
        [Paragraph("Web API Framework", styles['TableCell']), Paragraph("FastAPI", styles['TableCell']), Paragraph("0.109.0+", styles['TableCell']), Paragraph("Asynchronous, high-throughput ASGI microframework.", styles['TableCell'])],
        [Paragraph("ASGI Web Server", styles['TableCell']), Paragraph("Uvicorn", styles['TableCell']), Paragraph("0.27.0+", styles['TableCell']), Paragraph("Lightning-fast ASGI server powered by uvloop.", styles['TableCell'])],
        [Paragraph("ML & Scientific Stack", styles['TableCell']), Paragraph("scikit-learn & NumPy", styles['TableCell']), Paragraph("1.4.0+ / 1.26.0+", styles['TableCell']), Paragraph("Model training, vector math, and inference pipelines.", styles['TableCell'])],
        [Paragraph("Gradient Boosting", styles['TableCell']), Paragraph("XGBoost", styles['TableCell']), Paragraph("2.0.3+", styles['TableCell']), Paragraph("High-performance regularized tree ensemble engine.", styles['TableCell'])],
        [Paragraph("Bytecode Parser", styles['TableCell']), Paragraph("Androguard", styles['TableCell']), Paragraph("3.4.0+", styles['TableCell']), Paragraph("Static Dalvik DEX and Android XML manifest parser.", styles['TableCell'])],
        [Paragraph("Primary Database", styles['TableCell']), Paragraph("MongoDB Community", styles['TableCell']), Paragraph("7.0+", styles['TableCell']), Paragraph("Document-oriented NoSQL storage for threat logs.", styles['TableCell'])],
        [Paragraph("Fallback Database", styles['TableCell']), Paragraph("SQLite", styles['TableCell']), Paragraph("3.42.0", styles['TableCell']), Paragraph("Zero-config embedded relational database failover.", styles['TableCell'])],
        [Paragraph("Frontend Runtime", styles['TableCell']), Paragraph("Node.js / React", styles['TableCell']), Paragraph("20.x / 18.2+", styles['TableCell']), Paragraph("Reactive Single Page Application (SPA) dashboard.", styles['TableCell'])],
        [Paragraph("UI Styling Engine", styles['TableCell']), Paragraph("Tailwind CSS", styles['TableCell']), Paragraph("3.4.0+", styles['TableCell']), Paragraph("Utility-first styling for cyberpunk aesthetic HUD.", styles['TableCell'])],
    ]
    t42 = Table(t42_data, colWidths=[95, 110, 68, 160])
    t42.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t42)
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 4.6: SUMMARY
    # =========================================================================
    story.append(PageMarker('S4_6'))
    story.append(Paragraph("4.6 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 4 comprehensively detailed the functional capabilities, non-functional quality attributes, and hardware/software "
        "specifications required to realize the CyberGuard platform. By codifying eight distinct functional requirements and establishing "
        "stringent latency and fault-tolerance constraints, we established a clear engineering blueprint for the system design phase.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    return story
