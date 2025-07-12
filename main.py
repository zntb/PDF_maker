from fpdf import FPDF
from fpdf.enums import XPos, YPos  # For new positioning system
import pandas as pd

# Initialize PDF
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    # Set font (required before adding text)
    pdf.set_font("helvetica", size=24, style="B")
    pdf.set_text_color(100, 100, 100)

    # Modern cell() usage without deprecated parameters:
    pdf.cell(
        w=0, 
        h=12, 
        text=row["Topic"], 
        border=0,
        align="L",
        new_x=XPos.LMARGIN,  # Replaces ln=1
        new_y=YPos.NEXT      # Replaces ln=1
    )
    pdf.line(10, 22, 200, 22)
    
    
    # Set the footer
    pdf.ln(265)
    pdf.set_font("helvetica", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, text=row["Topic"], border=0, align="R", new_x=XPos.RMARGIN, new_y=YPos.NEXT)
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font("helvetica", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, text=row["Topic"], border=0, align="R", new_x=XPos.RMARGIN, new_y=YPos.NEXT)

# Modern output() usage without deprecated "dest" parameter:
pdf.output("output.pdf")  # Removed "F" parameter