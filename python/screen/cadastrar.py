from modules.mysql import MySQL
from modules.aluno import Aluno
from PySide6.QtWidgets import(
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco =  MySQL()
        
        self.campos = {}
        
        self.configurar_janela()
        self.criar_componentes()
        
    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastro Aluno")
        self.janela.resize(400, 300)
        self.janela.setMinimumSize(350, 250)
        self.janela.setLayout(self.layout)
        
    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu cpf:",
            "telefone": "Digite seu telefone:",
            "endereco": "Digite seu endereco:"
        }
        
        for chave, texto in componentes.items():
            label = QLabel(texto)
            campo = QLineEdit()
            
            self.layout.addWidget(label)
            self.layout.addWidget(campo)
            
            self.campos[chave] = campo
            
        botao_cadastro = QPushButton("Cadastro")
        self.layout.addWidget(botao_cadastro)
        
        botao_cadastro.clicked.connect(self.cadastrar)
        
        self.janela.adjustSize()
        
    def validar_campos(self):
        nome = self.campos["nome"].text().strip()
        email = self.campos["email"].text().strip()
        cpf = self.campos["cpf"].text().strip()
        telefone = self.campos["telefone"].text().strip()
        endereco = self.campos["endereco"].text().strip()
        
        if not nome or not email or not cpf or not telefone or not endereco:
            QMessageBox.warning(self.janela, "Erro", "Todos os campos devem ser preenchidos.")
            return False
        
        if "@" not in email or "." not in email:
            QMessageBox.warning(self.janela, "Erro", "Email inválido.")
            return False
        
        if not cpf.isdigit() or len(cpf) != 11:
            QMessageBox.warning(self.janela, "Erro", "CPF deve conter 11 números.")
            return False
        
        if not telefone.isdigit():
            QMessageBox.warning(self.janela, "Erro", "Telefone deve conter apenas números.")
            return False
        
        return True
        
    def cadastrar(self):
        if not self.validar_campos():
            return
        
        aluno = Aluno(
            self.campos["nome"].text(),
            self.campos["email"].text(),
            self.campos["cpf"].text(),
            self.campos["telefone"].text(),
            self.campos["endereco"].text()
        )
        
        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)
            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno Cadastrado!!!"
            )
            self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao Cadastrar: {e}"
            )
        finally:
            self.banco.disconnect()
            
    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()
