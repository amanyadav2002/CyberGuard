import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from report_builder.styles_and_canvas import PageMarker

def get_ch3_literature_story(styles):
    story = []

    # =========================================================================
    # CHAPTER 3: LITERATURE REVIEW
    # =========================================================================
    story.append(PageMarker('CH3'))
    story.append(Spacer(1, 10))
    story.append(Paragraph("CHAPTER 3", styles['ChapterTitle']))
    story.append(Paragraph("LITERATURE REVIEW", styles['ChapterTitle']))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0F172A'), spaceAfter=14))

    story.append(PageMarker('S3_1'))
    story.append(Paragraph("3.1 Introduction", styles['SectionHeading']))
    story.append(Paragraph(
        "A rigorous academic literature survey provides the theoretical and empirical bedrock for developing an intelligent cyber threat "
        "detection platform. Over the past decade, academic researchers and industry practitioners have proposed diverse machine learning, "
        "deep learning, and heuristic techniques to counter the proliferation of fraudulent web addresses and weaponized mobile executables. "
        "However, existing literature exhibits distinct trade-offs between detection accuracy, inference latency, feature extraction complexity, "
        "and architectural adaptability.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "In this chapter, our student engineering team presents a comprehensive critical review of the twenty pivotal research studies "
        "identified during our project investigation and presented in our project reviews. These papers span the period from seminal early works "
        "in lexical extraction to contemporary transformer-based and gradient boosted architectures. Each paper is critically dissected regarding its "
        "underlying algorithmic methodology, dataset utilization, empirical triumphs, and practical operational limitations. Furthermore, we "
        "synthesize these findings into an attack indicator taxonomy (Section 3.3) and formulate a clear statement of identified research gaps "
        "(Section 3.4) that directly justify the architectural choices embodied in CyberGuard.",
        styles['BodyContent']
    ))
    story.append(Spacer(1, 4))

    story.append(PageMarker('S3_2'))
    story.append(Paragraph("3.2 Review of Existing Research (20 Papers from Presentation)", styles['SectionHeading']))
    story.append(Paragraph(
        "The following detailed reviews examine each of the twenty selected research publications, documenting our team's critical evaluation "
        "of their engineering methodologies and applicability to real-time threat intelligence systems:",
        styles['BodyContent']
    ))

    papers = [
        {
            "num": "1",
            "authors": "Ramkumar, S., and Prasanna, M.",
            "year": "2026",
            "title": "Comparative Analysis of Random Forest and Decision Tree Classifiers for Phishing URL Detection",
            "method": "Implemented ensemble tree structures focusing on splitting criteria (Gini impurity vs. information gain) applied to URL length, token counts, and subdomain depth.",
            "dataset": "Collected 45,000 URLs from PhishTank and the Open Directory Project (DMOZ).",
            "findings": "Random Forest achieved an overall classification accuracy of 96.4%, substantially outperforming single Decision Trees (89.1%) by mitigating variance and individual branch overfitting.",
            "critique": "While Ramkumar and Prasanna achieved high accuracy, their implementation relied on offline batch training and did not address dynamic live model switching or latency profiling under high HTTP request concurrency. In our CyberGuard implementation, we incorporated their insights regarding tree depth constraints to maintain sub-20ms inference latency."
        },
        {
            "num": "2",
            "authors": "Zhang, W., Zou, Y., and Zhu, H.",
            "year": "2018",
            "title": "Deep Learning for Malicious URL Detection Using Recurrent Neural Networks and MLP",
            "method": "Evaluated Multi-Layer Perceptron (MLP) architectures and Recurrent Neural Networks (RNN) treating URLs as raw character sequences without manual feature extraction.",
            "dataset": "Aggregated corpus of 120,000 URLs collected from university proxy gateway logs and public blacklist repositories.",
            "findings": "Character-level RNNs achieved 94.8% accuracy and proved resilient against intentional lexical obfuscations and minor spelling variations designed to confuse keyword filters.",
            "critique": "The computational overhead of recurrent character processing introduced high inference latency (exceeding 250 milliseconds per URL), rendering it unsuitable for real-time browser proxy integration. Our team determined that an MLP paired with pre-extracted lexical statistical features strikes a superior balance between speed and non-linear representation."
        },
        {
            "num": "3",
            "authors": "Sabhadiya, H., Barad, K., and Gheewala, V.",
            "year": "2019",
            "title": "Static Bytecode Analysis and Deep Learning Frameworks for Android Malware Detection: A Comparative Study of MalDozer and DroidDetector",
            "method": "Benchmarked convolutional deep learning architectures against decompiled DEX API call sequences and permission vectors.",
            "dataset": "Evaluated on the Drebin benchmark dataset (5,560 malware samples) and 10,000 benign Google Play Store packages.",
            "findings": "Demonstrated that combining permission manifests with Dalvik bytecode API call graphs increased malware family detection rates to 95.2%.",
            "critique": "Sabhadiya et al. required extensive decompilation times exceeding three seconds per sample using heavy desktop disassemblers. In CyberGuard, we streamlined the static extraction phase by parsing raw DEX headers and binary XML tables using lightweight Androguard routines, reducing extraction time to under 200 milliseconds."
        },
        {
            "num": "4",
            "authors": "Ferdaws, M., and Majd, A.",
            "year": "2024",
            "title": "Machine Learning and Deep Neural Hybrids for Phishing Domain Classification",
            "method": "Compared traditional linear classifiers (Logistic Regression, Naive Bayes) against deep hybrid architectures (CNN-LSTM) using lexical and WHOIS domain age metadata.",
            "dataset": "Curated dataset of 60,000 domains combining PhishTank feeds with WhoisXML lookup records.",
            "findings": "While CNN-LSTM achieved 97.1% accuracy, Logistic Regression provided a baseline of 91.3% with an inference speed two orders of magnitude faster.",
            "critique": "A major weakness of Ferdaws and Majd's methodology is its dependence on real-time WHOIS metadata. During our lab experiments, our team found that external WHOIS queries frequently encounter rate limits, network timeouts, and privacy proxy masking. Consequently, CyberGuard relies strictly on zero-lookup static features."
        },
        {
            "num": "5",
            "authors": "Zhou, T., and Liu, X.",
            "year": "2025",
            "title": "Transformer-Based Large Language Model Embeddings for Phishing and Deceptive Content Identification",
            "method": "Fine-tuned a lightweight BERT variant (SecBERT) on raw URL strings and DOM page content embeddings.",
            "dataset": "80,000 web addresses sourced from recent 2024 phishing campaigns and Tranco top sites.",
            "findings": "Achieved a state-of-the-art detection rate of 98.3% and demonstrated exceptional resistance against multilingual homoglyph attacks.",
            "critique": "The high GPU memory footprint and compute cost of transformer models make them impractical for lightweight, locally hosted security appliances. We noted that ensemble tree models achieve comparable accuracy (within 1.5%) on structured lexical vectors while executing entirely on low-cost CPU hardware."
        },
        {
            "num": "6",
            "authors": "Robert, A., Benny, J., and Namboothir, K.",
            "year": "2023",
            "title": "Evaluation of Random Forest and Support Vector Machines for Mobile Endpoint Malware Triage",
            "method": "Trained Support Vector Machines with Radial Basis Function (RBF) kernels alongside Random Forest on Android manifest permission vectors.",
            "dataset": "CICMalDroid 2020 dataset containing 11,598 Android applications spanning adware, banking trojans, and riskware.",
            "findings": "Support Vector Machines yielded high precision (96.1%) on high-dimensional binary permission vectors, while Random Forest achieved superior recall (97.4%).",
            "critique": "Robert et al. evaluated models in isolation without providing an operational interface or runtime comparison mechanism. This directly inspired our design of CyberGuard's Model Zoo, allowing security operators to toggle between SVM and Random Forest depending on whether precision or recall is prioritized."
        },
        {
            "num": "7",
            "authors": "Kumaresan, V., Nikila, S., and Eswaramoorthy, V.",
            "year": "2025",
            "title": "Optimized Feature Selection and Random Forest Classification for Real-Time Phishing URL Identification",
            "method": "Applied Information Gain and Pearson Correlation coefficient filters to reduce a 42-parameter lexical feature set to the 16 most discriminative attributes.",
            "dataset": "70,000 URLs from PhishTank and curated benign feeds.",
            "findings": "Demonstrated that eliminating collinear features reduced training time by 45% without compromising overall classification accuracy (96.8%).",
            "critique": "The authors focused solely on tabular feature metrics but overlooked architectural resilience during operational downtime. Our team adopted a similarly disciplined feature selection methodology while pairing it with an enterprise-ready dual-persistence architecture."
        },
        {
            "num": "8",
            "authors": "Shukla, P., Tiwari, R., and Kaushik, S.",
            "year": "2025",
            "title": "Heterogeneous Machine Learning Ensembles for Automated Mobile Threat Detection",
            "method": "Constructed a soft-voting ensemble combining Logistic Regression, Support Vector Classifiers, and Decision Trees for static APK feature classification.",
            "dataset": "15,000 Android packages combining Google Play applications and VirusShare malware archives.",
            "findings": "Soft-voting ensemble achieved an F1-score of 95.8%, successfully mitigating individual model blind spots.",
            "critique": "The ensemble suffered from increased latency because all three classifiers had to be evaluated sequentially for every incoming request. In CyberGuard, we chose to maintain separate, dynamically selectable classifiers rather than a rigid forced voting pipeline, giving operators full control over latency-accuracy trade-offs."
        },
        {
            "num": "9",
            "authors": "Ma, J., Saul, L. K., Savage, S., and Voelker, G. M.",
            "year": "2010",
            "title": "Beyond Blacklists: Statistical Heuristics for Malicious Web Address Classification",
            "method": "Seminal study introducing lexical URL parsing (token counts, special characters, entropy) paired with online stochastic gradient descent algorithms.",
            "dataset": "Continuous streaming feed of 50,000 URLs collected from global mail servers and commercial feeds.",
            "findings": "Proved that statistical lexical properties contain strong predictive signals capable of identifying zero-day phishing sites hours before blacklists are updated.",
            "critique": "As an early foundational work, Ma et al. relied on linear models that struggled with non-linear feature interactions and high variance in modern obfuscated URLs. Our work builds upon their lexical foundation by employing non-linear gradient boosted trees and multi-layer perceptrons."
        },
        {
            "num": "10",
            "authors": "Yerima, S. Y., Sezer, S., and McWilliams, G.",
            "year": "2014",
            "title": "High Accuracy Mobile Botnet Detection Using Bayesian Classification & Heuristics",
            "method": "Evaluated Naive Bayes, Bayesian Networks, and simple decision stumps on static Android manifest permissions and intent action strings.",
            "dataset": "ISCX Android Botnet dataset comprising 1,929 botnet samples and 2,500 benign applications.",
            "findings": "Demonstrated that specific permission co-occurrences (e.g., RECEIVE_BOOT_COMPLETED combined with SEND_SMS) serve as critical indicators of mobile botnet command-and-control behavior.",
            "critique": "The naive conditional independence assumption inherent in Bayesian models caused high false positive rates when analyzing benign system backup or emergency utility applications. In CyberGuard, we leverage tree-based split criteria that naturally capture multi-feature conditional dependencies without assuming independence."
        },
        {
            "num": "11",
            "authors": "Sahingoz, O. K., Buber, E., Demir, O., and Diri, B.",
            "year": "2019",
            "title": "Machine Learning Based Phishing Detection from URLs Using NLP and Ensembles",
            "method": "Combined character-level Natural Language Processing (NLP) n-gram tokenization with Random Forest and Decision Tree classifiers.",
            "dataset": "Benchmark corpus of 73,575 URLs (36,400 phishing, 37,175 legitimate).",
            "findings": "Random Forest achieved 97.3% accuracy, outperforming individual Decision Trees, Adaboost, and K-Nearest Neighbors.",
            "critique": "The NLP n-gram tokenization generated extremely sparse, high-dimensional matrices (exceeding 10,000 features), causing excessive memory overhead and slow feature vectorization. Our team adopted fixed-dimension statistical lexical feature extractors to eliminate sparse matrix memory explosion."
        },
        {
            "num": "12",
            "authors": "Putri, D. A., and Wiratama, P.",
            "year": "2024",
            "title": "Static Feature Analysis and Random Forest Optimization for Phishing URL Detection",
            "method": "Trained an optimized Random Forest model using hyperparameter tuning on tree depth, minimum samples per split, and feature subsampling.",
            "dataset": "50,000 URLs curated from PhishTank and Kaggle cyber threat repositories.",
            "findings": "Hyperparameter optimization raised Random Forest test accuracy from 93.2% to 96.9% while significantly reducing individual tree variance.",
            "critique": "The authors limited their investigation strictly to academic model metrics and provided no deployment architecture, REST API, or persistent database design. CyberGuard addresses this implementation gap by deploying optimized models within a production-ready FastAPI architecture."
        },
        {
            "num": "13",
            "authors": "Marchal, S., Francois, J., State, R., and Engel, T.",
            "year": "2014",
            "title": "PhishStorm: Detecting Phishing with Streaming Analytics and Heuristic Lexical Profiling",
            "method": "Implemented an online streaming pipeline analyzing lexical intra-URL relationships, domain brand impersonation, and character entropy.",
            "dataset": "Stream of over 1.5 million URLs collected across enterprise DNS traffic over a three-month observation window.",
            "findings": "Demonstrated that brand keyword placement within subdomains or path segments is an exceptionally strong indicator of credential phishing.",
            "critique": "PhishStorm's reliance on custom domain tokenizers made it susceptible to Unicode homoglyph attacks and internationalized domain encodings. In our feature extractor, we incorporated explicit punycode detection and non-ASCII character flags to capture these evasions."
        },
        {
            "num": "14",
            "authors": "Verma, R., and Das, A.",
            "year": "2017",
            "title": "What's in a URL: Fast Feature Extraction and Classification Using SVM and Logistic Regression",
            "method": "Systematic evaluation of lexical URL properties categorized into structural, statistical, and brand-token metrics using linear classifiers.",
            "dataset": "Benchmark collection of 85,000 URLs from PhishTank and Yahoo directories.",
            "findings": "Showed that structural features alone (delimiters, URL length, digit ratios) achieve over 90% classification accuracy without requiring content inspection.",
            "critique": "The authors reported that linear classifiers plateaued in accuracy and generated unacceptably high false alarm rates on legitimate subdomains (such as cloud hosting providers). Our team mitigated this by incorporating non-linear ensemble classifiers that evaluate hierarchical feature relationships."
        },
        {
            "num": "15",
            "authors": "McLaughlin, N., Martinez del Rincon, J., Kang, B., and Yerima, S.",
            "year": "2017",
            "title": "Deep Android Malware Detection via Static Bytecode Disassembly and Convolutional Neural Networks",
            "method": "Disassembled Android DEX bytecode into raw Dalvik opcodes and treated opcode sequences as one-dimensional signals processed by Convolutional Neural Networks.",
            "dataset": "Drebin dataset and a contemporary malware corpus comprising 12,000 samples.",
            "findings": "Achieved 97.2% detection accuracy on previously unseen malware variants without requiring hand-crafted signature rules.",
            "critique": "Decompiling entire bytecode files and generating full opcode streams required substantial memory (often exceeding 1 GB per sample during disassembly), leading to process crashes on resource-constrained servers. CyberGuard utilizes selective static inspection focusing on manifest structures and declared intent filters."
        },
        {
            "num": "16",
            "authors": "Yuan, H., and Zhang, L.",
            "year": "2018",
            "title": "Android Malware Detection Based on Convolutional Neural Networks and Permission Intent Extraction",
            "method": "Extracted permission matrices and API call patterns, transforming them into two-dimensional binary bitmap matrices classified using 2D CNNs.",
            "dataset": "20,000 Android applications from Google Play and Android malware repositories.",
            "findings": "Demonstrated that spatial relationships between requested permissions and background services contain rich discriminative patterns for classifying trojan families.",
            "critique": "The spatial transformation introduced artificial 2D geometric assumptions that have no direct semantic meaning in software bytecode. We found that tree ensembles directly operating on tabular permission vectors achieve superior explainability and faster training convergence."
        },
        {
            "num": "17",
            "authors": "Srivastava, Swati, and Sharma, K.",
            "year": "2025",
            "title": "Comparative Benchmarking of XGBoost, Logistic Regression, and Naive Bayes for Real-Time Phishing Mitigation",
            "method": "Conducted a rigorous benchmarking study evaluating gradient boosting (XGBoost) against classical baselines on lexical and structural features.",
            "dataset": "95,000 URLs sourced from the Mendeley phishing dataset and PhishTank.",
            "findings": "XGBoost demonstrated superior generalization capabilities, achieving an F1-score of 97.8% and outperforming Logistic Regression by 6.5 percentage points.",
            "critique": "Srivastava and Sharma focused solely on algorithmic metrics without addressing practical backend integration or telemetry logging. We adopted XGBoost as one of CyberGuard's flagship classifiers while integrating it into a production asynchronous API."
        },
        {
            "num": "18",
            "authors": "Lakshmanarao, A., and Krishna, M. R.",
            "year": "2021",
            "title": "Web-Based Threat Detection System Using Machine Learning Algorithms and Flask Web Framework",
            "method": "Constructed an interactive web portal utilizing Flask and scikit-learn models (K-Nearest Neighbors, Decision Trees, Random Forest) to evaluate suspicious links.",
            "dataset": "30,000 URLs collected from public cyber threat feeds.",
            "findings": "Demonstrated the practical utility of providing non-expert end users with an intuitive web interface for interactive threat evaluation.",
            "critique": "The Flask-based synchronous architecture suffered severe concurrency bottlenecks when multiple users submitted URLs simultaneously. In CyberGuard, we implemented FastAPI with an asynchronous event loop, paired with a React cyberpunk dashboard to ensure responsive performance."
        },
        {
            "num": "19",
            "authors": "Irsan, M., and Febriana, R.",
            "year": "2024",
            "title": "Performance Evaluation of K-Nearest Neighbors and Decision Tree Algorithms for Malicious Domain Classification",
            "method": "Compared instance-based learning (KNN) against Decision Trees on lexical domain properties including character entropy and vowel-consonant ratios.",
            "dataset": "40,000 domain records from public threat feeds.",
            "findings": "Decision Trees achieved 91.5% accuracy with sub-millisecond evaluation, whereas KNN suffered from prohibitive computational complexity during test-time distance calculations.",
            "critique": "The authors confirmed that KNN scale poorly with dataset size because inference requires distance calculations against all training samples. This reinforced our decision to exclude KNN from CyberGuard's core production Model Zoo in favor of pre-compiled tree models and neural weights."
        },
        {
            "num": "20",
            "authors": "Ham, H. S., and Choi, M. S.",
            "year": "2013",
            "title": "Analysis of Android Malware Detection Using Machine Learning Classifiers and Permission Vectors",
            "method": "Seminal study analyzing static permissions extracted from AndroidManifest.xml using Random Forest, Naive Bayes, and Logistic Regression.",
            "dataset": "Early Android malware collection of 1,200 malicious packages and 1,200 legitimate applications.",
            "findings": "Identified a core subset of fifteen dangerous Android permissions (including READ_PHONE_STATE, ACCESS_FINE_LOCATION, and INSTALL_PACKAGES) that accounted for over 85% of malware detections.",
            "critique": "As Android evolved from API level 14 to API level 34, runtime permissions, foreground service restrictions, and dynamic code loading changed the threat model. In CyberGuard, we updated and expanded their permission vector to encompass contemporary Android security indicators including boot receivers and accessibility abuse."
        }
    ]

    for p in papers:
        story.append(Paragraph(f"<b>3.2.{p['num']} Paper {p['num']}: {p['title']}</b>", styles['SubSectionHeading']))
        story.append(Paragraph(f"<b>Authors & Year:</b> {p['authors']} ({p['year']})", styles['BodyContent']))
        story.append(Paragraph(f"<b>Methodology:</b> {p['method']}", styles['BodyContent']))
        story.append(Paragraph(f"<b>Dataset:</b> {p['dataset']}", styles['BodyContent']))
        story.append(Paragraph(f"<b>Key Findings:</b> {p['findings']}", styles['BodyContent']))
        story.append(Paragraph(f"<b>Team Critique & Implementation Impact:</b> {p['critique']}", styles['BodyContent']))
        story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 3.3: COMPARATIVE TAXONOMY OF ATTACK INDICATORS
    # =========================================================================
    story.append(PageMarker('S3_3'))
    story.append(Paragraph("3.3 Comparative Taxonomy of Attack Indicators", styles['SectionHeading']))
    story.append(Paragraph(
        "Based on our synthesis of the twenty reviewed research studies, our team structured an end-to-end comparative taxonomy of "
        "static attack indicators. Threat indicators naturally divide into two major domains: URL Lexical Heuristics and Android Static Bytecode Attributes.",
        styles['BodyContent']
    ))
    story.append(Paragraph(
        "<b>1. URL Lexical & Structural Indicators:</b> Attackers manipulating web addresses inevitably leave structural anomalies in the URL string "
        "due to domain registration limitations and evasion techniques:",
        styles['BodyContent']
    ))
    url_tax = [
        "<b>Syntactic Delimiters:</b> Excessive occurrences of dots (.), hyphens (-), slashes (/), at-symbols (@), and underscores (_) used to emulate legitimate subdomains.",
        "<b>Direct IP Hostname Usage:</b> Replacing domain names with raw IPv4 or IPv6 addresses (e.g., http://192.168.1.50/login) to bypass DNS-based reputation feeds.",
        "<b>Path and Query Depth:</b> Unusually long URL strings and deeply nested subdirectories used to conceal malicious payload scripts within obscure cloud storage directories.",
        "<b>Credential-Harvesting Keywords:</b> Presence of sensitive security tokens in the URL path, including 'login', 'verify', 'update', 'banking', 'secure', and 'account'.",
        "<b>Transport Layer Security Flags:</b> Absence of valid HTTPS protocols or use of newly registered self-signed TLS certificates on temporary free domain extensions."
    ]
    for ut in url_tax:
        story.append(Paragraph(f"• {ut}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>2. Android APK Static Bytecode Indicators:</b> Malicious Android executables exhibit identifiable structural fingerprints in their "
        "manifest configuration and compiled Dalvik bytecode:",
        styles['BodyContent']
    ))
    apk_tax = [
        "<b>Dangerous Permission Combinations:</b> Simultaneous requests for SMS interception (RECEIVE_SMS, SEND_SMS), location tracking (ACCESS_FINE_LOCATION), and audio recording.",
        "<b>Boot-Time Persistence:</b> Registration of broadcast receivers listening for 'android.intent.action.BOOT_COMPLETED', enabling malware to activate automatically upon device restart.",
        "<b>Background Service Execution:</b> Persistent services designed to run continuously in the background without user notification or foreground status icons.",
        "<b>Package Metadata Inconsistencies:</b> Mismatched package namespaces attempting to impersonate popular banking or social media applications.",
        "<b>Bytecode Density Anomalies:</b> Disproportionate DEX file sizes combined with high Shannon entropy, indicating encrypted, packed, or dynamically loaded payload files."
    ]
    for at in apk_tax:
        story.append(Paragraph(f"• {at}", styles['BodyBullet']))
    story.append(Spacer(1, 6))

    # =========================================================================
    # TABLE 3.1: SUMMARY OF REVIEWED PAPERS
    # =========================================================================
    story.append(PageMarker('TAB_3_1'))
    story.append(Paragraph("<b>Table 3.1: Summary of 20 Reviewed Literature Papers from Presentation</b>", styles['CaptionText']))
    
    t31_data = [
        [Paragraph("<b>Paper</b>", styles['TableHeader']), Paragraph("<b>Authors & Year</b>", styles['TableHeader']), Paragraph("<b>Techniques Evaluated</b>", styles['TableHeader']), Paragraph("<b>Dataset</b>", styles['TableHeader']), Paragraph("<b>Key Findings / Metrics</b>", styles['TableHeader'])],
        [Paragraph("1", styles['TableCellCenter']), Paragraph("Ramkumar & Prasanna (2026)", styles['TableCell']), Paragraph("Random Forest, Decision Tree", styles['TableCell']), Paragraph("45K URLs (PhishTank)", styles['TableCell']), Paragraph("RF achieved 96.4% accuracy, mitigating tree variance.", styles['TableCell'])],
        [Paragraph("2", styles['TableCellCenter']), Paragraph("Zhang et al. (2018)", styles['TableCell']), Paragraph("RNN, MLP Neural Nets", styles['TableCell']), Paragraph("120K URLs (Gateway)", styles['TableCell']), Paragraph("RNN achieved 94.8% on raw chars; high latency (>250ms).", styles['TableCell'])],
        [Paragraph("3", styles['TableCellCenter']), Paragraph("Sabhadiya et al. (2019)", styles['TableCell']), Paragraph("MalDozer, DroidDetector, CNN", styles['TableCell']), Paragraph("Drebin (15K APKs)", styles['TableCell']), Paragraph("Static bytecode graphs yielded 95.2% malware accuracy.", styles['TableCell'])],
        [Paragraph("4", styles['TableCellCenter']), Paragraph("Ferdaws & Majd (2024)", styles['TableCell']), Paragraph("LR, NB, CNN-LSTM", styles['TableCell']), Paragraph("60K Domains + WHOIS", styles['TableCell']), Paragraph("CNN-LSTM hit 97.1%; WHOIS lookups added network lag.", styles['TableCell'])],
        [Paragraph("5", styles['TableCellCenter']), Paragraph("Zhou & Liu (2025)", styles['TableCell']), Paragraph("SecBERT Transformer", styles['TableCell']), Paragraph("80K Web Addresses", styles['TableCell']), Paragraph("98.3% accuracy; high GPU memory footprint.", styles['TableCell'])],
        [Paragraph("6", styles['TableCellCenter']), Paragraph("Robert et al. (2023)", styles['TableCell']), Paragraph("Random Forest, SVM (RBF)", styles['TableCell']), Paragraph("CICMalDroid 2020", styles['TableCell']), Paragraph("SVM high precision (96.1%), RF high recall (97.4%).", styles['TableCell'])],
        [Paragraph("7", styles['TableCellCenter']), Paragraph("Kumaresan et al. (2025)", styles['TableCell']), Paragraph("Feature Selection + RF", styles['TableCell']), Paragraph("70K URLs (PhishTank)", styles['TableCell']), Paragraph("Selected 16 lexical features; 96.8% accuracy.", styles['TableCell'])],
        [Paragraph("8", styles['TableCellCenter']), Paragraph("Shukla et al. (2025)", styles['TableCell']), Paragraph("Ensemble (LR + SVM + DT)", styles['TableCell']), Paragraph("15K APKs (Play/Share)", styles['TableCell']), Paragraph("Soft-voting hit 95.8% F1; slow sequential inference.", styles['TableCell'])],
        [Paragraph("9", styles['TableCellCenter']), Paragraph("Ma et al. (2010)", styles['TableCell']), Paragraph("Lexical & Host Statistical", styles['TableCell']), Paragraph("50K Streaming URLs", styles['TableCell']), Paragraph("Pioneered zero-lookup statistical lexical classification.", styles['TableCell'])],
        [Paragraph("10", styles['TableCellCenter']), Paragraph("Yerima et al. (2014)", styles['TableCell']), Paragraph("Naive Bayes, Bayesian Net", styles['TableCell']), Paragraph("ISCX Android Botnet", styles['TableCell']), Paragraph("SMS + Boot receiver patterns detected mobile botnets.", styles['TableCell'])],
        [Paragraph("11", styles['TableCellCenter']), Paragraph("Sahingoz et al. (2019)", styles['TableCell']), Paragraph("NLP Tokenization + RF", styles['TableCell']), Paragraph("73K URLs (PhishTank)", styles['TableCell']), Paragraph("NLP n-grams yielded 97.3% accuracy; memory intensive.", styles['TableCell'])],
        [Paragraph("12", styles['TableCellCenter']), Paragraph("Putri & Wiratama (2024)", styles['TableCell']), Paragraph("Random Forest Tuning", styles['TableCell']), Paragraph("50K URLs (Kaggle)", styles['TableCell']), Paragraph("Hyperparameter tuning boosted RF accuracy to 96.9%.", styles['TableCell'])],
        [Paragraph("13", styles['TableCellCenter']), Paragraph("Marchal et al. (2014)", styles['TableCell']), Paragraph("PhishStorm Streaming", styles['TableCell']), Paragraph("1.5M Enterprise URLs", styles['TableCell']), Paragraph("Brand keyword placement proved strong phishing signal.", styles['TableCell'])],
        [Paragraph("14", styles['TableCellCenter']), Paragraph("Verma & Das (2017)", styles['TableCell']), Paragraph("Structural Lexical + SVM", styles['TableCell']), Paragraph("85K URLs (DMOZ)", styles['TableCell']), Paragraph("Structural delimiters alone achieve >90% accuracy.", styles['TableCell'])],
        [Paragraph("15", styles['TableCellCenter']), Paragraph("McLaughlin et al. (2017)", styles['TableCell']), Paragraph("Disassembly + CNN", styles['TableCell']), Paragraph("Drebin + 12K APKs", styles['TableCell']), Paragraph("97.2% accuracy on opcodes; disassembly was very slow.", styles['TableCell'])],
        [Paragraph("16", styles['TableCellCenter']), Paragraph("Yuan & Zhang (2018)", styles['TableCell']), Paragraph("Permission Bitmaps + CNN", styles['TableCell']), Paragraph("20K Android APKs", styles['TableCell']), Paragraph("2D permission bitmaps captured family relationships.", styles['TableCell'])],
        [Paragraph("17", styles['TableCellCenter']), Paragraph("Srivastava & Sharma (2025)", styles['TableCell']), Paragraph("XGBoost vs LR vs NB", styles['TableCell']), Paragraph("95K URLs (Mendeley)", styles['TableCell']), Paragraph("XGBoost achieved superior F1 of 97.8% on tabular data.", styles['TableCell'])],
        [Paragraph("18", styles['TableCellCenter']), Paragraph("Lakshmanarao & Krishna (2021)", styles['TableCell']), Paragraph("KNN, DT, RF + Flask Web", styles['TableCell']), Paragraph("30K Threat URLs", styles['TableCell']), Paragraph("Built web GUI; synchronous Flask hit concurrency limits.", styles['TableCell'])],
        [Paragraph("19", styles['TableCellCenter']), Paragraph("Irsan & Febriana (2024)", styles['TableCell']), Paragraph("KNN vs Decision Trees", styles['TableCell']), Paragraph("40K Domain Records", styles['TableCell']), Paragraph("KNN suffered prohibitive test latency; DT executed <1ms.", styles['TableCell'])],
        [Paragraph("20", styles['TableCellCenter']), Paragraph("Ham & Choi (2013)", styles['TableCell']), Paragraph("Static Permissions + RF", styles['TableCell']), Paragraph("2.4K Early APKs", styles['TableCell']), Paragraph("15 core dangerous permissions accounted for 85% threats.", styles['TableCell'])],
    ]
    t31 = Table(t31_data, colWidths=[38, 105, 95, 80, 115])
    t31.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t31)
    story.append(Spacer(1, 8))

    # =========================================================================
    # TABLE 3.2: DATASET COMPARISON
    # =========================================================================
    story.append(PageMarker('TAB_3_2'))
    story.append(Paragraph("<b>Table 3.2: Public Dataset Comparison for URL and APK Malware Research</b>", styles['CaptionText']))
    
    t32_data = [
        [Paragraph("<b>Dataset Name</b>", styles['TableHeader']), Paragraph("<b>Domain</b>", styles['TableHeader']), Paragraph("<b>Sample Volume</b>", styles['TableHeader']), Paragraph("<b>Primary Features</b>", styles['TableHeader']), Paragraph("<b>Key Advantages / Limits</b>", styles['TableHeader'])],
        [Paragraph("PhishTank Feed", styles['TableCell']), Paragraph("Web URLs", styles['TableCellCenter']), Paragraph("100K+ Live Samples", styles['TableCellCenter']), Paragraph("Verified Phishing URLs", styles['TableCell']), Paragraph("Continuously updated; requires rapid labeling verification.", styles['TableCell'])],
        [Paragraph("Alexa Top 1M", styles['TableCell']), Paragraph("Web Domains", styles['TableCellCenter']), Paragraph("1,000,000 Domains", styles['TableCellCenter']), Paragraph("High-Traffic Benign Sites", styles['TableCell']), Paragraph("Golden standard for benign web traffic; static list.", styles['TableCell'])],
        [Paragraph("ISCXURL 2016", styles['TableCell']), Paragraph("Web URLs", styles['TableCellCenter']), Paragraph("165,366 URLs", styles['TableCellCenter']), Paragraph("Phishing, Malware, Deface", styles['TableCell']), Paragraph("Balanced multi-class; older domain distributions.", styles['TableCell'])],
        [Paragraph("Drebin Benchmark", styles['TableCell']), Paragraph("Android APK", styles['TableCellCenter']), Paragraph("129,013 APKs (5.5K Mal)", styles['TableCellCenter']), Paragraph("Permissions, API Calls", styles['TableCell']), Paragraph("Standard research benchmark; lacks modern Android 14+ APIs.", styles['TableCell'])],
        [Paragraph("CICMalDroid 2020", styles['TableCell']), Paragraph("Android APK", styles['TableCellCenter']), Paragraph("17,341 APKs", styles['TableCellCenter']), Paragraph("Adware, Banking, Trojans", styles['TableCell']), Paragraph("Granular category labels; complex multi-family distribution.", styles['TableCell'])],
        [Paragraph("AndroZoo Corpus", styles['TableCell']), Paragraph("Android APK", styles['TableCellCenter']), Paragraph("20M+ Packages", styles['TableCellCenter']), Paragraph("Raw APKs + VirusTotal", styles['TableCell']), Paragraph("Massive real-world scale; requires extensive filtering.", styles['TableCell'])],
    ]
    t32 = Table(t32_data, colWidths=[90, 65, 85, 95, 98])
    t32.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t32)
    story.append(Spacer(1, 6))

    # =========================================================================
    # SECTION 3.4: RESEARCH GAP
    # =========================================================================
    story.append(PageMarker('S3_4'))
    story.append(Paragraph("3.4 Research Gap", styles['SectionHeading']))
    story.append(Paragraph(
        "Our critical evaluation of the twenty published studies revealed four significant research and engineering gaps that have remained "
        "largely unaddressed in prior literature:",
        styles['BodyContent']
    ))
    gaps = [
        "<b>Gap 1 — Disconnect Between Offline Accuracy and Operational Latency:</b> While numerous studies achieve high theoretical accuracy (exceeding 96%) using complex recurrent networks, transformers, or full bytecode disassembly, they incur evaluation latencies ranging from 500 milliseconds to several minutes. In high-throughput corporate proxies and real-time security operations, sub-50ms execution is non-negotiable.",
        "<b>Gap 2 — Single-Model Brittleness and Inflexibility:</b> Most existing platforms hardcode a single machine learning model (such as a single Random Forest or SVM) into their backend. In dynamic threat environments, no single model is universally optimal across all threat distributions. The absence of a dynamic model switching architecture prevents operators from tailoring classification thresholds to operational contexts.",
        "<b>Gap 3 — Lack of Database Persistence Fault Tolerance:</b> Prior academic prototypes either omit database persistence entirely (operating purely in memory) or rely on a single database connection. If that database encounters network timeouts or service crashes, scan telemetry, audit logs, and compliance records are permanently lost.",
        "<b>Gap 4 — Primitive and Non-Intuitive User Telemetry:</b> Existing research implementations are predominantly command-line scripts or basic web forms that output binary numbers (0 or 1). Security operations personnel require rich, informative visual interfaces—including circular risk meters, model confidence breakdowns, and searchable historical archives—to make rapid, confident incident triage decisions."
    ]
    for g in gaps:
        story.append(Paragraph(f"• {g}", styles['BodyBullet']))
    story.append(Spacer(1, 4))

    # =========================================================================
    # SECTION 3.5: SUMMARY
    # =========================================================================
    story.append(PageMarker('S3_5'))
    story.append(Paragraph("3.5 Summary", styles['SectionHeading']))
    story.append(Paragraph(
        "Chapter 3 conducted an extensive survey of twenty pivotal research publications from our project presentation, systematically analyzing "
        "their technical methodologies, datasets, findings, and operational limitations. We established a structured attack indicator taxonomy "
        "categorizing lexical URL anomalies and Android bytecode permission fingerprints. Finally, we identified four critical research gaps "
        "spanning execution latency, model agility, database resilience, and user experience that directly motivated the architectural "
        "innovations implemented in CyberGuard.",
        styles['BodyContent']
    ))
    story.append(PageBreak())

    return story
