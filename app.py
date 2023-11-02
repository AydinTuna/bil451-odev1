import tkinter as tk
from tkinter import filedialog
import re


def addFile():
    if not filePath.get():
        filePath.set(filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")]))
        if filePath.get():
            addFileButton.config(state="disabled")
            fileContent.set(readFileContent(filePath.get()))


def search():
    pattern = regexTextBox.get()
    file_content = fileContent.get()
    if pattern and file_content:
        filtered_text = filterText(pattern, file_content)
        showResults(filtered_text)


def showResults(results):
    resultWindow = tk.Toplevel(mainForm)
    resultWindow.title("Search Results")
    resultWindow.geometry("600x500")

    resultListbox = tk.Listbox(resultWindow, width=600, height=500)
    resultListbox.pack(padx=10, pady=10)

    for item in results:
        resultListbox.insert(tk.END, item)


def performMorphologicalAnalysis():
    # todo
    pass


def openAnalysisPage():
    analysisWindow = tk.Toplevel(mainForm)
    analysisWindow.title("Morphological Analysis")
    analysisWindow.geometry("600x500")

    analysisLabel = tk.Label(analysisWindow, text="Morphological Analysis:")
    analysisLabel.pack(pady=20)

    analysisButton = tk.Button(
        analysisWindow, text="Analysis", command=performMorphologicalAnalysis)
    analysisButton.pack(pady=20)


def readFileContent(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            print("file content: ", content)
            return content
    except FileNotFoundError:
        print("File is not found")
    except Exception as e:
        print(f"Error: {e}")


def filterText(pattern, text):
    try:
        filtered_text = re.findall(pattern, text)
        return filtered_text
    except re.error as e:
        print(f"Regex Error: {e}")
        return []


mainForm = tk.Tk()
mainForm.title("RegEx/Morphological Analysis")
mainForm.geometry("600x500")

filePath = tk.StringVar()
fileContent = tk.StringVar()

addFileButton = tk.Button(mainForm, text="Add File", command=addFile)
addFileButton.grid(row=0, column=0, pady=20, padx=10)

filePathLabel = tk.Label(mainForm, text="Selected file path: ")
filePathLabel.grid(row=0, column=1, pady=20, padx=10)

filePathTextLabel = tk.Label(mainForm, textvariable=filePath)
filePathTextLabel.grid(row=0, column=2, pady=20, padx=10)

regexLabel = tk.Label(mainForm, text="Regex search:")
regexLabel.grid(row=2, column=0, pady=10, padx=10)

regexTextBox = tk.Entry(mainForm)
regexTextBox.grid(row=2, column=1, pady=10, padx=10)

searchButton = tk.Button(mainForm, text="Search", command=search)
searchButton.grid(row=2, column=2, pady=10, padx=10)

analysisLabel = tk.Label(mainForm, text="Morphological Analysis:")
analysisLabel.grid(row=3, column=0, pady=10, padx=10)

analysisButton = tk.Button(mainForm, text="Analysis", command=openAnalysisPage)
analysisButton.grid(row=3, column=1, pady=10, padx=10)

mainForm.mainloop()
