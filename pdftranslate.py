import tkinter as tk
import PyPDF2
import googletrans


from tkinter.filedialog import askopenfile


root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=500)
canvas.grid(columnspan=3, rowspan=3)

#Heading

heading = tk.Label(root, text="Sinhalen PDF", font="Raleway")
heading.grid(columnspan=1, column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to translate to Sinhala", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("loading")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()


        from googletrans import Translator

        file_translate = Translator(service_urls=['translate.googleapis.com'])


        result =  file_translate.translate(page_content, dest='si')
        print(result.text)

        text_box = tk.Text(root, height=50, width=133, padx=15, pady=15)
        text_box.insert(1.0, result.text)
        text_box.tag_configure("left", justify="left")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Translate")


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#abdbe3", fg="white", height=2, width=15)
browse_text.set("Translate")
browse_btn.grid(column=1, row=2)



canvas = tk.Canvas(root, width=1000, height=400)
canvas.grid(columnspan=3)

root.mainloop()