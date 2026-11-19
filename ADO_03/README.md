# 💥 ADO 03 · Colisões e Conservação de Momento

Animação interativa de **colisões elásticas unidimensionais**, focada no Teorema do Impulso e na conservação de momento linear e de energia cinética (Opção A do roteiro).

🌐 **Teste online:** https://gustavfreitas.github.io/pi_fisica_extensiva/ADO_03/web/

## 🎯 O que a simulação faz

- Anima a colisão entre dois blocos, com tamanho proporcional à raiz da massa
- Calcula as **velocidades após o choque** (u₁ e u₂)
- Mostra o **momento linear** e a **energia cinética** antes e depois, em gráficos de barras
- Calcula o **impulso** de cada bloco (J₁ e J₂) e a **força média** F_med a partir do tempo de contato Δt
- Avisa quando **não há colisão** (v₁ ≤ v₂)
- Oferece três casos prontos:

| Caso | m₁ | m₂ | v₁ | v₂ |
|------|----|----|----|----|
| 1 · Massas iguais | 1 kg | 1 kg | 4 m/s | 0 |
| 2 · Alvo pesado | 1 kg | 4 kg | 5 m/s | 0 |
| 3 · Projétil pesado | 4 kg | 1 kg | 5 m/s | 0 |

## 📐 Equações utilizadas

```
u₁ = ((m₁ − m₂)·v₁ + 2·m₂·v₂) / (m₁ + m₂)
u₂ = ((m₂ − m₁)·v₂ + 2·m₁·v₁) / (m₁ + m₂)

p = m₁·v₁ + m₂·v₂            (conservado)
K = ½·m₁·v₁² + ½·m₂·v₂²      (conservado na colisão elástica, ΔK = 0)

J_i = m_i·(u_i − v_i)         F_med = |J₁| / Δt
```

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `simulacao_colisoes.py` | Versão desktop (Matplotlib com sliders, botões e animação) |
| `relatorio_ado03.py` | Gera o relatório da atividade em PDF |
| `relatorio_ado3_colisoes.pdf` | Relatório da atividade |
| `bilhar_2D.py` | 🎱 Extra opcional: bilhar 2D, só por diversão |
| `web/app.py` | Versão para navegador (Streamlit) |
| `web/index.html` | Página que carrega a versão web com stlite |

## ▶️ Como executar

### Online
Abra o link no topo. Na primeira visita pode levar de 10 a 30 segundos para carregar.

### Versão desktop
```bash
pip install numpy matplotlib
python simulacao_colisoes.py
```

### Relatório em PDF
```bash
pip install reportlab
python relatorio_ado03.py
```

### Extra: bilhar 2D (opcional)
```bash
python bilhar_2D.py
```
Não faz parte dos requisitos da atividade.

### Versão web no seu computador
```bash
pip install streamlit numpy matplotlib
streamlit run web/app.py
```

Ou, sem instalar o Streamlit, na raiz do repositório:
```bash
python -m http.server 8000
```
e abra `http://localhost:8000/ADO_03/web/` (não abra o HTML com duplo clique).

## 🛠️ Tecnologias

Python 3 · NumPy · Matplotlib · ReportLab · Streamlit (versão web) · stlite

[← Voltar ao repositório](../README.md)
