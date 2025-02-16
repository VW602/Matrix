# Importar la librería Pygame
import pygame
# Importar la librería Random para generar valores aleatorios
import random

# Inicializar Pygame
pygame.init()

# Establecer el tamaño de la pantalla
screen_width = 800
screen_height = 600
# Creamos la ventana
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir los caracteres que caerán
# Creamos una lista con los caracteres que van a caer
characters = ["0", "1"]

# Definir los colores
# Creamos dos variables para almacenar los colores a utilizar
black = (0, 0, 0)
green = (0, 255, 0)

# Clase para representar cada carácter que cae
class Character:
    def __init__(self, x, y):
        # Posición en el eje X y Y donde aparecerá el carácter
        self.x = x
        self.y = y
        # Velocidad a la que cae el carácter, se genera de manera aleatoria
        self.speed = random.randint(0, 5)
        # Carácter que se mostrará en la pantalla, se selecciona de manera aleatoria
        self.char = random.choice(characters)
        # Color que tendrá el carácter en la pantalla
        self.color = green

    # Función que actualiza la posición del carácter
    def update(self):
        self.y += self.speed

    # Función que dibuja el carácter en la pantalla
    def draw(self, screen):
        font = pygame.font.Font(None, 20)
        text = font.render(self.char, True, self.color)
        screen.blit(text, (self.x, self.y))

# Lista para mantener un registro de todos los caracteres que caen
# Creamos una lista vacía donde vamos a almacenar los objetos de la clase Character
characters_list = []

# Bucle principal del programa
# Creamos una variable booleana que se utiliza para salir del bucle principal y cerrar el programa
running = True
while running:
    # Eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Añadir un nuevo carácter a la lista de caracteres cada 10 fotogramas
    # Si la lista de caracteres es menor a 100, se crea un nuevo objeto Character y se añade a la lista
    if len(characters_list) < 100:
        character = Character(random.randint(0, screen_width), 0)
        characters_list.append(character)

    # Actualizar y dibujar cada carácter en la lista
    # Limpiamos la pantalla para que los caracteres caigan uno encima del otro
    screen.fill(black)
    # Para cada objeto Character en la lista, se actualiza su posición y se dibuja en la pantalla
    for character in characters_list:
        character.update()
        character.draw(screen)

    # Eliminar los caracteres que ya están fuera de la pantalla
    # Creamos una nueva lista que contiene solamente los objetos Character que aún no han salido de la pantalla
    characters_list = [character for character in characters_list if character.y < screen_height]

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()