from PyQt5.QtWidgets import *
import random

app = QApplication([])
strings = [
    "Ты прекрасен!",
    "Твоя улыбка светит как солнце!",
    "У тебя отличное чувство юмора!",
    "Ты очень талантлив!",
    "Ты вдохновляешь окружающих!",
    "Ты такой добрый и заботливый!",
    "Ты умный и обаятельный!",
    "Ты умеешь находить выход из любой ситуации!",
    "Ты делаешь мир лучше своим присутствием!",
    "Твоя энергия заразительна!"
]
button = QPushButton('Мне грустно')
def on_button_clicked():
    alert = QMessageBox()
    random_string = random.choice(strings)
    alert.setText(random_string)
    alert.exec()


button.clicked.connect(on_button_clicked)
button.show()
app.exec()