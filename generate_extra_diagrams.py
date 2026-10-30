import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('report_assets', exist_ok=True)
ap = dict(arrowstyle='->', color='#37474f', lw=1.4)

# 1. UML Class Diagram
fig, ax = plt.subplots(figsize=(9, 7))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

classes = [
    (1.8, 8.2, 3.2, 2.8, 'FastAPIGateway', [
        '+ app: FastAPI',
        '+ origins: List[str]'
    ], [
        '+ lifespan(app): AsyncContext',
        '+ read_root(): Dict',
        '+ include_router(router): void'
    ], '#e1f5fe', '#0288d1'),
    
    (6.8, 8.2, 3.4, 2.8, 'ModelManager (Singleton)', [
        '+ active_model_name: str',
        '+ models_cache: Dict[str, Dict]',
        '+ MODEL_NAMES_MAP: Dict'
    ], [
        '+ initialize_all_models(): void',
        '+ train_and_save_all_models(): void',
        '+ set_active_model(name): bool',
        '+ predict_threat(task, feat): Tuple'
    ], '#fce4ec', '#c2185b'),
    
    (1.8, 4.4, 3.2, 2.8, 'FeatureExtractor', [
        '+ SENSITIVE_WORDS: List[str]',
        '+ DANGEROUS_PERMS: List[str]'
    ], [
        '+ extract_url_features(url): Dict',
        '+ extract_apk_features(path): Dict',
        '+ parse_manifest(apk): Dict',
        '+ vectorize(features): List[float]'
    ], '#fff3e0', '#ef6c00'),
    
    (6.8, 4.4, 3.4, 2.8, 'DatabaseManager', [
        '+ DB_FILE: str',
        '+ MONGO_URI: str',
        '+ use_mongodb: bool'
    ], [
        '+ init_db(): void',
        '+ get_sqlite_conn(): Connection',
        '+ log_scan(type, score, ...): bool',
        '+ get_scans_history(): List[Dict]',
        '+ clear_scans_history(): void'
    ], '#e8f5e9', '#2e7d32'),
    
    (4.3, 0.9, 3.6, 2.4, 'UserAuthManager', [
        '+ SECRET_KEY: str',
        '+ ALGORITHM: str = "HS256"',
        '+ ACCESS_TOKEN_EXPIRE: int'
    ], [
        '+ verify_password(plain, hash): bool',
        '+ get_password_hash(password): str',
        '+ create_access_token(data): str',
        '+ get_current_user(token): str'
    ], '#ede7f6', '#512da8')
]

for x, y, w, h, name, attrs, methods, fc, ec in classes:
    p = patches.FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle='round,pad=0.08', fc=fc, ec=ec, lw=1.5)
    ax.add_patch(p)
    ax.text(x, y+h/2-0.3, name, ha='center', va='center', fontsize=8, fontweight='bold', color=ec)
    ax.plot([x-w/2, x+w/2], [y+h/2-0.55, y+h/2-0.55], color=ec, lw=1)
    
    curr_y = y+h/2-0.8
    for a in attrs:
        ax.text(x-w/2+0.15, curr_y, a, ha='left', va='center', fontsize=6.8, fontfamily='monospace', color='#263238')
        curr_y -= 0.28
        
    ax.plot([x-w/2, x+w/2], [curr_y-0.1, curr_y-0.1], color=ec, lw=0.8)
    curr_y -= 0.3
    for m in methods:
        ax.text(x-w/2+0.15, curr_y, m, ha='left', va='center', fontsize=6.8, fontfamily='monospace', color='#263238')
        curr_y -= 0.28

# Relationships
ax.annotate('', xy=(5.1, 8.2), xytext=(3.4, 8.2), arrowprops=dict(arrowstyle='->', color='#37474f', lw=1.4))
ax.text(4.25, 8.4, 'queries', ha='center', fontsize=7, color='#37474f')

ax.annotate('', xy=(1.8, 5.8), xytext=(1.8, 6.8), arrowprops=dict(arrowstyle='->', color='#37474f', lw=1.4))
ax.text(2.1, 6.3, 'invokes', ha='left', fontsize=7, color='#37474f')

ax.annotate('', xy=(6.8, 5.8), xytext=(6.8, 6.8), arrowprops=dict(arrowstyle='->', color='#37474f', lw=1.4))
ax.text(7.1, 6.3, 'commits to', ha='left', fontsize=7, color='#37474f')

ax.annotate('', xy=(4.3, 2.1), xytext=(2.5, 4.4), arrowprops=dict(arrowstyle='->', color='#37474f', lw=1.4))
ax.text(3.1, 3.1, 'protects', ha='center', fontsize=7, color='#37474f')

plt.title('Figure 5.4: UML Class Diagram of CyberGuard Platform Modules', fontsize=10, fontweight='bold', pad=12)
fig.savefig('report_assets/fig_class.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved fig_class.png')

# 2. Activity Diagram
fig, ax = plt.subplots(figsize=(8, 7.5))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 11)

acts = [
    (5.0, 10.4, 'Start: User Submits Inspection Request', '#e0f7fa', '#006064'),
    (5.0, 9.2, 'Validate Input String / Binary Payload', '#e8eaf6', '#1a237e'),
    (5.0, 8.0, 'Input Valid?', '#fff8e1', '#f57f17'),
    (5.0, 6.6, 'Branch by Target Domain Type', '#ede7f6', '#4a148c'),
    (2.5, 5.2, 'Extract Lexical URL Features\n(Protocol, Delimiters, IP, Keywords)', '#f1f8e9', '#33691e'),
    (7.5, 5.2, 'Static APK Decompilation\n(Manifest Permissions, Services, Receivers)', '#fce4ec', '#880e4f'),
    (5.0, 3.8, 'Construct 1xN Numeric Feature Matrix', '#e0f2f1', '#004d40'),
    (5.0, 2.5, 'Execute Inference on Active ML Model (e.g. Random Forest)', '#e8f5e9', '#1b5e20'),
    (5.0, 1.2, 'Log to Database & Transmit HUD Risk Payload', '#efebe9', '#3e2723')
]

for x, y, text, fc, ec in acts:
    if '?' in text:
        poly = patches.Polygon([[x, y+0.45], [x+1.5, y], [x, y-0.45], [x-1.5, y]], closed=True, fc=fc, ec=ec, lw=1.5)
        ax.add_patch(poly)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.5, fontweight='bold', color=ec)
    else:
        p = patches.FancyBboxPatch((x-2.0, y-0.45), 4.0, 0.9, boxstyle='round,pad=0.1', fc=fc, ec=ec, lw=1.5)
        ax.add_patch(p)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.5, fontweight='bold', color=ec)

ax.annotate('', xy=(5.0, 9.65), xytext=(5.0, 9.95), arrowprops=ap)
ax.annotate('', xy=(5.0, 8.45), xytext=(5.0, 8.75), arrowprops=ap)
ax.annotate('', xy=(5.0, 7.05), xytext=(5.0, 7.55), arrowprops=ap)
ax.text(5.2, 7.3, 'Yes', fontsize=7.5, fontweight='bold', color='#1b5e20')

ax.annotate('', xy=(8.5, 9.2), xytext=(6.5, 8.0), arrowprops=ap)
ax.text(7.6, 8.3, 'No (Reject 400)', fontsize=7, color='#b71c1c')

ax.annotate('', xy=(2.5, 5.65), xytext=(4.0, 6.6), arrowprops=ap)
ax.annotate('', xy=(7.5, 5.65), xytext=(6.0, 6.6), arrowprops=ap)
ax.annotate('', xy=(4.0, 3.8), xytext=(2.5, 4.75), arrowprops=ap)
ax.annotate('', xy=(6.0, 3.8), xytext=(7.5, 4.75), arrowprops=ap)

ax.annotate('', xy=(5.0, 2.95), xytext=(5.0, 3.35), arrowprops=ap)
ax.annotate('', xy=(5.0, 1.65), xytext=(5.0, 2.05), arrowprops=ap)

plt.title('Figure 5.8: UML Activity Diagram for Threat Evaluation Workflow', fontsize=10, fontweight='bold', pad=10)
fig.savefig('report_assets/fig_activity.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved fig_activity.png')

# 3. DFD Level 0 Context Diagram
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

p_ent = patches.Rectangle((0.6, 2.2), 2.0, 1.6, fc='#e3f2fd', ec='#1565c0', lw=1.5)
ax.add_patch(p_ent)
ax.text(1.6, 3.0, 'Security Analyst /\nSOC Operator', ha='center', va='center', fontsize=8, fontweight='bold', color='#0d47a1')

p_proc = patches.Circle((5.2, 3.0), 1.4, fc='#fff9c4', ec='#fbc02d', lw=2)
ax.add_patch(p_proc)
ax.text(5.2, 3.0, '0.0\nCyberGuard\nThreat Intelligence\nPlatform', ha='center', va='center', fontsize=8.5, fontweight='bold', color='#f57f17')

p_db = patches.Rectangle((8.0, 2.2), 1.6, 1.6, fc='#e8f5e9', ec='#2e7d32', lw=1.5)
ax.add_patch(p_db)
ax.text(8.8, 3.0, 'Dual Persistence\nDatabase\n(Mongo/SQLite)', ha='center', va='center', fontsize=8, fontweight='bold', color='#1b5e20')

ax.annotate('', xy=(3.8, 3.5), xytext=(2.6, 3.5), arrowprops=ap)
ax.text(3.2, 3.7, 'URL / APK Target', ha='center', fontsize=7, color='#263238')

ax.annotate('', xy=(2.6, 2.5), xytext=(3.8, 2.5), arrowprops=ap)
ax.text(3.2, 2.2, 'Risk Score & Telemetry', ha='center', fontsize=7, color='#263238')

ax.annotate('', xy=(8.0, 3.5), xytext=(6.6, 3.5), arrowprops=ap)
ax.text(7.3, 3.7, 'Persist Scan Log', ha='center', fontsize=7, color='#263238')

ax.annotate('', xy=(6.6, 2.5), xytext=(8.0, 2.5), arrowprops=ap)
ax.text(7.3, 2.2, 'Historical Queries', ha='center', fontsize=7, color='#263238')

plt.title('Figure 5.9: Data Flow Diagram (DFD Level 0 - Context Diagram)', fontsize=10, fontweight='bold', pad=12)
fig.savefig('report_assets/fig_dfd0.png', dpi=300, bbox_inches='tight')
plt.close(fig)
print('Saved fig_dfd0.png')
