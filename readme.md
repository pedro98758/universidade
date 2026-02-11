# Projeto Universidade

Modelagem em Orientação à Objetos das Entidades Alunos,Cursos e Turmas

# Caso de Uso
```mermaid
flowchart LR
    Usuario([Secretaria])
    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Alunos))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno{
        - nome
        - email
        - cpf
        - telefone
        - endereço
        - matrícula
        + cadastrar()
        + editar()
        + transferir
    }
```

## Dependências
+ **VsCode**: IDE(Interface de desenvolvimento)
- **Mermaid**: Linguagem para confecção de diagrama em documentos MD(Mark Down)
+ **Material Icon Theme**: Tema para colorir as pastas.
- **Git Lens**: Interface gráfica pra o versionamento .git integrada ao VSCode.
