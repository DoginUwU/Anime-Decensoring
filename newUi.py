import time
import tkinter as tk
from python.gui.menu import create_menu, bind_menu_accelrator_keys
from python.gui.editor import draw_line_options, create_tool_bar, create_drawing_canvas, create_tool_bar_buttons, show_selected_tool_icon_in_top_bar, draw_irregular_line


class AnimeDecensoring(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.drawn_img = None
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.start_x, self.start_y = 0, 0
        self.end_x, self.end_y = 0, 0
        self.current_item = None
        self.fill = "#00ff00"
        self.fill_pil = (0, 255, 0, 255)
        self.brush_width = 2
        self.background = '#222'
        self.background_menu = '#9152ff'
        self.background_gray = '#171717'
        self.file_name = './python/icons/without_image.png'
        self.save_name = './decensor_input/' + str(time.time()) + '.png'
        self.tool_bar_functions = ["draw_irregular_line"]
        self.root.geometry('1400x700')
        self.root.configure(bg=self.background)
        self.root.resizable(0, 0)
        self.root.title('Choose a .png file')

        self.create_gui()

    def create_gui(self):
        create_menu(self)
        create_tool_bar(self)
        create_tool_bar_buttons(self)
        create_drawing_canvas(self)
        bind_menu_accelrator_keys(self)
        # show_selected_tool_icon_in_top_bar(self, self.tool_bar_functions[0])
        draw_line_options(self)
        self.on_tool_bar_button_clicked(0)

    def set_fill(self, event=None):
        fill_color = self.fill_combobox.get()
        if fill_color == 'none':
            self.fill = ''  # transparent
        elif fill_color == 'fg':
            self.fill = self.foreground
        elif fill_color == 'bg':
            self.fill = self.background
        else:
            self.fill = fill_color

    def set_outline(self, event=None):
        outline_color = self.outline_combobox.get()
        if outline_color == 'none':
            self.outline = ''  # transparent
        elif outline_color == 'fg':
            self.outline = self.foreground
        elif outline_color == 'bg':
            self.outline = self.background
        else:
            self.outline = outline_color

    def set_brush_width(self, event):
        self.brush_width = float(self.width_combobox.get())

    def remove_options_from_top_bar(self):
        # for child in self.top_bar.winfo_children():
        #    child.destroy()
        return

    def bind_mouse(self):
        self.canvas.bind("<Button-1>", self.on_mouse_button_pressed)
        self.canvas.bind(
            "<Button1-Motion>", self.on_mouse_button_pressed_motion)
        self.canvas.bind(
            "<Button1-ButtonRelease>", self.on_mouse_button_released)
        self.canvas.bind("<Motion>", self.on_mouse_unpressed_motion)

    def on_tool_bar_button_clicked(self, button_index):
        self.selected_tool_bar_function = self.tool_bar_functions[button_index]
        self.remove_options_from_top_bar()
        self.button_decensor.config(text='Decensor color enabled')
        # self.display_options_in_the_top_bar()
        self.bind_mouse()

    def display_options_in_the_top_bar(self):
        show_selected_tool_icon_in_top_bar(
            self, self.selected_tool_bar_function)
        options_function_name = "{}_options".format(
            self.selected_tool_bar_function)
        func = getattr(self, options_function_name, self.function_not_defined)
        func()

    def on_mouse_button_pressed(self, event):
        self.start_x = self.end_x = self.canvas.canvasx(event.x)
        self.start_y = self.end_y = self.canvas.canvasy(event.y)
        self.execute_selected_method()

    def on_mouse_button_pressed_motion(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.delete(self.current_item)
        self.execute_selected_method()

    def on_mouse_button_released(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)

    def on_mouse_unpressed_motion(self, event):
        return

    def execute_selected_method(self):
        self.current_item = None
        draw_irregular_line(self)
        # func = getattr(
        #     self, self.selected_tool_bar_function, self.function_not_defined)
        # func()


if __name__ == '__main__':
    root = tk.Tk()
    app = AnimeDecensoring(root)
    root.mainloop()
