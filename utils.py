import fitz  # PyMuPDF
import google.generativeai as genai
import json

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyAL-MjVLwrEybLGihXvH1cZ41tqjYpAlpw")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
        if len(text) > 3000:
            break
    return text

def check_scuML_with_gemini(text):
    prompt = f"""
You are an AI assistant trained on Nigeria's EFCC SCUML regulations.

Below is a business objective from a company's Memorandum of Association (MoA):

\"\"\"{text}\"\"\"

Does this company require SCUML registration?

Respond in JSON format with:
- "status": "Required" or "Not Required"
- "explanation": a short reason
- "keywords": list of up to 5 important business keywords
"""

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        result = json.loads(response.text)
        return {
            "status": result.get("status", "Unknown"),
            "explanation": result.get("explanation", "No explanation provided."),
            "keywords": result.get("keywords", [])
        }
    except Exception as e:
        return {
            "status": "Error",
            "explanation": str(e),
            "keywords": []
        }
