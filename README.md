# 🪐 Portfólio Acadêmico: Simulações Físicas em Python

Este repositório documenta os projetos e simulações interativas desenvolvidos durante a disciplina de **Física Práticas Extensivas / Mecânica e Física Moderna**. 

O objetivo central deste portfólio é demonstrar a aplicação prática de conceitos físicos fundamentais através de modelagem matemática e engenharia de software, construindo interfaces gráficas que permitem a visualização de sistemas físicos em tempo real.

## 👨‍💻 Autor / Equipe
**[Membros do Grupo]** - Estudantes de Ciência da Computação: 
* Pedro Canute
* Gustavo Souza Freitas
* Miguel Hakira Mendes Kato
* Thiago Oliete Ogata Almeida


## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3
* **Bibliotecas Científicas:** NumPy, Matplotlib
* **Interfaces Gráficas (GUI):** Matplotlib.widgets (Sliders, Buttons), Tkinter
* **Documentação:** Markdown, Jupyter Notebook

---

## 📂 Índice de Atividades (Projetos)

Ao longo do semestre, as seguintes simulações foram desenvolvidas. Clique nos links para acessar o código-fonte, as instruções de execução e os relatórios de cada projeto:

### 🚀 [ADO 01: Lançamento de Projéteis](./ADO_01/)
* **Descrição:** Simulação interativa do movimento parabólico de projéteis considerando o caso ideal (sem a resistência do ar).
* **Conceitos Físicos:** Cinemática, decomposição de vetores, equações analíticas para alcance total, altura máxima e tempo de voo.
* **Destaque Técnico:** Atualização do gráfico de trajetória em tempo real conforme a alteração interativa de parâmetros (velocidade inicial, ângulo e gravidade).

### 🍎 [ADO 02: Leis de Newton e Simulação Interativa](./ADO_02/)
* **Descrição:** Modelagem do comportamento de sistemas físicos clássicos (como Plano Inclinado, Força Centrípeta e Força de Arrasto) utilizando fórmulas matemáticas fechadas.
* **Conceitos Físicos:** Segunda Lei de Newton $(\Sigma\vec{F}=m\vec{a})$, força de atrito, tração, movimento circular uniforme e cinemática de forças não constantes.
* **Destaque Técnico:** Demonstração visual da evolução da posição e velocidade no tempo sem o uso de laços de integração numérica, avaliando vetores de tempo com NumPy e construindo interfaces de seleção de cenários.

---

## 🧠 Competências Desenvolvidas

* **Modelagem Física:** Capacidade de extrair equações de movimento a partir de diagramas de corpo livre e traduzi-las em lógica de programação.
* **Desenvolvimento de GUI:** Criação de ferramentas visuais focadas na experiência do usuário para alterar parâmetros ($m$, $\theta$, $\mu$, etc.) e observar mudanças instantâneas no sistema.
* **Análise de Dados:** Compreensão profunda de fórmulas fechadas e cálculo vetorizado para dispensar a necessidade de integração numérica passo a passo (como métodos de Euler) em sistemas analíticos.
