# PRIMORA

# Vetor_ETL

Projeto acadêmico desenvolvido no contexto da Primora, com foco na criação de um pipeline ETL para tratamento, limpeza e padronização de dados cadastrais de clientes da Distribuidora Vetor.

**Sobre o projeto**

O **Vetor_ETL** tem como objetivo melhorar a qualidade e a consistência dos dados cadastrais por meio de etapas de extração, transformação e preparação dos dados.

O projeto contempla o tratamento de informações como CNPJ, telefone, CEP e data de cadastro, além da integração com APIs externas para consulta de CEPs.

**Objetivos**

Padronizar dados cadastrais.
Identificar informações inválidas ou inconsistentes.
Reduzir problemas durante o processamento dos dados.
Consultar informações de CEP por meio de APIs externas.
Armazenar resultados de consultas em cache para evitar requisições repetidas.
Separar registros processados daqueles que precisam de revisão.

**Tecnologias utilizadas**

**Python:** desenvolvimento da lógica de tratamento dos dados.
**Pandas:** leitura, manipulação e processamento de arquivos CSV.
**Expressões regulares (Regex):** validação e padronização de formatos.
**Requests:** comunicação com APIs externas.
**JSON:** armazenamento de dados em cache.
**Pytest:** execução de testes automatizados.
**Git e GitHub:** versionamento e gerenciamento do código.

**Minha contribuição**

Minha contribuição no projeto está relacionada à validação, normalização e formatação de CEPs, desenvolvida no arquivo `validators/postal_code.py`.

Foram implementadas três funções principais:

**`normalizar_cep()`**: valida o formato do CEP e retorna uma versão padronizada, sem hífen.
**`verifica_cep()`**: informa se o CEP corresponde ao formato esperado.
**`formatar_cep()`**: retorna o CEP no formato `00000-000`.

A implementação utiliza expressões regulares (*Regex*) para verificar o padrão de oito dígitos, com ou sem hífen. Também trata entradas inválidas, retornando `None` na normalização e na formatação, ou `False` na verificação.

**Observação:** a validação de formato não garante que o CEP exista ou corresponda a um endereço real.

## Estrutura do projeto

```text
Vetor_ETL/
├── validators/
│   ├── postal_code.py
│   └── limpeza.py
├── integrations/
│   ├── viacep.py
│   └── brasilapi.py
├── service/
│   └── postal_code_service.py
├── tests/
│   ├── test_postal_code.py
│   ├── test_limpeza.py
│   └── test_postal_code_service.py
├── data/
│   └── clean/
├── etl_clientes.py
└── README.md
```

## Funcionamento do pipeline

De forma geral, o processo contempla as seguintes etapas:

1. **Extração:** leitura dos dados cadastrais a partir de um arquivo CSV.
2. **Transformação:** limpeza e padronização de campos como CNPJ, telefone, CEP e data de cadastro.
3. **Validação:** verificação dos formatos e identificação de dados inconsistentes.
4. **Integração:** consulta às APIs ViaCEP e BrasilAPI para obter informações de CEP quando necessário.
5. **Cache:** armazenamento dos resultados das consultas em arquivo JSON, evitando requisições repetidas.
6. **Separação dos registros:** geração de arquivos para dados processados e registros que precisam de revisão.


O projeto possui testes automatizados para verificar comportamentos das funções de tratamento de dados, incluindo cenários de CEPs válidos e inválidos.

Para executar os testes, com o `pytest` instalado, utilize:

```bash
pytest
```

Os testes auxiliam na identificação de falhas e na verificação do comportamento esperado do código.

**Limitações**

A validação de CEP verifica o formato, mas não confirma, por si só, a existência do código postal.
As consultas às APIs externas dependem da disponibilidade dos serviços e da conexão com a internet.
A qualidade dos resultados depende dos dados de entrada e das regras de tratamento implementadas.

Aprendizados

O desenvolvimento do projeto proporciona experiência prática com manipulação de dados, validação de informações, expressões regulares, integração com APIs, armazenamento em cache, organização modular de código e testes automatizados.

**Status**

Projeto acadêmico em desenvolvimento.

**Autoria**

Desenvolvido como parte de um projeto acadêmico de ETL.
