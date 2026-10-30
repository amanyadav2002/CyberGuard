import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from report_builder.styles_and_canvas import PageMarker

def get_ch1_and_ch2_story(styles):
    story = []

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    story.append(PageMarker('CH1'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 1", styles['ChapterTitle']))
    story.append(Paragraph("INTRODUCTION", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S1_1'))
    story.append(Paragraph("1.1 Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "In modern computing environments, the rapid expansion of interconnected digital services has brought unprecedented "
        "convenience while simultaneously expanding the attack surface exposed to malicious cyber adversaries. Among the broad spectrum "
        "of contemporary cyber threats, two attack vectors stand out as exceptionally destructive and prevalent: fraudulent phishing "
        "web addresses and weaponized mobile Android application packages (APKs). Attackers routinely weaponize deceptive domain names "
        "and obfuscated mobile executables to deceive unsuspecting users, bypass traditional signature-based security controls, and "
        "exfiltrate sensitive personal, financial, and organizational data.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "Phishing attacks have evolved far beyond crude email hoaxes with misspelled domain names. Modern phishing operations leverage "
        "automated domain generation algorithms (DGAs), homograph attacks using internationalized domain names (IDN), multi-tiered URL "
        "shortening services, and rapid-flux DNS networks to create ephemeral attack links that often live for less than two hours. "
        "By the time a centralized security vendor identifies a fraudulent link and broadcasts an updated blacklist, hundreds or thousands "
        "of enterprise users and everyday consumers may have already fallen victim to credential harvesting or session hijacking.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "Simultaneously, the Android operating system commands over seventy percent of the worldwide mobile operating system market share. "
        "Because Android allows users to sideload applications from third-party application stores and arbitrary web links, cybercriminals "
        "frequently repackage legitimate applications with malicious payloads such as banking trojans, SMS forwarders, ransomware, and "
        "covert spyware. Once installed on a victim's smartphone, these malicious packages abuse Android permissions, intercept one-time "
        "passwords (OTPs), record ambient audio, and establish persistent command-and-control (C2) communication channels.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "To address these critical security vulnerabilities, our student engineering team designed and developed <b>CyberGuard</b>—a "
        "unified, high-performance cybersecurity threat intelligence and triage platform powered by advanced machine learning classifiers. "
        "CyberGuard bridges the gap between slow, resource-heavy dynamic sandbox environments and brittle signature blacklists by performing "
        "instantaneous static heuristic inspection on both suspicious web links and Android APK binaries.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_2'))
    story.append(Paragraph("1.2 Objectives", styles['SectionHeading']))
    story.append(Paragraph(
        "The primary objective of this project is to research, design, implement, and validate an intelligent, multi-model cybersecurity "
        "platform capable of detecting phishing URLs and malicious Android applications with high accuracy and sub-second execution speed. "
        "Our work focuses on achieving the following concrete technical goals:",
        styles['BodyContent']
    ))
    objectives = [
        "<b>Comprehensive Static Feature Engineering:</b> To engineer a high-speed lexical feature extraction engine for URLs capable of extracting syntactic densities, security indicators, and keyword anomalies, as well as an Androguard-based static bytecode analyzer capable of extracting requested permissions, declared intent filters, and suspicious background services without executing untrusted code.",
        "<b>Multi-Model Machine Learning Zoo:</b> To train, calibrate, and deploy a suite of six supervised learning algorithms—Random Forest, XGBoost, Support Vector Machines (SVM), Decision Trees, Logistic Regression, and Multi-Layer Perceptron (MLP) Neural Networks—enabling granular performance benchmarking and adaptive classification.",
        "<b>Dynamic Model Switching Mechanism:</b> To design and implement a thread-safe singleton Model Manager architecture within a FastAPI backend that allows security operators to switch between different detection models at runtime without restarting the server or dropping active connections.",
        "<b>Fault-Tolerant Dual-Persistence Engine:</b> To implement a hybrid database architecture that leverages MongoDB for scalable, schema-less threat telemetry and audit logging while seamlessly falling back to a local SQLite database during network interruptions or database outages.",
        "<b>Interactive Cyberpunk Telemetry HUD:</b> To design and build an intuitive, high-visibility web user interface featuring real-time risk gauges, comparative model matrices, telemetry search filters, and actionable security recommendations for incident response teams.",
        "<b>Empirical Verification and Validation:</b> To rigorously validate detection performance against standardized benchmark datasets (including PhishTank, Alexa Top 1M, and Drebin Android malware samples), ensuring high detection rates (F1 > 96%) while keeping inference latency strictly below 50 milliseconds."
    ]
    for obj in objectives:
        story.append(Paragraph(f"• {obj}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_3'))
    story.append(Paragraph("1.3 Scope of the Project", styles['SectionHeading']))
    story.append(Paragraph(
        "The scope of the CyberGuard project encompasses the complete end-to-end design, software implementation, and empirical evaluation "
        "of a multi-tiered cyber threat classification system. The project specifically covers:",
        styles['BodyContent']
    ))
    scope_points = [
        "<b>Input Processing:</b> Ingestion of arbitrary URL strings via REST endpoints or web form inputs, as well as binary file upload of Android APK packages up to 100 megabytes in size.",
        "<b>Static Bytecode & Lexical Analysis:</b> Decompilation and parsing of Android Manifest files, DEX bytecode structure, and URI syntactical structures entirely in memory without requiring target emulation or virtualized sandboxes.",
        "<b>Feature Transformation:</b> Converting raw syntactic properties into standardized numeric feature vectors compatible with scikit-learn and XGBoost inference pipelines.",
        "<b>Classification & Probability Scoring:</b> Producing binary verdicts (Malicious vs. Benign) accompanied by normalized confidence probabilities and human-readable risk indicators.",
        "<b>Audit Trail & Analytics:</b> Real-time persistence of threat telemetry, scanning history, model inference latency metrics, and user management records.",
        "<b>Delimitations:</b> The project explicitly focuses on static pre-execution analysis. Dynamic run-time instrumentation, sandbox hypervisor emulation, and hardware-assisted kernel debugging are outside the primary scope of this platform, ensuring minimal computational overhead and instant response times."
    ]
    for sp in scope_points:
        story.append(Paragraph(f"• {sp}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_4'))
    story.append(Paragraph("1.4 Applications", styles['SectionHeading']))
    story.append(Paragraph(
        "CyberGuard has been developed with practical applicability across diverse operational security environments:",
        styles['BodyContent']
    ))
    applications = [
        "<b>Enterprise Security Operations Centers (SOC):</b> Frontline triage tool for security analysts to quickly evaluate suspicious URLs reported in employee phishing tickets and assess sideloaded APKs detected on corporate mobile devices.",
        "<b>Third-Party Mobile App Store Vetting:</b> Automated pre-ingestion screening pipeline for app repositories to detect trojanized or repackaged malware before public distribution.",
        "<b>Network Edge and Proxy Filtering:</b> Integration into DNS resolvers and secure web gateways to perform zero-delay threat classification on outbound web traffic.",
        "<b>Educational and Research Laboratories:</b> Practical platform for academic cybersecurity research, enabling students and researchers to benchmark novel ML algorithms against standardized threat corpora."
    ]
    for app in applications:
        story.append(Paragraph(f"• {app}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_5'))
    story.append(Paragraph("1.5 Organization of Report", styles['SectionHeading']))
    story.append(Paragraph(
        "This project report is structured into nine sequential chapters adhering to academic report guidelines:",
        styles['BodyContent']
    ))
    org_points = [
        "<b>Chapter 1 — Introduction:</b> Outlines the project context, technical objectives, system scope, and operational applications.",
        "<b>Chapter 2 — Problem Identification:</b> Analyzes the fundamental limitations of existing signature-based blacklists and dynamic sandboxes, presenting the proposed CyberGuard approach.",
        "<b>Chapter 3 — Literature Review:</b> Provides a comprehensive critical survey of twenty peer-reviewed research papers from the project presentation, a comparative taxonomy of attack indicators, and identified research gaps.",
        "<b>Chapter 4 — System Requirements:</b> Formulates detailed functional requirements (FR-01 to FR-08), non-functional quality attributes, and minimum hardware/software specifications.",
        "<b>Chapter 5 — System Design:</b> Details high-level architecture, module decomposition, UML diagrams (Use Case, Sequence, Class, Activity), Data Flow Diagrams (Level 0 and 1), Database schema, and execution flowcharts.",
        "<b>Chapter 6 — System Implementation:</b> Presents the development environment, file directory structure, core module walkthroughs, mathematical ML formulations, and core algorithms.",
        "<b>Chapter 7 — System Testing:</b> Documents verification and validation methodologies, a comprehensive test suite of twenty test cases (TC-01 to TC-20), and a traceability matrix.",
        "<b>Chapter 8 — Results and Discussion:</b> Illustrates UI snapshots, ML performance benchmarks, latency profiling, ROC curves, confusion matrices, and comparative evaluations.",
        "<b>Chapter 9 — Conclusion and Future Scope:</b> Concludes the report with key engineering achievements, limitations encountered, and prospective future enhancements."
    ]
    for op in org_points:
        story.append(Paragraph(f"• {op}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S1_6'))
    story.append(Paragraph("1.6 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 1 established the overarching necessity for modernizing cyber threat intelligence through automated machine learning. "
        "It defined the project scope, highlighted six core technical objectives, and outlined the structural roadmap for this document.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: PROBLEM IDENTIFICATION
    # =========================================================================
    story.append(PageMarker('CH2'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 2", styles['ChapterTitle']))
    story.append(Paragraph("PROBLEM IDENTIFICATION", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S2_1'))
    story.append(Paragraph("2.1 Problem Overview", styles['SectionHeading']))
    story.append(Paragraph(
        "The digital threat landscape is defined by an asymmetrical relationship between cyber defenders and attackers. "
        "Adversaries need only discover a single unpatched vulnerability or craft a convincing deceptive link to breach an organization, "
        "whereas security teams must protect all entry points continuously. Modern phishing and mobile malware attacks capitalize "
        "on this asymmetry by employing rapid variation and obfuscation techniques that render conventional security mechanisms ineffective.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "In the domain of web threat detection, attackers routinely register disposable top-level domains (such as .xyz, .top, .tk) "
        "and deploy automated kits that clone legitimate banking or corporate authentication portals. These portals often remain online "
        "for only a few hours—sufficient time to harvest hundreds of credentials—before the domain DNS records are purged and pointed "
        "elsewhere. This ephemeral attack lifecycle creates a critical detection blind spot for conventional security feeds.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "In the mobile ecosystem, malicious actors actively repackage legitimate applications by injecting trojanized DEX bytecode "
        "or malicious background services. These applications bypass superficial app store scanners by deferring payload execution, "
        "monitoring device sensors to verify human interaction, and disguising dangerous permissions under benign utility names. "
        "There is an urgent engineering need for a localized, high-speed triage platform that can evaluate structural threat signatures "
        "in real time without relying on external cloud lookups or heavy emulation sandboxes.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S2_2'))
    story.append(Paragraph("2.2 Existing System", styles['SectionHeading']))
    story.append(Paragraph(
        "Contemporary cybersecurity defenses typically rely on two established operational paradigms: centralized signature blacklists "
        "and dynamic sandbox virtual machines.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "<b>1. Centralized Signature Blacklisting:</b> Platforms such as Google Safe Browsing, PhishTank, and commercial antivirus feeds "
        "maintain global repositories of known malicious URLs, domain names, and cryptographic file hashes (MD5, SHA-256). When a user requests "
        "a web link or downloads an APK, the client computes its hash or queries its domain against the remote blacklist. If a match is found, "
        "the transaction is blocked.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "<b>2. Dynamic Sandbox Virtualization:</b> Systems such as Cuckoo Sandbox or enterprise malware detonation chambers execute "
        "suspicious APKs or open URLs inside isolated virtual machine environments. The sandbox monitors system calls, network sockets, "
        "process creation, and file system modifications over an observation window ranging from three to fifteen minutes to detect hostile behavior.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S2_2_1'))
    story.append(Paragraph("2.2.1 Drawbacks of Existing System", styles['SubSectionHeading']))
    story.append(Paragraph(
        "While both traditional approaches provide value, they exhibit fundamental operational and architectural limitations when "
        "confronted with modern, high-volume threats:",
        styles['BodyContent']
    ))
    drawbacks = [
        "<b>Zero-Day Vulnerability:</b> Signature blacklists are fundamentally reactive. A malicious link or APK can only be blacklisted after it has already compromised a victim and been manually reported, verified, and propagated. During this latency window (often 12 to 48 hours), all zero-day threats pass undetected.",
        "<b>Trivial Signature Evasion:</b> Attackers evade cryptographic hash matching effortlessly by changing a single comment in an APK, recompiling code, or altering non-functional URL query parameters. This changes the SHA-256 hash completely while preserving malicious payload logic.",
        "<b>Prohibitive Execution Latency:</b> Dynamic sandbox execution requires several minutes per sample to spin up virtual machines, execute the application, simulate user interaction, and analyze log traces. This latency is unacceptable for real-time web browsing, instant messaging triage, or high-throughput SOC monitoring.",
        "<b>Sandbox Evasion Tactics:</b> Advanced mobile malware easily detects virtualized execution environments by checking system properties (such as QEMU drivers, zero battery drain rate, absence of contact lists, or sensor stillness) and sleeps quietly during analysis, revealing malicious intent only when installed on physical consumer devices.",
        "<b>High Infrastructure and Operational Cost:</b> Maintaining hypervisor clusters for dynamic detonation requires substantial CPU, GPU, and RAM resources, making dynamic sandboxes cost-prohibitive for small organizations and edge deployments."
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
    story.append(Spacer(1, 4))

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

    return story
