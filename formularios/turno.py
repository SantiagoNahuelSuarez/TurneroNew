from enum import Enum
import tkinter as tk
from tkinter.font import Font


class Side(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 3


class ControlLabel(tk.Frame):
    def __init__(self, parent, *args, text="", **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self._inner_label = tk.Label(self, text=text, bg=kwargs.get("bg", ""))
        self._inner_label.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(0)

        font = Font(font=self._inner_label["font"])
        text_width = font.measure(text)
        text_height = font.metrics('linespace')

        self._min_height = max(kwargs.get("height", text_height), text_height)
        self._min_width = max(kwargs.get("width", text_width), text_width)
        self.configure(height=self._min_height, width=self._min_width)

        self.max_side_trigger_dist = 5

        self._start_x = 0
        self._start_y = 0
        self._start_height = 0
        self._start_width = 0
        self._clicked_side = None

        self._inner_label.bind("<Motion>", self.on_mouse_move)
        self._inner_label.bind("<B1-Motion>", self.on_mouse_drag)

    def on_mouse_drag(self, event):
        x = self.winfo_x()
        y = self.winfo_y()
        height = self.winfo_height()

        match self._clicked_side:
            case Side.TOP:
                bottom_left_y = height + y
                height = min(max(self._min_height, height - event.y), bottom_left_y)
                y = bottom_left_y - height
            case Side.BOTTOM:
                height = min(max(self._min_height, event.y), self.parent.winfo_height() - y)
            case _:
                max_x = self.parent.winfo_width() - self._start_width
                max_y = self.parent.winfo_height() - self._start_height
                x = min(max(0, x - self._start_x + event.x), max_x)
                y = min(max(0, y - self._start_y + event.y), max_y)

        self.place(x=x, y=y, height=height)

    def on_mouse_move(self, event):
        self._start_x = event.x
        self._start_y = event.y
        self._start_width = self.winfo_width()
        self._start_height = self.winfo_height()

        # Verificar si el click fue en esquinas
        if event.y <= self.max_side_trigger_dist:
            self._clicked_side = Side.TOP
            self.configure(cursor="top_side")

        elif event.y >= self._start_height - self.max_side_trigger_dist:
            self._clicked_side = Side.BOTTOM
            self.configure(cursor="bottom_side")
        else:
            self._clicked_side = None
            self.configure(cursor="hand1")


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.principal_body = tk.Frame(self, bg="white")
        self.principal_body.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)
        self.principal_body_controls()

    def principal_body_controls(self):
        self.control_label = ControlLabel(
            self.principal_body,
            text="Stack Overflow en Español",
            bg="green",
            width=300,
            height=30
            )
        self.control_label.place(x=100, y=100)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    App(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()