import os
import re
from pypdf import PdfReader, PdfWriter

def sanitize_filename(name):
    # Remove characters that are unsafe for Windows filenames
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def split_pdf():
    input_pdf = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    output_dir = "Chapters"
    
    # physical page index = logical_page + OFFSET - 1
    OFFSET = 11 

    chapters = [
        ("1 Introduction to Vectors", 1),
        ("1.1 Vectors and Linear Combinations", 2),
        ("1.2 Lengths and Dot Products", 11),
        ("1.3 Matrices", 22),
        ("2 Solving Linear Equations & 2.1 Vectors and Linear Equations", 31),
        ("2.2 The Idea of Elimination", 46),
        ("2.3 Elimination Using Matrices", 58),
        ("2.4 Rules for Matrix Operations", 70),
        ("2.5 Inverse Matrices", 83),
        ("2.6 Elimination Factorization A=LU", 97),
        ("2.7 Transposes and Permutations", 109),
        ("3 Vector Spaces and Subspaces & 3.1 Spaces of Vectors", 123),
        ("3.2 The Nullspace of A", 135),
        ("3.3 The Complete Solution to Ax = b", 150),
        ("3.4 Independence, Basis and Dimension", 164),
        ("3.5 Dimensions of the Four Subspaces", 181)
    ]

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    for i in range(len(chapters)):
        title, start_logic = chapters[i]
        
        # Determine the logical end page
        if i < len(chapters) - 1:
            end_logic = chapters[i+1][1] - 1
        else:
            # For the last specified chapter, we just assume it goes up to +15 pages 
            # (or up to page 199 logical)
            end_logic = start_logic + 18 

        # If start and end are inverted or same, make sure at least 1 page is extracted
        # except when they literally start at the same page (already merged above)
        if end_logic < start_logic:
            end_logic = start_logic

        start_idx = start_logic + OFFSET - 1
        end_idx = end_logic + OFFSET - 1

        # Bounds check
        start_idx = max(0, min(start_idx, total_pages - 1))
        end_idx = max(start_idx, min(end_idx, total_pages - 1))

        writer = PdfWriter()
        for idx in range(start_idx, end_idx + 1):
            writer.add_page(reader.pages[idx])
        
        safe_title = sanitize_filename(title)
        out_filename = os.path.join(output_dir, f"{safe_title}.pdf")
        
        with open(out_filename, "wb") as out_pdf:
            writer.write(out_pdf)
        print(f"Created '{out_filename}' (Logical pages {start_logic}-{end_logic})")

if __name__ == "__main__":
    split_pdf()
