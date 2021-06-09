import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


def create_top_bar(self):
    self.top_bar = tk.Frame(self.root, height=25,
                            relief="raised", bg=self.background_menu)
    self.top_bar.pack(fill="x", side="top")


def create_tool_bar(self):
    self.tool_bar = tk.Frame(self.root, relief="raised",
                             width=1400, height=45, bg=self.background_menu)
    self.tool_bar.pack(side="top")


def create_tool_bar_buttons(self):
    for index, name in enumerate(self.tool_bar_functions):
        self.button_decensor = tk.Button(
            self.tool_bar, text='Click to enable decensor color', fg='#FFF', command=lambda index=index: self.on_tool_bar_button_clicked(index), bg=self.background_menu, border=0)
        self.button_decensor.place(x=index + 20, y=10)


def create_drawing_canvas(self):
    self.canvas_frame = tk.Frame(
        self.root, width=1300, height=600, bg=self.background_gray, border=0, highlightthickness=0, padx=0, pady=0)
    self.canvas_frame.place(x=40, y=60)
    self.canvas = tk.Canvas(self.canvas_frame, background=self.background_gray,
                            width=1300, height=600, scrollregion=(0, 0, 1400, 900), highlightthickness=0)
    create_scroll_bar(self)

    self.canvas.img = Image.open(self.file_name).convert('RGBA')
    self.canvas.tk_img = ImageTk.PhotoImage(self.canvas.img)
    self.canvas.create_image(0, 0, image=self.canvas.tk_img, anchor="nw")
    self.canvas.config(scrollregion=(
        0, 0, self.canvas.img.size[0], self.canvas.img.size[1]))
    self.root.title('Editing: ' + self.file_name)


def create_scroll_bar(self):
    self.x_scroll = tk.Scrollbar(self.canvas_frame, orient="horizontal")
    self.x_scroll.pack(side="bottom", fill="x")
    self.x_scroll.config(command=self.canvas.xview)

    self.y_scroll = tk.Scrollbar(self.canvas_frame, orient="vertical")
    self.y_scroll.pack(side="right", fill="y")
    self.y_scroll.config(command=self.canvas.yview)

    self.canvas.configure(yscrollcommand=self.y_scroll.set,
                          xscrollcommand=self.x_scroll.set)
    self.canvas.pack()


def xview(self, event, pos):
    print(self.x_scroll.get())
    self.canvas.xview(event, 1 - (float(pos)))


def yview(self, event, pos):
    self.canvas.yview(event, 1 - (float(pos)))


def remove_options_from_top_bar(self):
    for child in self.top_bar.winfo_children():
        child.destroy()


def show_selected_tool_icon_in_top_bar(self, function_name):
    return


def draw_line_options(self):
    create_width_options_combobox(self)


def create_width_options_combobox(self):
    posX = 250
    tk.Label(self.tool_bar, text='Width:', fg="#FFF",
             bg=self.background_menu).place(x=posX, y=10)
    self.width_combobox = ttk.Combobox(
        self.tool_bar, state='readonly', width=3)
    self.width_combobox.place(x=posX + 50, y=10)
    self.width_combobox['values'] = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50)
    self.width_combobox.bind('<<ComboboxSelected>>', self.set_brush_width)
    self.width_combobox.set(self.brush_width)


def draw_irregular_line(self):
    self.draw = ImageDraw.Draw(self.canvas.img)
    self.draw.line((self.start_x, self.start_y, self.end_x,
                   self.end_y), fill=self.fill, width=int(self.brush_width))
    display_canvas(self)

    self.canvas.bind(
        "<B1-Motion>", lambda event: draw_irregular_line_update_x_y(self, event))


def display_canvas(self):
    if self.canvas.img is None:
        return
    if self.drawn_img is None:
        return

    composite_img = Image.alpha_composite(
        self.canvas.img.convert('RGBA'), self.drawn_img).convert('RGB')
    self.canvas.tk_img = ImageTk.PhotoImage(composite_img)

    self.canvas.create_image(0, 0, image=self.canvas.tk_img, anchor="nw")


def draw_irregular_line_update_x_y(self, event=None):
    self.start_x, self.start_y = self.end_x, self.end_y
    self.end_x, self.end_y = adjust_canvas_coords(self, event.x, event.y)
    draw_irregular_line(self)


def adjust_canvas_coords(self, x_coordinate, y_coordinate):
    print(self.x_scroll.get())
    low_x = self.x_scroll.get()[0]
    low_y = self.y_scroll.get()[0]
    return low_x * self.canvas.img.size[0] + x_coordinate, low_y * self.canvas.img.size[1] + y_coordinate
