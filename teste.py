from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])  # Inicia o aplicativo
window = QWidget()  # Cria a janela
layout = QVBoxLayout()  # Layout vertical principal

# Layout horizontal para os botões
button_layout = QHBoxLayout()

# Botões
confirm_bt = QPushButton('Confirmar')
exit_bt = QPushButton('Sair')

# Adiciona os botões ao layout horizontal
button_layout.addWidget(confirm_bt)
button_layout.addWidget(exit_bt)

# Adiciona um espaço expansível acima do layout de botões
layout.addStretch(1)
layout.addLayout(button_layout)  # Adiciona o layout de botões ao layout principal

# Configurações da janela
window.setWindowTitle("Botões na Parte Inferior")
window.resize(400, 300)
window.setLayout(layout)
window.show()

app.exec()
