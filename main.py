import tkinter as tk
from tkinter import simpledialog, Text
import pyperclip

def generate_quiz_html(questions, answers):
    html = '<!DOCTYPE html>\n<html>\n  <head>\n    <title>True/False Quiz</title>\n  </head>\n  <body>\n'
    html += '    <form>\n'
    for i in range(len(questions)):
        html += f'      <p>{questions[i]}</p>\n'
        html += f'      <label><input type="radio" name="question{i}" value="true">True</label>\n'
        html += f'      <label><input type="radio" name="question{i}" value="false">False</label>\n'
    html += '      <button type="button" onclick="checkAnswers()">Submit</button>\n'
    html += '    </form>\n'
    html += '    <div id="result"></div>\n'
    html += '    <script>\n'
    html += '      function checkAnswers() {\n'
    html += f'        let answers = {answers}\n'
    html += '        let correctAnswers = 0;\n'
    html += '        for (let i = 0; i < answers.length; i++) {\n'
    html += '          let radios = document.getElementsByName(`question${i}`);\n'
    html += '          for (let j = 0; j < radios.length; j++) {\n'
    html += '            if (radios[j].value === answers[i] && radios[j].checked) {\n'
    html += '              correctAnswers++;\n'
    html += '            }\n'
    html += '          }\n'
    html += '        }\n'
    html += '        let result = document.getElementById("result");\n'
    html += '        result.innerHTML = `You got ${correctAnswers} out of ${answers.length} questions correct.`;\n'
    html += '      }\n'
    html += '    </script>\n'
    html += '  </body>\n</html>'
    return html

root = tk.Tk()
questions = []
answers = []
while True:
    question = simpledialog.askstring("Input", "Enter a true/false question (or leave blank to finish)", parent=root)
    if question == '':
        break
    questions.append(question)
    answer = simpledialog.askstring("Input", "Enter the answer (true or false)", parent=root)
    answers.append(answer)

html = generate_quiz_html(questions, answers)

# write the HTML to a file
with open("quiz.html", "w") as file:
    file.write(html)

# display the HTML code in a text box
text_box = Text(root)
text_box.insert("1.0", html)
text_box.pack()

#Add a button to copy the HTML code to clipboard
import pyperclip
def copy_to_clipboard():
pyperclip.copy(text_box.get("1.0", "end"))

copy_button = tk.Button(root, text="Copy to clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()

#Now the user can copy the HTML code to the clipboard by clicking on the "Copy to clipboard" button, and then paste it into their HTML editor of choice to create their True/False quiz.
