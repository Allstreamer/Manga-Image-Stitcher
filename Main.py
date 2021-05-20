from tkinter import filedialog
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image
from PIL import ImageColor
import os


class ImageStitcher:
    def __init__(self, master=None):
        self.inputFolderPath = "./"
        self.outputFolderPath = "./"
        self.images = []
        self.status = "Waiting..."

        # build ui
        self.TopLevel4 = tk.Tk() if master is None else tk.Toplevel(master)
        self.TopLevel4.title("Image Stitcher")
        self.MainFrame = ttk.Frame(self.TopLevel4)
        self.TitleFrame = ttk.Frame(self.MainFrame)
        self.TitleLabel = ttk.Label(self.TitleFrame)
        self.TitleLabel.configure(compound='bottom', text='Image Stitcher')
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
        self.StatusLabel.configure(text=self.status)
        self.StatusLabel.pack(side='right')
        self.RenderFrame.configure(height='200', width='200')
        self.RenderFrame.pack(side='top')
        self.MainFrame.configure(height='200', width='200')
        self.MainFrame.pack(side='top')
        self.TopLevel4.configure(height='200', width='200')

        # Main widget
        self.mainWindow = self.TopLevel4

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
        self.images = []
        for filename in sorted(os.listdir(self.inputFolderPath)):
            try:
                im = Image.open(f"{self.inputFolderPath}/{filename}")
                print(f"Found {filename}")
                self.images.append(im)
            except IOError:
                print(f"{filename} is not an image!")

    def render_image(self):
        print("Rendering")
        self.StatusLabel.config(text="Rendering...")
        self.load_images()

        total_width = 0
        total_height = 0

        for img in self.images:
            total_width = img.width if img.width > total_width else total_width

            total_height += img.height

        print(total_width, total_height)

        new_img = Image.new('RGB', (total_width, total_height), ImageColor.getrgb("#ffffff"))

        height_offset = 0
        for img in self.images:
            image_centering_buffer = int((total_width - img.width) / 2)

            new_img.paste(img, (image_centering_buffer, height_offset))

            height_offset += img.height

        print(self.outputFolderPath + "/Stitched.png")
        new_img.save(self.outputFolderPath + "/Stitched.png")
        self.StatusLabel.config(text="Done!")

    def run(self):
        self.mainWindow.mainloop()


if __name__ == '__main__':
    app = ImageStitcher()
    app.run()
