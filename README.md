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

2. **Crie um ambiente virtual (recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. **Crie um ambiente virtual (recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

4. **Configure o banco de dados**:

   - O projeto usa SQLite por padrão. Para usar outro banco de dados, configure o arquivo settings.py.

5. **Execute as migrações**:
   ```bash
   python manage.py migrate
   
6. **Crie um superusuário (para acessar o painel administrativo)**:
   ```bash
   python manage.py createsuperuser

7. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver

8. **Acesse o sistema**:
   ```bash
   Abra o navegador e acesse: http://127.0.0.1:8000/.

## Como Usar

###  Painel Administrativo

  - Acesse o painel administrativo em http://127.0.0.1:8000/admin/.
  - Use as credenciais do superusuário criado anteriormente.

###  Gestão de Membros

  - Acesse a lista de membros em http://127.0.0.1:8000/membros/.

  -  Adicione, edite ou exclua membros conforme necessário.

###  Registro de Dízimos

  -  Acesse a página de registro de dízimos em http://127.0.0.1:8000/dizimos/registrar/.

  -  Preencha o formulário para registrar um novo dízimo.

###  Geração de Carteirinhas

  -  Na lista de membros, clique em "Gerar Carteirinha" ao lado de um membro para gerar um PDF com os detalhes.

###  Estrutura do Projeto
    
    gestao-igrejas/
    ├── core/                     # Configurações principais do Django
    ├── membros/                  # App para gestão de membros
    │   ├── models.py             # Modelos de dados (Membros, Dízimos, etc.)
    │   ├── views.py              # Lógica das views
    │   ├── templates/            # Templates HTML
    │   └── ...
    ├── templates/                # Templates globais (base.html, etc.)
    ├── static/                   # Arquivos estáticos (CSS, JS, imagens)
    ├── manage.py                 # Script de gerenciamento do Django
    └── requirements.txt          # Lista de dependências do projeto

###  Licença
  Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

###  Contato

  -  **Autor:** Celso Reis
  -  **Email:** celsosr87@gmail.com
  -  **LinkedIn:** https://www.linkedin.com/in/celso-reis-ads/
