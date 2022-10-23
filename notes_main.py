import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QListWidget, QLineEdit, QInputDialog
notes = {"Добро пожаловать":
{"текст": "В этом приложении можно создавать заметки с тегами...",
"теги": ["умные заметки", "инструкция"]},
}
app = QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметки')
layout_main = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layout_main.addLayout(layoutV1)
layout_main.addLayout(layoutV2)

def cr_zam():
    note_name, result = QInputDialog.getText(window, "Добавить заметку", "Название заметки:")
    if result and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        list_zam.addItem(note_name)
        list_tag.addItems(notes[note_name]["теги"])
        print(notes)
def del_zam():
    if list_zam.selectedItems():
        key = list_zam.selectedItems()[0].text()
        del notes[key]
        field_text.clear()
        list_tag.clear()
        list_zam.clear()
        list_zam.addItems(notes)
        with open("notes.json", "w", encoding="utf8") as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print("Заметка удаления не выбрана!")
def savezam():
    if list_zam.selectedItems():
        key = list_zam.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()
        with open("notes.json", "w", encoding="utf8") as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print("Заметка сохранения не выбрана!")
def addtag():
    if list_tag.selectedItems():
        key = list_zam.selectedItems()[0].text()
        tag = list_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            field_tag.clear()
        with open("notes.json", "w", encoding="utf8") as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")
def remtag():
    if list_tag.selectedItems():
        key = list_zam.selectedItems()[0].text()
        tag = list_tag.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[key]["теги"])
        with open("notes.json", "w", encoding="utf8") as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print("Тег для удаления не выбран!")
def findzam():
    tag = vvod.text()
    if find_zam.text() == "Искать заметки по тегу" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        find_zam.setText("Сбросить поиск")
        list_zam.clear()
        list_tag.clear()
        list_zam.addItems(notes_filtered)
    elif find_zam.text() == "Сбросить поиск":
        vvod.clear()
        list_zam.clear()
        list_tag.clear()
        list_zam.addItems(notes)
        find_zam.setText("Искать заметки по тегу")
    else:
        pass
def show_note():
    name = list_zam.selectedItems()[0].text()
    field_text.setText(notes[name]["текст"])
    list_tag.clear()
    list_tag.addItems(notes[name]["теги"])

with open("notes.json", "w", encoding="utf8") as file:
    json.dump(notes,file)
add_zam = QPushButton("Создать заметку")
rem_zam = QPushButton("Удалить заметку")
save_zam = QPushButton("Сохранить заметку")
add_tag = QPushButton("Добавить к заметке")
rem_tag = QPushButton("Открепить от заметки")
find_zam = QPushButton("Искать заметки по тегу")
vvod = QLineEdit()
vvod.setPlaceholderText("Введите тег...")
field_text = QTextEdit()
zam_spis=QLabel("Список заметок")
list_zam = QListWidget()
tag_spis=QLabel("Список тегов")
list_tag = QListWidget()
layoutV1.addWidget(field_text)
layoutV2.addWidget(zam_spis)
layoutV2.addWidget(list_zam)
layoutV2.addLayout(layoutH1)
layoutH1.addWidget(add_zam)
layoutH1.addWidget(rem_zam)
layoutV2.addWidget(save_zam)
layoutV2.addWidget(tag_spis)
layoutV2.addWidget(list_tag)
layoutV2.addWidget(vvod)
layoutV2.addLayout(layoutH2)
layoutH2.addWidget(add_tag)
layoutH2.addWidget(rem_tag)
layoutV2.addWidget(find_zam)

add_zam.clicked.connect(cr_zam)
rem_zam.clicked.connect(del_zam)
save_zam.clicked.connect(savezam)
add_tag.clicked.connect(addtag)
rem_tag.clicked.connect(remtag)
find_zam.clicked.connect(findzam)

window.setLayout(layout_main)
window.show()

with open("notes.json", "r", encoding="utf8") as file:
    notes = json.load(file)
list_zam.addItems(notes)
list_zam.itemClicked.connect(show_note)

app.exec_()