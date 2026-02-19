from pathlib import Path

def extract_pdf_text(filepath: str) -> str:
    """
    Reads a PDF or text file and returns extracted text.
    """
    path = Path(filepath)

    if not path.exists():
        return "File not found."

    if path.suffix == ".txt":
        return path.read_text(encoding="utf-8")

    if path.suffix == ".pdf":
        try:
            import fitz  # PyMuPDF
            text = ""
            with fitz.open(filepath) as doc:
                for page in doc:
                    text += page.get_text()
            return text
        except Exception as e:
            return f"PDF read error: {e}"

    return "Unsupported file type."
