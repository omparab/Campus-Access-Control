import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Campus Access Control",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        height: 200px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
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
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("🎓 Campus Access Control System")
st.markdown('<p class="subtitle">Select an access control option to proceed</p>', unsafe_allow_html=True)

# Create three columns for the options
col1, col2, col3 = st.columns(3)

# URLs for redirection (replace these with your actual URLs)
ID_CARD_URL = "https://patta-detection.streamlit.app/"
IDENTITY_URL = "https://identity-recognition-system.streamlit.app/"
LICENSE_PLATE_URL = "https://license-plate-test-7szorvfhkefe6wjavtbx9f.streamlit.app/"

with col1:
    st.markdown("### 🪪 ID Card Detection")
    st.markdown("Scan and verify student/staff ID cards for campus entry")
    if st.button("🪪 Launch ID Card Detection", key="btn1"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={ID_CARD_URL}">', unsafe_allow_html=True)
        st.success(f"Redirecting to ID Card Detection...")
        st.markdown(f"[Click here if not redirected automatically]({ID_CARD_URL})")

with col2:
    st.markdown("### 👤 Identity Verification")
    st.markdown("Biometric verification for authorized personnel")
    if st.button("👤 Launch Identity Verification", key="btn2"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={IDENTITY_URL}">', unsafe_allow_html=True)
        st.success(f"Redirecting to Identity Verification...")
        st.markdown(f"[Click here if not redirected automatically]({IDENTITY_URL})")

with col3:
    st.markdown("### 🚗 License Plate Verification")
    st.markdown("Automatic vehicle registration verification")
    if st.button("🚗 Launch License Plate Verification", key="btn3"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={LICENSE_PLATE_URL}">', unsafe_allow_html=True)
        st.success(f"Redirecting to License Plate Verification...")
        st.markdown(f"[Click here if not redirected automatically]({LICENSE_PLATE_URL})")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; padding: 2rem 0;'>
        <p>Campus Access Control System v1.0</p>
        <p>For support, contact: security@campus.edu</p>
    </div>
""", unsafe_allow_html=True)
