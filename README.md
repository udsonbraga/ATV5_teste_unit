pip# Projeto com exemplos de Teste variados

## Aplicações no pacote `apps`

## Testes no pacote `test_apps`

### Executando teste com unittest apenas

`python -m unittest`

### Executando testes com coverage

#### Criar um ambiente virtual
`python3 -m venv venv`

#### Instalar a biblioteca coverage
`pip install coverage`

#### Alterar o executor do unittest para coverage 
#### (na raiz do projeto por padrão utilizar test_*.py na frente dos módulos de teste)
`python -m unittest discover`

#### Executar o teste com o coverage
`coverage run -m unittest discover` 

### Rodar cobertura de teste em app (runtime)
`python -m coverage run apps/main.py`

#### Gerar report no terminal
`coverage report -m`

#### Gerar report HTML
`coverage html`
