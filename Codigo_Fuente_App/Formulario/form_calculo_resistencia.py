from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from config import COLOR_CUERPO_PRINCIPAL

from Logica.ohm_color import (
    get_value as get_value_resistance,
    get_range_tolerance,
    get_tolerance,
)

class FormularioCalculoResistencia:
    color_map = {
        "Negro": "black",
        "Marron": "brown",
        "Rojo": "red",
        "Naranja": "orange",
        "Amarillo": "yellow",
        "Verde": "green",
        "Azul": "blue",
        "Violeta": "violet",
        "Gris": "gray",
        "Blanco": "white",
        "Oro": "gold",
        "Plata": "silver"
    }

    colors_band1 = (
        "Negro",
        "Marron",
        "Rojo",
        "Naranja",
        "Amarillo",
        "Verde",
        "Azul",
        "Violeta",
        "Gris",
        "Blanco",
    )

    colors_band2 = (
        "Negro",
        "Marron",
        "Rojo",
        "Naranja",
        "Amarillo",
        "Verde",
        "Azul",
        "Violeta",
        "Gris",
        "Blanco",
    )

    multiplier_band = (
        "Negro",
        "Marron",
        "Rojo",
        "Naranja",
        "Amarillo",
        "Verde",
        "Azul",
        "Violeta",
        "Gris",
        "Blanco",
        "Oro",
        "Plata",
    )

    tolerances = ("Marron", "Rojo", "Verde", "Azul", "Violeta", "Gris", "Oro", "Plata")

    def __init__(self, panel_principal):
        self.root = panel_principal
        self.build_gui()

    def create_range_str(self, down=0.0, up=0.0):
        return "{0:1.4f}? <= R <= {1:1.4f}?".format(down, up)

    def calculate_to_ui(self):
        value_ohm = get_value_resistance(
            band_1_name=self.color_map.get(self.band_1_str.get(), "").lower(),
            band_2_name=self.color_map.get(self.band_2_str.get(), "").lower(),
            multiplier_name=self.color_map.get(self.band_multiplier_str.get(), "").lower(),
        )

        self.result_str.set(f"{value_ohm}?")

        color_tolerance = self.color_map.get(self.band_tolerance_str.get(), "").lower()
        range_down, range_up = get_range_tolerance(value_ohm, color_tolerance)

        self.range_str.set(self.create_range_str(range_down, range_up))

        percentage = get_tolerance(color=color_tolerance)["percentage"]
        self.tolerance_str.set(f"{percentage}%")

        self.update_colors()

    def event_change_band(self, ev):
        self.calculate_to_ui()

    def update_colors(self):
        self.canvas.itemconfig(self.band1_rect, fill=self.color_map.get(self.band_1_str.get(), ""))
        self.canvas.itemconfig(self.band2_rect, fill=self.color_map.get(self.band_2_str.get(), ""))
        self.canvas.itemconfig(self.band3_rect, fill=self.color_map.get(self.band_multiplier_str.get(), ""))
        self.canvas.itemconfig(self.band4_rect, fill=self.color_map.get(self.band_tolerance_str.get(), ""))

    def build_gui(self):
        Label(self.root, text="Colores de las Resistencias", font=("Hack", 20, "bold")).pack(
            expand=True, fill=BOTH, padx=8, pady=8
        )

        self.main_container = Frame(self.root)
        self.main_container.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Configurar las columnas del grid para que se expandan equitativamente
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(2, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        container_bands_values = Frame(self.main_container)
        container_bands_values.grid(row=0, column=0, padx=10, pady=20, sticky=N)

        container_resistance = Frame(self.main_container)
        container_resistance.grid(row=0, column=1, padx=10, pady=20, sticky=N)

        container_values = Frame(self.main_container)
        container_values.grid(row=0, column=2, padx=10, pady=60, sticky=N)

        # Banda 1
        Label(container_bands_values, text="Banda 1", font=("Hack", 10, "bold")).grid(row=0, column=0, pady=10, sticky=W)
        self.band_1_str = StringVar()
        band_1 = Combobox(container_bands_values, values=self.colors_band1, state="readonly", textvariable=self.band_1_str)
        band_1.grid(row=1, column=0, pady=10, sticky=W)
        band_1.current(1)
        band_1.bind("<<ComboboxSelected>>", self.event_change_band)

        # Banda 2
        Label(container_bands_values, text="Banda 2", font=("Hack", 10, "bold")).grid(row=2, column=0, pady=10, sticky=W)
        self.band_2_str = StringVar()
        band_2 = Combobox(container_bands_values, values=self.colors_band2, state="readonly", textvariable=self.band_2_str)
        band_2.grid(row=3, column=0, pady=10, sticky=W)
        band_2.current(0)
        band_2.bind("<<ComboboxSelected>>", self.event_change_band)

        # Banda 3
        Label(container_bands_values, text="Banda 3", font=("Hack", 10, "bold")).grid(row=4, column=0, pady=10, sticky=W)
        self.band_multiplier_str = StringVar()
        band_3 = Combobox(container_bands_values, values=self.multiplier_band, state="readonly", textvariable=self.band_multiplier_str)
        band_3.grid(row=5, column=0, pady=10, sticky=W)
        band_3.current(2)
        band_3.bind("<<ComboboxSelected>>", self.event_change_band)

        # Banda 4
        Label(container_bands_values, text="Banda 4", font=("Hack", 10, "bold")).grid(row=6, column=0, pady=10, sticky=W)
        self.band_tolerance_str = StringVar()
        band_4 = Combobox(container_bands_values, values=self.tolerances, state="readonly", textvariable=self.band_tolerance_str)
        band_4.grid(row=7, column=0, pady=10, sticky=W)
        band_4.current(6)
        band_4.bind("<<ComboboxSelected>>", self.event_change_band)

        # Imagen de la resistencia
        self.canvas = Canvas(container_resistance, width=100, height=400)
        self.canvas.grid(row=0, column=0, pady=20)
        
        # Dibujar la resistencia
        self.canvas.create_rectangle(45, 10, 55, 70, fill="silver", outline="silver")
        self.canvas.create_oval(25, 50, 75, 110, fill="tan", outline="tan")
        self.canvas.create_rectangle(35, 100, 65, 200, fill="tan", outline="tan")
        self.canvas.create_oval(25, 190, 75, 250, fill="tan", outline="tan")
        self.canvas.create_rectangle(45, 240, 55, 290, fill="silver", outline="silver")
        
        # Ajustar las bandas de colores para que estén centradas
        self.band1_rect = self.canvas.create_rectangle(35, 115, 65, 125, fill=self.color_map.get(self.band_1_str.get(), ""), outline="black")
        self.band2_rect = self.canvas.create_rectangle(35, 135, 65, 145, fill=self.color_map.get(self.band_2_str.get(), ""), outline="black")
        self.band3_rect = self.canvas.create_rectangle(35, 155, 65, 165, fill=self.color_map.get(self.band_multiplier_str.get(), ""), outline="black")
        self.band4_rect = self.canvas.create_rectangle(35, 175, 65, 185, fill=self.color_map.get(self.band_tolerance_str.get(), ""), outline="black")

        # Valores
        Label(container_values, text="Valor:", font=("Hack", 10, "bold")).grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.result_str = StringVar()
        label_result = Label(container_values, font=("Hack", 10, "bold"), fg="blue", textvariable=self.result_str)
        label_result.grid(row=1, column=0, pady=10, padx=10, sticky=W)

        Label(container_values, text="Tolerancia:", font=("Hack", 10, "bold")).grid(row=2, column=0, pady=10, padx=10, sticky=W)
        self.tolerance_str = StringVar()
        Label(container_values, textvariable=self.tolerance_str, font=("Hack", 10, "bold"), fg="red").grid(row=3, column=0, pady=10, padx=10, sticky=W)

        Label(container_values, text="Rango:", font=("Hack", 10, "bold")).grid(row=4, column=0, pady=10, padx=10, sticky=W)
        self.range_str = StringVar()
        label_range = Label(container_values, textvariable=self.range_str, font=("Hack", 10, "bold"))
        label_range.grid(row=5, column=0, pady=10, padx=10, sticky=W)

        self.calculate_to_ui()
