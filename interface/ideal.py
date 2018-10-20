import tkinter as tk
from tkinter import ttk


class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fisica")
        self.window.minsize(800, 600)
        self.window.maxsize(1280, 960)
        self.deslizador_posicion = ttk.Entry()

        self.pestañas = ttk.Notebook(self.window)
        self.tab_ideal = tk.Frame(self.pestañas)
        self.opciones = ttk.Frame(self.tab_ideal)

        # Inicializar los botones de la interfaz
        self.boton_velocidad = ttk.Button(self.opciones, text="Velocidad", width=10)

        self.create_widgets()

    def create_widgets(self):

        self.pestañas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, ipadx=10, ipady=10)

        tab_balistica = tk.Frame(self.pestañas)
        tab_seguridad = tk.Frame(self.pestañas)

        self.pestañas.add(self.tab_ideal, text="Movimiento Ideal", compound=tk.TOP)
        self.pestañas.add(tab_balistica, text="Movimiento Balistico", compound=tk.TOP)
        self.pestañas.add(tab_seguridad, text="Parabola Seguridad", compound=tk.TOP)

        # tutorial = ttk.LabelFrame(self.window, text="Instrucciones")
        # tutorial.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=10, pady=10)

        self.opciones.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False, padx=5, pady=5)

        self.boton_velocidad.pack(side=tk.TOP, padx=10, pady=10)

        graphics = ttk.LabelFrame(self.tab_ideal, text="Gráfica")
        graphics.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        separador = ttk.Separator(self.tab_ideal, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        variables = ttk.LabelFrame(self.tab_ideal, text="Controles")
        variables.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # Contenedores de los controles
        posicion = ttk.Frame(variables)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        angulo = ttk.Frame(variables)
        angulo.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        aceleracion = ttk.Frame(variables)
        aceleracion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)

        # Añadir elementos de entrada de texto
        self.deslizador_posicion = ttk.Entry(posicion, width=15, justify=tk.CENTER)
        self.deslizador_posicion.pack(side=tk.TOP)
        self.deslizador_posicion.insert(tk.END, "Posición inicial")
        var_x = ttk.Scale(posicion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        var_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_x.set(50)
        var_x.bind("<B1-Motion>", self.update_position_value)
        var_x.bind("<ButtonRelease-1>", self.update_position_value)

        angulo_entry = ttk.Entry(angulo, width=15, justify=tk.CENTER)
        angulo_entry.pack(side=tk.TOP)
        angulo_entry.insert(tk.END, "Angulo")
        var_y = ttk.Scale(angulo, from_=0, to=360, orient=tk.HORIZONTAL, length=100)
        var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_y.set(180)
        # var_y.bind("<B1-Motion>", update_angle_value)
        # var_y.bind("<ButtonRelease-1>", update_angle_value)

        aceleracion_entry = ttk.Entry(aceleracion, width=15, justify=tk.CENTER)
        aceleracion_entry.pack(side=tk.TOP)
        aceleracion_entry.insert(tk.END, "Aceleración")
        var_y = ttk.Scale(aceleracion, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        var_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)
        var_y.set(50)
        # var_y.bind("<B1-Motion>", update_acceleration_value)
        # var_y.bind("<ButtonRelease-1>", update_acceleration_value)

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_position_value(self):
        self.deslizador_posicion.insert(tk.END, self.deslizador_posicion.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_angle_value(self):
        self.deslizador_posicion.insert(tk.END, self.deslizador_posicion.get())

    # Todo declarar todos los elementos de la interfaz dentro del __init__
    def update_acceleration_value(self):
        self.deslizador_posicion.insert(tk.END, self.deslizador_posicion.get())
