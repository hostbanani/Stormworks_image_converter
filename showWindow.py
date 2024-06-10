from tkinter import *
from tkinter import ttk

class Show(Toplevel):
    def __init__(self, parent, size, code, load):
        super().__init__(parent)
        self.title("Image")
        load.set_progress(0)
        
            
        if size[1] > 96:
            self.geometry(str(size[0]*2+30) + "x" + str(size[1]*2+20) + "+300+300")
        else:
            self.geometry(str(size[0]*2+100) + "x" + str(size[1]*2+100) + "+300+300")
        self.resizable(0, 0)
        x = 1
        y = 1
        canvas = Canvas(self)
        char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        start_len = len(code)
        buf = ""
        while code != "" or buf != "":
            if len(buf) < 2000 and code != "":
                buf += code[:4000]
                code = code[4000:]
            load.set_progress(((start_len - len(code)) / start_len) * 100)
            if len(buf) < 4:
                break  # Stop if the remaining buffer is too small for further processing
            if buf[1] != "_":
                if buf[1] != "-":
                    try:
                        col = "#%02x%02x%02x" % (char.find(buf[1]) * 8, char.find(buf[2]) * 8, char.find(buf[3]) * 8)
                    except ValueError:
                        break  # Stop if the character is not found in char
                else:
                    try:
                        col = "#%02x%02x%02x" % (char.find(buf[2]) * 8, char.find(buf[2]) * 8, char.find(buf[2]) * 8)
                    except ValueError:
                        break  # Stop if the character is not found in char
                canvas.create_line(x * 2, y * 2, x * 2 + char.find(buf[0]) * 2, y * 2, fill=col)
                canvas.create_line(x * 2, y * 2 + 1, x * 2 + char.find(buf[0]) * 2, y * 2 + 1, fill=col)
                x += char.find(buf[0])
                if buf[1] != "-":
                    buf = buf[4:]
                else:
                    buf = buf[3:]
            else:
                x += char.find(buf[0])
                buf = buf[2:]
            if x > size[0]:
                x = 1
                y += 1
        canvas.place(relx=.5, rely=.5, anchor="c", height=size[1] * 2 + 4, width=size[0] * 2 + 4, bordermode='outside')
