from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    #set the header
    pdf.set_font(family= "times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    #add line
    for y in range(20, 290, 10):
        pdf.line(10, y, 200, y)

    #set the footer
    pdf.ln(260)
    pdf.set_font(family="times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # for add page
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # add line
        for y in range(20, 290, 10):
            pdf.line(10, y, 200, y)

        # set the footer
        pdf.ln(270)
        pdf.set_font(family="times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")