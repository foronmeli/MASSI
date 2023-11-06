
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import tkinter.messagebox
import json


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

def crear_auto():
    
    codigo = simpledialog.askstring("Crear Auto", "Ingrese el código del auto:")
    modelo = simpledialog.askstring("Crear Auto", "Ingrese el modelo del auto:")
    marca = simpledialog.askstring("Crear Auto", "Ingrese la marca del auto:")
    precio = simpledialog.askfloat("Crear Auto", "Ingrese el precio del auto:")
    existencias = simpledialog.askinteger("Crear Auto", "Ingrese las existencias del auto:")

    if codigo and modelo and marca and precio and existencias is not None:
        nuevo_auto = {
            "Código": codigo,
            "Marca": marca,
            "Modelo": modelo,
            "Precio (USD)": precio,
            "Existencias": existencias
        }
        data.append(nuevo_auto)
        tk.messagebox.showinfo("Éxito", "El auto ha sido creado exitosamente.")
    else:
        tk.messagebox.showerror("Error", "Todos los campos deben estar completos.")

def modificar_auto():
    
    codigo_modificar = simpledialog.askstring("Modificar Auto", "Ingrese el código del auto que desea modificar:")

    auto_modificado = None
    for auto in data:
        if auto["Código"] == codigo_modificar:
            nueva_marca = simpledialog.askstring("Modificar Auto", "Ingrese la nueva marca:")
            nuevo_modelo = simpledialog.askstring("Modificar Auto", "Ingrese el nuevo modelo:")
            nuevo_precio = simpledialog.askfloat("Modificar Auto", "Ingrese el nuevo precio:")
            nuevas_existencias = simpledialog.askinteger("Modificar Auto", "Ingrese las nuevas existencias:")

            if nueva_marca and nuevo_modelo and nuevo_precio and nuevas_existencias is not None:
                auto["Marca"] = nueva_marca
                auto["Modelo"] = nuevo_modelo
                auto["Precio (USD)"] = nuevo_precio
                auto["Existencias"] = nuevas_existencias
                auto_modificado = auto
                break
            else:
                tk.messagebox.showerror("Error", "Todos los campos deben estar completos.")

    if auto_modificado:
        tk.messagebox.showinfo("Éxito", "El auto ha sido modificadado exitosamente.")
    else:
        tk.messagebox.showerror("Error", "El código del auto no se encontró en el catálogo.")

def informacion_ventas():
    info_ventas_window = tk.Toplevel(root)
    info_ventas_window.title("Información Ventas")

   
    table = ttk.Treeview(info_ventas_window, columns=("Cliente", "Código auto", "Fecha"), show="headings")

    table.heading("Cliente", text="Cliente")
    table.heading("Código auto", text="Código auto")
    table.heading("Fecha", text="Fecha")

    for index, row in enumerate(ventas_data):
        table.insert("", index, values=(row["Cliente"], row["Código auto"], row["Fecha"]))

    table.pack()

def modificar_venta():
    
    registro_modificar = simpledialog.askinteger("Modificar Venta", "Ingrese el registro de la venta que desea modificar:")
    
    if registro_modificar is not None and registro_modificar > 0 and registro_modificar <= len(ventas_data):
        nuevo_nombre = simpledialog.askstring("Modificar Venta", "Ingrese el nuevo nombre:")
        nuevo_codigo_auto = simpledialog.askstring("Modificar Venta", "Ingrese el nuevo código del auto:")
        nueva_fecha = simpledialog.askstring("Modificar Venta", "Ingrese la nueva fecha de venta (DD-MM-YY HH:mm):")

        if nuevo_nombre and nuevo_codigo_auto and nueva_fecha:
            venta_modificada = ventas_data[registro_modificar - 1]
            venta_modificada["Cliente"] = nuevo_nombre
            venta_modificada["Código auto"] = nuevo_codigo_auto
            venta_modificada["Fecha"] = nueva_fecha

            tk.messagebox.showinfo("Éxito", "La venta ha sido modificada exitosamente.")
        else:
            tk.messagebox.showerror("Error", "Todos los campos deben estar completos.")
    else:
        tk.messagebox.showerror("Error", "El número de registro ingresado no es válido.")

def informacion_clientes():
    info_clientes_window = tk.Toplevel(root)
    info_clientes_window.title("Información Clientes")

    
    info_clientes_table = ttk.Treeview(info_clientes_window, columns=("Nombre", "Dirección", "Teléfono"), show="headings")

    info_clientes_table.heading("Nombre", text="Nombres")
    info_clientes_table.heading("Dirección", text="Direcciones")
    info_clientes_table.heading("Teléfono", text="Teléfonos")

    for index, row in enumerate(clientes_data):
        info_clientes_table.insert("", index, values=(row["Nombre"], row["Dirección"], row["Teléfono"]))

    info_clientes_table.pack()

def modificar_cliente():
   
    cliente_modificar = simpledialog.askstring("Modificar Cliente", "Ingrese el nombre del cliente que desea modificar:")
    
    if cliente_modificar:
        cliente_encontrado = None
        for cliente in clientes_data:
            if cliente["Nombre"] == cliente_modificar:
                nuevo_nombre = simpledialog.askstring("Modificar Cliente", "Ingrese el nuevo nombre:")
                nueva_direccion = simpledialog.askstring("Modificar Cliente", "Ingrese la nueva dirección:")
                nuevo_telefono = simpledialog.askstring("Modificar Cliente", "Ingrese el nuevo teléfono:")

                if nuevo_nombre and nueva_direccion and nuevo_telefono:
                    cliente["Nombre"] = nuevo_nombre
                    cliente["Dirección"] = nueva_direccion
                    cliente["Teléfono"] = nuevo_telefono
                    cliente_encontrado = cliente
                    break
                else:
                    tk.messagebox.showerror("Error", "Todos los campos deben estar completos.")
        
        if cliente_encontrado:
            tk.messagebox.showinfo("Éxito", "La información del cliente ha sido modificada exitosamente.")
        else:
            tk.messagebox.showerror("Error", "El cliente no se encontró en la lista.")
    else:
        tk.messagebox.showerror("Error", "Por favor, ingrese un nombre de cliente válido.")

def guardar_catalogo():
    
    informacion = {
        "catálogo": data,
        "ventas": ventas_data,
        "clientes": clientes_data
    }

    with open("informacion.json", "w") as archivo:
        json.dump(informacion, archivo)

    tk.messagebox.showinfo("Éxito", "La información ha sido guardada exitosamente en 'informacion.json'.")

def salir():
    
    root.destroy()

root = tk.Tk()
root.title("MASSI")

menu = tk.Menu(root)
root.config(menu=menu)

menu_catalogo = tk.Menu(menu)
menu.add_cascade(label="Catálogo", menu=menu_catalogo)
menu_catalogo.add_command(label="Mostrar Catálogo", command=catalogo)

menu.add_command(label="Crear auto", command=crear_auto)
menu.add_command(label="Modificar auto", command=modificar_auto)

menu_ventas = tk.Menu(menu)
menu.add_cascade(label="Informacion ventas", menu=menu_ventas)
menu_ventas.add_command(label="Mostrar información ventas", command=informacion_ventas)
menu_ventas.add_command(label="Modificar venta", command=modificar_venta)

menu_clientes = tk.Menu(menu)
menu.add_cascade(label="Informacion clientes", menu=menu_clientes)
menu_clientes.add_command(label="Mostrar información clientes", command=informacion_clientes)
menu_clientes.add_command(label="Modificar cliente", command=modificar_cliente)

menu.add_command(label="Guardar catálogo", command=guardar_catalogo)
menu.add_command(label="Salir", command=salir)


root.configure(bg="gray")
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, padx=10, pady=10)
titulo_label = tk.Label(main_frame, text="MASSI" "\n""\n", font=("Garamond", 70), foreground="red")
titulo_label.grid(row=0, column=0, columnspan=2, pady=(root.winfo_screenheight() // 2 - titulo_label.winfo_reqheight() // 2), padx=(root.winfo_screenwidth() // 2 - titulo_label.winfo_reqwidth() // 2))
titulo_label2 = tk.Label(main_frame, text= "\n" "Compra y Venta de Autos", font=("Garamond", 32), foreground="black")
titulo_label2.grid(row=0, column=0, columnspan=2, pady=10)

imagen = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro1.gif")
nuevo_ancho = 298
nuevo_alto = 140
imagen = imagen.subsample(int(imagen.width() / nuevo_ancho), int(imagen.height() / nuevo_alto))

etiqueta_imagen = tk.Label(root, image=imagen)
etiqueta_imagen.place(x=0, y=0)

imagen2 = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro1.gif")
nuevo_ancho = 298
nuevo_alto = 140
imagen2 = imagen2.subsample(imagen2.width() // nuevo_ancho, imagen2.height() // nuevo_alto)
etiqueta_imagen2 = tk.Label(root, image=imagen2)
etiqueta_imagen2.place(x=imagen.width(), y=0)
root.geometry(f"{imagen.width() + imagen2.width()}x{max(imagen.height(), imagen2.height())}")

imagen3 = tk.PhotoImage(file="C:/Users/Cristina/Desktop/autosp/Proyecto_aula/Tkinter.py/imagenes/carro1.gif")
imagen3 = imagen3.subsample(imagen3.width() // nuevo_ancho, imagen3.height() // nuevo_alto)

etiqueta_imagen3 = tk.Label(root, image=imagen3)
etiqueta_imagen3.place(x=imagen.width() + imagen2.width(), y=0)

ancho_total = imagen.width() + imagen2.width() + imagen3.width()
alto_maximo = max(imagen.height(), imagen2.height(), imagen3.height())
root.geometry(f"{ancho_total}x{alto_maximo}")


data = [
    {"Código": "001", "Marca": "Mazda", "Modelo": "Mazda 3", "Precio (USD)": 83486.3, "Existencias": 8},
    {"Código": "002", "Marca": "MiniCooper", "Modelo": "ClubMan", "Precio (USD)": 31929.77, "Existencias": 14},
    {"Código": "003", "Marca": "Mercedes Benz", "Modelo": "HatchBack", "Precio (USD)": 47537.4, "Existencias": 30},
    {"Código": "004", "Marca": "Porsche", "Modelo": "Cayenne", "Precio (USD)": 256900, "Existencias": 27},
    {"Código": "005", "Marca": "BMW", "Modelo": "i4", "Precio (USD)": 95990.26, "Existencias": 0},
    {"Código": "006", "Marca": "Lamborghini", "Modelo": "Urus", "Precio (USD)": 650000, "Existencias": 10},
    {"Código": "007", "Marca": "Tesla", "Modelo": "Model Y", "Precio (USD)": 64970, "Existencias": 21}
]

ventas_data = [
    {"Cliente": "Sofia", "Código auto": "002", "Fecha": "12-03-06"},
    {"Cliente": "Santiago", "Código auto": "007", "Fecha": "22-12-10"},
    {"Cliente": "Stiven", "Código auto": "001", "Fecha": "14-07-11"},
    {"Cliente": "Michell", "Código auto": "002", "Fecha": "30-09-21"},
    {"Cliente": "Ana", "Código auto": "003", "Fecha": "03-03-23"}
]

clientes_data = [
    {"Nombre": "Sofia", "Dirección": "Cl 10 # 10B", "Teléfono": "3117953412"},
    {"Nombre": "Santiago", "Dirección": "Cr 5 #2A", "Teléfono": "310271231"},
    {"Nombre": "Stiven", "Dirección": "Cr 10 # 10-30", "Teléfono": "3183204577"},
    {"Nombre": "Michell", "Dirección": "Cl 14 # 2-345", "Teléfono": "3142702298"},
    {"Nombre": "Ana", "Dirección": "Cl 20 # 10B-7", "Teléfono": "3117659860"}
]

root.mainloop()
