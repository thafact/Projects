import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
        if len(text) > 3000:
            break
    return text

dnfi_keywords = {
    "real estate": "DNFI",
    "estate": "DNFI",
    "law firm": "DNFI",
    "legal": "DNFI",
    "accounting": "DNFI",
    "audit": "DNFI",
    "tax": "DNFI",
    "casino": "DNFI",
    "betting": "DNFI",
    "lottery": "DNFI",
    "hotel": "DNFI",
    "hospitality": "DNFI",
    "supermarket": "DNFI",
    "retail": "DNFI",
    "jewelry": "DNFI",
    "luxury": "DNFI",
    "car dealer": "DNFI",
    "auto dealer": "DNFI",
    "precious": "DNFI",
    "mining": "DNFI",
    "consulting": "DNFI",
    "advisory": "DNFI",
    "non-profit": "DNFI",
    "ngo": "DNFI",
    "charity": "DNFI",
    "mortgage": "DNFI",
    "clearing": "DNFI",
    "freight": "DNFI",
    "farming": "DNFI",
    "construction": "DNFI",
    "export": "DNFI",
    "import": "DNFI",
    "investment": "DNFI",
    "pharmacy": "DNFI",
    "oil": "DNFI",
    "gas": "DNFI"
}

def check_scuML_keywords(text):
    matched_keywords = []

    for keyword in dnfi_keywords:
        if keyword in text.lower():
            matched_keywords.append(keyword)

    if matched_keywords:
        return {
            "status": "Required",
            "matched_keywords": matched_keywords[:5],
            "explanation": f"The following business keywords were detected: {', '.join(matched_keywords[:5])}. These match SCUML-listed DNFI categories."
        }
    else:
        return {
            "status": "Not Required",
            "matched_keywords": [],
            "explanation": "No SCUML-triggering business objective found in the document."
        }