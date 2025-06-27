# TestiFYI 🧬

Your AI-Powered Evidence Copilot


---

## 📌 What is TestiFYI?

Imagine being an officer juggling body-cam footage, audio clips, witness statements, and scribbled reports.......all while the clock’s ticking on paperwork and investigations. It’s chaotic, exhausting, and inefficient.

**TestiFYI** steps in as your AI-powered case co-pilot. It’s a multi-source investigation assistant built to:  
🎯 *To make sense of scattered evidence and help law enforcement focus more on the field, not the filing cabinet.*

TestiFYI lets you upload videos, audios, text notes, and even scanned images — and intelligently processes them to:
- 🎧 Transcribe what was said.
- 🗣️ Detect who said it.
- 👀 Extract key details.
- 🤖 Run powerful LLM-based analysis to flag contradictions or gaps like "Accoridng to the informer the suspect is wearing a blue hoodie, but the person arrested is wearing ablack one"
- 💬 Let officers query the case in natural language like “Where did the robbery happen?”

This project draws inspiration from the incredible work by the folks at [**Code Four**](https://codefour.us)....... a groundbreaking platform that’s revolutionizing how cops handle digital evidence. Their tool auto-generates reports, summarizes videos in real-time, and reduces desk-time for officers by up to 60%. If you haven’t seen their launch post, [check it out here](https://www.ycombinator.com/companies/code-four). It’s 🔥.

**TestiFYI** is a smaller, simplified take on what CodeFour is building — with a focus on linking insights across multiple evidence sources and enabling case-level reasoning through LLMs.......all built using open source and free-tier resources! ✌️

---

## 🛠 Tech Stack

| Area              | Tool / Library                   |
|-------------------|----------------------------------|
| Frontend UI       | `streamlit`                      |
| Audio Transcribe  | `whisper`                        |
| Diarization       | `pyannote.audio`, `torchaudio`   |
| OCR               | `pytesseract`, `Pillow`          |
| PDF/Text Parsing  | `PyMuPDF` (fitz)                 |
| Video Processing  | `moviepy`, `pydub`               |
| LLM Integration   | `Groq API` with `llama-3.3-70b`  |
| Backend Utils     | Python (`json`, `os`, `datetime`)|

---

## 🚀 Features

- 👮 Upload **body-cam video**, **audio recordings**, **scanned images**, or **text files**.
- 🧾 Automatic **transcription** using Whisper & **speaker diarization** with pyannote.audio.
- 🖼️ Perform **OCR** on scanned documents like police reports or handwritten notes.
- 📦 Generate a **structured JSON** aligning speech, speakers, and source metadata.
- 🧠 **LLM-powered analysis** to uncover inconsistencies or red flags across evidence.
- 💬 Ask natural-language questions and get answers based **only on uploaded sources**.
- 🎛️ All features accessible via an interactive **Streamlit-based UI**.

---

## 📁 Repository Structure

- `app.py` — Streamlit-based frontend for uploading, analyzing, and querying evidence.
- `requirements.txt` — All Python dependencies.
- `prompts/` — 📄 Prompt templates for LLM interactions
- `src/` — 🔧 Core utility logic
  - `diarize.py` — Speaker diarization with `pyannote.audio`
  - `json_formatter.py` — Aligns and saves structured `JSON` from segments
  - `llm_utils.py` — Handles `Groq` LLM interactions with templates
  - `ocr_utils.py` — Extracts text from scanned images using `OCR`
  - `parse_texts.py` — Extracts raw text from `.txt` and `.pdf` files
  - `transcribe.py` — Audio transcription using `Whisper`
  - `video_to_audio.py` — Converts video files to `WAV` audio for transcription
 
---
## Flow 🌱

<img width="647" alt="Screenshot 2025-06-27 at 18 20 59" src="https://github.com/user-attachments/assets/da6bd442-890a-4be4-882e-29df5d275984" />

---

## ⚙️ Getting Started

### 1. 🚀 Clone the Repository

```bash
git clone https://github.com/Keerthanareddy17/TestiFYI.git
cd testify
```
### 2. 🧪 Create a Virtual Environment

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 📦 Install Dependencies

```
pip install -r requirements.txt
```

### 4. 🔑 Set Environment Variables

- Create a `.env` file at the project root and add your Hugging Face Token. You can get one [here](https://huggingface.co/docs/hub/en/security-tokens):
  ```
  HUGGINGFACE_TOKEN=your_huggingface_token_here
  ```
- Set the Groq API key securely in your `.env` file :
  ```
  GROQ_API_KEY=your_groq_api_key_here
  ```
### 5. 🖥️ Run the Streamlit App

```
streamlit run app.py
```
---

## 🌟 Interface Overview

### 📂 Upload Evidence Tab

Upload any combination of supported evidence files:
- Body-cam videos (.mp4, .avi, etc.)
- Audio clips (.wav, .mp3)
- Text documents (.txt)
- Scanned images (.png, .jpg, .jpeg)
- Uploading all types is not mandatory. A single file is enough to proceed.

### 🧠 Explore & Investigate Tab

- Click 🔍 Run Evidence Analysis
- Let the LLM highlight inconsistencies, contradictions, or suspicious patterns across your evidence.
- Ask natural language case questions like:
    - “What did the witness say about the hoodie?”
    - “Where was the robbery reported to happen?”

⚠️ All responses are generated solely based on your uploaded data.

---

## 📸 Snapshots of TestiFYI 

<img width="1606" alt="Screenshot 2025-06-27 at 15 19 23" src="https://github.com/user-attachments/assets/2db89aad-3559-4a8a-8e3e-d26aa3f37920" />



<img width="1604" alt="Screenshot 2025-06-27 at 15 30 32" src="https://github.com/user-attachments/assets/7c583b72-8aae-4d45-9223-cec20dde97b1" />


<img width="1605" alt="Screenshot 2025-06-27 at 15 32 35" src="https://github.com/user-attachments/assets/f1a89768-9579-45f0-9fae-bf02cd33c8ca" />


---


feel free to reach out! 🤝

I'm always up for talking tech, feedback, collaborations, weird LLM behavior stories 😮‍💨

- 📬 **Email:** [katasanikeerthanareddy@gmail.com](mailto:katasanikeerthanareddy@gmail.com)  
- 🌐 [LinkedIn](https://www.linkedin.com/in/keerthana-reddy-katasani-b07238268/)

