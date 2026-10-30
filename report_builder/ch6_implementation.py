import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from report_builder.styles_and_canvas import PageMarker

def get_ch6_implementation_story(styles):
    story = []

    # =========================================================================
    # CHAPTER 6: SYSTEM IMPLEMENTATION
    # =========================================================================
    story.append(PageMarker('CH6'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 6", styles['ChapterTitle']))
    story.append(Paragraph("SYSTEM IMPLEMENTATION", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S6_1'))
    story.append(Paragraph("6.1 Implementation Environment", styles['SectionHeading']))
    story.append(Paragraph(
        "Translating the architectural designs of CyberGuard into a functional, resilient, and enterprise-grade software product required "
        "establishing a disciplined software engineering environment. Our student development team followed standard Git version control "
        "practices, automated virtual environment isolation via Python venv, and component-based frontend engineering using Vite and React. "
        "The backend services were constructed on Python 3.10 utilizing the modern FastAPI asynchronous framework, while machine learning "
        "inference was realized using scikit-learn, XGBoost, and Androguard static parsing libraries.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "During our development sprint, our team placed significant emphasis on non-blocking asynchronous I/O. By leveraging Python's "
        "asyncio event loop and Starlette routing foundations within FastAPI, CyberGuard handles concurrent threat evaluation requests "
        "efficiently without spawning memory-heavy OS threads for every incoming HTTP connection.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S6_2'))
    story.append(Paragraph("6.2 Project Directory Structure", styles['SectionHeading']))
    story.append(Paragraph(
        "To ensure modularity and ease of maintenance, the codebase was organized into a clean multi-tier directory layout:",
        styles['BodyContent']
    ))
    
    dir_tree = (
        "CyberGuard/<br/>"
        "├── backend/<br/>"
        "│&nbsp;&nbsp;&nbsp;├── venv/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Isolated Python virtual runtime<br/>"
        "│&nbsp;&nbsp;&nbsp;├── main.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# FastAPI entrypoint, ASGI routing & CORS<br/>"
        "│&nbsp;&nbsp;&nbsp;├── auth.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# JWT token generation & bcrypt authentication<br/>"
        "│&nbsp;&nbsp;&nbsp;├── database.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Dual-persistence engine (MongoDB + SQLite failover)<br/>"
        "│&nbsp;&nbsp;&nbsp;├── model_manager.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Thread-safe Model Zoo singleton & switcher<br/>"
        "│&nbsp;&nbsp;&nbsp;├── extractors/<br/>"
        "│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── url_extractor.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 16-dimensional lexical & entropy parser<br/>"
        "│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── apk_extractor.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Androguard bytecode & manifest analyzer<br/>"
        "│&nbsp;&nbsp;&nbsp;├── models/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Pre-trained serialized model artifacts (.pkl)<br/>"
        "│&nbsp;&nbsp;&nbsp;└── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Backend library dependencies<br/>"
        "├── frontend/<br/>"
        "│&nbsp;&nbsp;&nbsp;├── src/<br/>"
        "│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── components/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Cyberpunk HUD, Threat Gauges, Feed Table<br/>"
        "│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── App.jsx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Root React application & state container<br/>"
        "│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── main.jsx&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# React DOM bootstrap mount<br/>"
        "│&nbsp;&nbsp;&nbsp;├── tailwind.config.js&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Cyberpunk neon color palette configuration<br/>"
        "│&nbsp;&nbsp;&nbsp;└── package.json&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Frontend Node.js dependencies<br/>"
        "└── README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Project deployment & operational documentation"
    )
    story.append(Paragraph(dir_tree, styles['CodeSnippet']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 6.3: CORE BACKEND MODULES & FILE WALKTHROUGH
    # =========================================================================
    story.append(PageMarker('S6_3'))
    story.append(Paragraph("6.3 Core Backend Modules & File Walkthrough", styles['SectionHeading']))
    story.append(Paragraph(
        "Each core component within the backend fulfills a distinct role in orchestrating secure threat classification:",
        styles['BodyContent']
    ))

    modules_walk = [
        ("1. Application Orchestrator (backend/main.py):",
         "The main.py file serves as the ASGI entrypoint. It configures Cross-Origin Resource Sharing (CORS) middleware to allow secure communication with the React frontend, registers API route routers, and initializes application lifespan events. Lifespan handlers trigger the ModelManager singleton on startup to load pre-trained binary model files into memory, eliminating cold-start delays during active scanning."),
        ("2. Authentication Subsystem (backend/auth.py):",
         "Implements RFC 7519 compliant JSON Web Tokens (JWT). The module exposes create_access_token() which signs payloads with an HMAC-SHA256 secret key and a configurable expiration delta (default: 60 minutes). Incoming requests to protected endpoints pass through the get_current_user() FastAPI dependency, which extracts and verifies the bearer token from the HTTP Authorization header."),
        ("3. URL Lexical Extraction Pipeline (backend/extractors/url_extractor.py):",
         "Extracts a 16-dimensional numerical vector from raw URL strings without making external network queries. It computes length metrics (url_length, domain_length, path_length), delimiter counts (dots, hyphens, underscores, slashes, question marks, equal signs, at-symbols), detects raw IPv4/IPv6 address patterns via regular expressions, checks HTTPS protocol presence, and calculates character-level Shannon entropy to capture algorithmic domain generation."),
        ("4. APK Bytecode Extraction Pipeline (backend/extractors/apk_extractor.py):",
         "Handles uploaded Android application packages. Using Androguard's APK class, it parses the binary AndroidManifest.xml and classes.dex files directly from memory buffers. It maps requested permissions against a curated list of fifteen critical Android dangerous permissions (e.g., READ_SMS, ACCESS_FINE_LOCATION, CAMERA, SYSTEM_ALERT_WINDOW), checks for BOOT_COMPLETED broadcast receivers, and returns a normalized 15-dimensional binary feature vector in under 200 milliseconds."),
        ("5. Dynamic Model Zoo Manager (backend/model_manager.py):",
         "Constructed as a thread-safe singleton. On initialization, it deserializes six trained classifiers (Random Forest, XGBoost, SVM, Decision Tree, Logistic Regression, and MLP) using joblib. It provides an atomic switch_model(model_name) method that rebinds the internal active classifier reference without requiring service restarts or interrupting in-flight requests."),
        ("6. Resilient Dual-Persistence Adapter (backend/database.py):",
         "Manages threat telemetry persistence. It establishes an asynchronous connection pool to MongoDB via Motor/PyMongo. When save_scan_telemetry() is called, the adapter attempts to insert the document into the MongoDB 'threat_scans' collection. If an exception occurs (network timeout or connection refused), it catches the error and commits the record to a local SQLite database (cyberguard_fallback.db), ensuring zero data loss.")
    ]

    for title, desc in modules_walk:
        story.append(Paragraph(f"<b>{title}</b>", styles['SubSectionHeading']))
        story.append(Paragraph(desc, styles['BodyContent']))
        story.append(Spacer(1, 2))

    # =========================================================================
    # SECTION 6.4: MATHEMATICAL FORMULATIONS
    # =========================================================================
    story.append(PageMarker('S6_4'))
    story.append(Paragraph("6.4 Machine Learning Classification Formulations", styles['SectionHeading']))
    story.append(Paragraph(
        "To provide rigorous mathematical justification for our classification models, our team formulated the optimization objectives "
        "and decision boundaries governing each deployed algorithm:",
        styles['BodyContent']
    ))

    story.append(Paragraph("<b>1. Random Forest & Decision Tree (Gini Impurity Criterion):</b>", styles['SubSectionHeading']))
    story.append(Paragraph(
        "For a node dataset D containing samples belonging to C threat classes (where C = 2 for Benign vs. Malicious), the Gini impurity "
        "I_G(D) measures the probability of misclassifying a randomly chosen element:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>I<sub>G</sub>(D) = 1 &minus; &sum;<sub>i=1</sub><sup>C</sup> (p<sub>i</sub>)<sup>2</sup></i>", styles['EquationText']))
    story.append(Paragraph(
        "When evaluating a potential feature split s on feature f with threshold &theta;, the dataset is partitioned into subsets D<sub>L</sub> "
        "and D<sub>R</sub>. The optimal split maximizes the Information Gain &Delta;I<sub>G</sub>(D, s):",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>&Delta;I<sub>G</sub>(D, s) = I<sub>G</sub>(D) &minus; [ (|D<sub>L</sub>| / |D|) I<sub>G</sub>(D<sub>L</sub>) + (|D<sub>R</sub>| / |D|) I<sub>G</sub>(D<sub>R</sub>) ]</i>", styles['EquationText']))
    story.append(Paragraph(
        "In our Random Forest ensemble, B = 100 bootstrap trees are constructed, each trained on a random subsample of &radic;m features. "
        "The final ensemble prediction is computed via majority voting across all individual trees.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2. XGBoost (Regularized Objective Optimization):</b>", styles['SubSectionHeading']))
    story.append(Paragraph(
        "XGBoost minimizes a regularized objective function combining convex loss and tree complexity penalties at round t:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>&Omega;(f<sub>t</sub>) = &gamma; T + &frac12; &lambda; &sum;<sub>j=1</sub><sup>T</sup> (w<sub>j</sub>)<sup>2</sup></i>", styles['EquationText']))
    story.append(Paragraph(
        "Taking a second-order Taylor expansion of the loss function yields the simplified objective:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>L<sup>(t)</sup> &approx; &sum;<sub>i=1</sub><sup>n</sup> [ g<sub>i</sub> f<sub>t</sub>(x<sub>i</sub>) + &frac12; h<sub>i</sub> (f<sub>t</sub>(x<sub>i</sub>))<sup>2</sup> ] + &Omega;(f<sub>t</sub>)</i>", styles['EquationText']))
    story.append(Paragraph(
        "where g<sub>i</sub> = &part;L / &part;y&#770;<sup>(t-1)</sup> and h<sub>i</sub> = &part;<sup>2</sup>L / &part;(y&#770;<sup>(t-1)</sup>)<sup>2</sup> "
        "represent the first and second-order gradient statistics of the logistic loss function.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>3. Support Vector Machine (Dual Formulation with RBF Kernel):</b>", styles['SubSectionHeading']))
    story.append(Paragraph(
        "For non-linearly separable feature spaces, the SVM solves the soft-margin dual optimization problem:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>Maximize &sum;<sub>i=1</sub><sup>n</sup> &alpha;<sub>i</sub> &minus; &frac12; &sum;<sub>i=1</sub><sup>n</sup> &sum;<sub>j=1</sub><sup>n</sup> &alpha;<sub>i</sub> &alpha;<sub>j</sub> y<sub>i</sub> y<sub>j</sub> K(x<sub>i</sub>, x<sub>j</sub>)</i>", styles['EquationText']))
    story.append(Paragraph("<i>subject to: 0 &le; &alpha;<sub>i</sub> &le; C &nbsp;&nbsp; and &nbsp;&nbsp; &sum;<sub>i=1</sub><sup>n</sup> &alpha;<sub>i</sub> y<sub>i</sub> = 0</i>", styles['EquationText']))
    story.append(Paragraph(
        "where K(x<sub>i</sub>, x<sub>j</sub>) is the Radial Basis Function (RBF) kernel defined as:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>K(x<sub>i</sub>, x<sub>j</sub>) = exp( &minus; &gamma; ||x<sub>i</sub> &minus; x<sub>j</sub>||<sup>2</sup> )</i>", styles['EquationText']))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>4. Multi-Layer Perceptron (Forward Propagation and Cross-Entropy Loss):</b>", styles['SubSectionHeading']))
    story.append(Paragraph(
        "Our neural network utilizes an input layer (16 or 15 neurons), two hidden layers with ReLU activations, and a sigmoid output neuron. "
        "Forward propagation at layer l is governed by:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>z<sup>[l]</sup> = W<sup>[l]</sup> a<sup>[l-1]</sup> + b<sup>[l]</sup> &nbsp;&nbsp;;&nbsp;&nbsp; a<sup>[l]</sup> = ReLU(z<sup>[l]</sup>) = max(0, z<sup>[l]</sup>)</i>", styles['EquationText']))
    story.append(Paragraph(
        "The model weights are updated via backpropagation minimizing the binary cross-entropy loss:",
        styles['BodyContent']
    ))
    story.append(Paragraph("<i>L(y, y&#770;) = &minus; [ y &middot; ln(y&#770;) + (1 &minus; y) &middot; ln(1 &minus; y&#770;) ]</i>", styles['EquationText']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 6.5: FRONTEND HUD IMPLEMENTATION
    # =========================================================================
    story.append(PageMarker('S6_5'))
    story.append(Paragraph("6.5 Frontend HUD Implementation", styles['SectionHeading']))
    story.append(Paragraph(
        "The user interface was constructed using React 18 and styled with Tailwind CSS to deliver an immersive cyberpunk terminal aesthetic. "
        "Key interface components include:",
        styles['BodyContent']
    ))
    frontend_comps = [
        "<b>Circular Threat Gauge (SVG):</b> Dynamically animates a circular radial progress ring representing the confidence score from 0% to 100%. Color transitions smoothly from Emerald Green (#10B981) for benign artifacts to Warning Amber (#F59E0B) and Crimson Red (#EF4444) for confirmed threats.",
        "<b>Model Selector Switcher:</b> An interactive dropdown menu that issues asynchronous PATCH requests to /api/v1/models/switch, updating the active model badge in real time.",
        "<b>Live Telemetry Feed:</b> A responsive data table that polls recent scan transactions, displaying truncated artifact identifiers, timestamps, active model tags, and latency indicators.",
        "<b>Indicator Breakdown Cards:</b> Expands upon scan completion to highlight the top three risk factors (e.g., 'IP Address in Hostname Detected', 'SMS Interception Permission Requested')."
    ]
    for fc in frontend_comps:
        story.append(Paragraph(f"• {fc}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 6.6: CORE ALGORITHMIC PSEUDOCODE
    # =========================================================================
    story.append(PageMarker('S6_6'))
    story.append(Paragraph("6.6 Core Algorithmic Pseudocode", styles['SectionHeading']))
    story.append(Paragraph(
        "The following structured pseudocode algorithms specify the execution logic for our feature extraction and dual-persistence engines:",
        styles['BodyContent']
    ))

    algo1_code = (
        "<b>Algorithm 6.1: Lexical URL Feature Extraction Pipeline</b><br/>"
        "<b>Input:</b> raw_url (string)<br/>"
        "<b>Output:</b> feature_vector (array of 16 float values)<br/>"
        "1:&nbsp;&nbsp;parsed = parse_url_components(raw_url)<br/>"
        "2:&nbsp;&nbsp;vec[0] &larr; length(raw_url); &nbsp;vec[1] &larr; length(parsed.domain); &nbsp;vec[2] &larr; length(parsed.path)<br/>"
        "3:&nbsp;&nbsp;vec[3] &larr; count_occurrences(raw_url, '.')<br/>"
        "4:&nbsp;&nbsp;vec[4] &larr; count_occurrences(raw_url, '-')<br/>"
        "5:&nbsp;&nbsp;vec[5] &larr; count_occurrences(raw_url, '@')<br/>"
        "6:&nbsp;&nbsp;vec[6] &larr; count_occurrences(raw_url, '?')<br/>"
        "7:&nbsp;&nbsp;vec[7] &larr; count_occurrences(raw_url, '=')<br/>"
        "8:&nbsp;&nbsp;vec[8] &larr; count_occurrences(raw_url, '_')<br/>"
        "9:&nbsp;&nbsp;vec[9] &larr; (1 if matches_ipv4_regex(parsed.domain) else 0)<br/>"
        "10: vec[10] &larr; (1 if parsed.scheme == 'https' else 0)<br/>"
        "11: vec[11] &larr; compute_shannon_entropy(parsed.domain)<br/>"
        "12: vec[12] &larr; count_digits(raw_url) / max(1, length(raw_url))<br/>"
        "13: vec[13] &larr; check_keywords(raw_url, ['login', 'verify', 'bank', 'secure', 'update'])<br/>"
        "14: vec[14] &larr; count_subdomains(parsed.domain)<br/>"
        "15: vec[15] &larr; (1 if contains_punycode_or_idn(parsed.domain) else 0)<br/>"
        "16: <b>return</b> normalize_features(vec)"
    )
    story.append(Paragraph(algo1_code, styles['CodeSnippet']))
    story.append(Spacer(1, 4))

    algo2_code = (
        "<b>Algorithm 6.2: Resilient Dual-Database Telemetry Persist & Failover</b><br/>"
        "<b>Input:</b> telemetry_record (dict)<br/>"
        "<b>Output:</b> status (boolean: success or fail)<br/>"
        "1:&nbsp;&nbsp;<b>try:</b><br/>"
        "2:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mongo_client = get_mongo_connection_pool()<br/>"
        "3:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = await mongo_client.threat_db.scans.insert_one(telemetry_record, timeout=2.0)<br/>"
        "4:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>return</b> True<br/>"
        "5:&nbsp;&nbsp;<b>except</b> (ServerSelectionTimeoutError, ConnectionFailure) <b>as</b> err:<br/>"
        "6:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log_warning(\"MongoDB unreachable. Triggering SQLite failover...\")<br/>"
        "7:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sqlite_conn = open_sqlite_connection(\"cyberguard_fallback.db\")<br/>"
        "8:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;execute_insert_query(sqlite_conn, telemetry_record, synced_to_cloud=False)<br/>"
        "9:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sqlite_conn.commit()<br/>"
        "10:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;schedule_background_cloud_sync_task()<br/>"
        "11:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>return</b> True"
    )
    story.append(Paragraph(algo2_code, styles['CodeSnippet']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 6.7: SUMMARY
    # =========================================================================
    story.append(PageMarker('S6_7'))
    story.append(Paragraph("6.7 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 6 presented the complete software realization of CyberGuard across backend microservices, feature extraction engines, "
        "mathematical classification formulations, reactive frontend interfaces, and core algorithms. By combining asynchronous FastAPI "
        "concurrency with dual database resilience and lightweight static parsing, the implementation fulfills all functional and "
        "non-functional design requirements.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    return story
