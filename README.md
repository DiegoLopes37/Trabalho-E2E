# Trabalho-E2E
# Testes E2E com Selenium e Pytest - OrangeHRM
Autor: Diego Lopes

## Objetivo
Automatizar testes End-to-End (E2E) no sistema OrangeHRM Demo utilizando Selenium WebDriver e Pytest, aplicando Page Object Model (POM), fixtures e boas práticas de automação.

## Sistema
- **URL**: https://opensource-demo.orangehrmlive.com  
- **Credenciais**: Admin / admin123  

## Tecnologias
- Python 3  
- Selenium WebDriver  
- Pytest  
- WebDriver Manager  
- Google Chrome  

## Estrutura
orangehrm-e2e/
├── paginas/
│   ├── __init__.py
│   ├── dashboard_pagina.py
│   ├── login_pagina.py
│   ├── menu_pagina.py
│   └── pagina_rh.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_navigation.py
│   └── test_rh.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md