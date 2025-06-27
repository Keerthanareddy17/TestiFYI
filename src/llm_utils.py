import os
import json
from groq import Groq
from pathlib import Path

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Loadin prompts
BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_DIR = BASE_DIR / "prompts"

def load_prompt(file_name):
    with open(PROMPT_DIR / file_name, "r") as f:
        return f.read()

analyze_template = load_prompt("analyze_prompt.txt")
qa_template = load_prompt("qa_prompt.txt")

def read_combined_json(json_path):
    with open(json_path, "r") as f:
        return json.load(f)

def analyze_evidence(json_path):
    data = read_combined_json(json_path)
    filled_prompt = analyze_template.replace("{{evidence_json}}", json.dumps(data, indent=2))

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": filled_prompt}
        ]
    )
    return chat_completion.choices[0].message.content

def query_case_insights(json_path, question):
    data = read_combined_json(json_path)
    filled_prompt = qa_template.replace("{{evidence_json}}", json.dumps(data, indent=2))
    filled_prompt = filled_prompt.replace("{{question}}", question)

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": filled_prompt}
        ]
    )
    return chat_completion.choices[0].message.content