from datetime import datetime
from rich.table import Table
from rich.console import Console


class Tarea:
    """
    Representa una tarea
    """

    def __init__(self, titulo: str, descripcion: str):
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.__completada: bool = False
        self.fecha_creacion = datetime.now()

    def marcar_compeltada(self) -> None:
        """
        cambia el estado de la tarea
        """
        self.__completada = True

    @property
    def estado(self) -> str:
        """
        Getter tematico para mostrar el estado de forma limpia
        """
        return "Completada" if self.__completada else "Pendiente"

    def __repr__(self):
        return (
            f"\n TITULO : {self.titulo}"
            f"\n DESCRIPCION : {self.descripcion}"
            f"\n ESTADO : {self.estado}"
            f"\n FECHA : {self.fecha_creacion}\n"
        )


class GestorDeTareas:
    """
    Clase gestora de una coleccion de tareas
    """

    def __init__(self):
        self.console = Console()
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)
        self.console.print(f"TAREA {tarea} AGREGADA")

    def mostrar_tablero(self):

        table = Table(title="Mi tablero de tareas")

        table.add_column("TITULO", style="cyan")
        table.add_column("DESCRIPCION", style="magenta")
        table.add_column("ESTADO", justify="center")
        table.add_column("Creada el", style="magenta")

        for tarea in self.tareas:
            table.add_row(
                tarea.titulo,
                tarea.descripcion,
                tarea.estado,
                str(tarea.fecha_creacion),
            )

        self.console.print(table)


def main():
    tarea_calculo = Tarea(titulo="Calculo", descripcion="Tarea1")

    mi_gestor = GestorDeTareas()

    mi_gestor.agregar_tarea(tarea_calculo)

    mi_gestor.mostrar_tablero()


if __name__ == "__main__":
    main()
