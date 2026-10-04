import csv
import os

archivo = "productos.csv"

# Guardar

def guardar_productos(lista, archivo):
    with open(archivo, mode='w', newline='') as f:
        campos = ["id", "nombre", "precio", "stock", "activo"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)

# Leer

def leer_productos(archivo):
    try:
        with open(archivo, mode='r') as f:
            reader = csv.DictReader(f)
            productos = list(reader)

            for p in productos:
                p["id"] = int(p["id"])
                p["precio"] = float(p["precio"])
                p["stock"] = int(p["stock"])
                p["activo"] = p["activo"].lower() == "true"

            return productos

    except FileNotFoundError:
        return []

productos = leer_productos(archivo)

class Producto:
    def __init__(self, id, nombre, precio, stock, activo):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.activo = activo

    def eliminar_producto(self, id):
        if self.id == id:
            self.activo = "inactivo"
            print("Se ha eliminado el producto")
        else:
            print("No existe el producto")
    
    def modificar_producto(self, id):
        if self.id == id:
            self.nombre = input("Ingrese el nuevo nombre: ")
            self.precio = int(input("Ingrese el nuevo precio: "))
            self.stock = int(input("Ingrese la nueva cantidad en stock: "))
        else:
            print("No existe el producto")

def agregar_producto(lista, archivo):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    activo = True
    nuevo = {
    "id": len(lista) + 1,
    "nombre": nombre,
    "precio": precio,
    "stock": stock,
    "activo": activo
    }
    productos.append(nuevo)
    print(f"Producto '{nombre}' agregado con éxito.")
    guardar_productos(lista, archivo)

while True:
    print("\n--- MENÚ DE PRODUCTOS ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Modificar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto(productos, archivo)
        os.system("cls" if os.name == "nt" else "clear")

    elif opcion == "2":
        os.system("cls" if os.name == "nt" else "clear")
        leer_productos(archivo)
        for producto in productos:
            print(producto)

    elif opcion == "3":
        modificar_producto()
        os.system("cls" if os.name == "nt" else "clear")


    elif opcion == "4":
        eliminar_producto()
        os.system("cls" if os.name == "nt" else "clear")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        os.system("cls" if os.name == "nt" else "clear")

leer_productos(archivo)