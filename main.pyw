import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image 
import sys
import subprocess
import sys
import os

class PantallaInicial:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HUNDIR LA FLOTA")
        self.root.geometry("800x800") 
        self.root.resizable(False, False)
    
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            IMG_PATH = os.path.join(BASE_DIR, ".", "img", "battleship.jpg")
            imagen = Image.open(IMG_PATH).resize((800, 800), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(imagen)
            self.bg_label = tk.Label(self.root, image=self.bg_img)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            # self.bg_color = "#0a1d37"  # ← color de fallback, úsalo en widgets
        except:
            print("Imagen no encontrada, fondo azul")
            self.root.configure(bg="#0a1d37")
            self.bg_color = "#0a1d37"
        
        self.crear_pantalla_inicial()
        self.root.mainloop()
        
    
    def crear_pantalla_inicial(self):
        titulo = tk.Label(self.root, 
                        text="HUNDIR LA FLOTA", 
                        font=("Arial", 20, "bold"),
                        fg="#ffd700",
                        bg="#0a1d37")
        titulo.place(relx=0.5, y=40, anchor="center")

        subtitulo = tk.Label(self.root,
                        text="¡La batalla naval épica!",
                        font=("Arial", 16),
                        fg="white",
                        bg="#0a1d37")
        subtitulo.place(relx=0.5, y=90, anchor="center")

        # Botones centrados con place
        btn_new_hard = tk.Button(self.root, text="Dificil",
                                font=("Arial", 12, "bold"), bg="#4d0447", fg="white",
                                width=10, height=2, relief="raised", bd=3,
                                command=self.iniciar_juego_manual_dificil)
        btn_new_hard.place(relx=0.5, y=180, anchor="center")

        btn_new_easy = tk.Button(self.root, text="Facil",
                                font=("Arial", 12, "bold"), bg="#c601b9", fg="white",
                                width=10, height=2, relief="raised", bd=3,
                                command=self.iniciar_juego_manual_facil)
        btn_new_easy.place(relx=0.5, y=280, anchor="center")

        btn_new_semi = tk.Button(self.root, text="Semi",
                                font=("Arial", 12, "bold"), bg="#3e0304", fg="white",
                                width=10, height=2, relief="raised", bd=3,
                                command=self.iniciar_juego_semi)
        btn_new_semi.place(relx=0.5, y=380, anchor="center")

        btn_new_full = tk.Button(self.root, text="Full",
                                font=("Arial", 12, "bold"), bg="#fa0808", fg="white",
                                width=10, height=2, relief="raised", bd=3,
                                command=self.iniciar_juego_auto)
        btn_new_full.place(relx=0.5, y=480, anchor="center")

        btn_info = tk.Button(self.root, text="INSTRUCCIONES",
                            font=("Arial", 6), bg="#4444ff", fg="white",
                            width=20, height=2, relief="raised", bd=3,
                            command=self.mostrar_instrucciones)
        btn_info.place(relx=0.5, y=580, anchor="center")

        btn_salir = tk.Button(self.root, text="SALIR",
                            font=("Arial", 10), bg="#666666", fg="white",
                            width=10, height=1, relief="raised", bd=3,
                            command=self.root.quit)
        btn_salir.place(relx=0.5, y=660, anchor="center")

        version = tk.Label(self.root,
                        text="v2.0 - Powered by Python & Tkinter",
                        font=("Arial", 10), fg="#888888", bg="#0a1d37")
        version.place(relx=0.5, y=760, anchor="center")

       
    def iniciar_juego_manual_dificil(self):
        messagebox.showinfo("¡Listo!", "¡Juego iniciado!\n")
        ruta_juego = os.path.join(os.path.dirname(__file__), "Battleship_Test_Manual_V3_Class_Hard.py")
        subprocess.Popen([sys.executable, ruta_juego]) 

    def iniciar_juego_manual_facil(self):
        messagebox.showinfo("¡Listo!", "¡Juego iniciado, pero que facil!\n")
        ruta_juego = os.path.join(os.path.dirname(__file__), "Battleship_Test_Manual_V2_Class.py")
        subprocess.Popen([sys.executable, ruta_juego]) 
    
    def iniciar_juego_semi(self):
        messagebox.showinfo("¡Listo!", "¡Semi relax!\n")
        ruta_juego = os.path.join(os.path.dirname(__file__), "Battleship_Test_Semi.py")
        subprocess.Popen([sys.executable, ruta_juego]) 
    
    def iniciar_juego_auto(self):
        messagebox.showinfo("¡Listo!", "¡Juego facil, automatico, solo contempla la batalla!\n")
        ruta_juego = os.path.join(os.path.dirname(__file__), "Battleship_Test.py")
        subprocess.Popen([sys.executable, ruta_juego]) 

   
    
    def mostrar_instrucciones(self):
        messagebox.showinfo("Instrucciones",
                           "1. Tienes 3 modos de juego\n"
                           "2. El modo AUTO juega maquina contra maquina, solo tienes que relajarte \n"
                           "3. El modo SEMI te permite jugar un poquito, sólo cuando tu maquina acierta un disparo\n\n"
                           "4. El modo MANUAL Facil te permite jugar cada turno \n"
                           "5. El modo MANUAL Dificil te permite jugar cada turno, pero la maquina juega con ventaja \n"
                           "6. En el modo manual, si aciertas, vuelves a disparar \n"
                           "7. Disfruta!"
                           
                           
                           )
    
    def run(self):
        self.root.mainloop()

# ¡Ejecutar!
if __name__ == "__main__":
    app = PantallaInicial()
    app.run()
