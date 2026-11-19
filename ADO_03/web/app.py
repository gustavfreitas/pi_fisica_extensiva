import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ADO 03 - Colisões e Momento", page_icon="💥", layout="wide")


def mostrar_html(html, altura):
    """Mostra um trecho de HTML/JS (compatível com versões novas e antigas do Streamlit)."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=altura)
    else:
        components.html(html, height=altura, scrolling=True)


# ---------------------------------------------------------------------------
# NÚCLEO DE FÍSICA (fórmulas fechadas)
# ---------------------------------------------------------------------------
def calcular_fisica(m1, m2, v1, v2, dt_ms):
    if v1 <= v2:
        return {"colisao": False}

    # Colisão elástica 1D
    u1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    u2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

    p_antes = m1 * v1 + m2 * v2
    p_depois = m1 * u1 + m2 * u2

    k_antes = 0.5 * m1 * v1**2 + 0.5 * m2 * v2**2
    k_depois = 0.5 * m1 * u1**2 + 0.5 * m2 * u2**2

    j1 = m1 * (u1 - v1)
    j2 = m2 * (u2 - v2)
    dt_s = dt_ms / 1000.0
    f_med = abs(j1) / dt_s if dt_s > 0 else 0.0

    return {
        "colisao": True,
        "u1": u1, "u2": u2,
        "p_antes": p_antes, "p_depois": p_depois,
        "k_antes": k_antes, "k_depois": k_depois, "delta_k": k_depois - k_antes,
        "j1": j1, "j2": j2, "f_med": f_med,
    }


# ---------------------------------------------------------------------------
# ANIMAÇÃO (canvas em JavaScript, roda no próprio navegador)
# ---------------------------------------------------------------------------
HTML_ANIM = """
<div style="font-family:system-ui,sans-serif">
  <canvas id="c" width="1000" height="230" style="width:100%;border-radius:10px;background:#f6f8fc"></canvas>
  <div style="margin-top:8px;display:flex;gap:8px;align-items:center">
    <button id="pp" style="padding:6px 14px;border-radius:8px;border:1px solid #bbb;cursor:pointer">Pausar</button>
    <button id="rs" style="padding:6px 14px;border-radius:8px;border:1px solid #bbb;cursor:pointer">Reiniciar</button>
    <span id="tt" style="margin-left:auto;color:#445;font-size:14px"></span>
  </div>
</div>
<script>
const D = __DATA__;
const cv = document.getElementById('c'), ctx = cv.getContext('2d');
const XMIN = -2, XMAX = 20, W = cv.width, H = cv.height;
const sx = x => (x - XMIN) / (XMAX - XMIN) * W;
const ground = H - 55, scale = W / (XMAX - XMIN);
const w1 = Math.sqrt(D.m1), w2 = Math.sqrt(D.m2);
const x1_0 = 0, x2_0 = 8;
const tc = D.tc, tEnd = tc + 6;
let t = 0, paused = false, last = null, hold = 0;

function pos(t) {
  if (t < tc) return [x1_0 + D.v1 * t, x2_0 + D.v2 * t];
  const a = x1_0 + D.v1 * tc, b = x2_0 + D.v2 * tc;
  return [a + D.u1 * (t - tc), b + D.u2 * (t - tc)];
}
function block(x, w, color, label) {
  const px = w * scale * 0.9;
  ctx.fillStyle = color; ctx.globalAlpha = 0.85;
  ctx.fillRect(sx(x), ground - px, w * scale, px);
  ctx.globalAlpha = 1; ctx.fillStyle = '#fff';
  ctx.font = 'bold 15px system-ui'; ctx.textAlign = 'center';
  ctx.fillText(label, sx(x) + w * scale / 2, ground - px / 2 + 5);
}
function draw() {
  ctx.clearRect(0, 0, W, H);
  ctx.strokeStyle = '#222'; ctx.lineWidth = 3;
  ctx.beginPath(); ctx.moveTo(0, ground); ctx.lineTo(W, ground); ctx.stroke();
  ctx.lineWidth = 1; ctx.fillStyle = '#667'; ctx.font = '12px system-ui'; ctx.textAlign = 'center';
  for (let m = 0; m <= XMAX; m += 2) {
    ctx.beginPath(); ctx.moveTo(sx(m), ground); ctx.lineTo(sx(m), ground + 7); ctx.stroke();
    ctx.fillText(m + ' m', sx(m), ground + 22);
  }
  const [x1, x2] = pos(t);
  block(x1, w1, '#2563eb', 'm1');
  block(x2, w2, '#dc2626', 'm2');
  const v1c = t < tc ? D.v1 : D.u1, v2c = t < tc ? D.v2 : D.u2;
  ctx.fillStyle = '#2563eb'; ctx.font = '13px system-ui'; ctx.textAlign = 'left';
  ctx.fillText('v1 = ' + v1c.toFixed(2) + ' m/s', 12, 24);
  ctx.fillStyle = '#dc2626';
  ctx.fillText('v2 = ' + v2c.toFixed(2) + ' m/s', 12, 44);
  if (t >= tc && t < tc + 0.4) {
    ctx.fillStyle = '#ea580c'; ctx.font = 'bold 22px system-ui'; ctx.textAlign = 'center';
    ctx.fillText('COLISÃO!', W / 2, 36);
  }
  document.getElementById('tt').textContent = 'Tempo: ' + t.toFixed(2) + ' s';
  return [x1, x2];
}
function frame(ts) {
  if (last === null) last = ts;
  const dtReal = Math.min((ts - last) / 1000, 0.1); last = ts;
  if (!paused) {
    if (hold > 0) { hold -= dtReal; if (hold <= 0) { t = 0; } }
    else {
      t += dtReal * 1.5;
      const [x1, x2] = pos(t);
      if (t > tEnd || x1 > XMAX + 1 || x2 > XMAX + 1 || x1 < XMIN - 4 || x2 < XMIN - 4) hold = 0.9;
    }
  }
  draw();
  requestAnimationFrame(frame);
}
document.getElementById('pp').onclick = e => { paused = !paused; e.target.textContent = paused ? 'Continuar' : 'Pausar'; };
document.getElementById('rs').onclick = () => { t = 0; hold = 0; };
requestAnimationFrame(frame);
</script>
"""


def montar_animacao(m1, m2, v1, v2, f):
    # o bloco 1 começa em x=0 (canto esquerdo) e o bloco 2 em x=8
    tc = (8.0 - 0.0 - np.sqrt(m1)) / (v1 - v2)
    dados = {"m1": m1, "m2": m2, "v1": v1, "v2": v2, "u1": f["u1"], "u2": f["u2"], "tc": tc}
    return HTML_ANIM.replace("__DATA__", json.dumps(dados))


# ---------------------------------------------------------------------------
# ESTADO E CASOS PRÉ-DEFINIDOS
# ---------------------------------------------------------------------------
PADRAO = {"m1": 1.0, "m2": 1.0, "v1": 4.0, "v2": 0.0, "dt": 10.0}
CASOS = {
    "Caso 1: Massas Iguais": {"m1": 1.0, "m2": 1.0, "v1": 4.0, "v2": 0.0},
    "Caso 2: Alvo Pesado": {"m1": 1.0, "m2": 4.0, "v1": 5.0, "v2": 0.0},
    "Caso 3: Projétil Pesado": {"m1": 4.0, "m2": 1.0, "v1": 5.0, "v2": 0.0},
}
for k, v in PADRAO.items():
    st.session_state.setdefault(k, v)


def aplicar_caso():
    for k, v in CASOS[st.session_state.caso].items():
        st.session_state[k] = v


# ---------------------------------------------------------------------------
# INTERFACE
# ---------------------------------------------------------------------------
st.title("💥 ADO 03 · Colisões e Conservação de Momento")
st.caption(
    "Colisão elástica unidimensional: Teorema do Impulso, conservação de momento linear "
    "e de energia cinética. Escolha um caso ou ajuste os parâmetros."
)

with st.sidebar:
    st.header("Casos prontos")
    st.radio("Caso", list(CASOS.keys()), key="caso", on_change=aplicar_caso, index=None,
             label_visibility="collapsed")
    st.header("Parâmetros")
    st.slider("m1 (kg)", 0.1, 10.0, step=0.1, key="m1")
    st.slider("m2 (kg)", 0.1, 10.0, step=0.1, key="m2")
    st.slider("v1 (m/s)", 0.0, 15.0, step=0.1, key="v1")
    st.slider("v2 (m/s)", 0.0, 10.0, step=0.1, key="v2")
    st.slider("Δt — duração do impacto (ms)", 1.0, 100.0, step=1.0, key="dt")

m1, m2 = float(st.session_state.m1), float(st.session_state.m2)
v1, v2 = float(st.session_state.v1), float(st.session_state.v2)
dt = float(st.session_state.dt)

f = calcular_fisica(m1, m2, v1, v2, dt)

if not f["colisao"]:
    st.error("NÃO HÁ COLISÃO (v1 ≤ v2): o projétil nunca alcançará o alvo. Aumente v1 ou diminua v2.")
    st.stop()

mostrar_html(montar_animacao(m1, m2, v1, v2, f), 330)

st.subheader("Resultados")
c1, c2, c3, c4 = st.columns(4)
c1.metric("u1 (após)", f"{f['u1']:.2f} m/s", f"{f['u1'] - v1:+.2f} m/s")
c2.metric("u2 (após)", f"{f['u2']:.2f} m/s", f"{f['u2'] - v2:+.2f} m/s")
c3.metric("ΔK", f"{f['delta_k']:.2f} J")
c4.metric("Força média F_med", f"{f['f_med']:.1f} N")

c5, c6 = st.columns(2)
c5.metric("Impulso J1", f"{f['j1']:.2f} N·s")
c6.metric("Impulso J2", f"{f['j2']:.2f} N·s")

if abs(f["p_antes"] - f["p_depois"]) < 1e-9 and abs(f["delta_k"]) < 1e-9:
    st.success("Momento linear e energia cinética conservados (colisão elástica). J1 = −J2.")


def barras(titulo, antes, depois, cor, unidade):
    fig, ax = plt.subplots(figsize=(4, 3.2), dpi=90)
    bars = ax.bar(["Antes", "Depois"], [antes, depois], color=cor)
    ax.bar_label(bars, fmt="%.2f", padding=2)
    ax.set_title(titulo)
    ax.set_ylabel(unidade)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    ax.set_ylim(0, max(antes, depois, 1e-9) * 1.2)
    fig.tight_layout()
    return fig


g1, g2 = st.columns(2)
with g1:
    fig = barras("Momento linear (p)", f["p_antes"], f["p_depois"], "orange", "kg·m/s")
    st.pyplot(fig)
    plt.close(fig)
with g2:
    fig = barras("Energia cinética (K)", f["k_antes"], f["k_depois"], "green", "J")
    st.pyplot(fig)
    plt.close(fig)

with st.expander("Equações utilizadas"):
    st.latex(r"u_1 = \dfrac{(m_1 - m_2)v_1 + 2m_2 v_2}{m_1 + m_2}")
    st.latex(r"u_2 = \dfrac{(m_2 - m_1)v_2 + 2m_1 v_1}{m_1 + m_2}")
    st.latex(r"J_i = m_i (u_i - v_i) \qquad F_{med} = \dfrac{|J_1|}{\Delta t}")
