from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QVBoxLayout, QFrame, QLabel, QHBoxLayout, QComboBox, QSizePolicy


def menu_de_selecao():
    app = QApplication([])  # Inicia o aplicativo
    window = QWidget()  # Cria uma janela básica
    layout = QVBoxLayout()  # Layout principal

    # Frame para destacar botões inferiores
    botton_frame = QFrame()
    botton_frame.setFrameShape(QFrame.StyledPanel)  # Estilo com borda em relevo
    botton_frame.setFrameShadow(QFrame.Raised)
    botton_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    bt_layout_inferior = QHBoxLayout()  # Layout horizontal para os botões Confirmar e Sair
    layout_escrever_form = QHBoxLayout()  # Layout horizontal para o campo de texto e botão Confirmar

    # Botão para capturar o texto
    confirm_text_bt = QPushButton('Confirmar')
    confirm_text_bt.clicked.connect(lambda: print(f"Nome da planilha: {text_nome_plan.text()}"))

    # Campo de texto
    text_nome_plan = QLineEdit()
    text_nome_plan.setPlaceholderText("Escreva aqui...")

    # Faz o campo de texto ocupar o máximo de espaço no layout
    text_nome_plan.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    # Adiciona o campo de texto e botão ao layout horizontal
    layout_escrever_form.addWidget(text_nome_plan)  # Campo de texto
    layout_escrever_form.addWidget(confirm_text_bt)  # Botão Confirmar

    # Formulários de mês e ano
    form_mes = QComboBox()
    form_mes.addItems(['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])

    form_ano = QComboBox()
    form_ano.addItems([str(ano) for ano in range(2011, 2026)])

    # Adiciona os botões Confirmar e Sair ao layout horizontal
    confirm_bt = QPushButton('Confirmar')
    exit_bt = QPushButton('Sair')
    bt_layout_inferior.addWidget(confirm_bt)
    bt_layout_inferior.addWidget(exit_bt)
   

    botton_frame.setLayout(bt_layout_inferior)  # Aplica layout ao frame

    # Adiciona widgets ao layout principal
    layout.addWidget(QLabel('Nome da planilha (sem extensão):'))
    layout.addLayout(layout_escrever_form)  # Campo de texto e botão Confirmar
    layout.addWidget(form_mes)  # Formulário para mês
    layout.addWidget(form_ano)  # Formulário para ano
    layout.addStretch()  # Adiciona espaço expansível entre os formulários e o frame inferior
    layout.addWidget(botton_frame)  # Adiciona o frame inferior ao final do layout principal

    valores = {}
    
    def capturar_valores():
        valores['nome_da_planilha'] = text_nome_plan.text()
        valores['mes'] = form_mes.currentText()
        valores['ano'] = form_ano.currentText()
        app.quit() #fecha a janela
    
    confirm_bt.clicked.connect(capturar_valores)
    confirm_bt.clicked.connect(lambda: teste( nome_da_planilha, ano_elemento_selecionado, mes_elemento_selecionado))
        
    # Configurações da janela
    window.setWindowTitle("Ministério do Desenvolvimento Social")
    window.resize(400, 300)  # Define o tamanho da janela
    window.setLayout(layout)  # Aplica o layout à janela
    window.show()  # Exibe a janela

    app.exec()
    
    return valores






    


