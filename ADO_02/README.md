# 🍎 ADO 02 · Leis de Newton e Simulação Interativa

Simulador de sistemas físicos clássicos modelados com **fórmulas matemáticas fechadas**, sem integração numérica: plano inclinado, força centrípeta e força de arrasto.

🌐 **Teste online:** https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_02/web/

## 🎯 Cenários

### 1. Plano inclinado com bloco pendurado
Dois blocos ligados por um fio: m₁ sobre o plano e m₂ pendurado. O gráfico mostra posição e velocidade no tempo, e o painel mostra a aceleração e a tração. Se o atrito estático for suficiente, o sistema permanece em repouso.

Parâmetros: massa 1, massa 2, ângulo do plano e coeficiente de atrito μ.

### 2. Força centrípeta (movimento circular uniforme)
Trajetória circular de uma partícula, com cálculo da velocidade angular ω e da força centrípeta F_c.

Parâmetros: raio, velocidade e massa.

### 3. Arrasto
Compara a queda livre com a queda sob arrasto **linear** ou **quadrático**, mostrando a velocidade terminal.

Parâmetros: massa, coeficiente de arrasto e tipo de arrasto.

## 📐 Equações utilizadas

```
Plano inclinado:  a = (m₂·g − m₁·g·senθ − μ·m₁·g·cosθ) / (m₁ + m₂)
                  T = m₂·(g − a)

Centrípeta:       ω = v / r        F_c = m·v² / r

Arrasto linear:      v(t) = (m·g/b)·(1 − e^(−b·t/m))
Arrasto quadrático:  v(t) = v_t·tanh(g·t / v_t),   v_t = √(m·g/k)
```

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `simulacao_newto.py` | Versão desktop (Tkinter + Matplotlib) |
| `web/app.py` | Versão para navegador (Streamlit) |
| `web/index.html` | Página que carrega a versão web com stlite |

## ▶️ Como executar

### Online
Abra o link no topo. Na primeira visita pode levar de 10 a 30 segundos para carregar.

### Versão desktop
```bash
pip install numpy matplotlib
python simulacao_newto.py
```
O Tkinter já vem com o Python no Windows e no macOS. No Linux (Debian/Ubuntu): `sudo apt install python3-tk`.

### Versão web no seu computador
```bash
pip install streamlit numpy matplotlib
streamlit run web/app.py
```

Ou, sem instalar o Streamlit, na raiz do repositório:
```bash
python -m http.server 8000
```
e abra `http://localhost:8000/ADO_02/web/` (não abra o HTML com duplo clique).

## 🛠️ Tecnologias

Python 3 · NumPy · Matplotlib · Tkinter · Streamlit (versão web) · stlite

[← Voltar ao repositório](../README.md)
