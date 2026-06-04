Trabalho-E2E
Testes E2E com Selenium e Pytest - OrangeHRM
Autor: Diego Vieira Lopes

Sistema escolhido
Sistema: OrangeHRM Demo

Link: https://opensource-demo.orangehrmlive.com/

Descrição: O OrangeHRM é um sistema de gestão de recursos humanos (HRM) que oferece funcionalidades como administração de usuários, gerenciamento de funcionários, folha de ponto, férias e relatórios.

Fluxos testados
Login válido → acesso ao Dashboard.

Login inválido → mensagem de erro "Invalid credentials".

Logout → retorno à tela de login.

Navegação entre módulos → Admin, PIM, Leave, Time.

Busca de funcionário → pesquisa por "Linda Anderson" no módulo PIM.

Ferramentas utilizadas
Python 3.12

Selenium WebDriver

Pytest

WebDriver Manager (para gerenciar o ChromeDriver)

Dependências necessárias
Instale todas as dependências com:

bash
pip install -r requirements.txt
Exemplo de requirements.txt:

Código
selenium
pytest
webdriver-manager
Como subir o ambiente
Instale o Python 3.12 ou superior.

Crie um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Como executar os testes
Na raiz do projeto, rode:

bash
pytest -v
Para rodar apenas um grupo de testes (exemplo: login):

bash
pytest -m login
Estrutura do projeto
text
orange_testes_e2e/
│
├── paginas/                # Page Objects
│   ├── __init__.py
│   ├── login_pagina.py
│   ├── dashboard_pagina.py
│   ├── menu_pagina.py
│   └── pagina_rh.py
│
├── tests/                  # Arquivos de teste
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_navigation.py
│   └── test_rh.py
│
├── conftest.py             # Fixture do driver
├── pytest.ini              # Configuração do Pytest
└── README.md               # Documentação
Testes implementados
test_login_sucesso

test_login_invalido

test_logout

test_navegacao (parametrizado para Admin, PIM, Leave, Time)

test_pesquisar_funcionario

Limitações conhecidas
O sistema OrangeHRM Demo é público e pode sofrer alterações na interface, o que pode quebrar seletores.

O ambiente de demonstração pode estar instável ou lento em alguns momentos.

time.sleep() foi usado em alguns pontos apenas para fins de demonstração em vídeo (não recomendado em produção).

Vídeo explicativo
Um vídeo foi gravado mostrando:

A execução dos testes no navegador.

O fluxo completo de login, navegação, busca e logout.

A validação das mensagens e URLs.