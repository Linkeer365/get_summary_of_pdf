import os
import PyPDF2

target_dir=r"D:\AllDowns\newbooks"

output_name="summary.pdf"

books=sorted(os.listdir(target_dir),key=lambda x: os.path.getmtime(os.path.join(target_dir, x)),reverse=True)
books=[book for book in books if book.endswith(".pdf")]

all_pages=[]
all_booknames=[]

page_num=10
for each_book in books:
    book_path=f"{target_dir}{os.sep}{each_book}"
    rd=PyPDF2.PdfFileReader(book_path)
    # 一般是从第2页到第11页之间，一共10页...
    # 这里是保险起见，反正（从前翻起的话）每次翻动的页数都差不多...
    pages=[rd.getPage(each) for each in range(1,1+page_num)]
    all_booknames.append(each_book)
    all_pages.extend(pages)

wt=PyPDF2.PdfFileWriter()


for each_idx,each in enumerate(all_pages):
    wt.addPage(each)
    if each_idx%page_num==0:
        wt.addBookmark(title=all_booknames[each_idx//page_num],pagenum=each_idx)

output_fd=open(f"{target_dir}{os.sep}{output_name}","wb")
wt.write(output_fd)
output_fd.close()

print("done.")