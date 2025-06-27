import whisper

model = whisper.load_model("base")  
def transcribe_audio_whisper(audio_path):
    result = model.transcribe(audio_path, word_timestamps=True)  # Includes timestamps
    return result
