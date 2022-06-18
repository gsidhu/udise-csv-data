import tabula
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("UDISE+2019_20_Booklet.pdf", "rb"))

for i in range(23,133):
    output = PdfFileWriter()
    pageObj = inputpdf.getPage(i)
    output.addPage(pageObj)
    with open("./pdf_pages/document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

## convert PDF into CSV
files = os.listdir('./pdf_pages/')
for f in files:
  if f == ".DS_Store":
    continue
  print(f)
  
  try:
    df = tabula.read_pdf('./pdf_pages/' + f, area=[4.973,28.611,49.343,586.296], pages=1)
    if df == []:
      df = tabula.read_pdf('./pdf_pages/' + f, area=[5.738,27.081,69.998,583.236], pages=1)
    title = df[0].to_csv().split(',')[1][1:]
    if "Table" not in title:
      title = df[0].to_csv().split(',')[2][1:]
    if "Table" not in title:
      title = f[:-4] + ".csv"
  except:
    pass

  pageno = int(f[f.find("page")+4:f.find(".pdf")]) + 1
  tabula.convert_into('./pdf_pages/' + f, "./csv_files/" + title + " - page " + str(pageno) + ".csv", lattice=True, output_format="csv", pages='all')


## rename CSV files
files = os.listdir('./csv_files/')

for f in files:
  if f == ".DS_Store":
    continue
  
  if ":" in f:
    print(f)
    new_name = f.replace(":", "")
    os.rename('./csv_files/' + f, './csv_files/' + new_name)