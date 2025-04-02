import streamlit as st

def apply_sidebar_styles():
    st.markdown("""
        <style>
        .stApp {background-color: #f0f2f6; font-size: 16px;}
        .sidebar .sidebar-content {
            background-color: #E0F7FA;
            color: #1A2525;
            padding: 15px;
            max-width: 280px;
            border-radius: 0 15px 15px 0;
            box-shadow: 3px 0 8px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }
        .sidebar h2 {color: #1A2525; font-size: 22px; text-align: center; margin: 10px 0; font-weight: bold;}
        .sidebar hr {border: 1px solid rgba(26, 37, 37, 0.2); margin: 10px 0;}
        .stButton>button {
            background: linear-gradient(90deg, #E0F7FA, #D1F0F5);
            color: #1A2525;
            border-radius: 10px;
            padding: 8px;
            font-size: 12px;
            font-weight: 500;
            width: 100%;
            margin: 2px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #D1F0F5, #B8E8EF);
            transform: scale(1.05);
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .stSelectbox, .stTextInput {
            background-color: #D1F0F5;
            color: #1A2525;
            border-radius: 8px;
            padding: 5px;
            font-size: 14px;
        }
        [data-testid="stSidebarNav"] {display: none !important;}
        .section-title {color: #1A2525; font-size: 14px; margin: 10px 0 5px 0; text-transform: uppercase;}
        @media (max-width: 768px) {
            .stApp {font-size: 14px;}
            .sidebar .sidebar-content {max-width: 100%; border-radius: 0;}
            .stButton>button {font-size: 10px; padding: 6px;}
            .stColumn {margin-bottom: 5px;}
            .main h1 {font-size: 24px;}
            .main p {font-size: 14px;}
        }
        </style>
    """, unsafe_allow_html=True)