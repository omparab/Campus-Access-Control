import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Campus Access Control",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    h1 {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 3rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 3rem;
    }
    .card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease;
        border: 2px solid #e0e0e0;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        border-color: #1f77b4;
    }
    .card-icon {
        font-size: 60px;
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        margin-bottom: 15px;
    }
    .card-description {
        color: #666;
        margin-bottom: 25px;
        font-size: 16px;
    }
    .access-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
        display: inline-block;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    .access-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# URLs for redirection (replace these with your actual URLs)
ID_CARD_URL = "https://patta-detection.streamlit.app/"
IDENTITY_URL = "https://identity-recognition-system.streamlit.app/"
LICENSE_PLATE_URL = "https://license-plate-test-7szorvfhkefe6wjavtbx9f.streamlit.app/"

# Initialize session state for tracking redirects
if 'redirect' not in st.session_state:
    st.session_state.redirect = None

# Title and subtitle
st.title("Campus Access Control System")
st.markdown('<p class="subtitle">Select an access control option to proceed</p>', unsafe_allow_html=True)

# Create three columns for the options
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div class="card">
            <div class="card-icon">🪪</div>
            <div class="card-title">ID Card Detection</div>
            <div class="card-description">Scan and verify student/staff ID cards for campus entry</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Launch ID Card Detection", key="btn1", use_container_width=True):
        st.session_state.redirect = ID_CARD_URL

with col2:
    st.markdown(f"""
        <div class="card">
            <div class="card-icon">👤</div>
            <div class="card-title">Identity Verification</div>
            <div class="card-description">Biometric verification for authorized personnel</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Identity Verification", key="btn2", use_container_width=True):
        st.session_state.redirect = IDENTITY_URL

with col3:
    st.markdown(f"""
        <div class="card">
            <div class="card-icon">🚗</div>
            <div class="card-title">License Plate Verification</div>
            <div class="card-description">Automatic vehicle registration verification</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Launch License Plate Verification", key="btn3", use_container_width=True):
        st.session_state.redirect = LICENSE_PLATE_URL

# Handle redirect using JavaScript - opens in new tab
if st.session_state.redirect:
    components.html(
        f"""
        <script>
            window.open("{st.session_state.redirect}", "_blank");
        </script>
        """,
        height=0,
    )
    st.session_state.redirect = None

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 2rem 0;'>
        <p><strong>Campus Access Control System v1.0</strong></p>
    </div>
""", unsafe_allow_html=True)
