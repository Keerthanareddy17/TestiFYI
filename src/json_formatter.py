import json
import os
from datetime import datetime

def align_diarization_with_transcript(transcript, diarization_segments):
    aligned = []

    for seg in transcript['segments']:
        seg_start = seg['start']
        seg_end = seg['end']
        seg_text = seg['text'].strip()

        speaker = "Unknown"
        for dia in diarization_segments:
            if dia['start'] <= seg_start < dia['end']:
                speaker = dia['speaker']
                break

        aligned.append({
            "start": round(seg_start, 2),
            "end": round(seg_end, 2),
            "speaker": speaker,
            "text": seg_text
        })

    return aligned


def save_structured_json(transcript, diarization_segments, source="unknown_source", file_name="unknown_file"):
    aligned_segments = align_diarization_with_transcript(transcript, diarization_segments)

    result = {
        "source": source,
        "file_name": file_name,
        "generated_at": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "segments": aligned_segments
    }

    os.makedirs("data/outputs", exist_ok=True)
    path = os.path.join("data/outputs", f"{source}_structured.json")
    with open(path, "w") as f:
        json.dump(result, f, indent=2)

    return path


def save_combined_json(input_dict):
    output = {
        "generated_at": datetime.now().strftime("%Y%m%d_%H%M%S"),
        "sources": {}
    }

    for source_type, data in input_dict.items():
        file_name = data.get("file_name", "unknown")

        # Text-only sources (text or image OCR)
        if "text" in data and "segments" not in data:
            output["sources"][source_type] = {
                "file_name": file_name,
                "text": data["text"].strip()
            }

        # Audio/Video with diarization
        elif all(k in data for k in ("segments", "diarization")):
            aligned_segments = align_diarization_with_transcript(
                {"segments": data["segments"]}, data["diarization"]
            )
            output["sources"][source_type] = {
                "file_name": file_name,
                "segments": aligned_segments
            }

    os.makedirs("data/outputs", exist_ok=True)
    path = os.path.join("data/outputs", f"combined_transcript_{output['generated_at']}.json")
    with open(path, "w") as f:
        json.dump(output, f, indent=2)

    return path
