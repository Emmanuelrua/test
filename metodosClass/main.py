class Pizza:
    def __init__(self,ingredientes : list):
        self.ingredientes : list = ingredientes
    
    @classmethod
    def crear_hawaiana(cls) -> 'Pizza':
        return cls(["Queso","Piña","Jamon"])
    
    def __repr__(self):
        return f"PIZZA\n {self.ingredientes}"
        



def main():
    pizza1=Pizza(["chicharron","queso","peperoni"])
    pizza_hawaiana= Pizza.crear_hawaiana()

    print(pizza1)
    print(pizza_hawaiana)

    print("Hello from metodosclass!")


if __name__ == "__main__":
    main()
