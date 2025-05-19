import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
historial_datos = []

def Producto():
    Limpio()
    tk.Label(area_dinamica, text="Aquí va un mensaje de bienvenida", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Título", "Mensaje temporal")).pack()

def Introducir_datos():
    Limpio()
    tk.Label(area_dinamica, text="Aquí coloca un letrero o label que identifique al alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre del alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección A:").pack()
    opcion_elegida = tk.StringVar(value="mujer")
    tk.Radiobutton(area_dinamica, text="mujer", variable=opcion_elegida, value="mujer").pack()
    tk.Radiobutton(area_dinamica, text="hombre", variable=opcion_elegida, value="hombre").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["1", "2", "3", "4", "5", "6"])
    combo.pack()
    combo.current(0)

    def Guardar():
        nombre = campo_texto_uno.get()
        genero = opcion_elegida.get()
        lista = combo.get()
        historial_datos.append({
            "nombre": nombre,
            "genero": genero,
            "opcion": lista
        })

        messagebox.showinfo("Revisión", f"Texto: {nombre}\nSelección: {genero}\nLista: {lista}")

    tk.Button(area_dinamica, text="Botón 2", command=Guardar).pack(pady=10)

def Ver_historial():
    Limpio()
    tk.Label(area_dinamica, text="Historial de Datos", font=("Arial", 14)).pack(pady=10)

    if not historial_datos:
        tk.Label(area_dinamica, text="No hay datos registrados aún.").pack(pady=5)
        return

    for i, entrada in enumerate(historial_datos, start=1):
        texto = f"{i}. Nombre: {entrada['nombre']}, Género: {entrada['genero']}, Opción: {entrada['opcion']}"
        tk.Label(area_dinamica, text=texto, anchor="w", justify="left").pack(fill="x", padx=10, pady=2)

def Color_fondo():
    Limpio()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color(col)).pack(pady=2)

def Mejoras():
    Limpio()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

def Limpio():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para prácticas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

tk.Button(menu_lateral, text="Inicio", command=Producto, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Pantalla 2", command=Introducir_datos, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Pantalla 3", command=Color_fondo, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Pantalla 4", command=Mejoras, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ver Historial", command=Ver_historial, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

Producto()
ventana_principal.mainloop()

