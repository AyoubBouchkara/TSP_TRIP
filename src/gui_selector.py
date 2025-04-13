import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from config import VILLES
from map_generator import generate_map_with_selected_villes

def run_gui():
    # Creation de la window principale
    root = tk.Tk()
    root.title("Sélection des villes à visiter")

    tk.Label(root, text="Sélectionnez les villes à visiter :").pack()

    # Liste des noms des villes afficher dans le dropDown
    ville_names = [ville['name'] for ville in VILLES]

    # Liste dropDown
    listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=15)
    for name in ville_names:
        listbox.insert(tk.END, name)
    listbox.pack(padx=10, pady=10)

    # Fonction pour valider la selection des villes
    def valider_selection():
        selected_indices = listbox.curselection()
        if len(selected_indices) < 2:
            messagebox.showwarning("Attention", "Sélectionnez au moins deux villes.")
            return

        selected_villes = [VILLES[i] for i in selected_indices]
        generate_map_with_selected_villes(selected_villes)
        messagebox.showinfo("Succès", "Carte générée avec succès !")

    # Bouton pour valider la selection
    bouton = tk.Button(root, text="Valider", command=valider_selection)
    bouton.pack(pady=10)

    # Lancer une interface graphique
    root.mainloop()

if __name__ == "__main__":
    run_gui()
