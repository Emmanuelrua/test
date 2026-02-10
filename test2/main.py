from dataclasses import dataclass
from abc import ABC, abstractmethod

import pandas as pd
from rich.table import Table
from rich.console import Console



@dataclass
class Producto(ABC):
    nombre: str
    precio: float

    @abstractmethod
    def precio_final(self) -> float:
        pass


class ProductoNormal(Producto):

    def precio_final(self) -> float:
        return self.precio



@dataclass
class ProductoDescuento(Producto):
    descuento: float   

    def precio_final(self) -> float:
        return self.precio * (1 - self.descuento / 100)



def total_factura(productos: list[Producto]) -> float:
    total = 0

    for p in productos:
        total += p.precio_final()

    return total



def mostrar_tabla_rich(productos: list[Producto]) -> None:

    console = Console()

    table = Table(title="Factura")

    table.add_column("Producto")
    table.add_column("Precio base", justify="right")
    table.add_column("Precio final", justify="right")
    table.add_column("Tipo")

    for p in productos:

        tipo = p.__class__.__name__

        table.add_row(
            p.nombre,
            f"{p.precio:.2f}",
            f"{p.precio_final():.2f}",
            tipo
        )

    console.print(table)
    console.print(f"[bold]Total:[/bold] {total_factura(productos):.2f}")



def crear_dataframe(productos: list[Producto]) -> pd.DataFrame:

    filas = []

    for p in productos:

        filas.append({
            "nombre": p.nombre,
            "precio_base": p.precio,
            "precio_final": p.precio_final(),
            "tipo": p.__class__.__name__
        })

    df = pd.DataFrame(filas)

    return df


def main():

    p1 = ProductoNormal("Cuaderno", 5000)
    p2 = ProductoDescuento("Lapicero", 2000, 10)
    p3 = ProductoDescuento("Borrador", 1000, 50)

    productos = [p1, p2, p3]

    for p in productos:
        print(p.nombre, p.precio_final())

    print("Total:", total_factura(productos))

    
    mostrar_tabla_rich(productos)

   
    df = crear_dataframe(productos)

    print("\nDataFrame (pandas):")
    print(df)

    print("\nTotal desde pandas:")
    print(df["precio_final"].sum())


if __name__ == "__main__":
    main()
