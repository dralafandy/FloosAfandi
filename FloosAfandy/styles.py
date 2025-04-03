# styles.py
import streamlit as st

def apply_sidebar_styles():
    st.markdown("""
    <style>
        /* Sidebar background and padding */
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }

        /* Section title styling (used in sidebar) */
        .section-title {
            font-weight: bold;
            color: #1A2525;
            font-size: 18px;
            margin-bottom: 10px;
            text-align: center;
        }

        /* Button hover effect */
        button:hover {
            opacity: 0.9;
        }

        /* Ensure buttons with gradients look consistent */
        button[kind="primary"] {
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
        }

        /* General layout tweaks */
        .stButton > button {
            width: 100%;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .sidebar .sidebar-content {
                padding: 5px;
            }
        }
    </style>
    """, unsafe_allow_html=True)
