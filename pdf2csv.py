import tabula
import os
import re
from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("./UDISE 2018-19/UDISE+2018_19_Booklet.pdf", "rb"))

def split_pdf():
  for i in range(7,117):
    output = PdfFileWriter()
    pageObj = inputpdf.getPage(i)
    output.addPage(pageObj)
    with open("./UDISE 2018-19/pdf_pages/document-page%s.pdf" % str(i+1), "wb") as outputStream:
      output.write(outputStream)

# split_pdf()

## convert PDF into CSV
def convert_pdf_to_csv():
  # files = ['document-page197.pdf']
  files = os.listdir('./UDISE 2018-19/pdf_pages/')
  for f in files:
    if f in [".DS_Store"]:
      continue
    print(f)
    
    try:
      df = tabula.read_pdf('./UDISE 2018-19/pdf_pages/' + f, area=[10.046,9.302,833.82,587.506], stream=True, pages=1)
      title = ""
      splitified = df[0].to_csv().split('\n')
      for i in range(len(splitified)):
        if "Table" in splitified[i]:
          title = splitified[i][2:]
          break
      title = title.replace(":", "")
      title = title.replace('"', "")
      title = title.replace('/', ", ")
      if "Unnamed" in title:
        title = re.sub(r'Unnamed \d', '', title)
        title = title.replace(",,", "")
    except:
      pass
    print(title)
    pageno = int(f[f.find("page")+4:f.find(".pdf")])
    try:
      tabula.convert_into('./UDISE 2018-19/pdf_pages/' + f, "./UDISE 2018-19/csv_files/" + title + " - page " + str(pageno) + ".csv", lattice=True, output_format="csv", pages='all')
    except Exception as e:
      print(e)

# convert_pdf_to_csv()

## rename CSV files
def rename_csv_files():
  files = os.listdir('./UDISE 2018-19/csv_files/')
  for f in files:
    if f == ".DS_Store":
      continue
    
    if ", -" in f:
      new_name = f.replace(", -", " -")
      os.rename('./UDISE 2018-19/csv_files/' + f, './UDISE 2018-19/csv_files/' + new_name)

rename_csv_files()