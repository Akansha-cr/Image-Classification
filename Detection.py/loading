import streamlit as st
import time

# Custom CSS for loading screen
st.markdown(
    """
    <style>
    .loading-overlay {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background: rgba(255, 255, 255, 0.9);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        color: #333;
    }
    .spinner {
        border: 8px solid #f3f3f3;
        border-top: 8px solid #3498db;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 2s linear infinite;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Show loading screen
st.markdown('<div class="loading-overlay"><div class="spinner"></div>Loading...</div>', unsafe_allow_html=True)

# Simulate a long process
time.sleep(3)

# Hide loading screen after the process is done
st.markdown(
    """
    <style>
    .loading-overlay {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your main app content goes here
st.title("Welcome to the Image Classification App")
st.write("This is the main content of the app.")
