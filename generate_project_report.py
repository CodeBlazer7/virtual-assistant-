from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT = Path(__file__).with_name("Himank_Gupta_AI_Assistant_Project.pdf")
TOTAL_PAGES = 24

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=31, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="CoverSubtitle", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=18, leading=24, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="PageTitle", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=20, leading=25, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=17, spaceBefore=8, spaceAfter=7))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, alignment=TA_JUSTIFY, spaceAfter=9))
styles.add(ParagraphStyle(name="BodyLeft", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, alignment=TA_LEFT, spaceAfter=7))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontName="Helvetica", fontSize=9, leading=12, alignment=TA_LEFT, spaceAfter=5))
styles.add(ParagraphStyle(name="CodeBlock", parent=styles["Code"], fontName="Courier", fontSize=7.1, leading=9, leftIndent=8, rightIndent=8, backColor=colors.HexColor("#f1f3f5"), borderColor=colors.HexColor("#c9ced3"), borderWidth=0.5, borderPadding=7))
styles.add(ParagraphStyle(name="Footer", parent=styles["Normal"], fontName="Helvetica", fontSize=8, alignment=TA_CENTER, textColor=colors.HexColor("#555555")))


def P(text, style="Body"):
    return Paragraph(text, styles[style])


def bullet(text):
    return P("&bull; " + text, "BodyLeft")


def page_title(text):
    return [P(text, "PageTitle"), Spacer(1, 4)]


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#b7b7b7"))
    canvas.line(22 * mm, 16 * mm, 188 * mm, 16 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawCentredString(A4[0] / 2, 10 * mm, f"Himank Gupta | TARS Voice-Controlled AI Assistant | Page {doc.page} of {TOTAL_PAGES}")
    canvas.restoreState()


def table(data, widths):
    result = Table(data, colWidths=widths, repeatRows=1)
    result.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, colors.HexColor("#9aa0a6")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9edf0")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("LEADING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return result


def build_story():
    story = []

    # 1. Cover
    story += [Spacer(1, 18 * mm), P("Himalaya Public Sr. Sec. School", "CoverTitle"), Spacer(1, 10 * mm), P("COMPUTER SCIENCE (083)", "CoverSubtitle"), P("PROJECT FILE", "CoverSubtitle"), Spacer(1, 8 * mm), P("TARS Voice-Controlled AI Assistant", "CoverSubtitle"), P("Session: 2026-27", "CoverSubtitle"), Spacer(1, 25 * mm)]
    story.append(table([[P("<b>Submitted To:</b>", "BodyLeft"), P("<b>Submitted By:</b>", "BodyLeft")]], [82 * mm, 82 * mm]))
    story.append(table([[P("Mrs. Priyanka Nagdev Negi<br/>PGT (Computer Science)", "BodyLeft"), P("Himank Gupta<br/>XII B<br/>R.no:", "BodyLeft")]], [82 * mm, 82 * mm]))
    story.append(PageBreak())

    # 2. Certificate
    story += page_title("CERTIFICATE")
    story += [P("This is to certify that <b>Himank Gupta</b> of class XII B has successfully completed the Computer Science (083) Investigatory Project titled <b>\"TARS Voice-Controlled AI Assistant\"</b> under the guidance of Mrs. Priyanka Nagdev Negi during the academic year 2025-26."), Spacer(1, 35 * mm)]
    story.append(table([["________________", "________________"], ["Principal", "Teacher"], ["________________", ""], ["Examiner", ""]], [82 * mm, 82 * mm]))
    story.append(PageBreak())

    # 3. Acknowledgement
    story += page_title("ACKNOWLEDGEMENT")
    story += [P("I would like to express my gratitude towards my teacher Mrs. Priyanka Nagdev Negi as well as principal Ms. Aruna Sivaraj, who gave me the opportunity to work on this Computer Science (083) project. This project helped me research and learn about speech recognition, text-to-speech systems, graphical interfaces, and Python programming. Without their guidance and support, this project would not have been possible."), P("I would also like to thank my friends and family for their encouragement and support during the development and testing of the assistant. I made this project not only for marks, but also to improve my programming knowledge and problem-solving ability."), Spacer(1, 12 * mm), P("~ Himank Gupta (XII B)", "BodyLeft")]
    story.append(PageBreak())

    # 4. Index
    story += page_title("INDEX")
    contents = [["S. No.", "Content", "Page No."], ["1", "Introduction", "5"], ["2", "Objectives of the Project", "6"], ["3", "System Requirements", "7"], ["4", "Feasibility Study", "8"], ["5", "Errors and Their Types", "9"], ["6", "Testing of the System", "11"], ["7", "Maintenance of the System", "13"], ["8", "Flowchart of the Program", "14"], ["9", "Python Program Code", "15"], ["10", "Output Screens / Results", "20"], ["11", "Conclusion", "23"], ["12", "Bibliography", "24"]]
    story.append(table(contents, [25 * mm, 110 * mm, 25 * mm]))
    story.append(PageBreak())

    # 5. Introduction
    story += page_title("INTRODUCTION")
    story += [P("Voice-controlled systems allow people to interact with computers through spoken commands. They reduce dependence on traditional input devices and make computing more accessible and engaging."), P("This project develops a voice and text assistant named TARS using Python. The application provides a futuristic Tkinter interface with an animated cyan avatar, a text input field, a SEND button, voice input, and spoken output. It can tell the date and time, show system specifications, open websites, search YouTube, launch Task Manager, play a local chess game, recommend anime, and give humorous replies."), P("The project demonstrates practical programming concepts including functions, conditional logic, modular design, external libraries, random data generation, GUI event handling, speech recognition, text-to-speech, and web integration.")]
    story.append(PageBreak())

    # 6. Objectives
    story += page_title("OBJECTIVES OF THE PROJECT")
    for item in ["To develop an interactive AI assistant using Python.", "To understand speech recognition and text-to-speech systems.", "To provide both voice and text command input.", "To design a responsive Tkinter graphical interface.", "To implement system utilities and web integrations.", "To add an animated avatar that communicates assistant status.", "To provide fun features such as jokes, anime suggestions, games, and playful responses."]:
        story.append(bullet(item))
    story.append(PageBreak())

    # 7. Requirements
    story += page_title("SYSTEM REQUIREMENTS")
    story += [P("Hardware Requirements", "Section"), bullet("Computer or laptop"), bullet("Microphone for voice input"), bullet("Speakers or headphones for audio output"), bullet("Minimum 4 GB RAM"), P("Software Requirements", "Section"), bullet("Windows 10 or Windows 11"), bullet("Python 3.12 or a compatible Python version"), bullet("Tkinter, Pillow, SpeechRecognition, PyAudio, pyttsx3, requests-html, and python-chess"), bullet("Internet connection for Google speech recognition, weather, and web searches")]
    story.append(PageBreak())

    # 8. Feasibility
    story += page_title("FEASIBILITY STUDY")
    story += [P("A feasibility study determines whether a project is practical and achievable within its constraints."), P("1. Economic Feasibility", "Section"), P("The project is economically feasible because Python and the project libraries are freely available. The required hardware, such as a microphone and speakers, is commonly available on a computer."), P("2. Technical Feasibility", "Section"), P("The project is technically feasible because Python provides libraries for GUI development, speech recognition, text-to-speech, browser control, and chess rules. The application runs on a standard Windows computer."), P("3. Operational Feasibility", "Section"), P("The assistant is simple to operate. Users can type a command into the input field and click SEND, press Enter, or use the ASK VOICE button.")]
    story.append(PageBreak())

    # 9. Errors 1
    story += page_title("ERRORS AND THEIR TYPES")
    story += [P("Errors are mistakes in a program that can produce incorrect results or stop execution."), P("1. Syntax Errors", "Section"), P("Syntax errors occur when Python grammar rules are not followed. For example, a missing colon or incorrect indentation can prevent the assistant from starting."), P("2. Runtime Errors", "Section"), P("Runtime errors occur while the program is running. Examples include an unavailable microphone, a missing package, a missing local music folder, or an unavailable internet connection.")]
    story.append(PageBreak())

    # 10. Errors 2
    story += page_title("ERRORS AND THEIR TYPES (CONTINUED)")
    story += [P("3. Logical Errors", "Section"), P("Logical errors occur when the program runs but produces an unexpected response. For example, an overly broad command condition may select the wrong action."), P("4. Handling Errors", "Section"), P("The assistant handles microphone failures by returning a clear message. External actions are kept inside command branches, and the GUI catches the exit signal so the application can close cleanly."), P("5. Dependency Errors", "Section"), P("Dependency errors occur when a required Python package is not installed. The requirement file lists the required packages, including python-chess for the playable chess feature.")]
    story.append(PageBreak())

    # 11. Testing 1
    story += page_title("TESTING OF THE SYSTEM")
    story += [P("Testing evaluates whether the assistant works correctly under different conditions."), P("1. Unit Testing", "Section"), P("Individual command branches were tested with text input, including date, system specifications, jokes, anime recommendations, chess, and school information."), P("2. Integration Testing", "Section"), P("The GUI, command dispatcher, speech output, avatar, browser actions, and chess module were tested together."), P("3. User Interface Testing", "Section"), P("The SEND button, Enter key, ASK VOICE button, CLEAR OUTPUT button, status label, and animated avatar were checked for correct behavior.")]
    story.append(PageBreak())

    # 12. Testing 2
    story += page_title("TESTING OF THE SYSTEM (CONTINUED)")
    testing = [["Test Case", "Input", "Expected Result"], ["Greeting", "hello", "Assistant gives a greeting"], ["Date", "what's the date", "Current date is spoken and displayed"], ["Joke", "tell me a joke", "A random joke is returned"], ["Anime", "recommend an anime", "An anime recommendation is returned"], ["Chess", "play chess with me", "Chess window opens"], ["Movie", "play a movie", "Baahubali YouTube search opens"], ["School", "who is the principal...", "Aruna Sivaraj is returned"]]
    story.append(table(testing, [38 * mm, 55 * mm, 67 * mm]))
    story.append(PageBreak())

    # 13. Maintenance
    story += page_title("MAINTENANCE OF THE SYSTEM")
    story += [P("Maintenance keeps a software system reliable and useful after development."), P("1. Corrective Maintenance", "Section"), P("Fixing microphone, package, browser, GUI, or command-dispatch errors."), P("2. Adaptive Maintenance", "Section"), P("Updating the project for new Python versions, Windows versions, browser behavior, or speech-recognition services."), P("3. Perfective Maintenance", "Section"), P("Adding new commands, improving the avatar, improving voice feedback, expanding the chess opponent, and adding more games or educational features."), P("4. Preventive Maintenance", "Section"), P("Keeping dependencies documented, testing commands regularly, and avoiding hard-coded paths where possible.")]
    story.append(PageBreak())

    # 14. Flowchart
    story += page_title("FLOWCHART OF THE PROGRAM")
    flow = [["START"], ["Create Tkinter window and animated avatar"], ["Wait for text or voice input"], ["Command received?"], ["YES: Send command to Action()"], ["Match command and execute action"], ["Speak and display response"], ["Return to input"], ["Exit command? YES -> END"]]
    story.append(table([[row[0]] for row in flow], [150 * mm]))
    story.append(Spacer(1, 8))
    story.append(P("The GUI event loop remains active while the avatar animates. Text commands are sent through the SEND button or Enter key. Voice commands are captured through the microphone and passed to the same dispatcher, ensuring both input modes share the same behavior."))
    story.append(PageBreak())

    # 15. Code intro
    story += page_title("PYTHON PROGRAM CODE")
    story += [P("The project is divided into small modules so each responsibility remains clear:"), bullet("gui.py: builds the combined interface and handles input events."), bullet("action.py: matches commands and performs actions."), bullet("avatar.py: draws and animates the cyan assistant face."), bullet("chess_game.py: provides a playable chess board with legal moves."), bullet("speak.py: produces asynchronous voice output."), bullet("spech_to_text.py: captures and recognizes microphone input."), bullet("weather.py: retrieves weather information."), P("Selected implementation excerpts are shown on the following pages.")]
    story.append(PageBreak())

    # 16-19 code pages
    code_pages = [
        ("PYTHON PROGRAM CODE: COMMAND DISPATCH", '''def Action(send, parent=None):\n    data_btn = (send or "").lower().strip()\n\n    if "tell me a joke" in data_btn:\n        return _random_reply(JOKES)\n    elif "play chess with me" in data_btn:\n        launch_chess(parent)\n        return _speak_and_return(\n            "Chess is ready. You play White, and I will play Black."\n        )'''),
        ("PYTHON PROGRAM CODE: GUI INPUT", '''def send_command(event=None):\n    command = entry.get()\n    entry.delete(0, tk.END)\n    run_command(command)\n\nentry.bind("<Return>", send_command)\nsend_button = tk.Button(\n    input_panel, text="SEND", command=send_command\n)'''),
        ("PYTHON PROGRAM CODE: ANIMATED AVATAR", '''class AvatarCanvas:\n    def animate(self):\n        self.draw()\n        self.canvas.after(55, self.animate)\n\n    def draw(self):\n        self.canvas.delete("all")\n        pulse = (math.sin(self.phase) + 1) / 2\n        self.canvas.create_polygon(mask, outline=bright, fill="#071722")'''),
        ("PYTHON PROGRAM CODE: SPEECH AND CHESS", '''def speak(text):\n    threading.Thread(\n        target=_speak_worker, args=(text,), daemon=True\n    ).start()\n\nmove = chess.Move(selected_square, destination_square)\nif move in board.legal_moves:\n    board.push(move)'''),
    ]
    for title, code in code_pages:
        story += page_title(title)
        story.append(Preformatted(code, styles["CodeBlock"]))
        story.append(Spacer(1, 12))
        story.append(P("These modules work together through the command dispatcher and Tkinter event loop."))
        story.append(PageBreak())

    # 20. Output 1
    story += page_title("OUTPUT SCREENS / RESULTS")
    story += [P("The completed application opens a dark cyber-themed interface with the animated cyan avatar on the left and the conversation panel on the right."), P("Startup output", "Section"), P("ASSISTANT > Systems online. Type a command and press SEND."), P("The avatar continuously pulses to indicate that the assistant is active. The interface contains a text field, a SEND button, an ASK VOICE button, and a CLEAR OUTPUT button.")]
    story.append(PageBreak())

    # 21. Output 2
    story += page_title("OUTPUT SCREENS / RESULTS (CONTINUED)")
    story += [P("Example command output", "Section"), P("YOU > show system specs"), P("ASSISTANT > OS, CPU, and RAM information are displayed and spoken."), P("YOU > tell me a joke"), P("ASSISTANT > Why do programmers prefer dark mode? Because light attracts bugs."), P("YOU > recommend an anime"), P("ASSISTANT > Try Jujutsu Kaisen, Erased, or Fullmetal Alchemist Brotherhood."), P("The same output behavior is used for typed commands and recognized voice commands.")]
    story.append(PageBreak())

    # 22. Output 3
    story += page_title("OUTPUT SCREENS / RESULTS (CONTINUED)")
    story += [P("Interactive features", "Section"), bullet("Play chess with me opens a local chess board with shaped pieces and legal move validation."), bullet("Play a movie opens a YouTube search for Baahubali."), bullet("School information opens a Google search for Himalaya Public Senior Secondary School, Sector 7, Rohini, Delhi."), bullet("Voice output runs asynchronously so the GUI remains responsive."), P("Exception handling", "Section"), P("If no microphone is available, the assistant displays a clear message and the user can continue with text input.")]
    story.append(PageBreak())

    # 23. Conclusion
    story += page_title("CONCLUSION")
    story += [P("The TARS Voice-Controlled AI Assistant was successfully developed using Python. The project demonstrates the practical use of speech recognition, text-to-speech, GUI programming, modular design, browser integration, system utilities, and game logic."), P("The final application provides a responsive combined interface with an animated avatar, text and voice input, spoken output, humorous personality responses, anime recommendations, school information, a playable chess game, and useful system commands."), P("This project improved understanding of Python programming and human-computer interaction. It can be enhanced further by adding a stronger chess opponent, offline speech recognition, more games, persistent preferences, and a database of commands.")]
    story.append(PageBreak())

    # 24. Bibliography
    story += page_title("BIBLIOGRAPHY")
    story += [P("The following resources were used for learning, implementation, and troubleshooting:"), bullet("Python Documentation - https://docs.python.org/"), bullet("Tkinter Documentation - https://docs.python.org/3/library/tkinter.html"), bullet("SpeechRecognition Documentation - https://pypi.org/project/SpeechRecognition/"), bullet("pyttsx3 Documentation - https://pyttsx3.readthedocs.io/"), bullet("python-chess Documentation - https://python-chess.readthedocs.io/"), bullet("ReportLab Documentation - https://docs.reportlab.com/"), bullet("W3Schools - https://www.w3schools.com/"), bullet("GeeksforGeeks - https://www.geeksforgeeks.org/"), bullet("Stack Overflow - https://stackoverflow.com/")]

    return story


def main():
    document = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=18 * mm, bottomMargin=23 * mm, title="TARS Voice-Controlled AI Assistant - Himank Gupta", author="Himank Gupta")
    document.build(build_story(), onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    main()
