import streamlit as st
import os
from src.video_to_audio import extract_audio_from_video
from src.transcribe import transcribe_audio_whisper
from src.diarize import run_diarization
from src.json_formatter import save_combined_json
from src.parse_texts import extract_text_from_txt
from src.ocr_utils import extract_text_from_image
from src.llm_utils import analyze_evidence, query_case_insights

st.set_page_config(page_title="TestiFYI 🧬", layout="wide")
st.sidebar.title("👮‍♂️ TestiFYI")
st.sidebar.markdown("Built for investigative officers to extract, analyze & query structured evidence.")

# Sidebar Navigation
tabs = ["📂 Upload Evidence", "🧠 Explore & Investigate"]
selected_tab = st.sidebar.radio("Navigation 🧭", tabs)

if selected_tab == "📂 Upload Evidence":
    st.title("🧠 TestiFYI: Multi-Source Evidence Analyzer")
    st.markdown("TestiFYI is an intelligence tool that allows officers to upload, transcribe, and extract insights from body-cam videos, audio, scanned reports, and more.")
    st.info("You may upload any combination of files....... only one source is enough to begin analysis.")

    st.subheader("🎥 Video Input")
    video_file = st.file_uploader("Upload a Body-Cam Video", type=["mp4", "mov", "avi"], key="video")
    if video_file:
        if st.button("📽️ Process Video"):
            with st.spinner("Transcribing & diarizing video evidence..."):
                video_path = os.path.join("data/inputs", video_file.name)
                os.makedirs("data/inputs", exist_ok=True)
                with open(video_path, "wb") as f:
                    f.write(video_file.read())
                audio_path = extract_audio_from_video(video_path)
                transcript = transcribe_audio_whisper(audio_path)
                diarization_segments = run_diarization(audio_path)
                st.session_state["video_output"] = {
                    "file_name": video_file.name,
                    "segments": transcript["segments"],
                    "diarization": diarization_segments
                }
            st.success("✅ Video processed successfully!")

    st.subheader("🎙️ Audio Input")
    audio_file = st.file_uploader("Upload an Audio Clip", type=["wav", "mp3"], key="audio")
    if audio_file:
        if st.button("🔊 Process Audio"):
            with st.spinner("Transcribing & diarizing audio clip..."):
                audio_path = os.path.join("data/inputs", audio_file.name)
                os.makedirs("data/inputs", exist_ok=True)
                with open(audio_path, "wb") as f:
                    f.write(audio_file.read())
                transcript = transcribe_audio_whisper(audio_path)
                diarization_segments = run_diarization(audio_path)
                st.session_state["audio_output"] = {
                    "file_name": audio_file.name,
                    "segments": transcript["segments"],
                    "diarization": diarization_segments
                }
            st.success("✅ Audio processed successfully!")

    st.subheader("📄 Text File Input")
    text_file = st.file_uploader("Upload a Text File (.txt only)", type=["txt"], key="text")
    if text_file:
        if st.button("📑 Process Text File"):
            with st.spinner("Reading case notes from text file..."):
                text_path = os.path.join("data/inputs", text_file.name)
                os.makedirs("data/inputs", exist_ok=True)
                with open(text_path, "wb") as f:
                    f.write(text_file.read())
                extracted_text = extract_text_from_txt(text_path)
                st.session_state["text_output"] = {
                    "file_name": text_file.name,
                    "text": extracted_text
                }
            st.success("✅ Text file processed and loaded!")

    st.subheader("🖼️ Scanned Image Input")
    image_file = st.file_uploader("Upload a Scanned Image (png/jpg/jpeg)", type=["png", "jpg", "jpeg"], key="image")
    if image_file:
        if st.button("🧾 Process Scanned Image"):
            with st.spinner("Extracting text via OCR..."):
                image_path = os.path.join("data/inputs", image_file.name)
                os.makedirs("data/inputs", exist_ok=True)
                with open(image_path, "wb") as f:
                    f.write(image_file.read())
                extracted_text = extract_text_from_image(image_path)
                st.session_state["image_output"] = {
                    "file_name": image_file.name,
                    "text": extracted_text
                }
            st.success("✅ Image processed successfully!")

    st.subheader("💾 Export Structured Transcripts")
    if any(k in st.session_state for k in ["video_output", "audio_output", "text_output", "image_output"]):
        if st.button("📦 Save Final JSON Output"):
            combined_data = {}
            if "video_output" in st.session_state:
                combined_data["video"] = st.session_state["video_output"]
            if "audio_output" in st.session_state:
                combined_data["audio"] = st.session_state["audio_output"]
            if "text_output" in st.session_state:
                combined_data["text"] = st.session_state["text_output"]
            if "image_output" in st.session_state:
                combined_data["image"] = st.session_state["image_output"]
            output_path = save_combined_json(combined_data)
            st.session_state["combined_json_path"] = output_path
            st.success(f"✅ Combined structured JSON saved at: `{output_path}`")

elif selected_tab == "🧠 Explore & Investigate":
    st.title("🧠 LLM-Powered Case Insights")
    st.markdown("Get analytical observations or ask targeted questions about your uploaded evidence.")

    if "combined_json_path" in st.session_state:
        json_path = st.session_state["combined_json_path"]

        if st.button("🔍 Run Evidence Analysis"):
            with st.spinner("LLM analyzing the full case transcript and evidence..."):
                analysis = analyze_evidence(json_path)
                st.subheader("📌 Case Observations")
                st.markdown(analysis)

        st.markdown("---")
        st.subheader("💬 Ask the Case Copilot")
        st.caption("🔖 Responses are based solely on the uploaded evidence.")
        question = st.text_input("👮 Ask a question about the case:", placeholder="e.g., What did the witness say about the suspect?")
        if st.button("🧠 Get Answer") and question:
            with st.spinner("LLM searching through structured evidence..."):
                answer = query_case_insights(json_path, question)
                st.markdown(f"#### 🧾 Answer\n{answer}")
    else:
        st.warning("Please upload evidence and export a structured JSON from the 'Upload Evidence' tab.")

# Footer
st.markdown("---")
st.markdown("Built by ~kr · Inspired by CodeFour ⭐")