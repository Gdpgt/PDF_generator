from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100) # RGB for gray. Goes from 0 to 254
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

pdf.output("output.pdf")
