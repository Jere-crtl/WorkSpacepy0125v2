class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()
    
    def asignar_horario(self,hora):
        if hora in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {hora}")
            return False
        self.horarios.add(hora)
        return True

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None 
        self.horarios = set()
        self.conductor = None
    
    def asignar_ruta(self, ruta):
        self.ruta = ruta
    
    def registrar_horario(self, hora):
        self.horarios.add(hora)
    
    def asignar_conductor(self, conductor):
        for hora in self.horarios:
            if hora in conductor.horarios:
                print(f"No se puede asignar el conductor {conductor.nombre} al bus {self.id_bus} en el horario {hora}, ya esta ocupado. ")
                return False
        self.conductor = conductor 
        for hora in self.horarios:
            conductor.asignar_horario(hora)
        return True

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self, id_bus):
        self.buses.append(Bus(id_bus))
    
    def agregar_conductor(self, nombre):
        self.conductores.append(Conductor(nombre))
    
    def buscar_bus(self, id_bus):
        return next((bus for bus in self.buses if bus.id_bus == id_bus), None)
    
    def buscar_conductor(self, nombre):
        return next((c for c in self.conductores if c.nombre == nombre), None)
    
    def menu(self):
        while True:
            print("1. Agregar Bus")
            print("2. Agregar Ruta a Bus")
            print("3. Registrar Horario a Bus")
            print("4. Agregar Conductor")
            print("5. Agregar Horario a Conductor")
            print("6. Asignar Bus a Conductor")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_bus = input("Ingrese ID del bus: ")
                self.agregar_bus(id_bus)
                print("Bus agregado correctamente")
            elif opcion == "2":
                id_bus =input("Ingrese ID del Bus: ")
                bus = self.buscar_bus(id_bus)
                if bus:
                    ruta = input("Ingrese la ruta del Bus: ")
                    bus.asignar_ruta(ruta)
                    print("Ruta asignada correctamente.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "3":
                id_bus = input("Ingrese ID del Bus: ")
                bus = self.buscar_bus(id_bus)
                if bus:
                    hora = input("Ingrese horario (HH:MM): ")
                    bus.registrar_horario(hora)
                    print("Horario registrado correctamente.")
                else:
                    print("Bus no econtrado.")
            elif opcion == "4":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
                print("Conductor agregado correctamente.")
            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = self.buscar_conductor(nombre)
                self.agregar_conductor(nombre)
                if conductor:
                    hora = input("Ingrese horario (HH:MM): ")
                    if conductor.asignar_horario(hora):
                        print("Horario asignado correctamente.")
                else:
                    print("conductor no encontrado")
            elif opcion == "6":
                id_bus = input("Ingrese ID del bus: ")
                nombre = input("Ingrese nombre del conductor:")
                bus = self.buscar_bus(id_bus)
                conductor = self.buscar_conductor(nombre)
                if bus and conductor:
                    if bus.asignar_conductor(conductor):
                        print("Conductor asignado correctamente.")
                else:
                    print("Bus o conductor no encontrado.")
            elif opcion == "7":
                print("Saliendo del sistema")
                break
            else:
                print("Invalido")

if __name__ == "__main__":
    admin = Admin()
    admin.menu()
    