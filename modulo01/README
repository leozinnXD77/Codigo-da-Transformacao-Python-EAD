# ✂️ Sistema de Cortes - Barbearia (CLI)

Este projeto consiste em um Sistema de Cortes para Barbearia desenvolvido em Python, que funciona via linha de comando (CLI - *Command Line Interface*). O sistema permite cadastrar cortes de cabelo/barba, consultar o catálogo de serviços disponíveis e realizar agendamentos de forma simples e interativa.

---

## 👥 Visão Geral e Papéis do Projeto

O sistema foi estruturado considerando as necessidades de diferentes atores e papéis do negócio:

* **PO (Dono do Negócio):** Controle centralizado dos cortes cadastrados e dos agendamentos efetuados na barbearia.
* **QA (Visão do Cliente):** Facilidade e rapidez na escolha e no agendamento do corte desejado.
* **Tech / Dev (Programador):** Código funcional e estruturado, aplicando recursos eficientes para atender às necessidades do negócio e dos clientes.
* **UX (Designer de Experiência):** Planejamento voltado para uma navegação limpa, fluida e amigável no terminal, garantindo uma experiência satisfatória para o usuário.
* **IA (Analista de Dados):** Estrutura preparada para identificar padrões de consumo, agendamentos e criar algoritmos de recomendação em Marketing.

---

## 🔄 Ciclo de Vida do Desenvolvimento

1. **Planejamento:** Definição dos requisitos do sistema e mapeamento das necessidades da barbearia e de seus clientes.
2. **Análise:** Modelagem dos dados do corte (nome, quantidade em estoque/vagas, preço, validade e descrição) e validação dos fluxos.
3. **Desenvolvimento:** Construção da lógica em Python com navegação interativa via CLI e simulação de tempo de carregamento usando o módulo `time`.
4. **Testes:** Validação dos fluxos de cadastro (limite de até 5 cortes), listagem dos serviços cadastrados e processo de agendamento.
5. **Implantação:** Execução do script em ambiente Python no terminal local.
6. **Manutenção:** Ajustes de código e preparação do sistema para a futura versão com Interface Gráfica (GUI).

---

## 🚀 Funcionalidades do Sistema

* **`1` - Cadastrar corte:** Permite o registro de até 5 cortes individuais, armazenando nome, quantidade disponível em estoque/vagas, preço e descrição do corte.
* **`2` - Listar cortes:** Exibe todos os cortes cadastrados no sistema com seus respectivos detalhes (Nome, Estoque, Preço e Descrição).
* **`3` - Realizar agendamento:** Exibe os cortes disponíveis com seus respectivos valores e permite ao cliente escolher o corte desejado para agendar.
* **`0` - Sair do sistema:** Encerra a execução do programa de forma segura.

---

## 🛠️ Tecnologias e Conceitos Utilizados

* **Linguagem:** Python 3
* **Módulo Nativo:** `time` (utilizado para inserir pausas com `time.sleep()`, proporcionando dinamismo e simulação de processamento na CLI).
* **Estruturas de Repetição:** Laço `while True` para manter o menu interativo em execução até a finalização pelo usuário.
* **Estruturas Condicionais:** `if / elif / else` para gerenciamento das opções do menu e verificação das variáveis de armazenamento de cortes (`c1` a `c5`).
* **Interatividade & Saída:** Uso de *f-strings* e emojis decorativos (✂️, 💠) para melhorar a apresentação dos dados no terminal.

---

## 💻 Como Executar o Programa

### Pré-requisitos

* **Python 3.x** instalado no sistema.

### Passo a Passo

1. **Baixar o Código:** Salve o arquivo Python (por exemplo, `barbearia.py`) na sua máquina.
2. **Abrir o Terminal:** Navegue até a pasta onde o arquivo foi salvo.
3. **Executar a Aplicação:** Execute o seguinte comando no terminal:
   ```bash
   python barbearia.py