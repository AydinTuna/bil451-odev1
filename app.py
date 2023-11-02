import tkinter as tk
from tkinter import filedialog


def addFile():
    filePath = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt")])
    filePathLabel = tk.Label(filePath)


mainForm = tk.Tk()
mainForm.title("RegEx/Morphological Analysis")

addFileButton = tk.Button(mainForm, text="Add File", command=addFile)
addFileButton.pack(pady=20)


mainForm.mainloop()
