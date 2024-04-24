import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import sqlite3
import json

class AddDataWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data to Database")
        self.resize(400, 300)
        self.data_pairs_layout = QVBoxLayout()
        self.data_bonus_layout = QVBoxLayout()
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.subject_label = QLabel("Subject:")
        self.subject_input = QLineEdit()
        self.requirements_label = QLabel("requirements:")
        self.requirements_input = QLineEdit()
        self.BVI_label = QLabel("BVI:")
        self.BVI_input = QLineEdit()
        self.points_label = QLabel("100 points:")
        self.points_input = QLineEdit()
        self.stages_label = QLabel("Stages:")
        self.stages_input = QLineEdit()
        self.spec_label = QLabel("Specialization:")
        self.spec_input = QLineEdit()
        self.inf_label = QLabel("Information:")
        self.inf_input = QLineEdit()
        self.link_label = QLabel("Link:")
        self.link_input = QLineEdit()
        self.dates_label = QLabel("Dates:")
        self.add_bonus_button = QPushButton("Add bonus")
        self.add_bonus_button.clicked.connect(self.add_bonus)
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.subject_label)
        layout.addWidget(self.subject_input)

        layout.addLayout(self.data_bonus_layout)
        layout.addWidget(self.add_bonus_button)

        layout.addWidget(self.stages_label)
        layout.addWidget(self.stages_input)

        layout.addWidget(self.spec_label)
        layout.addWidget(self.spec_input)
        layout.addWidget(self.inf_label)
        layout.addWidget(self.inf_input)
        layout.addWidget(self.link_label)
        layout.addWidget(self.link_input)
        layout.addWidget(self.dates_label)

        self.add_pair_button = QPushButton("Add Date Pair")
        self.add_pair_button.clicked.connect(self.add_date_pair)



        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_data)

        layout.addLayout(self.data_pairs_layout)
        layout.addWidget(self.add_pair_button)

        layout.addWidget(self.submit_button)
        self.add_date_pair()
        self.add_bonus()
        self.setLayout(layout)


    def add_date_pair(self):
            data_pair_layout = QHBoxLayout()

            key_label = QLabel("Key:")
            key_input = QLineEdit()

            value_label = QLabel("Value:")
            value_input = QLineEdit()

            data_pair_layout.addWidget(key_label)
            data_pair_layout.addWidget(key_input)
            data_pair_layout.addWidget(value_label)
            data_pair_layout.addWidget(value_input)

            self.data_pairs_layout.addLayout(data_pair_layout)

    def add_bonus(self):
            data_bonus_layout = QHBoxLayout()

            univ_label = QLabel("University:")
            univ_input = QLineEdit()

            required_label = QLabel("Requirements:")
            required_input = QLineEdit()

            BVI_label = QLabel("BVI:")
            BVI_input = QLineEdit()

            points_label = QLabel("points:")
            points_input = QLineEdit()

            data_bonus_layout.addWidget(univ_label)
            data_bonus_layout.addWidget(univ_input)
            data_bonus_layout.addWidget(required_label)
            data_bonus_layout.addWidget(required_input)
            data_bonus_layout.addWidget(BVI_label)
            data_bonus_layout.addWidget(BVI_input)
            data_bonus_layout.addWidget(points_label)
            data_bonus_layout.addWidget(points_input)


            self.data_bonus_layout.addLayout(data_bonus_layout)

    def add_data(self):
        connection = sqlite3.connect("Проект Школа.sqlite")
        cursor = connection.cursor()

        name = self.name_input.text()
        subject = self.subject_input.text()

        stages = self.stages_input.text()
        spec = self.spec_input.text()
        inf = self.inf_input.text()
        link = self.link_input.text()

        data_pairs = {}
        for i in range(self.data_pairs_layout.count()):
            data_pair_layout = self.data_pairs_layout.itemAt(i)
            key_input = data_pair_layout.itemAt(1).widget()
            value_input = data_pair_layout.itemAt(3).widget()

            data_pairs[key_input.text()] = value_input.text()
        data_result = str(data_pairs)  

        
        for i in range(self.data_bonus_layout.count()):
            data_bonus_layout = self.data_bonus_layout.itemAt(i)
            univ_name = data_bonus_layout.itemAt(1).widget()
            req = data_bonus_layout.itemAt(3).widget()
            Bvi_1 = data_bonus_layout.itemAt(5).widget()
            points_1 = data_bonus_layout.itemAt(7).widget()

            res1 = cursor.execute(f"""SELECT id FROM O""").fetchall()
            id_o = len(res1) + 1
            res2 = cursor.execute(f"""SELECT id FROM V WHERE name = ("{univ_name.text()}")""").fetchall()
            id_v = res2[0][0]

            cursor.execute("INSERT INTO O_V (ol_id, v_id, requirements, BVI, points) VALUES (?, ?, ?, ?, ?)",
                       (id_o, id_v, req.text(), Bvi_1.text(), points_1.text()))

        
        data_result = str(data_pairs)  

        cursor.execute("INSERT INTO O (id, name, subject, stages, spec, inf, link, dates) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (id_o, name, subject, stages, spec, inf, link, data_result))
        connection.commit()

        connection.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddDataWindow()
    window.show()
    sys.exit(app.exec_())
