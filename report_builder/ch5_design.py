import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
from report_builder.styles_and_canvas import PageMarker, USABLE_WIDTH

def get_ch5_design_story(styles):
    story = []

    # =========================================================================
    # CHAPTER 5: SYSTEM DESIGN
    # =========================================================================
    story.append(PageMarker('CH5'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 5", styles['ChapterTitle']))
    story.append(Paragraph("SYSTEM DESIGN", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S5_1'))
    story.append(Paragraph("5.1 System Design Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "System design represents the vital transitional phase where abstract cybersecurity requirements are converted into a concrete, "
        "modular, and verifiable architectural implementation. To ensure that CyberGuard operates with lightning-fast responsiveness, "
        "flawless database fault tolerance, and zero-downtime model adaptability, our engineering team adopted a decoupled, service-oriented "
        "architecture. The system separates responsibilities cleanly between user presentation, RESTful API orchestration, domain-specific "
        "feature extractors, machine learning inference engines, and persistent data storage.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "This chapter comprehensively details the architectural blueprints of CyberGuard. We present the high-level system architecture, "
        "decompose the system into six core functional modules, illustrate operational dynamics through formal UML diagrams (Use Case, "
        "Sequence, Class, and Activity models), chart data transformations across Level 0 and Level 1 Data Flow Diagrams, define the "
        "dual-persistence database schema, and chart the end-to-end algorithmic decision flowchart.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 5.2: SYSTEM ARCHITECTURE
    # =========================================================================
    story.append(PageMarker('S5_2'))
    story.append(Paragraph("5.2 System Architecture", styles['SectionHeading']))
    story.append(Paragraph(
        "Figure 5.1 illustrates the complete multi-tiered system architecture of the CyberGuard cyber threat detection platform. "
        "The architecture is organized into five tightly integrated, decoupled tiers:",
        styles['BodyContent']
    ))
    
    # Figure 5.1
    story.append(PageMarker('FIG_5_1'))
    story.append(Image('report_assets/fig_architecture.png', width=USABLE_WIDTH, height=220))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.1: CyberGuard High-Level Modular System Architecture</b>", styles['CaptionText']))
    story.append(Spacer(1, 6))

    arch_tiers = [
        "<b>1. Client Presentation Tier:</b> A responsive React Single Page Application (SPA) designed with a cyberpunk terminal aesthetic. It provides analysts with intuitive drag-and-drop file upload zones for APKs, input text bars for URL evaluation, real-time SVG risk dials, model selection controls, and searchable audit feed tables.",
        "<b>2. API Gateway & Orchestration Tier:</b> Powered by Python FastAPI and Uvicorn ASGI server. This layer handles JWT authentication, enforces rate limiting, validates request schemas via Pydantic models, and dispatches analysis workloads asynchronously without blocking the event loop.",
        "<b>3. Feature Engineering Processing Tier:</b> Houses two specialized extraction pipelines: the URL Lexical Extractor (which computes syntactic densities, delimiter ratios, and brand impersonation flags in &lt;10ms) and the APK Bytecode Parser (which decompresses packages and audits binary XML manifests and Dalvik DEX headers via Androguard in &lt;200ms).",
        "<b>4. Machine Learning Inference Zoo:</b> A thread-safe singleton Model Manager maintaining six pre-compiled supervised learning models in host memory. It enables instantaneous on-the-fly model switching via atomic pointer swaps without restarting the server or dropping connections.",
        "<b>5. Dual-Persistence Database Tier:</b> A hybrid database layer featuring an active MongoDB document database for scalable telemetry indexing, backed by an embedded SQLite relational database with automatic failover routines that guarantee 100% audit log retention during network or server faults."
    ]
    for tier in arch_tiers:
        story.append(Paragraph(tier, styles['BodyContent']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 5.3: SYSTEM MODULES
    # =========================================================================
    story.append(PageMarker('S5_3'))
    story.append(Paragraph("5.3 System Modules (6 Core Modules)", styles['SectionHeading']))
    story.append(Paragraph(
        "As established in our project synopsis and architectural blueprints, the CyberGuard platform is modularized into six specialized "
        "subsystems. Table 5.1 provides an executive summary of each module's input, output, and operational role:",
        styles['BodyContent']
    ))
    
    # Table 5.1
    story.append(PageMarker('TAB_5_1'))
    story.append(Paragraph("<b>Table 5.1: Core Functional Modules of the CyberGuard Platform</b>", styles['CaptionText']))

    t51_data = [
        [Paragraph("<b>Module Name</b>", styles['TableHeader']), Paragraph("<b>Sub-Components</b>", styles['TableHeader']), Paragraph("<b>Input Artifact</b>", styles['TableHeader']), Paragraph("<b>Output Artifact</b>", styles['TableHeader']), Paragraph("<b>Operational Role</b>", styles['TableHeader'])],
        [Paragraph("1. Auth & Session Module", styles['TableCell']), Paragraph("JWT Manager, bcrypt hasher", styles['TableCell']), Paragraph("User credentials (JSON)", styles['TableCell']), Paragraph("Signed JWT bearer token", styles['TableCell']), Paragraph("Secures API endpoints and enforces role-based permissions.", styles['TableCell'])],
        [Paragraph("2. URL Lexical Engine", styles['TableCell']), Paragraph("Regex parser, entropy calculator", styles['TableCell']), Paragraph("Raw URL string", styles['TableCell']), Paragraph("16-dim numeric vector", styles['TableCell']), Paragraph("Extracts structural and lexical anomalies with zero network lag.", styles['TableCell'])],
        [Paragraph("3. APK Bytecode Engine", styles['TableCell']), Paragraph("ZIP inspector, Androguard parser", styles['TableCell']), Paragraph("Raw .apk binary file", styles['TableCell']), Paragraph("Binary permission vector", styles['TableCell']), Paragraph("Decompiles manifest and DEX headers in memory for rapid triage.", styles['TableCell'])],
        [Paragraph("4. Model Manager Zoo", styles['TableCell']), Paragraph("Singleton zoo, 6 ML models", styles['TableCell']), Paragraph("Extracted numeric vector", styles['TableCell']), Paragraph("Verdict, score, risk flags", styles['TableCell']), Paragraph("Executes inference and allows live switching among 6 algorithms.", styles['TableCell'])],
        [Paragraph("5. Dual-Persistence Engine", styles['TableCell']), Paragraph("Mongo client, SQLite adapter", styles['TableCell']), Paragraph("Scan telemetry dictionary", styles['TableCell']), Paragraph("Persisted audit record", styles['TableCell']), Paragraph("Provides fault-tolerant logging with automatic failover.", styles['TableCell'])],
        [Paragraph("6. Cyberpunk HUD Dashboard", styles['TableCell']), Paragraph("React widgets, SVG dials, Tailwind", styles['TableCell']), Paragraph("REST JSON responses", styles['TableCell']), Paragraph("Rendered UI telemetry", styles['TableCell']), Paragraph("Displays real-time threat gauges, metrics, and incident logs.", styles['TableCell'])],
    ]
    t51 = Table(t51_data, colWidths=[90, 85, 80, 85, 93])
    t51.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t51)
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 5.4: UML DIAGRAMS
    # =========================================================================
    story.append(PageMarker('S5_4'))
    story.append(Paragraph("5.4 UML Diagrams", styles['SectionHeading']))
    story.append(Paragraph(
        "To model system behavior, structural relationships, and interactions from multiple engineering perspectives, our team constructed "
        "four formal Unified Modeling Language (UML) diagrams:",
        styles['BodyContent']
    ))

    # Figure 5.2 Use Case
    story.append(PageMarker('FIG_5_2'))
    story.append(Image('report_assets/fig_usecase.png', width=USABLE_WIDTH, height=210))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.2: Use Case Diagram of Multi-Role Threat Analysis</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>Use Case Analysis:</b> Figure 5.2 portrays the primary interactions between system actors (Security Analyst, Threat Hunter, "
        "and System Administrator) and core CyberGuard use cases. Security Analysts invoke 'Scan Suspicious URL', 'Upload & Triage APK', "
        "and 'Export Threat Audit Report'. Threat Hunters access 'Evaluate Model Zoo Benchmarks' and 'Switch Active Classifier Engine'. "
        "Administrators oversee 'Manage User Credentials' and 'Configure Database Failover'. Secondary include relationships ensure that "
        "all scan operations automatically trigger 'Extract Static Heuristics' and 'Log Telemetry Record'.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # Figure 5.3 Sequence Diagram
    story.append(PageMarker('FIG_5_3'))
    story.append(Image('report_assets/fig_sequence.png', width=USABLE_WIDTH, height=210))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.3: Sequence Diagram of Live Threat Inspection Lifecycle</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>Sequence Analysis:</b> Figure 5.3 depicts the synchronous and asynchronous message flow during an incoming threat evaluation request. "
        "The Client initiates an HTTP POST request carrying an artifact payload and a JWT authorization header to the API Gateway. "
        "The Gateway validates the token, selects the appropriate feature extraction engine, and requests vector transformation. "
        "The extracted vector is passed to the Model Manager singleton, which invokes predict_proba() on the currently active classifier. "
        "The resulting score and risk flags are dispatched asynchronously to the Dual-Persistence Engine for background persistence, "
        "while the JSON response is returned immediately to the client in under 50 milliseconds.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # Figure 5.4 Class Diagram
    story.append(PageMarker('FIG_5_4'))
    story.append(Image('report_assets/fig_class.png', width=USABLE_WIDTH, height=210))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.4: UML Class Hierarchy of Model Zoo and Feature Engines</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>Class Hierarchy Analysis:</b> Figure 5.4 details the object-oriented structure of CyberGuard's backend services. "
        "The core ModelManager singleton encapsulates references to the six trained classifier classes (RandomForestClassifier, "
        "XGBoostClassifier, SVMClassifier, DecisionTreeClassifier, LogisticRegressionClassifier, and MLPClassifier), which all implement "
        "a common BaseClassifier interface defining fit(), predict(), and predict_proba() methods. The FeatureExtractor base class "
        "is specialized by URLExtractor and APKExtractor, ensuring strict separation of concerns.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # Figure 5.8 Activity Diagram
    story.append(PageMarker('FIG_5_8'))
    story.append(Image('report_assets/fig_activity.png', width=USABLE_WIDTH, height=210))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.8: UML Activity Diagram of Threat Inspection Workflow</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>Activity Workflow:</b> Figure 5.8 tracks the execution flow from the moment an artifact enters the system through input validation, "
        "feature parsing, model scoring, risk threshold branching, dual-database failover routing, and final dashboard rendering.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 5.5: DATA FLOW DIAGRAMS
    # =========================================================================
    story.append(PageMarker('S5_5'))
    story.append(Paragraph("5.5 Data Flow Diagrams (Level 0 and Level 1)", styles['SectionHeading']))
    story.append(Paragraph(
        "Data Flow Diagrams (DFDs) illustrate the movement, transformation, and storage of information across system boundaries without "
        "assuming specific hardware or software implementations:",
        styles['BodyContent']
    ))

    # Figure 5.5 DFD 0
    story.append(PageMarker('FIG_5_5'))
    story.append(Image('report_assets/fig_dfd0.png', width=USABLE_WIDTH, height=180))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.5: Data Flow Diagram (Level 0 — Context Diagram)</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>DFD Level 0 (Context Diagram):</b> Figure 5.5 defines the highest-level operational context. The external entity (User / Security Analyst) "
        "submits suspicious URLs and APK files into the central CyberGuard System Process (Process 0.0) and receives structured threat verdicts, "
        "risk meters, and audit reports. The central system exchanges raw scan telemetry and retrieves configuration states from the persistent Threat Database.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # Figure 5.6 DFD 1
    story.append(PageMarker('FIG_5_6'))
    story.append(Image('report_assets/fig_dfd1.png', width=USABLE_WIDTH, height=200))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.6: Data Flow Diagram (Level 1 — Detailed Threat Pipeline)</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>DFD Level 1 Decomposition:</b> Figure 5.6 decomposes the main process into four interconnected sub-processes: Process 1.0 (Authenticate User), "
        "Process 2.0 (Extract Static Heuristic Features), Process 3.0 (Classify via Model Zoo), and Process 4.0 (Persist Telemetry & Log Audit). "
        "Information flows seamlessly between these processes and two shared data stores: Model Registry (D1) and Threat Telemetry Store (D2).",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 5.6: DATABASE DESIGN & ENTITY RELATIONSHIP
    # =========================================================================
    story.append(PageMarker('S5_6'))
    story.append(Paragraph("5.6 Database Design & Entity Relationship", styles['SectionHeading']))
    story.append(Paragraph(
        "To satisfy the dual-persistence requirement, our team designed a flexible relational and document schema. "
        "Figure 5.7 illustrates the Entity Relationship (ER) diagram governing the persistent data layer:",
        styles['BodyContent']
    ))

    # Figure 5.7 ER Diagram
    story.append(PageMarker('FIG_5_7'))
    story.append(Image('report_assets/fig_er.png', width=USABLE_WIDTH, height=200))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.7: Entity Relationship Diagram of Dual-Persistence Schema</b>", styles['CaptionText']))
    story.append(Spacer(1, 6))

    story.append(PageMarker('TAB_5_2'))
    story.append(Paragraph("<b>Table 5.2: Dual-Persistence Database Relational / Document Schema</b>", styles['CaptionText']))

    t52_data = [
        [Paragraph("<b>Entity / Table</b>", styles['TableHeader']), Paragraph("<b>Primary Key / ID</b>", styles['TableHeader']), Paragraph("<b>Attributes & Types</b>", styles['TableHeader']), Paragraph("<b>Constraints / Indexes</b>", styles['TableHeader']), Paragraph("<b>Failover Handling</b>", styles['TableHeader'])],
        [Paragraph("Users", styles['TableCell']), Paragraph("user_id (UUID / ObjectId)", styles['TableCell']), Paragraph("username (VARCHAR), password_hash (VARCHAR), role (VARCHAR), created_at (TIMESTAMP)", styles['TableCell']), Paragraph("UNIQUE(username), NOT NULL(password_hash)", styles['TableCell']), Paragraph("Mirrored locally in SQLite for offline analyst login.", styles['TableCell'])],
        [Paragraph("ThreatScans", styles['TableCell']), Paragraph("scan_id (UUID / ObjectId)", styles['TableCell']), Paragraph("user_id (FK), target_type (VARCHAR), target_name (TEXT), verdict (VARCHAR), confidence (FLOAT), latency_ms (FLOAT), created_at (TIMESTAMP)", styles['TableCell']), Paragraph("INDEX(target_type), INDEX(verdict), INDEX(created_at)", styles['TableCell']), Paragraph("Saved to SQLite if Mongo is down; synced via batch replay.", styles['TableCell'])],
        [Paragraph("ScanFeatures", styles['TableCell']), Paragraph("feature_id (UUID / ObjectId)", styles['TableCell']), Paragraph("scan_id (FK), raw_features (JSON / TEXT), top_indicators (JSON / TEXT)", styles['TableCell']), Paragraph("FOREIGN KEY(scan_id) REFERENCES ThreatScans(scan_id)", styles['TableCell']), Paragraph("Stored as JSON string in SQLite, nested doc in MongoDB.", styles['TableCell'])],
        [Paragraph("ModelMetrics", styles['TableCell']), Paragraph("metric_id (UUID / ObjectId)", styles['TableCell']), Paragraph("model_name (VARCHAR), accuracy (FLOAT), f1_score (FLOAT), avg_latency_ms (FLOAT), last_updated (TIMESTAMP)", styles['TableCell']), Paragraph("UNIQUE(model_name)", styles['TableCell']), Paragraph("Static seed in SQLite; updated dynamically in MongoDB.", styles['TableCell'])],
    ]
    t52 = Table(t52_data, colWidths=[70, 75, 140, 85, 63])
    t52.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t52)
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 5.7: FLOWCHART OF THREAT ANALYSIS
    # =========================================================================
    story.append(PageMarker('S5_7'))
    story.append(Paragraph("5.7 Flowchart of Threat Analysis", styles['SectionHeading']))
    story.append(Paragraph(
        "Figure 5.9 maps out the sequential algorithmic decision logic followed by CyberGuard when an input is submitted:",
        styles['BodyContent']
    ))

    # Figure 5.9 Flowchart
    story.append(PageMarker('FIG_5_9'))
    story.append(Image('report_assets/fig_flowchart.png', width=USABLE_WIDTH, height=210))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Figure 5.9: System Flowchart of Threat Decision Pipeline</b>", styles['CaptionText']))
    story.append(Paragraph(
        "<b>Flowchart Step Analysis:</b> Upon receipt of an artifact, the system first verifies whether the payload is a URL string or an APK binary. "
        "If a URL is provided, the URL Extractor executes sixteen lexical tests. If an APK is provided, Androguard unzips the archive and extracts "
        "the permission vector. The extracted vector is passed to the active Model Zoo classifier, which outputs a probability score P. "
        "If P &gt; 0.70, the artifact is classified as Malicious; if 0.40 &le; P &le; 0.70, it is classified as Suspicious; otherwise, it is Benign. "
        "The system then attempts to write to MongoDB. If MongoDB times out, the failover routine commits the record to SQLite and marks a sync flag. "
        "Finally, the formatted telemetry is delivered to the client interface.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 5.8: SUMMARY
    # =========================================================================
    story.append(PageMarker('S5_8'))
    story.append(Paragraph("5.8 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 5 articulated the structural architecture, module decomposition, UML diagrams, DFD data flows, database schemas, and "
        "execution flowcharts for CyberGuard. By establishing clear module boundaries and designing a resilient dual-persistence engine, "
        "the architecture provides the necessary foundation for high-performance software implementation.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    return story
