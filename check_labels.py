import pypdf

def find_offset():
    pdf_path = "introduction-to-linear-algebra-fifth-edition-5nbsped-0980232775-9780980232776_compress.pdf"
    
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        total_pages = len(reader.pages)
        print(f"Total pages: {total_pages}")
        
        try:
            # Check if there are page labels
            labels = reader.trailer["/Root"].get("/PageLabels")
            if labels:
                print("Page labels found.")
            else:
                print("No page labels.")
        except Exception as e:
            print(f"Error checking labels: {e}")

if __name__ == '__main__':
    find_offset()
