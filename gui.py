import tkinter as tk

import action
import spech_to_text
from avatar import AvatarCanvas


OBSIDIAN = "#05070b"
PANEL = "#0b1118"
CYAN = "#00d9ff"
MUTED = "#78a9b5"


def run_command(command):
    command = command.strip()
    if not command:
        return
    try:
        response = action.Action(command, root)
    except SystemExit:
        root.destroy()
        return
    output.insert(tk.END, f"YOU  > {command}\nASSISTANT > {response}\n\n")
    output.see(tk.END)


def send_command(event=None):
    command = entry.get()
    entry.delete(0, tk.END)
    run_command(command)


def ask_voice():
    avatar.set_listening(True)
    status.config(text="LISTENING FOR A VOICE COMMAND", fg=CYAN)
    root.update_idletasks()
    command = spech_to_text.spech_to_text()
    avatar.set_listening(False)
    status.config(text="READY FOR INPUT", fg="#d5faff")
    if command:
        run_command(command)
    else:
        output.insert(tk.END, "ASSISTANT > No voice command received. Type a command below.\n\n")
        output.see(tk.END)


def clear_output():
    output.delete("1.0", tk.END)
    output.insert(tk.END, "ASSISTANT > Conversation cleared. Ready for input.\n\n")


root = tk.Tk()
root.title("HERSHEY // AI ASSISTANT")
root.geometry("1050x700")
root.minsize(900, 620)
root.configure(bg=OBSIDIAN)

header = tk.Frame(root, bg=OBSIDIAN)
header.pack(fill=tk.X, padx=30, pady=(22, 10))
tk.Label(header, text="HERSHEY", bg=OBSIDIAN, fg=CYAN, font=("Consolas", 24, "bold")).pack(anchor=tk.W)
tk.Label(header, text="PERSONAL INTELLIGENCE // VOICE OUTPUT ONLINE", bg=OBSIDIAN, fg=MUTED, font=("Consolas", 9)).pack(anchor=tk.W, pady=(3, 0))

content = tk.Frame(root, bg=OBSIDIAN)
content.pack(fill=tk.BOTH, expand=True, padx=30)

avatar_panel = tk.Frame(content, bg=PANEL, highlightbackground="#123746", highlightthickness=1)
avatar_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 18))
tk.Label(avatar_panel, text="ACTIVE AVATAR", bg=PANEL, fg=MUTED, font=("Consolas", 9, "bold")).pack(pady=(16, 0))
avatar = AvatarCanvas(avatar_panel)

conversation = tk.Frame(content, bg=OBSIDIAN)
conversation.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
status = tk.Label(conversation, text="READY FOR INPUT", bg=PANEL, fg="#d5faff", anchor=tk.W, padx=14, pady=12, font=("Consolas", 10, "bold"))
status.pack(fill=tk.X)

output = tk.Text(conversation, bg="#071018", fg="#c5f8ff", insertbackground=CYAN, font=("Consolas", 10), relief=tk.FLAT, padx=16, pady=14, wrap=tk.WORD)
output.pack(fill=tk.BOTH, expand=True, pady=(12, 0))
output.insert(tk.END, "ASSISTANT > Systems online. Type a command and press SEND.\n\n")

input_panel = tk.Frame(conversation, bg=OBSIDIAN)
input_panel.pack(fill=tk.X, pady=(14, 0))
entry = tk.Entry(input_panel, bg="#0d1821", fg="#e7fdff", insertbackground=CYAN, relief=tk.FLAT, font=("Consolas", 11))
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=11)
entry.bind("<Return>", send_command)

send_button = tk.Button(input_panel, text="SEND", command=send_command, bg="#0d5f75", fg="white", activebackground="#168ba5", activeforeground="white", relief=tk.FLAT, font=("Consolas", 10, "bold"), padx=24, pady=10, cursor="hand2")
send_button.pack(side=tk.LEFT, padx=(10, 0))

controls = tk.Frame(conversation, bg=OBSIDIAN)
controls.pack(fill=tk.X, pady=(12, 18))
for label, command in (("ASK VOICE", ask_voice), ("CLEAR OUTPUT", clear_output)):
    tk.Button(controls, text=label, command=command, bg="#0d3442", fg="#d5faff", activebackground="#135b6e", activeforeground="white", relief=tk.FLAT, font=("Consolas", 9, "bold"), padx=16, pady=9, cursor="hand2").pack(side=tk.LEFT, padx=(0, 10))

root.after(250, entry.focus_set)
root.mainloop()
