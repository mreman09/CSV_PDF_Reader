import csv
import PyPDF2

data = open('example.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)


full_name = []
all_id = []

for line in data_lines[1:]:
    all_id.append(line[3])
    full_name.append(line[1]+ ' '+ line[2])

file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(full_name)
print(all_id)
print(full_name)
file_to_output.close()




f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(f)
page_one = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfWriter()

pdf_writer.addPage(page_one)
pdf_output = open('New_PDF.pdf', 'wb')
pdf_writer.write(pdf_output)

page_1_text = page_one.extractText()
print(page_1_text)

pdf_text = []

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

f.close()
pdf_output.close()

print(pdf_text[0])
print(pdf_text[1])