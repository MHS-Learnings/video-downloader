import streamlit as st
import yt_dlp
import os

# Page Config with Dark Theme enforcement
st.set_page_config(
    page_title="MHS Pro Downloader", 
    page_icon="⚡", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Professional Custom Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .stTextInput input {
        background-color: #1f293d;
        color: #ffffff;
        border-radius: 12px;
        border: 1px solid #374151;
        padding: 12px;
    }
    .stSelectbox select {
        background-color: #1f293d;
        color: #ffffff;
        border-radius: 12px;
        border: 1px solid #374151;
    }
    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        width: 100%;
        padding: 12px;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        color: #fff;
    }
    .pro-card {
        background-color: #111827;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #1f2937;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: #f3f4f6;'>⚡ MHS Pro Video Downloader</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Aapka apna high-speed professional downloader tool.</p>", unsafe_allow_html=True)

# Main Box Layout
with st.container():
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    
    url = st.text_input("🔗 Target Video Link:", placeholder="Yahan YouTube, Facebook ya Instagram ka link paste karein...")
    
    col1, col2 = st.columns(2)
    with col1:
        quality_option = st.selectbox(
            "🎯 Format / Quality:",
            ["Best HD Quality", "Audio Only (MP3)", "Fast / Low Size"]
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        download_clicked = st.button("🚀 Start Download")
        
    st.markdown('</div>', unsafe_allow_html=True)

# Processing Logic
if download_clicked:
    if not url:
        st.error("⚠️ Pehle koi valid link toh enter karein boss!")
    else:
        with st.spinner("🔄 Server video process kar raha hai, zara sabr karein..."):
            try:
                ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}
                
                if quality_option == "Audio Only (MP3)":
                    ydl_opts['format'] = 'bestaudio/best'
                    ydl_opts['postprocessors'] = [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                elif quality_option == "Fast / Low Size":
                    ydl_opts['format'] = 'worst'
                else:
                    ydl_opts['format'] = 'best'

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    
                    if quality_option == "Audio Only (MP3)":
                        filename = os.path.splitext(filename)[0] + ".mp3"

                st.success("🎉 Video kamiyabi ke sath tayyar ho gayi hai!")
                
                with open(filename, "rb") as file:
                    st.download_button(
                        label="📥 Download File Now",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="application/octet-stream"
                    )
                
                if os.path.exists(filename):
                    os.remove(filename)

            except Exception as e:
                st.error(f"❌ Error aagaya: {e}")
