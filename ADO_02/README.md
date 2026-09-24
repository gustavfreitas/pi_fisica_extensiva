# Simulação Interativa de Sistemas Físicos Clássicos

Repositório contendo a entrega completa da Atividade de Programação (ADO 2) para a disciplina de Mecânica e Física Moderna do curso de Ciência da Computação. O projeto simula três sistemas físicos utilizando equações fechadas e renderização gráfica em tempo real.

## 🚀 Funcionalidades e Atualizações Implementadas

O projeto foi refatorado e aprimorado em relação aos requisitos básicos, contando com as seguintes características:

* **Interface Gráfica Dinâmica:** Desenvolvida em Python com `tkinter` e `ttk`, utilizando geração dinâmica de componentes (sliders) e dicionários para extração de dados em tempo real.
* **Processamento Vetorizado:** Cálculo direto das equações físicas em vetores de tempo utilizando `numpy`, dispensando laços de integração numérica (Euler/Runge-Kutta).
* **Correção de Renderização:** Integração estável com `matplotlib` (`FigureCanvasTkAgg`), com tratamento de limpeza de eixos (`ax.clear()`) e redefinição de proporções geométricas para evitar sobreposição e distorção de gráficos.
* **Animação Interativa (Upgrade):** Adição de um controle de tempo ("Tempo t") no módulo de Força Centrípeta, permitindo visualizar a posição exata da partícula (ponto vermelho) ao longo da trajetória circular em qualquer instante.
* **Geração Automatizada de Relatório:** Script independente utilizando `reportlab` que extrai as lógicas do código principal (como a utilização do operador ternário para a Força de Atrito) e gera um PDF formatado com todas as deduções matemáticas e análises exigidas.

## 📂 Estrutura do Projeto

* `simulacao_fisica.exe`: Ficheiro executável standalone da aplicação principal (permite correr a simulação sem ter o Python instalado).
* `simulacao_fisica.py`: Script principal com o código-fonte da interface gráfica e plotagem dos gráficos interativos.
* `gerar_relatorio.py`: Script secundário responsável por compilar e exportar o relatório académico de 3 páginas.
* `relatorio_fisica.pdf`: PDF final gerado (saída).

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **NumPy:** Álgebra vetorizada e manipulação de arrays contínuos.
* **Matplotlib:** Plotagem de gráficos 2D, trajetórias e assíntotas.
* **Tkinter:** Construção da interface de utilizador (GUI).
* **ReportLab:** Criação de documentos PDF via código.

## ⚙️ Instalação e Execução

### Opção 1: Através do Executável (Não requer Python)
1. Faça o download do ficheiro `simulacao_fisica.exe`.
2. Clique duas vezes sobre o ficheiro para abrir a interface gráfica instantaneamente.

### Opção 2: Através do Código-Fonte (Requer Python)
1. Clone o repositório para a sua máquina local.
2. Instale as dependências necessárias utilizando o gestor de pacotes `pip`:
   ```bash
   pip install numpy matplotlib reportlab
   ```
1. Para iniciar a simulação interativa, execute:
  ```bash
python simulacao_fisica.py
  ```
2. Para gerar o relatório em PDF atualizado na mesma pasta, execute:  
  ```Bash
python gerar_relatorio.py
  ```
  
## 📐 Sistemas Físicos Modelados
* **Plano Inclinado com Atrito e Tração:** Aplicação da 2ª Lei de Newton para avaliar tensão, força normal, atrito cinético/estático e transição de repouso para movimento retilíneo uniformemente variado (MRUV).

* **Força Centrípeta (MCU):** Avaliação de velocidade angular (ω), força centrípeta e plotagem paramétrica do raio de curvatura.

* **Força de Arrasto (Queda Vertical):** Comparação visual e analítica entre resistência linear (exponencial) e quadrática (tangente hiperbólica), evidenciando a saturação na velocidade terminal.
