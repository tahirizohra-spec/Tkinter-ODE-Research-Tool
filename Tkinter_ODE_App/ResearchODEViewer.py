import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import numpy as np

class ResearchODEViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Differential Equations Research Tool")
        self.geometry("900x600")
        self.df = None
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="x")

        ttk.Button(frame, text="Importer CSV (solution ODE)", command=self.load_csv).pack(side="left", padx=10)
        ttk.Button(frame, text="Afficher statistiques", command=self.show_stats).pack(side="left", padx=10)
        ttk.Button(frame, text="Tracer solution", command=self.plot_graph).pack(side="left", padx=10)
        ttk.Button(frame, text="Résoudre une ODE", command=self.solve_ode).pack(side="left", padx=10)
        ttk.Button(frame, text="Exporter JSON", command=self.export_json).pack(side="left", padx=10)

        self.text = tk.Text(self, height=25)
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

    # ----------------------------
    # 1) Importer CSV
    # ----------------------------
    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not filepath:
            return

        try:
            self.df = pd.read_csv(filepath)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, f"Fichier chargé : {os.path.basename(filepath)}\n")
            self.text.insert(tk.END, str(self.df.head()))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

    # ----------------------------
    # 2) Statistiques
    # ----------------------------
    def show_stats(self):
        if self.df is None:
            messagebox.showwarning("Attention", "Importer un fichier CSV.")
            return

        stats = self.df.describe(include="all")
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, str(stats))

    # ----------------------------
    # 3) Tracer solution ODE
    # ----------------------------
    def plot_graph(self):
        if self.df is None:
            messagebox.showwarning("Attention", "Importer un fichier CSV.")
            return

        numeric_cols = self.df.select_dtypes(include="number").columns
        if len(numeric_cols) < 2:
            messagebox.showerror("Erreur", "Le graphique nécessite au moins 2 colonnes numériques.")
            return

        x = numeric_cols[0]
        y = numeric_cols[1]

        plt.figure(figsize=(6,4))
        plt.plot(self.df[x], self.df[y])
        plt.title(f"Solution de l'équation différentielle : {y}(t)")
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid(True)
        plt.show()

    # ----------------------------
    # 4) Solveur d’équations différentielles (Runge-Kutta 4)
    # ----------------------------
    def solve_ode(self):
        # Exemple d’équation différentielle :
        # y' = -2y  avec solution y(t)=e^{-2t}
        def f(t, y):
            return -2 * y

        t0 = 0
        y0 = 1
        h = 0.1
        t_max = 5

        t_vals = [t0]
        y_vals = [y0]

        t = t0
        y = y0

        while t < t_max:
            k1 = f(t, y)
            k2 = f(t + h/2, y + h/2 * k1)
            k3 = f(t + h/2, y + h/2 * k2)
            k4 = f(t + h, y + h * k3)
            y = y + h * (k1 + 2*k2 + 2*k3 + k4) / 6
            t = t + h

            t_vals.append(t)
            y_vals.append(y)

        self.df = pd.DataFrame({"t": t_vals, "y(t)": y_vals})

        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, "Équation différentielle résolue avec RK4 : y' = -2y\n")
        self.text.insert(tk.END, str(self.df.head()))

    # ----------------------------
    # 5) Export JSON
    # ----------------------------
    def export_json(self):
        if self.df is None:
            messagebox.showwarning("Attention", "Importer un CSV ou résoudre une ODE.")
            return

        data_json = self.df.to_json(orient="records", indent=4)

        filepath = filedialog.asksaveasfilename(defaultextension=".json")
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(data_json)

            messagebox.showinfo("Succès", "Données exportées en JSON.")


if __name__ == "__main__":
    app = ResearchODEViewer()
    app.mainloop()

