import tkinter as tk
from tkinter import messagebox
import time
import threading
from PIL import Image, ImageTk
import requests
from io import BytesIO

class FlowerAnimation:
    def __init__(self, master):
        self.master = master
        master.title("Flor Animada")
        master.geometry("300x400")

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.message = tk.Label(master, text="¡Algo para tí!", font=("Arial", 14, 'bold'))
        self.message.pack(pady=5)

        self.start_button = tk.Button(master, text="Si me quieres dale click :o", command=self.start_animation)
        self.start_button.pack(pady=5)

        self.show_message_button = tk.Button(master, text="Algo más :3", command=self.show_message)
        self.show_message_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Salir", command=master.quit)
        self.quit_button.pack(pady=5)

        self.is_animating = False

        # Cargar la imagen del girasol
        self.load_sunflower_image()

    def load_sunflower_image(self):
        url = "https://img.icons8.com/dusk/64/sunflower.png"  # URL de la imagen del girasol
        response = requests.get(url)
        image_data = Image.open(BytesIO(response.content))
        self.sunflower_image = ImageTk.PhotoImage(image_data)

    def draw_flower(self, position):
        self.canvas.delete("all")
        self.canvas.create_image(position, 100, image=self.sunflower_image, anchor=tk.CENTER)

    def animate_flower(self):
        position = 150  # Posición inicial
        direction = 5   # Dirección de movimiento
        while self.is_animating:
            self.draw_flower(position)
            position += direction

            # Cambiar dirección si llega al borde
            if position > 300 or position < 0:
                direction = -direction
            
            time.sleep(0.1)

    def start_animation(self):
        if not self.is_animating:
            self.is_animating = True
            threading.Thread(target=self.animate_flower, daemon=True).start()
            self.start_button.config(text="Detener animación")
        else:
            self.is_animating = False
            self.start_button.config(text="Ver animación")

    def show_message(self):
        # Crear una nueva ventana para el mensaje
        message_window = tk.Toplevel(self.master)
        message_window.title("Mensaje")

        # Mensaje en la primera línea
        message_label = tk.Label(message_window, text="¡Te quiero ❤︎🌻!", font=("Arial", 12))
        message_label.pack(pady=5)

        # Mensaje en la segunda línea en negrita
        bold_message = tk.Label(message_window, text="-para ti", font=("Arial", 12, 'bold'))
        bold_message.pack(pady=5)

        # Botón para cerrar la ventana
        close_button = tk.Button(message_window, text="Cerrar", command=message_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlowerAnimation(root)
    root.mainloop()

# Instrucciones para crear el ejecutable:
# 1. Instala PyInstaller: pip install pyinstaller
# 2. Ejecuta: pyinstaller --onefile --windowed flor_animada.py
# El ejecutable se creará en la carpeta 'dist'.
