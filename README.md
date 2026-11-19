# 🪐 Portfólio Acadêmico: Simulações Físicas em Python

[![Portal online](https://img.shields.io/badge/🌐_Portal-online-5b9dff)](https://gustavfreitas.github.io/pi_fisica_extensiva/)
[![Python](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![Licença MIT](https://img.shields.io/badge/licença-MIT-green)](LICENSE)

Este repositório documenta os projetos e simulações interativas desenvolvidos durante a disciplina de **Física Práticas Extensivas / Mecânica e Física Moderna**.

O objetivo central deste portfólio é demonstrar a aplicação prática de conceitos físicos fundamentais através de modelagem matemática e engenharia de software, construindo interfaces gráficas que permitam a visualização de sistemas físicos em tempo real.

## 🌐 Teste online (sem instalar nada)

As três simulações rodam direto no navegador, em computador ou celular:

| Atividade | Simulação online |
|-----------|------------------|
| **ADO 01** · Lançamento de Projéteis | [Abrir simulação](https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_01/web/) |
| **ADO 02** · Leis de Newton | [Abrir simulação](https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_02/web/) |
| **ADO 03** · Colisões e Conservação de Momento | [Abrir simulação](https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_03/web/) |

📚 **Portal com todas as entregas:** https://gustavfreitas.github.io/pi_fisica_extensiva/

> Na primeira visita, o navegador baixa o Python e as bibliotecas (de 10 a 30 segundos). Depois disso, a página abre rápido.

## 👨‍💻 Autor / Equipe

Estudantes de Ciência da Computação:

- Pedro Cristiano Batista Canute
- Gustavo Souza Freitas
- Miguel Hakira Mendes Kato
- Thiago Oliete Ogata Almeida

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3
- **Bibliotecas científicas:** NumPy, Matplotlib
- **Interfaces gráficas (versão desktop):** Matplotlib.widgets (Sliders, Buttons, RadioButtons) e Tkinter
- **Versão web:** Streamlit executado no navegador com [stlite](https://github.com/whitphx/stlite) (Pyodide/WebAssembly)
- **Relatórios automatizados:** ReportLab (geração de PDFs)
- **Documentação:** Markdown, Jupyter Notebook

## 📂 Índice de Atividades

Cada pasta tem um `README.md` próprio, com explicação, instruções de execução e link para a versão online.

### 🚀 [ADO 01: Lançamento de Projéteis](ADO_01/)
- **Descrição:** simulação interativa do movimento parabólico de projéteis, considerando o caso ideal (sem resistência do ar).
- **Conceitos físicos:** cinemática, decomposição de vetores, equações analíticas para alcance total, altura máxima e tempo de voo.
- **Destaque técnico:** atualização do gráfico de trajetória em tempo real conforme a alteração interativa de parâmetros (velocidade inicial, ângulo e gravidade).

### 🍎 [ADO 02: Leis de Newton e Simulação Interativa](ADO_02/)
- **Descrição:** modelagem do comportamento de sistemas físicos clássicos (plano inclinado, força centrípeta e força de arrasto) utilizando fórmulas matemáticas fechadas.
- **Conceitos físicos:** Segunda Lei de Newton, força de atrito, tração, movimento circular uniforme e cinemática de forças não constantes.
- **Destaque técnico:** demonstração visual da evolução da posição e velocidade no tempo, sem laços de integração numérica, com vetores de tempo em NumPy e interface de seleção de cenários.

### 💥 [ADO 03: Colisões e Conservação de Momento](ADO_03/)
- **Descrição:** animação interativa 1D focada no Teorema do Impulso, conservação de momento linear e energia cinética (Opção A).
- **Conceitos físicos:** colisões elásticas, impulso (J), força média (F_med) e transferência de energia entre massas.
- **Destaque técnico:** casos prontos (massas iguais, alvo pesado, projétil pesado), gráficos de momento e energia antes e depois do choque e relatório em PDF. Inclui, como extra, um bilhar 2D.

## 🗂️ Estrutura do repositório

```
pi_fisica_extensiva/
├── index.html          # portal online (GitHub Pages)
├── ADO_01/             # lançamento de projéteis
│   ├── disparo_projetil.py
│   └── web/            # versão para navegador
├── ADO_02/             # leis de Newton
│   ├── simulacao_newto.py
│   └── web/
├── ADO_03/             # colisões e conservação de momento
│   ├── simulacao_colisoes.py
│   ├── bilhar_2D.py    # extra opcional
│   └── web/
├── LICENSE
└── README.md
```

## ▶️ Como executar no seu computador

```bash
# 1. Clonar o repositório
git clone https://github.com/gustavfreitas/pi_fisica_extensiva.git
cd pi_fisica_extensiva

# 2. (Opcional) criar ambiente virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / macOS

# 3. Instalar dependências
pip install numpy matplotlib reportlab

# 4. Executar uma das simulações
python ADO_01/disparo_projetil.py
python ADO_02/simulacao_newto.py
python ADO_03/simulacao_colisoes.py
```

> O Tkinter já vem com o Python no Windows e no macOS. No Linux (Debian/Ubuntu), instale com `sudo apt install python3-tk`.

Para rodar as versões web localmente, veja o README de cada pasta.

## 📜 Licença

Distribuído sob a licença [MIT](LICENSE).
