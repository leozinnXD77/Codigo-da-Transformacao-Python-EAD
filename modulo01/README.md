# ✂️ Sistema de Cortes - Barbearia (CLI)

Este projeto consiste num **Sistema de Cortes para Barbearia** desenvolvido em **Python**, que funciona via linha de comando (CLI - *Command Line Interface*). O sistema permite cadastrar cortes de cabelo e barba, consultar o catálogo disponível e realizar agendamentos com atualização automática do estoque/vagas.

---

## 👥 Visão Geral e Papéis do Projeto

O sistema foi estruturado considerando as necessidades de diferentes atores do negócio:

- **PO (Dono do Negócio):** Controle centralizado dos cortes e agendamentos da barbearia.
- **QA (Visão do Cliente):** Facilidade e rapidez no processo de escolha e agendamento do corte desejado.
- **Tech / Dev (Programador):** Código eficiente, funcional e preparado para manutenção e evolução.
- **UX (Designer):** Planejamento focado na experiência do usuário para futuras versões com interface visual.
- **IA (Analista de Dados):** Estrutura preparada para coleta de dados de consumo, identificação de padrões e recomendações em marketing.

---

## 🔄 Ciclo de Vida do Desenvolvimento

1. **Planejamento:** Definição dos requisitos do sistema e necessidades da barbearia.
2. **Análise:** Modelagem dos dados dos cortes e validação dos fluxos do sistema.
3. **Desenvolvimento:** Construção da lógica em Python via CLI com simulação de tempo de carregamento (`time.sleep`).
4. **Testes:** Validação dos fluxos de cadastro, listagem de serviços e confirmação de agendamentos.
5. **Implantação:** Execução do script no ambiente de produção/terminal local.
6. **Manutenção:** Refatoração de código, tratamento de exceções e preparação para o lançamento da versão com Interface Gráfica (GUI).

---

## 🚀 Funcionalidades do Sistema

- **1 - Cadastrar Corte:** Permite o registro dos cortes guardando nome, quantidade em estoque/vagas, preço, data de validade e descrição.
- **2 - Listar Cortes:** Exibe todos os cortes cadastrados com seus respectivos detalhes e quantidade disponível.
- **3 - Realizar Agendamento:** Permite selecionar o corte desejado, realizar o agendamento, calcular o valor e dar baixa automática na quantidade disponível.
- **0 - Sair:** Encerra a execução do programa de forma segura.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Módulos Nativos:** `time` para simulação de dinamismo nas respostas do terminal.
- **Estruturas de Repetição:** Laço `while True` para manter o menu ativo.
- **Estruturas Condicionais:** `if / elif / else` para controle do fluxo e opções do menu.
- **Validação de Estoque:** Subtração automática de vagas e impedimento de agendamentos sem quantidade suficiente.
- **Formatação de Texto:** Manipulação de strings, uso de *f-strings* e formatadores de moeda `:.2f`.

---

## 💻 Como Executar o Programa

### Pré-requisitos
- **Python 3.x** instalado no sistema.

### Passo a Passo

1. **Baixar o Código:**
   Salve o arquivo Python (por exemplo, `barbearia.py`) na sua máquina.

2. **Abrir o Terminal:**
   Navegue até a pasta onde o arquivo foi salvo.

3. **Executar a Aplicação:**
   Execute o seguinte comando no terminal:
   ```bash
   python barbearia.py
   python barbearia.py
