import tabula
import os
import re
from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("UDISE+2021_22_Booklet.pdf", "rb"))

# for i in range(22,207):
#     output = PdfFileWriter()
#     pageObj = inputpdf.getPage(i)
#     output.addPage(pageObj)
#     with open("./pdf_pages/document-page%s.pdf" % i, "wb") as outputStream:
#         output.write(outputStream)

## convert PDF into CSV
# files = os.listdir('./pdf_pages/')
# leftover_pages = ['document-page135.pdf', 'document-page176.pdf']
# files = ['document-page197.pdf']

# for f in files:
#   if f in [".DS_Store", "document-page24.pdf", "document-page23.pdf", "document-page22.pdf"]:
#     continue
#   print(f)
  
#   try:
#     # df = tabula.read_pdf('./pdf_pages/' + f, pages=1, stream=True)
#     # df = tabula.read_pdf('./pdf_pages/' + f, area=[4.973,28.611,49.343,586.296], pages=1)
#     # if df == []:
#     #   df = tabula.read_pdf('./pdf_pages/' + f, area=[5.738,27.081,69.998,583.236], pages=1)
#     df = tabula.read_pdf('./pdf_pages/' + f, area=[10.046,9.302,833.82,587.506], stream=True, pages=1)
    
#     # title = df[0].to_csv().split(',')[1][1:]
#     # if "Table" not in title:
#     #   title = df[0].to_csv().split(',')[2][1:]
#     # if "Table" not in title:
#     #   title = f[:-4] + ".csv"
#     title = ""
#     splitified = df[0].to_csv().split('\n')
#     for i in range(len(splitified)):
#       if "Table" in splitified[i]:
#         title = splitified[i][2:]
#         break
#     title = title.replace(":", "")
#     title = title.replace('"', "")
#     title = title.replace('/', ", ")
#   except:
#     pass
#   print(title)
#   pageno = int(f[f.find("page")+4:f.find(".pdf")]) + 1
#   try:
#     tabula.convert_into('./pdf_pages/' + f, "./csv_files/" + title + " - page " + str(pageno) + ".csv", lattice=True, output_format="csv", pages='all')
#   except Exception as e:
#     print(e)


## rename CSV files
files = os.listdir('./csv_files/')
for f in files:
  if f == ".DS_Store":
    continue
  
  if ", 2021-22, " in f:
    new_name = f.replace(", 2021-22, ", "")
    os.rename('./csv_files/' + f, './csv_files/' + new_name)
  # if "Unnamed" in f:
  #   print(f)
  #   # look for `Unnamed \d` and replace with `` using regex
  #   new_name = re.sub(r'Unnamed \d', '', f)
  #   new_name = new_name.replace(",,", "")
  #   print(new_name)
  #   os.rename('./csv_files/' + f, './csv_files/' + new_name)
