from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QComboBox, QLabel, QWidget, QMessageBox

def on_submit():
    selected_month = combo_box.currentText()
    QMessageBox.information(window, "Mês Selecionado", f"Você escolheu {selected_month}!")

app = QApplication([])

# Criando a janela principal
window = QWidget()
window.setWindowTitle("Escolha um Mês")

# Layout vertical
layout = QVBoxLayout()

# Label de instrução
label = QLabel("Selecione um mês:")
layout.addWidget(label)

# Criando o ComboBox com os meses
combo_box = QComboBox()
combo_box.addItems([
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
])
layout.addWidget(combo_box)

# Botão para confirmar a seleção
submit_button = QPushButton("Confirmar")
submit_button.clicked.connect(on_submit)
layout.addWidget(submit_button)

# Configurando o layout na janela principal
window.setLayout(layout)

# Exibindo a janela
window.show()
app.exec()
