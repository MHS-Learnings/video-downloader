import streamlit as st
import yt_dlp
import os

st.title("📥 My Personal Video Downloader")
st.write("Facebook, YouTube, Instagram ya kisi bhi platform ka link yahan paste karein:")

url = st.text_input("Video Link Daalein:")

if st.button("Download Video"):
    if url:
        with st.spinner("Video download ho rahi hai, zara sabr karein..."):
            try:
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': 'downloaded_video.%(ext)s',
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                
                st.success("Video successfully download ho gayi!")
                
                with open(filename, "rb") as file:
                    st.download_button(
                        label="Click Here to Save File",
                        data=file,
                        file_name=filename,
                        mime="video/mp4"
                    )
            except Exception as e:
                st.error(f"Koi error aa gaya: {e}")
    else:
        st.warning("Pehle koi link toh daalein!")