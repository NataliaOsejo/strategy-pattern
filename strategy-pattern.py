# Definimos la interfaz para el comportamiento de tipo de ataque
class TipoAtaque:
    def fly(self):
        pass

# Implementación del comportamiento de tipo de ataque para soldados
class AtaqueFuego(TipoAtaque):
    def atacar(self):
        print("¡Descarguen los fusiles! ¡Mantengan el fuego constante! \n -Tu especialidad son los disparos con fusiles, tu fuerte es el daño-")

# Implementación del comportamiento de tipo de ataque para arqueros
class DisparoPreciso(TipoAtaque):
    def atacar(self):
        print("¡Ajusten los arcos y suelten las flechas! ¡No dejen una sola flecha sin volar! \n -Tu especialidad es el manejo del arco y flecha, tu fuerte es la precisión-")

# Implementación del comportamiento de tipo de ataque para caballeros
class CargaHeroica(TipoAtaque):
    def atacar(self):
        print("¡Empuñen sus lanzas! ¡Que la punta de acero rompa las líneas enemigas! \n -Tu especialidad es el uso de lanzas, tu fuerte es la resistencia-")

# Definimos la interfaz para el comportamiento del movimiento especial
class MovimientoEspecial:
    def especial(self):
        pass

# Implementación del comportamiento del movimiento especial para soldados
class BombardeoAereo(MovimientoEspecial):
    def especial(self):
        print("¡Que el cielo tiemble con nuestra ira! \n -Has solicitado un bombardeo aéreo preciso sobre el objetivo enemigo. Las explosiones rugen como truenos, arrasando todo a su paso dejando un paisaje desolado.-")

# Implementación del comportamiento del movimiento especial para arqueros
class CamuflajeNatural(MovimientoEspecial):
    def especial(self):
        print("¡Sombras de la muerte, guíen mi mano! \n -Te has vuelto invisible para los enemigos. Desde las sombras, tus flechas vuelan con una precisión letal, sorprendiendo a tus adversarios y sembrando el pánico entre sus filas.-")

# Implementación del comportamiento del movimiento especial para caballeros
class MuroDeEscudos(MovimientoEspecial):
    def especial(self):
        print("¡Protejan a los nuestros, ningún enemigo pasará! \n -Tú y tus compañeros forman un impenetrable muro de escudos, protegiendo a los aliados de cualquier ataque. Como una fortaleza viviente, resisten el embate más feroz del enemigo, manteniendo la línea.-")

# Clase base para los militares. Cada militar tiene un tipo de ataque y un movimiento especial
class Militar:
    def __init__(self, tipo_ataque, movimiento_especial):
        self.tipo_ataque = tipo_ataque
        self.movimiento_especial = movimiento_especial

    def ataque(self):
        print("\nAtaque:")
        self.tipo_ataque.atacar()

    def movimiento(self):
        print("\nMovimiento especial:")
        self.movimiento_especial.especial()

    def frase(self): #Frase de inicio general para todos los militares
        print("¡Prepárate para la batalla y lucha con coraje por tu equipo! ¡Demuestra tu valentía y defiende a los tuyos hasta el final!")

# Clase concreta para un militar de tipo soldado
class Soldado(Militar):
    def __init__(self):
        super().__init__(AtaqueFuego(), BombardeoAereo())

# Clase concreta para un militar de tipo arquero
class Arquero(Militar):
    def __init__(self):
        super().__init__(DisparoPreciso(), CamuflajeNatural())

# Clase concreta para un militar de tipo caballero
class Caballero(Militar):
    def __init__(self):
        super().__init__(CargaHeroica(), MuroDeEscudos())

# existen 3 unidades militares: soldados, arqueros, caballeros
if __name__ == "__main__":
    soldado = Soldado()
    arquero = Arquero()
    caballero = Caballero()

    print("------------> Elegiste soldado:")
    soldado.frase()
    soldado.ataque()
    soldado.movimiento()

    print("\n------------> Elegiste arquero:")
    arquero.frase()
    arquero.ataque()
    arquero.movimiento()

    print("\n------------> Elegiste caballero:")
    caballero.frase()
    caballero.ataque()
    caballero.movimiento()

