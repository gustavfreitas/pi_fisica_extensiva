# 🚀 ADO 01 · Lançamento de Projéteis

Simulação interativa do movimento parabólico de um projétil no **caso ideal** (sem resistência do ar), calculado por fórmulas analíticas fechadas.

🌐 **Teste online:** https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_01/web/

## 🎯 O que a simulação faz

- Desenha a trajetória do projétil em tempo real conforme você altera os parâmetros
- Calcula o **tempo de voo**, a **altura máxima** e o **alcance horizontal**
- Guarda um **histórico de lançamentos** no mesmo gráfico, para comparar trajetórias
- Anima o último lançamento (botão **Lançar**) e limpa o gráfico (botão **Limpar**)
- Usa escala 1:1 nos eixos, para não distorcer a forma da trajetória

## ⚙️ Parâmetros

| Parâmetro | Símbolo | Intervalo |
|-----------|---------|-----------|
| Velocidade inicial | v₀ | 5 a 150 m/s |
| Ângulo de lançamento | θ | 1° a 89° |
| Altura inicial | y₀ | 0 a 50 m |
| Gravidade | g | 1,6 a 24,8 m/s² (Lua a Júpiter) |

## 📐 Equações utilizadas

```
x(t) = x₀ + v₀·cosθ·t
y(t) = y₀ + v₀·senθ·t − ½·g·t²

t_voo = ( v₀·senθ + √((v₀·senθ)² + 2·g·y₀) ) / g
y_max = y₀ + (v₀·senθ)² / (2·g)
R     = x₀ + v₀·cosθ·t_voo
```

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `disparo_projetil.py` | Versão desktop (Matplotlib com sliders e botões) |
| `web/app.py` | Versão para navegador (Streamlit) |
| `web/index.html` | Página que carrega a versão web com stlite |

## ▶️ Como executar

### Online
Abra o link no topo. Na primeira visita pode levar de 10 a 30 segundos para carregar.

### Versão desktop
```bash
pip install numpy matplotlib
python disparo_projetil.py
```

### Versão web no seu computador
```bash
pip install streamlit numpy matplotlib
streamlit run web/app.py
```

Ou, sem instalar o Streamlit, na raiz do repositório:
```bash
python -m http.server 8000
```
e abra `http://localhost:8000/ADO_01/web/` (não abra o HTML com duplo clique: o navegador bloqueia o carregamento do `app.py`).

## 🛠️ Tecnologias

Python 3 · NumPy · Matplotlib · Streamlit (versão web) · stlite

[← Voltar ao repositório](../README.md)
