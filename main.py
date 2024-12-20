import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import Frame, Label, Entry, Button, DISABLED, NORMAL
import random
import string

class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root['bg'] = '#cddafa'
        self.root.title('Вероятностный шифр')
        self.root.geometry('1100x600')

        frame = Frame(root, bg='white')
        frame.place(relx=0.05, rely=0.08, width=1000, height=500)

        labelInpt = Label(frame, text='Введите текст:', bg='#cddafa', font=("TkDefaultFont", 10), anchor="nw")
        labelInpt.grid(row=0, column=0, padx=80, pady=5, sticky='w')

        self.textInpt = ScrolledText(frame, width=100, height=8, relief="solid")
        self.textInpt.grid(row=1, column=0, padx=80, pady=5, sticky='w')

        labelKey = Label(frame, text='Ключ(32 байта):', bg='#cddafa', font=("TkDefaultFont", 10), anchor="nw")
        labelKey.grid(row=4, column=0, padx=80, pady=5, sticky='w')

        self.key = Entry(frame, width=133, borderwidth=1, relief="solid")
        self.key.grid(row=6, column=0, padx=80, pady=5, sticky="w")

        labelOutpt = Label(frame, text='Результат:', bg='#cddafa', font=("TkDefaultFont", 10), anchor="nw")
        labelOutpt.grid(row=7, column=0, padx=80, pady=5, sticky='w')

        self.textOutpt = ScrolledText(frame, width=100, height=8, relief="solid")
        self.textOutpt.grid(row=8, column=0, padx=80, pady=5, sticky='w')
        self.textOutpt.config(state=DISABLED)

        btnEncrypt = Button(frame, text='Хэшировать', bg='#cddafa', command=self.encrypt)
        btnEncrypt.grid(row=10, column=0, sticky="w", padx=80, pady=10)

    def encrypt(self):
        text = self.textInpt.get("1.0", "end-1c")
        key = self.key.get()

        if not key:
            key = self.generateRandomKey(32)
            self.key.delete(0, tk.END)
            self.key.insert(0, key)
            self.show_output(f"Сгенерированный ключ: {key}\n")

        elif len(key) != 32:
            self.show_output("Ключ должен быть 32 байта!")
            return

        hashed = self.sHash(text, key)
        self.show_output(hashed)

    def sHash(self, text, key):
        hashValue = 0
        for i, char in enumerate(text):
            hashValue += ord(char) ^ ord(key[i % len(key)])
        return hex(hashValue)

    def generateRandomKey(self, length):

        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def show_output(self, result):
        self.textOutpt.config(state=NORMAL)
        self.textOutpt.delete("1.0", "end")
        self.textOutpt.insert("1.0", result)
        self.textOutpt.config(state=DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()
