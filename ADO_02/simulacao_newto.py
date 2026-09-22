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
        self.geometry("900x600")

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

    def mudar_sistema(self):
        sistema_atual = self.sis_var.get()
        
        # Limpa o gráfico anterior
        self.ax.clear()
        self.ax.set_title(f"Gráfico: {sistema_atual.upper()}")
        self.ax.grid(True)
        
        # Atualiza o texto informativo
        self.lbl_res.config(text=f"Sistema selecionado:\n-> {sistema_atual}")
        
        # Atualiza a tela do Matplotlib dentro do Tkinter
        self.canvas.draw()

# Instanciação e execução
if __name__ == "__main__":
    app = SimuladorFisica()
    app.mainloop()