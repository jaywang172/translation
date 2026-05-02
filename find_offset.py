import pypdf

def find_offset():
    pdf_path = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    
    with open(pdf_path, 'rb') as f, open('pdf_output.txt', 'w', encoding='utf-8') as out:
        reader = pypdf.PdfReader(f)
        for i in range(min(50, len(reader.pages))):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                first_chars = text[:200].replace('\n', ' ')
                out.write(f"Physical Page {i}: {first_chars}\n")
                if "Introduction to Vectors" in text and "1.1" in text:
                    out.write(f"!!! Might be Chapter 1 on Physical Page {i}\n")
                if "Solving Linear Equations" in text:
                    out.write(f"!!! Might be Chapter 2 on Physical Page {i}\n")
                if "Vector Spaces and Subspaces" in text:
                    out.write(f"!!! Might be Chapter 3 on Physical Page {i}\n")

if __name__ == '__main__':
    find_offset()
