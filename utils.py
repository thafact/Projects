import fitz  # PyMuPDF
import google.generativeai as genai
import json

# SET YOUR GEMINI API KEY HERE
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

Here is a business objective extracted from a company's Memorandum of Association (MoA):

\"\"\"{text}\"\"\"

Please analyze this and respond in valid JSON format like this:

{{
  "status": "Required",
  "explanation": "Because the objectives include consulting and property services.",
  "keywords": ["consulting", "real estate", "investment"]
}}

Give your best judgment.
"""

    try:
        model = genai.GenerativeModel(model_name="models/gemini-pro")
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
            "explanation": f"Failed to connect to Gemini: {e}",
            "keywords": []
        }
