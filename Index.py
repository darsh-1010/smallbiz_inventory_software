import streamlit as st

st.set_page_config(
    page_title="SmallBiz Inventory & Quotation System",
    layout="wide",
    page_icon="📦",
    initial_sidebar_state="collapsed"  # This makes the sidebar retractable
)

# Professional CSS with subtle colors
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(120deg, #fafbfc 0%, #f5f7f9 100%);
    }
    
    /* Sidebar Customization */
    .css-1d391kg {  /* Sidebar */
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
        padding: 2rem 1rem;
    }
    .css-1d391kg .css-1vencpc {  /* Sidebar title */
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
    }
    [data-testid="stSidebarNav"] {  /* Sidebar navigation */
        background: rgba(255,255,255,0.05);
        padding: 0.75rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    [data-testid="stSidebarNav"] > ul {
        gap: 0.5rem;
    }
    [data-testid="stSidebarNav"] span {  /* Sidebar text */
        color: rgba(255,255,255,0.9) !important;
        font-size: 0.95rem !important;
    }
    [data-testid="stSidebarNav"] span:hover {
        color: white !important;
    }
    [data-testid="stSidebarNav"] [aria-selected="true"] {
        background: rgba(255,255,255,0.1) !important;
    }
    
    .hero-section {
        background: linear-gradient(90deg, #2c3e50 0%, #3498db 100%);
        border-radius: 12px;
        box-shadow: 0 4px 24px rgba(44,62,80,0.15);
        padding: 48px 0 36px 0;
        margin-bottom: 2.5em;
        text-align: center;
        position: relative;
        overflow: hidden;
        animation: fadeIn 0.8s ease-out;
    }
    .hero-logo {
        width: 84px;
        height: 84px;
        border-radius: 12px;
        background: rgba(255,255,255,0.95);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 20px rgba(44,62,80,0.2);
        margin-bottom: 18px;
        font-size: 42px;
    }
    .hero-title {
        font-size: 40px;
        font-weight: 600;
        color: #fff;
        margin-bottom: 0.3em;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .hero-subtitle {
        font-size: 20px;
        color: rgba(255,255,255,0.9);
        margin-bottom: 1.5em;
        font-weight: 400;
        letter-spacing: 0.2px;
        line-height: 1.6;
    }
    .get-started {
        background: rgba(255,255,255,0.95);
        color: #2c3e50 !important;
        font-size: 18px !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.8em 2.4em;
        border: none;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
        letter-spacing: 0.3px;
    }
    .get-started:hover {
        background: #fff;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    .section-header {
        background: linear-gradient(90deg, #2c3e50 0%, #34495e 100%);
        color: white;
        padding: 1.2rem 1.5rem;
        border-radius: 12px 12px 0 0;
        font-size: 22px;
        font-weight: 600;
        letter-spacing: -0.3px;
        margin: -28px -32px 20px -32px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    .section-title {
        font-size: 22px !important;
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1em;
        letter-spacing: -0.3px;
        display: flex;
        align-items: center;
        gap: 0.5em;
    }
    .card {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        padding: 28px 32px;
        margin-bottom: 1.5em;
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
    }
    .card:hover {
        box-shadow: 0 6px 24px rgba(0,0,0,0.08);
        transform: translateY(-2px);
        border-color: #3498db;
    }
    ul.feature-list, ol.howto-list {
        color: #2c3e50;
        font-size: 16px;
        margin: 0;
        padding-left: 1em;
        list-style-position: outside;
    }
    ul.feature-list li, ol.howto-list li {
        background: #f8fafc;
        border-radius: 6px;
        margin-bottom: 0.8em;
        padding: 0.8em 1em;
        transition: all 0.2s ease;
        border: 1px solid #e1e8ed;
        line-height: 1.5;
    }
    ul.feature-list li:hover, ol.howto-list li:hover {
        background: #f1f5f9;
        border-color: #3498db;
        transform: translateX(4px);
    }
    .feature-icon {
        display: inline-block;
        margin-right: 0.6em;
        opacity: 0.9;
    }
    .testimonial {
        background: #f8fafc;
        border-left: 4px solid #3498db;
        border-radius: 8px;
        padding: 24px 32px;
        margin: 2em 0;
        font-size: 16px;
        color: #2c3e50;
        font-style: italic;
        line-height: 1.6;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    }
    .testimonial-author {
        font-size: 15px;
        color: #3498db;
        font-weight: 500;
        margin-top: 1em;
        text-align: right;
        font-style: normal;
    }
    hr.custom-hr {
        border: none;
        border-top: 1px solid #e1e8ed;
        margin: 30px 0;
    }
    .footer {
        font-size: 14px;
        color: #64748b;
        margin-top: 50px;
        text-align: center;
        letter-spacing: 0.2px;
        padding: 20px 0;
        border-top: 1px solid #e1e8ed;
        background: linear-gradient(90deg, #f8fafc 0%, #f1f5f9 100%);
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hide Streamlit's default menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# HERO SECTION
st.markdown('''
<div class="hero-section">
    <div class="hero-logo">📦</div>
    <div class="hero-title">SmallBiz Inventory System</div>
    <div class="hero-subtitle">Professional inventory management, quotation generation,<br>and business automation solution.</div>
    <button class="get-started">Get Started →</button>
</div>
''', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card"><div class="section-header">Key Features</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class='feature-list'>
    <li><span class='feature-icon'>📋</span><b>Inventory Management</b> - Complete stock control</li>
    <li><span class='feature-icon'>✉️</span><b>Automated Quotations</b> - Email-based generation</li>
    <li><span class='feature-icon'>⚠️</span><b>Stock Monitoring</b> - Real-time alerts</li>
    <li><span class='feature-icon'>💰</span><b>Sales & Billing</b> - GST-compliant invoicing</li>
    <li><span class='feature-icon'>📈</span><b>Business Analytics</b> - Comprehensive logs</li>
    <li><span class='feature-icon'>📧</span><b>Follow-up System</b> - Automated client engagement</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><div class="section-header">Quick Start Guide</div>', unsafe_allow_html=True)
    st.markdown("""
    <ol class='howto-list'>
    <li><b>Navigation:</b> Access all features through the sidebar menu</li>
    <li><b>Quotations:</b> Simply paste client email to generate</li>
    <li><b>Monitoring:</b> Receive notifications for important updates</li>
    <li><b>Reports:</b> Access comprehensive business analytics</li>
    </ol>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# TESTIMONIAL SECTION
st.markdown('''
<div class="testimonial">
    "This system has streamlined our entire business operation. The automated quotation system and inventory management have significantly improved our efficiency and professionalism."
    <div class="testimonial-author">— Rajesh Kumar, Managing Director</div>
</div>
''', unsafe_allow_html=True)

st.info("👉 **Select a module from the sidebar to begin.**")

st.markdown('<div class="footer">SmallBiz Inventory Management System | Enterprise Solution<br>© 2024 Your Company Name</div>', unsafe_allow_html=True)
