import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.set_page_config(page_title="ADO 02 - Leis de Newton", page_icon="🍎", layout="wide")

G = 9.81

st.title("🍎 ADO 02 · Leis de Newton e Simulação Interativa")
st.caption(
    "Sistemas clássicos modelados com fórmulas fechadas (sem integração numérica): "
    "plano inclinado, força centrípeta e força de arrasto."
)

with st.sidebar:
    st.header("Sistema físico")
    sis = st.radio(
        "Escolha o cenário",
        ["Plano Inclinado", "Força Centrípeta", "Arrasto"],
        label_visibility="collapsed",
    )
    st.divider()
    st.header("Parâmetros")

    if sis == "Plano Inclinado":
        m1 = st.slider("Massa 1 — sobre o plano (kg)", 0.5, 20.0, 5.0, 0.1)
        m2 = st.slider("Massa 2 — pendurada (kg)", 0.5, 20.0, 7.0, 0.1)
        ang = st.slider("Ângulo do plano (°)", 0.0, 80.0, 30.0, 1.0)
        mu = st.slider("Coeficiente de atrito μ", 0.0, 1.0, 0.2, 0.01)
    elif sis == "Força Centrípeta":
        raio = st.slider("Raio (m)", 0.5, 10.0, 3.0, 0.1)
        vel = st.slider("Velocidade (m/s)", 1.0, 30.0, 10.0, 0.5)
        massa = st.slider("Massa (kg)", 0.1, 10.0, 2.0, 0.1)
        pos = st.slider("Posição da partícula (°)", 0, 360, 0, 5)
    else:
        massa = st.slider("Massa (kg)", 0.1, 10.0, 2.0, 0.1)
        coef = st.slider("Coeficiente de arrasto", 0.01, 2.0, 0.3, 0.01)
        tipo = st.radio("Tipo de arrasto", ["Linear", "Quadrático"], horizontal=True)

fig, ax = plt.subplots(figsize=(8, 5), dpi=90)

if sis == "Plano Inclinado":
    th = np.radians(ang)
    N = m1 * G * np.cos(th)
    F_motriz = m2 * G - m1 * G * np.sin(th)
    if abs(F_motriz) <= mu * N:
        a = 0.0  # atrito estático segura o sistema
    else:
        a = (F_motriz - mu * N * np.sign(F_motriz)) / (m1 + m2)

    t = np.linspace(0, 5, 100)
    ax.plot(t, 0.5 * a * t**2, "b-", label="Posição [m]")
    ax.plot(t, a * t, "r--", label="Velocidade [m/s]")
    ax.set_xlabel("Tempo (s)")
    ax.set_title("Plano inclinado com bloco pendurado")

    c1, c2, c3 = st.columns(3)
    c1.metric("Aceleração", f"{a:.2f} m/s²")
    c2.metric("Tração", f"{m2 * (G - a):.2f} N")
    c3.metric("Força normal", f"{N:.2f} N")
    if a == 0:
        st.info("O atrito é suficiente para manter o sistema em repouso (aceleração = 0).")

elif sis == "Força Centrípeta":
    w = vel / raio
    periodo = 2 * np.pi / w
    t = np.linspace(0, periodo, 300)
    x, y = raio * np.cos(w * t), raio * np.sin(w * t)
    ax.plot(x, y, "g-")

    ang_p = np.radians(pos)
    px, py = raio * np.cos(ang_p), raio * np.sin(ang_p)
    ax.scatter([px], [py], color="red", zorder=5, s=60, label="Partícula")
    ax.scatter([0], [0], color="black", s=20)
    ax.annotate(
        "", xy=(px * 0.45, py * 0.45), xytext=(px, py),
        arrowprops=dict(arrowstyle="->", color="purple", lw=2),
    )
    ax.text(px * 0.72, py * 0.72, " F_c", color="purple", fontsize=11)
    ax.set_aspect("equal", "box")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_title("Movimento circular uniforme")

    Fc = massa * vel**2 / raio
    c1, c2, c3 = st.columns(3)
    c1.metric("Velocidade angular ω", f"{w:.2f} rad/s")
    c2.metric("Força centrípeta", f"{Fc:.2f} N")
    c3.metric("Período", f"{periodo:.2f} s")

else:
    t = np.linspace(0, 10, 200)
    if tipo == "Linear":
        v_term = (massa * G) / coef
        v = v_term * (1 - np.exp(-t / (massa / coef)))
    else:
        v_term = np.sqrt((massa * G) / coef)
        v = v_term * np.tanh((G * t) / v_term)

    ax.plot(t, G * t, "k--", label="Queda livre")
    ax.plot(t, v, "b-", label="Com arrasto")
    ax.axhline(v_term, color="r", linestyle=":", label=f"v_term = {v_term:.2f}")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Velocidade (m/s)")
    ax.set_title(f"Queda com arrasto {tipo.lower()}")
    st.metric("Velocidade terminal", f"{v_term:.2f} m/s")

ax.grid(True, linestyle=":", alpha=0.6)
if ax.get_legend_handles_labels()[0]:
    ax.legend()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

with st.expander("Equações utilizadas"):
    if sis == "Plano Inclinado":
        st.latex(r"a = \dfrac{m_2 g - m_1 g\sin\theta - \mu\, m_1 g\cos\theta}{m_1 + m_2}")
        st.latex(r"T = m_2 (g - a)")
    elif sis == "Força Centrípeta":
        st.latex(r"\omega = \dfrac{v}{r} \qquad F_c = \dfrac{m v^2}{r}")
    else:
        st.latex(r"\text{Linear: } v(t) = \dfrac{mg}{b}\left(1 - e^{-bt/m}\right)")
        st.latex(r"\text{Quadrático: } v(t) = v_t \tanh\!\left(\dfrac{g t}{v_t}\right),\; v_t = \sqrt{\dfrac{mg}{k}}")
