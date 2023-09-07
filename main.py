from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
total_pdf_pages = df['Pages'].sum()

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)  # Essential for the footer to be correctly placed
count = 0

for index, row in df.iterrows():
    pdf.add_page()
    count += 1

    # Header :
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    # Adding lines :
    for y in range(31, 286, 10):
        pdf.line(10, y, 200, y)

    # Footer :
    pdf.ln(265)  # The total A4 page is 297m long
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f"{row['Topic']} {count}/{total_pdf_pages}", align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        count += 1

        # Adding lines :
        for y in range(21, 286, 10):
            pdf.line(10, y, 200, y)

        # Footer :
        pdf.ln(277)  # longer than the previous footer because there are no header
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=f"{row['Topic']} {count}/{total_pdf_pages}", align="R")

pdf.output("Note_sheets.pdf")
