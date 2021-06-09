import tkinter as tk
from PIL import Image, ImageDraw
from tkinter import filedialog
from tkinter import messagebox
import python.decensor as decensor
from python.gui.editor import create_drawing_canvas


def create_menu(self):
    self.menubar = tk.Menu(self.root)

    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.editmenu = tk.Menu(self.menubar, tearoff=0)
    self.viewmenu = tk.Menu(self.menubar, tearoff=0)
    self.aboutmenu = tk.Menu(self.menubar, tearoff=0)

    self.filemenu.add_command(
        label="Open", command=lambda: on_open_image_menu_clicked(self))
    self.filemenu.add_command(
        label="Make Image", command=lambda: on_decensor_menu_clicked(self))
    self.filemenu.add_command(
        label="Exit", command=lambda: on_close_menu_clicked(self))
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    self.editmenu.add_command(
        label="Undo", command=lambda: on_undo_menu_clicked(self))
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    self.aboutmenu.add_command(
        label="About", command=lambda: on_about_menu_clicked(self))
    self.menubar.add_cascade(label="About", menu=self.aboutmenu)

    self.root.config(menu=self.menubar)


def on_open_image_menu_clicked(self, event=None):
    open_image(self)


def on_save_menu_clicked(self, event=None):
    if self.file_name == 'untitled.ps':
        on_save_as_menu_clicked(self)
    else:
        actual_save(self)


def on_save_as_menu_clicked(self):
    file_name = filedialog.asksaveasfilename(
        master=self.root, filetypes=[('All Files', ('*.ps', '*.ps'))], title="Save...")
    if not file_name:
        return
    self.save_name = file_name
    actual_save(self)


def actual_save(self):
    self.canvas.img.save(self.save_name)
    # self.canvas.postscript(file=self.file_name, colormode='color')
    self.root.title(self.file_name)


def on_close_menu_clicked(self):
    close_window(self)


def close_window(self):
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        self.root.destroy()


def on_undo_menu_clicked(self, event=None):
    undo(self)


def undo(self):
    items_stack = list(self.canvas.find("all"))
    try:
        last_item_id = items_stack.pop()
    except IndexError:
        return
    self.canvas.delete(last_item_id)


def on_canvas_zoom_in_menu_clicked(self):
    canvas_zoom_in(self)


def on_canvas_zoom_out_menu_clicked(self):
    canvas_zoom_out(self)


def canvas_zoom_in(self):
    self.canvas.scale("all", 0, 0, 1.2, 1.2)
    self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
    self.canvas.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)


def canvas_zoom_out(self):
    self.canvas.scale("all", 0, 0, .8, .8)
    self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
    self.canvas.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)


def on_decensor_menu_clicked(self, event=None):
    messagebox.showinfo(
        "Decensoring", "Decensoring in progress... This may take a few minutes")
    self.root.title('Decensoring in progress...')
    combined_img = Image.alpha_composite(
        self.canvas.img.convert('RGBA'), self.drawn_img)
    decensorer = decensor.Decensor()
    decensorer.decensor_image(ori=self.canvas.img, colored=combined_img.convert(
        'RGB'))
    messagebox.showinfo(
        "Decensoring", "Decensoring complete!\nSaved on: decensor_output folder")

    self.root.title('Editing: ' + self.file_name)


def on_about_menu_clicked(self, event=None):
    messagebox.showinfo(
        "About", "2021 Editions by: DoginUwU\n\nFirst improviments by: liaoxiong3x\n")


def open_image(self):
    self.file_name = filedialog.askopenfilename(
        master=self.root, filetypes=[("Only png files", ('*.png'))], title="Open...")
    print(self.file_name)
    create_drawing_canvas(self)
    self.button_decensor.config(text='Click to enable decensor color')

    self.drawn_img = Image.new("RGBA", self.canvas.img.size)
    self.drawn_img_draw = ImageDraw.Draw(self.drawn_img)


def bind_menu_accelrator_keys(self):
    try:
        self.root.bind('<KeyPress-F1>', self.on_about_menu_clicked)
        self.root.bind('<Control-s>', self.on_save_menu_clicked)
        self.root.bind('<Control-S>', self.on_save_menu_clicked)
        self.root.bind('<Control-z>', self.on_undo_menu_clicked)
        self.root.bind('<Control-Z>', self.on_undo_menu_clicked)
    except:
        return
