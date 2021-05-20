from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image
from PIL import ImageColor
import os

class ImageSticher:
    def __init__(self, master=None):
        self.inputFolderPath = "./"
        self.outputFolderPath = "./"
        self.images = []

        # build ui
        self.toplevel4 = tk.Tk() if master is None else tk.Toplevel(master)
        self.MainFrame = ttk.Frame(self.toplevel4)
        self.TitleFrame = ttk.Frame(self.MainFrame)
        self.TitleLabel = ttk.Label(self.TitleFrame)
        self.TitleLabel.configure(compound='bottom', text='Image Sticher')
        self.TitleLabel.pack(side='top')
        self.TitleFrame.configure(height='200', width='200')
        self.TitleFrame.pack(side='top')
        self.InputFrame = ttk.Frame(self.MainFrame)
        self.InputPathLabel = ttk.Label(self.InputFrame)
        self.InputPathLabel.configure(text='Input Folder Path:')
        self.InputPathLabel.pack(side='top')
        self.InputPathEntry = ttk.Entry(self.InputFrame)
        _text_ = self.inputFolderPath
        self.InputPathEntry.delete('0', 'end')
        self.InputPathEntry.insert('0', _text_)
        self.InputPathEntry.pack(side='left')
        self.InputPathOpenButton = ttk.Button(self.InputFrame)
        self.InputPathOpenButton.configure(text='Open', command=self.get_input_folder)
        self.InputPathOpenButton.pack(side='right')
        self.InputFrame.configure(height='200', width='200')
        self.InputFrame.pack(side='top')
        self.OutputFrame = ttk.Frame(self.MainFrame)
        self.OutputPathLabel = ttk.Label(self.OutputFrame)
        self.OutputPathLabel.configure(text='Output Folder Path:')
        self.OutputPathLabel.pack(side='top')
        self.OutputPathEntry = ttk.Entry(self.OutputFrame)
        _text_ = self.inputFolderPath
        self.OutputPathEntry.delete('0', 'end')
        self.OutputPathEntry.insert('0', _text_)
        self.OutputPathEntry.pack(side='left')
        self.OutputPathOpen = ttk.Button(self.OutputFrame)
        self.OutputPathOpen.configure(text='Open', command=self.get_output_folder)
        self.OutputPathOpen.pack(side='right')
        self.OutputFrame.configure(height='200', width='200')
        self.OutputFrame.pack(side='top')
        self.RenderFrame = ttk.Frame(self.MainFrame)
        self.RenderButton = ttk.Button(self.RenderFrame)
        self.RenderButton.configure(text='Render', command=self.render_image)
        self.RenderButton.pack(side='left')
        self.StatusLabel = ttk.Label(self.RenderFrame)
        self.StatusLabel.configure(text='Waiting...')
        self.StatusLabel.pack(side='right')
        self.RenderFrame.configure(height='200', width='200')
        self.RenderFrame.pack(side='top')
        self.MainFrame.configure(height='200', width='200')
        self.MainFrame.pack(side='top')
        self.toplevel4.configure(height='200', width='200')

        # Main widget
        self.mainWindow = self.toplevel4

    def get_input_folder(self):
        print("selecting Input Folder")
        filename = filedialog.askdirectory()
        self.inputFolderPath = filename
        self.InputPathEntry.delete('0', 'end')
        self.InputPathEntry.insert('0', self.inputFolderPath)

    def get_output_folder(self):
        print("selecting Output Folder")
        filename = filedialog.askdirectory()
        self.outputFolderPath = filename
        self.OutputPathEntry.delete('0', 'end')
        self.OutputPathEntry.insert('0', self.outputFolderPath)

    def load_images(self):
        for filename in os.listdir(self.inputFolderPath):
            try:
                im = Image.open(f"{self.inputFolderPath}/{filename}")
                print(f"Found {filename}")
                self.images.append(im)
            except IOError:
                print(f"{filename} is not an image!")

    def render_image(self):
        print("Rendering")
        self.load_images()

        TotalWidth = 0
        TotalHeight = 0

        for img in self.images:
            if img.width > TotalWidth:
                TotalWidth = img.width

            TotalHeight += img.height

        print(TotalWidth, TotalHeight)

        newImg = Image.new('RGB', (TotalWidth, TotalHeight),ImageColor.getrgb("#ffffff"))

        heightOffset = 0
        for img in self.images:
            ImageCenteringBuffer = int((TotalWidth - img.width) / 2)

            newImg.paste(img, (ImageCenteringBuffer, heightOffset))

            heightOffset += img.height

        print(self.outputFolderPath + "/stiched.png")
        newImg.save(self.outputFolderPath + "/stiched.png")

    def run(self):
        self.mainWindow.mainloop()


if __name__ == '__main__':
    app = ImageSticher()
    app.run()
