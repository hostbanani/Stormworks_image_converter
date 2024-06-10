from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter.filedialog import *
from compileImage import *
from loadingWindow import *
from showWindow import *
from GenerateXML import *
import threading
import os

def thread(fn):
    def execute(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return execute
    
class topWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Imager")
        self.geometry("210x270+300+300")
        self.resizable(0,0)
        self.filePath = ""
        
        ## try to find the icon
        try:
            self.iconbitmap('icon.ico')
        except Exception:
            pass
        try:
            self.iconbitmap(resource_path('icon.ico'))
        except Exception:
            pass
        
        ## add button to open image selection window
        self.button_path = Button(self,                  
             text="Select image",       
             width=25,height=2,     
             bg="red",fg="black",
             command=self.select_File)
        self.button_path.pack()
        
        ## add checkbox for mode selection
        self.sprite_mode = IntVar()
        self.sprite_mode_button = ttk.Checkbutton(text="sprite mode", variable=self.sprite_mode)
        self.sprite_mode_button.pack()
        
        ## add entry for controller name
        self.XMLNameL = Label(self, text="XML file name")       
        self.XMLNameL.pack()   
        self.XMLNameObj = Entry(self, width=20)   
        self.XMLNameObj.insert(1, "My controller") 
        self.XMLNameObj.pack()
        
        ## specify compression ratio
        self.senceL = Label(self, text="Compression ratio")       
        self.senceL.pack() 
        self.sensitivity = IntVar()
        self.sensitivity.set(5)
        self.sence = Spinbox(self, from_=0, to=15, width=5, textvariable=self.sensitivity)  
        self.sence.pack()
        
        ## add size specification
        ### for X value
        self.sizeL = Label(self, text="image size X")      
        self.sizeL.pack()
        
        self.XsizeInput = Entry(self, width=10)   
        self.XsizeInput.insert(1, "96") 
        self.XsizeInput.pack()
        
        ### for Y value
        self.sizeL = Label(self, text="image size Y")      
        self.sizeL.pack()
        
        self.YsizeInput = Entry(self, width=10)   
        self.YsizeInput.insert(1, "96") 
        self.YsizeInput.pack()
        
        ## main action buttons
        self.button_show = Button(self,                  
             text="Show image",       
             width=12,height=2,     
             bg="white",fg="black",
             command=self.ShowImage)      
        self.button_show.pack(side='left', anchor='n', expand=True) 
        
        self.button_creat = Button(self,                  
             text="Creat XML",       
             width=12,height=2,     
             bg="white",fg="black",
             command=self.CreatXML)      
        self.button_creat.pack(side='right', anchor='n', expand=True) 

        self.mainloop()
        
    def select_File(self): # file selector logic
        filename = askopenfilename(title="Select File",
        initialdir="/",
        filetypes = (("image", "*.jpg *.bmp *.png *.gif"),("image", "*.jpg *.bmp *.png *.gif")))
        if filename:
            self.filePath = filename
            self.button_path.configure(bg='green')

    @thread ## since the function may take a long time, it cannot be run in the main thread
    def ShowImage(self): ## function first converts the image to a code and then displays it on the screen as it will appear in the game
    
        if len(self.filePath) == 0: ## check if the image is selected, display error and stop process if not
            messagebox.showerror('Error', 'The image file is not selected!')
            return
            
        converter = ImageConverter(self.filePath) ## create converter and just open the selected image for now
        
        if self.sprite_mode.get() == 1: ## check for sprite mode activation, in sprite mode the original image size is used 
            size = converter.Image_file.size
        else:
            
            ## if sprite mode is off, then check if the size input is correct
            if not (self.XsizeInput.get().isdigit() and self.YsizeInput.get().isdigit()): 
                messagebox.showerror('Error', 'incorrect size values!')
                return ## if input is incorrect, display error and stop the process
                
            size = [int(self.XsizeInput.get()), int(self.YsizeInput.get())] ## get size from UI
            
        converter.ToPNG() ## workaround for displaying images (if the image is a gif, it will display only 1 frame, not all frames)
        
        load = LoadingWindow(self) ## create loading window to display compression and display progress
        code = converter.convert(size, int(self.sence.get()), False, load) ## start the long conversion process 
        del converter
        Show(self, size, code, load) ## even longer process. draw the image based on the code 
        load.destroy()

    @thread ## since the function may take a long time, it cannot be run in the main thread
    def CreatXML(self): ## create code and add XML to adddata
    
        ## before compressing the file, check if the parameters are correct and if there is a place to save the result
    
        if len(self.filePath) == 0: ## check if the image is selected, display error and stop process if not
            messagebox.showerror('Error', 'The image file is not selected!')
            return
            
        converter = ImageConverter(self.filePath) ## create converter and just open the selected image for now
        
        if self.sprite_mode.get() == 1: ## check for sprite mode activation, in sprite mode the original image size is used
        
            size = converter.Image_file.size
            converter.ToPNG() ## sprite mode also does not support gifs, for animated sprites convert all frames separately
            
        else:
        
            ## if sprite mode is off, then check if the size input is correct
            if not (self.XsizeInput.get().isdigit() and self.YsizeInput.get().isdigit()):
                messagebox.showerror('Error', 'incorrect size values!')
                return  ## if input is incorrect, display error and stop the process
                
            size = [int(self.XsizeInput.get()), int(self.YsizeInput.get())] ## get size from UI
            
        if len(self.XMLNameObj.get()) == 0: ## check if the name is entered, display error and stop process if not 
            messagebox.showerror('Error', 'the file name cannot be empty')
            return
        
        if os.path.exists(os.getenv('APPDATA')+'/Stormworks/data/microprocessors/'+self.XMLNameObj.get()+'.xml'): ## check if the specified file exists
            if not messagebox.askyesno('Warning', 'Save File '+self.XMLNameObj.get()+".xml already exists! Replace?"): ## ask what to do with the existing file
                return ## if it should not be touched, stop the function
            else:
                os.remove(os.getenv('APPDATA')+'/Stormworks/data/microprocessors/'+self.XMLNameObj.get()+'.xml') ## or delete the file to replace it
                
        ## compress the image
        
        load = LoadingWindow(self) ## create loading window to display compression progress
        
        code = converter.convert(size, int(self.sence.get()), (self.filePath[-4:] == ".gif" or self.sprite_mode.get() == 1), load) ## start the long conversion process 
        
        del converter
        
        load.destroy()
        
        ## then save the result in XML
        
        ## format the XML text
        if self.sprite_mode.get() == 1: ## if sprite mode is on
            XMLtext = CompileSprite(code, self.XMLNameObj.get())
        elif self.filePath[-4:] == ".gif": ## if a gif is used
            XMLtext = CompileGIF(code, self.XMLNameObj.get(), size)
        else: ## if a regular image
            XMLtext = CompileImage(code, self.XMLNameObj.get(), size)
        
        file = open(os.getenv('APPDATA')+'/Stormworks/data/microprocessors/'+self.XMLNameObj.get()+'.xml','w') ## create file in write mode in Stormworks save files
        file.write(XMLtext)
        file.close()
        messagebox.showinfo('Done', 'Save File '+self.XMLNameObj.get()+'.xml successfully created in '+os.getenv('APPDATA')+'/Stormworks/data/microprocessors')
             
win = topWindow()
