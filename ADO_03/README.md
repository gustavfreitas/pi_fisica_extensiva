# ADO 3: Colisões, Impulso e Conservação do Momento Linear

Módulo desenvolvido para a disciplina de **Mecânica e Física Moderna** (Ciência da Computação), focado na simulação interativa de colisões unidimensionais elásticas (Opção A) e na análise de grandezas dinâmicas.

## 🚀 Funcionalidades da Aplicação (`simulacao_colisoes.py`)

* **Animação Vetorial Real-Time:** Utiliza `matplotlib.animation.FuncAnimation` para renderizar o movimento retilíneo uniforme (MRU) antes e depois do impacto.
* **Cálculo Analítico do Instante de Choque ($t_c$):** O momento exato da colisão entre os blocos é determinado matematicamente através de equações fechadas (Seção 2 do roteiro).
* **Três Casos de Teste Integrados:** Menu interativo com botões (`RadioButtons`) para alternar instantaneamente entre:
  1. Massas iguais ($m_1 = m_2$)
  2. Projétil leve e alvo pesado ($m_1 < m_2$)
  3. Projétil pesado e alvo leve ($m_1 > m_2$)
* **Painel de Telemetria Dinâmico:** Exibe em tempo real as velocidades antes/depois, momento linear total ($p$), energia cinética ($K$), variação da energia ($\Delta K$), impulsos ($J_1, J_2$) e a força média ($F_{med}$).
* **Gráficos de Barras Comparativos:** Visualização gráfica imediata da conservação do momento e da energia antes e depois do choque.
* **Tratamento de Exceções Físicas:** Mensagem integrada na tela para cenários sem colisão ($v_1 \le v_2$).

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **NumPy:** Processamento numérico e cálculos vetorizados.
* **Matplotlib:** Interface gráfica, widgets (`Slider`, `Button`, `RadioButtons`) e motor de animação.
* **ReportLab:** Biblioteca utilizada pelo script `relatorio_ado03.py` para compilar o relatório acadêmico automatizado em PDF.

## ⚙️ Como Executar

1. Certifique-se de estar na raiz do repositório e de que as dependências estão instaladas:
   ```bash
   pip install numpy matplotlib reportlab
   ```
2. Para rodar a simulação interativa da ADO 3:
   ```bash
   python ADO_03/simulacao_colisoes.py
   ```
3. Para gerar o relatório oficial em PDF formatado com base nas respostas Q1-Q5:
   ```bash
   python ADO_03/relatorio_ado03.py
   ```