from PyPDF2 import PdfReader, PdfWriter

def split_dissertation(input_pdf, chapter_pages):
    reader = PdfReader(input_pdf)
    
    for chapter, (start_page, end_page) in chapter_pages.items():
        writer = PdfWriter()
        
        # Add pages for this chapter
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])
            
        # Save the chapter as a separate PDF
        output_file = f"chapters/{chapter}.pdf"
        with open(output_file, "wb") as output:
            writer.write(output)

# Define page ranges for each chapter
chapter_pages = {
    "0_Dissertation_Setup": (1, 15), # 15 pages
    "1_Introduction": (16, 17), # 2 page
    "2_Background": (18, 52), # 34 pages
    "3_MTNCL_RTL_TO_GDS_FLOW": (53, 60), # 7 pages
    "4_Evaluation_Setup": (61, 86), # 25 pages
    "5_Results_and_Analysis": (87, 192), # 105 pages
    "6_Conclusions": (193, 200), # 7 pages
    "7_References": (201, 204) # 3 pages
}

# Introduction
# Background
# MTNCL RTL TO GDS FLOW
# Evaluation Setup
# Results and Analysis
# Conclusions
# References

# Split the PDF
split_dissertation("Dissertation Cole Sherrill Final.pdf", chapter_pages) 