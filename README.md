# Sistema de Gestão de Igrejas (Em desenvolvimento)

![GitHub](https://img.shields.io/github/license/seu-usuario/seu-repositorio)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.1%2B-green)

O **Sistema de Gestão de Igrejas** é uma aplicação web desenvolvida em Django para gerenciar membros, dízimos, eventos e outras atividades relacionadas à administração de uma igreja. Este sistema foi projetado em para facilitar o controle de informações e melhorar a organização da igreja.

---

## Funcionalidades Principais

- **Gestão de Membros**:
  - Cadastro, edição e exclusão de membros.
  - Visualização de detalhes dos membros.
  - Geração de carteirinhas em PDF.

- **Registro de Dízimos**:
  - Registro de dízimos com valor, data e membro associado.
  - Listagem de todos os dízimos registrados.

- **Eventos**:
  - Cadastro e gerenciamento de eventos da igreja.
  - Listagem de eventos com datas e descrições.

- **Relatórios**:
  - Geração de relatórios de dízimos por período.
  - Relatórios de membros ativos.

- **Autenticação e Permissões**:
  - Sistema de login e logout.
  - Controle de acesso baseado em permissões (pastor, administrador, etc.).

---

## Tecnologias Utilizadas

- **Backend**:
  - Python 3.8+
  - Django 4.1+

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Bootstrap 4.5+

- **Banco de Dados**:
  - SQLite (para desenvolvimento)
  - PostgreSQL (para produção)

- **Outras Ferramentas**:
  - ReportLab (para geração de PDFs)
  - Django REST Framework (para futuras APIs)

---

## Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Pip (gerenciador de pacotes do Python).
- Git (opcional, para clonar o repositório).

### Passos para Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/gestao-igrejas.git
   cd gestao-igrejas
