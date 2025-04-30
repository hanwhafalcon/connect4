import tkinter as tk
import time

ROWS = 6
COLS = 7
CIRCLE_SIZE = 80
PADDING = 10
COLORS = ["red", "yellow"]

class Connect4:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(
            root,
            width=COLS * (CIRCLE_SIZE + PADDING) + PADDING,
            height=ROWS * (CIRCLE_SIZE + PADDING) + PADDING,
            bg="blue"
        )
        self.canvas.pack()
        self.board = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.circles = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = 0
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self):
        for r in range(ROWS):
            for c in range(COLS):
                x1 = PADDING + c * (CIRCLE_SIZE + PADDING)
                y1 = PADDING + r * (CIRCLE_SIZE + PADDING)
                x2 = x1 + CIRCLE_SIZE
                y2 = y1 + CIRCLE_SIZE
                circle = self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
                self.circles[r][c] = circle

    def on_click(self, event):
        col = event.x // (CIRCLE_SIZE + PADDING)
        if col < 0 or col >= COLS:
            return
        row = self.get_available_row(col)
        if row is not None:
            self.animate_drop(row, col, self.current_player)
            self.board[row][col] = self.current_player
            self.current_player = 1 - self.current_player

    def get_available_row(self, col):
        for r in reversed(range(ROWS)):
            if self.board[r][col] is None:
                return r
        return None

    def animate_drop(self, target_row, col, player):
        for r in range(target_row + 1):
            if r > 0:
                self.canvas.itemconfig(self.circles[r - 1][col], fill="white")
            self.canvas.itemconfig(self.circles[r][col], fill=COLORS[player])
            self.root.update()
            time.sleep(0.05)

# Start GUI
root = tk.Tk()
root.title("Connect 4 - Animated")
game = Connect4(root)
root.mainloop()
