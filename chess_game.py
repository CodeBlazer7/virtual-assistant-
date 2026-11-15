import random
import tkinter as tk

import chess


PIECE_GLYPHS = {
    "P": "♙",
    "N": "♘",
    "B": "♗",
    "R": "♖",
    "Q": "♕",
    "K": "♔",
    "p": "♟",
    "n": "♞",
    "b": "♝",
    "r": "♜",
    "q": "♛",
    "k": "♚",
}


class ChessGame:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Hershey // Chess")
        self.window.configure(bg="#05070b")
        self.window.resizable(False, False)
        self.board = chess.Board()
        self.selected = None
        self.square_size = 64

        tk.Label(self.window, text="CHESS // YOU PLAY WHITE", bg="#05070b", fg="#00d9ff", font=("Consolas", 14, "bold")).pack(pady=(14, 4))
        self.status = tk.Label(self.window, text="Select one of your pieces", bg="#05070b", fg="#b8f7ff", font=("Consolas", 10))
        self.status.pack(pady=(0, 10))
        self.canvas = tk.Canvas(self.window, width=512, height=512, bg="#05070b", highlightthickness=0)
        self.canvas.pack(padx=14)
        tk.Button(self.window, text="CLOSE CHESS", command=self.window.destroy, bg="#0d3442", fg="#d5faff", relief=tk.FLAT, font=("Consolas", 9, "bold"), padx=14, pady=7).pack(pady=12)
        self.canvas.bind("<Button-1>", self.select_square)
        self.draw_board()

    def square_at(self, event):
        file_index = event.x // self.square_size
        rank_index = event.y // self.square_size
        if 0 <= file_index < 8 and 0 <= rank_index < 8:
            return chess.square(file_index, 7 - rank_index)
        return None

    def select_square(self, event):
        if self.board.is_game_over():
            return
        square = self.square_at(event)
        if square is None:
            return

        if self.selected is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == chess.WHITE:
                self.selected = square
                self.status.config(text="Choose a highlighted destination")
                self.draw_board()
            return

        move = chess.Move(self.selected, square)
        if move in self.board.legal_moves:
            self.board.push(move)
            self.selected = None
            self.status.config(text="Hershey is thinking...")
            self.draw_board()
            if not self.finish_if_needed():
                self.window.after(350, self.computer_move)
        else:
            self.selected = None
            self.status.config(text="That move is not legal. Select a white piece.")
            self.draw_board()

    def computer_move(self):
        if self.board.is_game_over():
            return
        legal_moves = list(self.board.legal_moves)
        if legal_moves:
            self.board.push(random.choice(legal_moves))
        self.status.config(text="Your move: select a white piece")
        self.draw_board()
        self.finish_if_needed()

    def finish_if_needed(self):
        if not self.board.is_game_over():
            return False
        if self.board.is_checkmate():
            winner = "You win!" if self.board.turn == chess.BLACK else "Hershey wins this round!"
        else:
            winner = "Draw game. Good battle!"
        self.status.config(text=winner)
        return True

    def draw_board(self):
        self.canvas.delete("all")
        light = "#173b4a"
        dark = "#071722"
        for rank in range(8):
            for file_index in range(8):
                square = chess.square(file_index, 7 - rank)
                color = light if (rank + file_index) % 2 == 0 else dark
                if square == self.selected:
                    color = "#0d91ad"
                elif self.selected is not None and chess.Move(self.selected, square) in self.board.legal_moves:
                    color = "#175f6e"
                x1 = file_index * self.square_size
                y1 = rank * self.square_size
                self.canvas.create_rectangle(x1, y1, x1 + self.square_size, y1 + self.square_size, fill=color, outline="#0a2630")
                piece = self.board.piece_at(square)
                if piece:
                    glyph = PIECE_GLYPHS[piece.symbol()]
                    self.canvas.create_text(x1 + 32, y1 + 31, text=glyph, fill="#d5faff" if piece.color else "#5ce1e6", font=("Segoe UI Symbol", 36))


def launch_chess(parent):
    if parent is None:
        parent = tk.Tk()
        game = ChessGame(parent)
        parent.mainloop()
        return game
    return ChessGame(parent)
