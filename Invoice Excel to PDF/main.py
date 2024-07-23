import pandas as pd
import glob
from pathlib import Path
from fpdf import FPDF

filepaths =  glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P",unit="mm", format= "A4")
    pdf.add_page()
    fn = Path(filepath).stem
    invoice_nr, Date = fn.split('-')
    pdf.set_font(family="Times",size=12, style="BI")
    pdf.cell(w=50, h=8, txt=f"Invoice No. {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date: {Date}", ln=1)

    columns = list(df.columns)
    columns = [i.replace('-',' ').title() for i in columns]
    pdf.set_font(family="Times",size=8,style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=50, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for n,i in df.iterrows():
        pdf.set_font(family="Times",size=8)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(i["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(i["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(i["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(i["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(i["total_price"]), border=1, ln=1)
    
    sums = df["total_price"].sum()
    pdf.set_font(family="Times",size=8)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt = str(sums), border=1, ln=1)

    pdf.set_font(family="Times",size=8)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=0, h=12, txt=f"The Total Price is {sums}")
    
    pdf.output(f"PDFs/{fn}.pdf")

