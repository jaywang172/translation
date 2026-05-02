import fitz

def print_page():
    pdf_path = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    doc = fitz.open(pdf_path)
    
    with open('pymupdf_output.txt', 'w', encoding='utf-8') as out:
        for i in range(10, 15):
            page = doc.load_page(i)
            text = page.get_text()
            out.write(f"--- Physical Page {i} ---\n")
            out.write(text[:800] + "\n\n")

if __name__ == "__main__":
    print_page()
