import math
import tkinter as tk


class AvatarCanvas:
    """Animated cyan geometric assistant face embedded in the main window."""

    def __init__(self, parent, width=360, height=360):
        self.canvas = tk.Canvas(parent, width=width, height=height, bg="#05070b", highlightthickness=0)
        self.width = width
        self.height = height
        self.phase = 0.0
        self.listening = False
        self.canvas.pack(pady=(18, 8))
        self.animate()

    def set_listening(self, listening):
        self.listening = listening

    def animate(self):
        self.draw()
        self.canvas.after(55, self.animate)

    def draw(self):
        self.canvas.delete("all")
        self.phase += 0.11
        pulse = (math.sin(self.phase) + 1) / 2
        glow = int(95 + pulse * 90)
        cyan = f"#00{glow:02x}ff"
        bright = "#b8f7ff"
        cx, cy = self.width // 2, 166
        outer = 112 + pulse * 3
        inner = 92 + pulse * 2

        self.canvas.create_oval(cx - outer, cy - outer, cx + outer, cy + outer, outline="#003b50", width=2)
        self.canvas.create_oval(cx - inner, cy - inner, cx + inner, cy + inner, outline=cyan, width=2)

        mask = [cx - 74, cy - 64, cx + 74, cy - 64, cx + 94, cy - 20, cx + 62, cy + 74, cx, cy + 96, cx - 62, cy + 74, cx - 94, cy - 20]
        self.canvas.create_polygon(mask, outline=bright, fill="#071722", width=3)
        self.canvas.create_line(cx - 74, cy - 64, cx - 105, cy - 37, fill=cyan, width=2)
        self.canvas.create_line(cx + 74, cy - 64, cx + 105, cy - 37, fill=cyan, width=2)
        self.canvas.create_line(cx - 94, cy - 20, cx - 119, cy + 4, fill=cyan, width=2)
        self.canvas.create_line(cx + 94, cy - 20, cx + 119, cy + 4, fill=cyan, width=2)
        self.canvas.create_line(cx - 60, cy - 14, cx - 16, cy - 6, fill=bright, width=5)
        self.canvas.create_line(cx + 16, cy - 6, cx + 60, cy - 14, fill=bright, width=5)
        self.canvas.create_oval(cx - 52, cy - 18, cx - 44, cy - 10, fill=cyan, outline="")
        self.canvas.create_oval(cx + 44, cy - 18, cx + 52, cy - 10, fill=cyan, outline="")
        self.canvas.create_line(cx, cy - 4, cx - 8, cy + 36, fill=cyan, width=3)
        self.canvas.create_line(cx - 8, cy + 36, cx + 12, cy + 36, fill=cyan, width=3)
        self.canvas.create_line(cx - 36, cy + 56, cx + 36, cy + 56, fill=bright, width=3)
        self.canvas.create_line(cx - 20, cy + 68, cx + 20, cy + 68, fill=cyan, width=2)
        label = "LISTENING" if self.listening else "ONLINE"
        self.canvas.create_text(cx, 318, text=f"{label} // VOICE OUTPUT READY", fill=cyan, font=("Consolas", 10, "bold"))
