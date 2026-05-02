import pypdf

def find_offset():
    pdf_path = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    
    with open(pdf_path, 'rb') as f, open('pdf_output2.txt', 'w', encoding='utf-8') as out:
        reader = pypdf.PdfReader(f)
        for i in range(10, 30):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                out.write(f"--- Physical Page {i} ---\n")
                out.write(text[:800] + "\n\n")

if __name__ == '__main__':
    find_offset()
