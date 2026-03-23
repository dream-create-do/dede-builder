"""
dede_app.py — DeDe Course Builder v4.0
Accepts original IMSCC + MeMe's GMO + design style selection.
"""

import streamlit as st
import os, sys, traceback

st.set_page_config(page_title="DeDe — Course Builder", page_icon="🏗️", layout="centered")

try:
    from dede_engine import run_dede, read_imscc, parse_gmo, LLM_ACTIONS
    from style_templates import STYLES
except ImportError as e:
    st.error(f"Could not load DeDe engine: {e}")
    st.stop()

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }
    .header-bar { background: linear-gradient(135deg, #6c5ce7, #a855f7, #ff6b9d); border-radius: 16px; padding: 2rem; margin-bottom: 1.5rem; text-align: center; color: white; }
    .header-bar h1 { font-size: 2.2rem; font-weight: 700; margin: 0; letter-spacing: 2px; }
    .header-bar p { margin: 0.25rem 0 0 0; opacity: 0.85; font-size: 0.9rem; font-weight: 300; letter-spacing: 1.5px; text-transform: uppercase; }
    .stat-card { background: #f8f9fa; border-radius: 8px; padding: 10px; text-align: center; }
    .stat-number { font-size: 22px; font-weight: 700; color: #6c5ce7; line-height: 1; }
    .stat-label { font-size: 11px; color: #888; margin-top: 4px; }
    .section-header { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; color: #888; margin: 1.5rem 0 0.5rem 0; }
    .stButton > button[kind="primary"], .stDownloadButton > button {
        background: linear-gradient(135deg, #6c5ce7, #a855f7) !important; color: white !important;
        border: none !important; border-radius: 10px !important; font-family: 'Lexend', sans-serif !important;
        font-weight: 600 !important; padding: 0.75rem 2rem !important; font-size: 15px !important; width: 100%; }
    footer { visibility: hidden; }
    #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-bar">
    <h1>🏗️ DeDe</h1>
    <p>Course Builder Agent</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Upload your Canvas course export and MeMe's GMO document. DeDe will apply 
structural changes, content rewrites, new pages, new assignments, and 
design styling — then give you an updated `.imscc` to import back into Canvas.
""")

# ── Step 1: IMSCC ───────────────────────────────────────────────
st.markdown('<p class="section-header">Step 1 — Upload your course export</p>', unsafe_allow_html=True)
imscc_file = st.file_uploader("Upload .imscc", type=["imscc", "zip"], label_visibility="collapsed")
if not imscc_file:
    st.info("Upload a .imscc file to get started.")
    st.stop()

# ── Step 2: GMO ─────────────────────────────────────────────────
st.markdown('<p class="section-header">Step 2 — MeMe\'s GMO document (optional)</p>', unsafe_allow_html=True)
st.markdown("Paste the GMO or upload the `.md` file MeMe generated.")
gmo_text = st.text_area("Paste GMO", height=200, placeholder="# FINAL CONSOLIDATED GMO...", label_visibility="collapsed")
gmo_file = st.file_uploader("Or upload GMO (.md)", type=["md", "txt"], label_visibility="collapsed")
if gmo_file:
    gmo_text = gmo_file.read().decode("utf-8", errors="ignore")
    st.success(f"Loaded GMO: {len(gmo_text):,} characters")

# ── Step 3: Style ───────────────────────────────────────────────
st.markdown('<p class="section-header">Step 3 — Design style</p>', unsafe_allow_html=True)
style_options = {v: k for k, v in STYLES.items()}
selected_label = st.selectbox("Design style", list(style_options.keys()), index=0, label_visibility="collapsed")
selected_style = style_options[selected_label]
if selected_style != 'none':
    st.info(f"🎨 **{selected_label}** will be applied to homepage, overview, and assignment pages.")

# ── Step 4: API Key ─────────────────────────────────────────────
api_key = None
has_content = any(a in gmo_text.upper() for a in ['CREATE_PAGE', 'REWRITE_CONTENT', 'CREATE_ASSIGNMENT', 'CREATE_SECTION']) if gmo_text else False
if has_content:
    st.markdown('<p class="section-header">Step 4 — API key (required for content changes)</p>', unsafe_allow_html=True)
    api_key = None
    try: api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
    except: pass
    if api_key:
        st.success("API key loaded from secrets.")
    else:
        api_key = st.text_input("Anthropic API Key", type="password", placeholder="sk-ant-...", label_visibility="collapsed")
        if not api_key:
            st.warning("Content changes will be skipped without an API key.")

# ── Preview ─────────────────────────────────────────────────────
imscc_bytes = imscc_file.read()
try:
    preview = read_imscc(imscc_bytes)
    st.markdown('<p class="section-header">Original course</p>', unsafe_allow_html=True)
    st.markdown(f"### {preview['identity'].get('title', 'Unknown')} — {preview['identity'].get('code', '')}")
    c1, c2, c3, c4 = st.columns(4)
    for col, val, label in [(c1, len(preview['modules']), 'Modules'), (c2, len(preview['assignments']), 'Assignments'),
                             (c3, len(preview['wiki_pages']), 'Pages'), (c4, len(preview['grading_groups']), 'Grade Groups')]:
        with col:
            st.markdown(f'<div class="stat-card"><div class="stat-number">{val}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

    # Show planned changes
    if gmo_text:
        changes, _ = parse_gmo(gmo_text)
        structural = [c for c in changes if c['action'] not in LLM_ACTIONS]
        content = [c for c in changes if c['action'] in LLM_ACTIONS]
        st.markdown("")
        if structural:
            st.markdown(f"🔧 **{len(structural)}** structural change(s) (no AI needed)")
        if content:
            st.markdown(f"🧠 **{len(content)}** content change(s) (AI-powered)")
        if selected_style != 'none':
            restyle_count = sum(1 for t in preview['page_types'].values() if t in ('homepage','overview')) + len(preview['assignments'])
            st.markdown(f"🎨 **{restyle_count}** pages to restyle")
except Exception as e:
    st.error(f"Could not read IMSCC: {e}")
    st.stop()

# ── Build ────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Build</p>', unsafe_allow_html=True)
build_btn = st.button("🏗️  Build Modified Course", type="primary", use_container_width=True)

if not build_btn and "last_build" not in st.session_state:
    st.stop()

cache_key = f"{imscc_file.name}_{imscc_file.size}_{selected_style}_{len(gmo_text or '')}"
if build_btn or st.session_state.get("last_key") != cache_key:
    progress = st.progress(0, text="Starting...")
    steps = [0]
    def cb(msg):
        steps[0] += 1
        progress.progress(min(steps[0]/15, 0.99), text=msg)
    try:
        out_bytes, log = run_dede(imscc_bytes, gmo_text=gmo_text or '', style=selected_style,
                                   api_key=api_key or None, progress_callback=cb)
        progress.progress(1.0, text="✅ Build complete!")
        st.session_state["last_build"] = {"bytes": out_bytes, "log": log, "filename": imscc_file.name, "style": selected_style}
        st.session_state["last_key"] = cache_key
    except Exception as e:
        st.error(f"Build failed: {e}")
        with st.expander("Error details"): st.code(traceback.format_exc())
        st.stop()

# ── Results ──────────────────────────────────────────────────────
result = st.session_state.get("last_build")
if not result: st.stop()

st.success("✅ Build complete!")
base = os.path.splitext(result["filename"])[0]
sfx = f"_{result['style']}" if result['style'] != 'none' else ''
kb = len(result["bytes"]) / 1024

st.download_button(f"⬇  Download Modified Course ({kb:.1f} KB)", data=result["bytes"],
    file_name=f"{base}_modified{sfx}.imscc", mime="application/zip", use_container_width=True)

st.markdown("""
**To import into Canvas:**
1. Open your course → **Settings** → **Import Course Content**
2. Select **Canvas Course Export Package**
3. Upload the `.imscc` file → **Import**
""")

with st.expander("📋 Build log"):
    for line in result["log"]: st.text(line)

st.markdown("---")
st.caption("DeDe v4 · Course Builder Agent · CeCe / MeMe / DeDe Suite · TOPkit / Florida SUS")
