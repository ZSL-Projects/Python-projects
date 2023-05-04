import tkinter as tk

def srednia_arytmetyczna(lista_liczb):
    if len(lista_liczb) == 0:
        return 0
    suma = sum(lista_liczb)
    return suma / len(lista_liczb)

oceny = []

def dodaj_ocene():
    liczba = float(entry_liczba.get())
    waga = int(entry_waga.get())
    for i in range(waga):
        oceny.append(liczba)
    entry_liczba.delete(0, tk.END)
    entry_waga.delete(0, tk.END)

def oblicz_srednia():
    srednia = srednia_arytmetyczna(oceny)
    label_wynik.config(text="Srednia arytmetyczna z podanych liczb to: {:.2f}".format(srednia))

root = tk.Tk()
root.title("Kalkulator sredniej arytmetycznej")

label_liczba = tk.Label(root, text="Podaj liczbe:")
entry_liczba = tk.Entry(root)
label_waga = tk.Label(root, text="Podaj wage:")
entry_waga = tk.Entry(root)
button_dodaj = tk.Button(root, text="Dodaj ocene", command=dodaj_ocene)
button_oblicz = tk.Button(root, text="Oblicz srednia", command=oblicz_srednia)
label_wynik = tk.Label(root, text="")

label_liczba.grid(row=0, column=0, padx=5, pady=5)
entry_liczba.grid(row=0, column=1, padx=5, pady=5)
label_waga.grid(row=1, column=0, padx=5, pady=5)
entry_waga.grid(row=1, column=1, padx=5, pady=5)
button_dodaj.grid(row=2, column=0, padx=5, pady=5)
button_oblicz.grid(row=2, column=1, padx=5, pady=5)
label_wynik.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()