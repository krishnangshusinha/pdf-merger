# PDF MERGER

# Explanation:  First import the module pypdf2 that would help us to deal with pdf modification. Then we take the
#               list of the all the pdf that we need to merge. Then we use a merger, where we would store the 
#               merged form of pdf. Then we run a loop and travel through all the pdf , and open it in binary read
#               format, and open it in pdfreader format and then append it to the merger. And the end close the
#               opened file. And finally write it to a output file.



import PyPDF2          # this module helps us the deal with pdf

pdffile = ["1.pdf" , "2.pdf" , "3.pdf"]         # list of all the files that are to merged

merger = PyPDF2.PdfMerger()             # this is the merger

for file in pdffile:                # traversing through the list of pdfs

    pdf = open(file , 'rb')                 # opens the file in binary format and reads it
    pdfreader = PyPDF2.PdfReader(pdf)       # reading the file
    merger.append(pdfreader)                # merging to a single variable


pdf.close()
merger.write('merged.pdf')