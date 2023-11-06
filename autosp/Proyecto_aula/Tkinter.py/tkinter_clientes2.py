import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import tkinter.messagebox
import json
from tkinter import PhotoImage
 
def catalogo():

    catalogo_window = tk.Toplevel(root)
    catalogo_window.title("Catálogo")

   
    data_sorted = sorted(data, key=lambda x: x["Código"])

    table = ttk.Treeview(catalogo_window, columns=("Código", "Marca", "Modelo", "Precio (USD)", "Existencias"), show="headings")

    table.heading("Código", text="Código")
    table.heading("Marca", text="Marca")
    table.heading("Modelo", text="Modelo")
    table.heading("Precio (USD)", text="Precio (USD)")
    table.heading("Existencias", text="Existencias")

    for index, row in enumerate(data_sorted):
        table.insert("", index, values=(row["Código"], row["Marca"], row["Modelo"], row["Precio (USD)"], row["Existencias"]))

    table.pack()

def hacer_compra():
    
    codigo_auto = simpledialog.askstring("Hacer Compra", "Ingrese el código del auto que desea comprar:")

    if codigo_auto:
        auto_encontrado = None
        for auto in data:
            if auto["Código"] == codigo_auto:
                cantidad_comprar = simpledialog.askinteger("Hacer Compra", f"Ingrese la cantidad de unidades del auto {codigo_auto} que desea comprar:")

                if cantidad_comprar is not None and cantidad_comprar > 0:
                    total = auto["Precio (USD)"] * cantidad_comprar
                    confirmacion = simpledialog.askinteger("Hacer Compra", f"El total para el auto {codigo_auto} con {cantidad_comprar} unidad/es es: {total}\nPresione 1 para continuar con la compra o 2 para cancelar:")

                    if confirmacion == 1:
                        numero_registro = simpledialog.askstring("Hacer Compra", "Ingrese el número de registro:")
                        comprador = simpledialog.askstring("Hacer Compra", "Ingrese su nombre:")

                        if numero_registro and comprador:
                            compra = {
                                "Código auto": codigo_auto,
                                "Cantidad": cantidad_comprar,
                                "Total": total,
                                "Número de Registro": numero_registro,
                                "Comprador": comprador
                            }

                            compras_data.append(compra)
                            auto["Existencias"] -= cantidad_comprar
                            tk.messagebox.showinfo("Éxito", "La compra ha sido registrada exitosamente.")
                        else:
                            tk.messagebox.showerror("Error", "Por favor, complete el número de registro y su nombre.")
                    else:
                        tk.messagebox.showinfo("Cancelado", "La compra ha sido cancelada.")
                else:
                    tk.messagebox.showerror("Error", "La cantidad de unidades debe ser mayor que cero.")
                auto_encontrado = auto
                break

        if not auto_encontrado:
            tk.messagebox.showerror("Error", "El auto no se encontró en el catálogo.")

def busqueda_auto():
    
    codigo_busqueda = simpledialog.askstring("Búsqueda Auto", "Ingrese el código del auto que desea buscar:")

    if codigo_busqueda:
        auto_encontrado = None
        for auto in data:
            if auto["Código"] == codigo_busqueda:
                resultado = f"{auto['Código']} {auto['Marca']} {auto['Modelo']} {auto['Precio (USD)']} {auto['Existencias']}"
                tk.messagebox.showinfo("Resultado de Búsqueda", resultado)
                auto_encontrado = auto
                break

        if not auto_encontrado:
            tk.messagebox.showerror("Error", "El auto no se encontró en el catálogo.")

def registrarse():
    
    nombre = simpledialog.askstring("Registrarse", "Ingrese su nombre:")
    direccion = simpledialog.askstring("Registrarse", "Ingrese su dirección:")
    telefono = simpledialog.askstring("Registrarse", "Ingrese su teléfono:")

    if nombre and direccion and telefono:
        registro = {
            "Nombre": nombre,
            "Dirección": direccion,
            "Teléfono": telefono
        }

        registro_data.append(registro)
        tk.messagebox.showinfo("Éxito", "Usted se ha registrado exitosamente.")
    else:
        tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")

def guardar_informacion():

    informacion = {
        "Compras": compras_data,
        "Registro": registro_data
    }

    with open("informacion.json", "w") as file:
        json.dump(informacion, file)

def salir():
  
    root.quit()

root = tk.Tk()
root.title("Sistema de Compras")


menu = tk.Menu(root)
root.config(menu=menu)

menu_catalogo = tk.Menu(menu)
menu.add_cascade(label="Catálogo", menu=menu_catalogo)
menu_catalogo.add_command(label="Mostrar Catálogo", command=catalogo)

menu_compra = tk.Menu(menu)
menu.add_cascade(label="Hacer Compra", menu=menu_compra)
menu_compra.add_command(label="Realizar Compra", command=hacer_compra)

menu_busqueda_auto = tk.Menu(menu)
menu.add_cascade(label="Búsqueda de Auto", menu=menu_busqueda_auto)
menu_busqueda_auto.add_command(label="Buscar Auto", command=busqueda_auto)

menu_registrarse = tk.Menu(menu)
menu.add_cascade(label="Registrarse", menu=menu_registrarse)
menu_registrarse.add_command(label="Registrar", command=registrarse)

menu.add_command(label="Guardar Información", command=guardar_informacion)

menu.add_command(label="Salir", command=salir)


root.configure(bg="gray")
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)
titulo_label = tk.Label(main_frame, text="MASSI" "\n""\n", font=("Garamond", 70), foreground="red")
titulo_label.grid(row=0, column=0, columnspan=2, pady=(root.winfo_screenheight() // 2 - titulo_label.winfo_reqheight() // 2), padx=(root.winfo_screenwidth() // 2 - titulo_label.winfo_reqwidth() // 2))
titulo_label2 = tk.Label(main_frame, text= "\n" "Compra y Venta de Autos", font=("Garamond", 32), foreground="black")
titulo_label2.grid(row=0, column=0, columnspan=2, pady=10)

imagen = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro3.gif")
nuevo_ancho = 298
nuevo_alto = 140
imagen = imagen.subsample(int(imagen.width() / nuevo_ancho), int(imagen.height() / nuevo_alto))

etiqueta_imagen = tk.Label(root, image=imagen)
etiqueta_imagen.place(x=0, y=0)

imagen2 = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro3.gif")
nuevo_ancho = 298
nuevo_alto = 140
imagen2 = imagen2.subsample(imagen2.width() // nuevo_ancho, imagen2.height() // nuevo_alto)
etiqueta_imagen2 = tk.Label(root, image=imagen2)
etiqueta_imagen2.place(x=imagen.width(), y=0)
root.geometry(f"{imagen.width() + imagen2.width()}x{max(imagen.height(), imagen2.height())}")

imagen3 = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro3.gif")
imagen3 = imagen3.subsample(imagen3.width() // nuevo_ancho, imagen3.height() // nuevo_alto)

etiqueta_imagen3 = tk.Label(root, image=imagen3)
etiqueta_imagen3.place(x=imagen.width() + imagen2.width(), y=0)

ancho_total = imagen.width() + imagen2.width() + imagen3.width()
alto_maximo = max(imagen.height(), imagen2.height(), imagen3.height())
root.geometry(f"{ancho_total}x{alto_maximo}")


compras_data = []
registro_data = []

data = [
    {"Código": "001", "Marca": "Mazda", "Modelo": "Mazda 3", "Precio (USD)": 83486.3, "Existencias": 8},
    {"Código": "002", "Marca": "MiniCooper", "Modelo": "ClubMan", "Precio (USD)": 31929.77, "Existencias": 14},
    {"Código": "003", "Marca": "Mercedes Benz", "Modelo": "HatchBack", "Precio (USD)": 47537.4, "Existencias": 30},
    {"Código": "004", "Marca": "Porsche", "Modelo": "Cayenne", "Precio (USD)": 256900, "Existencias": 27},
    {"Código": "005", "Marca": "BMW", "Modelo": "i4", "Precio (USD)": 95990.26, "Existencias": 0},
    {"Código": "006", "Marca": "Lamborghini", "Modelo": "Urus", "Precio (USD)": 650000, "Existencias": 10},
    {"Código": "007", "Marca": "Tesla", "Modelo": "Model Y", "Precio (USD)": 64970, "Existencias": 21}
]

root.mainloop()
