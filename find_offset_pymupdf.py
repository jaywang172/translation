import fitz

def find_pages():
    pdf_path = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    doc = fitz.open(pdf_path)
    
    # Check page labels
    labels = doc.get_page_labels()
    print("Page labels:", labels[:20]) # This returns a list of rule strings if there are labels
    
    # Try getting logical pages
    for physical_pg in range(20):
        # find the physical page for logical page 1 maybe?
        page = doc.load_page(physical_pg)
        text = page.get_text()
        
        # Searching for logical page 1 "Introduction to Vectors"
        # We also might find "1.1 Vectors and Linear Combinations"
        if "1.1 Vectors and Linear Combinations" in text[:500]:
            print(f"Physical page {physical_pg}: 1.1 Vectors and Linear Combinations (logical 2 probably)")
        if "Introduction to Vectors" in text and "2 Solving Linear Equations" not in text:
            print(f"Physical page {physical_pg}: Possible start of Chapter 1")
            
    print("Trying to find the physical page for '2 Solving Linear Equations'")
    for physical_pg in range(30, 50):
        page = doc.load_page(physical_pg)
        text = page.get_text()
        if "2 Solving Linear Equations" in text:
            print(f"Physical page {physical_pg}: 2 Solving Linear Equations")

if __name__ == "__main__":
    find_pages()
