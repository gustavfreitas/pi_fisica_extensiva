import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

G = 9.81

class SimuladorFisica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulação Interativa - Mecânica e Física Moderna")
        self.geometry("1200x720")

        # Layout: Controle (Esquerda) e Gráfico (Direita)
        painel_ctrl = ttk.Frame(self, padding=10)
        painel_ctrl.pack(side=tk.LEFT, fill=tk.Y)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Seletor de Sistema Físico
        self.sis_var = tk.StringVar(value="plano")
        sistemas = [("Plano Inclinado", "plano"), ("Força Centrípeta", "mcu"), ("Arrasto", "arrasto")]
        for txt, val in sistemas:
            ttk.Radiobutton(painel_ctrl, text=txt, value=val, variable=self.sis_var, command=self.mudar_sistema).pack(anchor=tk.W)

        ttk.Separator(painel_ctrl, orient='horizontal').pack(fill='x', pady=10)

        # Containers dinâmicos
        self.frame_sliders = ttk.Frame(painel_ctrl)
        self.frame_sliders.pack(fill=tk.X, expand=True)
        
        self.lbl_res = ttk.Label(painel_ctrl, font=("Consolas", 10), justify=tk.LEFT)
        self.lbl_res.pack(fill=tk.X, pady=10)

        self.sliders = {}
        self.mudar_sistema()

    def criar_slider(self, nome, vmin, vmax, vinit):
        lbl = ttk.Label(self.frame_sliders, text=f"{nome}: {vinit:.2f}")
        lbl.pack(anchor=tk.W)
        slider = ttk.Scale(self.frame_sliders, from_=vmin, to=vmax, value=vinit, 
                           command=lambda v, l=lbl, n=nome: self.atualizar(v, l, n))
        slider.pack(fill=tk.X, pady=2)
        self.sliders[nome] = slider

    def atualizar(self, val, lbl, nome):
        lbl.config(text=f"{nome}: {float(val):.2f}")
        self.simular()

    def mudar_sistema(self):
        # Limpa sliders antigos
        for w in self.frame_sliders.winfo_children(): w.destroy()
        self.sliders.clear()
        sis = self.sis_var.get()

        # Gera novos sliders dinamicamente usando listas
        if sis == "plano":
            for p in [("Massa_1", 0.5, 20, 5), ("Massa_2", 0.5, 20, 7), ("Angulo", 0, 80, 30), ("Movimento_Uniforme", 0, 1, 0.2)]: 
                self.criar_slider(*p)
        elif sis == "mcu":
            for p in [("Raio", 0.5, 10, 3), ("Velocidade", 1, 30, 10), ("Massa", 0.1, 10, 2)]: 
                self.criar_slider(*p)
        elif sis == "arrasto":
            for p in [("Massa", 0.1, 10, 2), ("Coeficiente", 0.01, 2, 0.3)]: 
                self.criar_slider(*p)
            
            self.tipo_arrasto = tk.StringVar(value="linear")
            for t in ["linear", "quadrático"]:
                ttk.Radiobutton(self.frame_sliders, text=t.capitalize(), value=t[:3], variable=self.tipo_arrasto, command=self.simular).pack(anchor=tk.W)
        
        self.simular()

    def simular(self):
        self.ax.clear()
        self.ax.set_aspect('auto')
        sis = self.sis_var.get()

        # Extrai os valores atuais de todos os sliders de uma vez
        v = {k: s.get() for k, s in self.sliders.items()}

        if sis == "plano":
            th = np.radians(v["Angulo"])
            N = v["Massa_1"] * G * np.cos(th)
            F_motriz = v["Massa_2"] * G - v["Massa_1"] * G * np.sin(th)
            
            # Condição de movimento condensada em uma linha (operador ternário)
            a = 0 if abs(F_motriz) <= v["Movimento_Uniforme"] * N else (F_motriz - v["Movimento_Uniforme"] * N * np.sign(F_motriz)) / (v["Massa_1"] + v["Massa_2"])
            
            t = np.linspace(0, 5, 100)
            self.ax.plot(t, 0.5 * a * t**2, 'b-', label='Posição [m]')
            self.ax.plot(t, a * t, 'r--', label='Velocidade [m/s]')
            self.lbl_res.config(text=f"Aceleração: {a:.2f} m/s²\nTração: {v['Massa_2']*(G-a):.2f} N")

        elif sis == "mcu":
            w = v["Velocidade"] / v["Raio"]
            t = np.linspace(0, 2 * np.pi / w if w > 0 else 5, 200)
            x, y = v["Raio"] * np.cos(w * t), v["Raio"] * np.sin(w * t)
            
            self.ax.plot(x, y, 'g-')
            self.ax.scatter([x[0]], [y[0]], color='red', zorder=5) # Partícula
            self.ax.set_aspect('equal', 'box')
            self.lbl_res.config(text=f"ω: {w:.2f} rad/s\nForça Centrípeta: {v['Massa']*(v['Velocidade']**2)/v['Raio']:.2f} N")

        elif sis == "arrasto":
            t = np.linspace(0, 10, 200)
            if self.tipo_arrasto.get() == "lin":
                v_term = (v["Massa"] * G) / v["Coeficiente"]
                vel = v_term * (1 - np.exp(-t / (v["Massa"] / v["Coeficiente"])))
            else:
                v_term = np.sqrt((v["Massa"] * G) / v["Coeficiente"])
                vel = v_term * np.tanh((G * t) / v_term)

            self.ax.plot(t, G * t, 'k--', label='Queda Livre')
            self.ax.plot(t, vel, 'b-', label='Com Arrasto')
            self.ax.axhline(v_term, color='r', linestyle=':', label=f'v_term = {v_term:.2f}')
            self.lbl_res.config(text=f"Vel. Terminal: {v_term:.2f} m/s")

        # Configurações visuais globais para todos os gráficos
        self.ax.grid(True, linestyle=':', alpha=0.6)
        if self.ax.get_legend_handles_labels()[0]: 
            self.ax.legend()
            self.fig.tight_layout()
            self.canvas.draw()

if __name__ == "__main__":
    SimuladorFisica().mainloop()