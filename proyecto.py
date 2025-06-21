import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from datetime import datetime

lista_trabajadores_registrados = []
contadorun = 0
contadordo = 0
contadortr = 0
contadorcu = 0
boton_vacu = None
boton_vacd = None
boton_vact = None
boton_vacc = None
historial_actividades = []
global_combobox_asistencia = None
global_label_trabajadores_listado = None
global_ventana_asistencia = None
global_entry_hora_entrada = None

COLOR_FONDO_CLARO = "#F0F8FF"
COLOR_FONDO_OSCURO = "#E0FFFF"
COLOR_BOTON_PRINCIPAL = "#1E90FF"
COLOR_TEXTO_BOTON = "white"
COLOR_BOTON_ACCION = "#32CD32"
COLOR_BOTON_VOLVER = "#696969"
COLOR_TEXTO_GENERAL = "#333333"
COLOR_BORDE_ENTRADA = "#B0C4DE"

FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_SUBTITULO = ("Helvetica", 16, "bold")
FUENTE_ETIQUETA = ("Verdana", 12)
FUENTE_ENTRADA = ("Consolas", 14)
FUENTE_BOTON_GRANDE = ("Arial", 16, "bold")
FUENTE_BOTON_NORMAL = ("Arial", 12, "bold")


class Trabajador:
    def __init__(self, nombre, edad, genero, curp, nss, puesto, horario):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.curp = curp
        self.nss = nss
        self.puesto = puesto
        self.horario = horario
        self.habilitado = True
        self.vacaciones_solicitadas_individual = {"Enero-Febrero": 0,"Marzo-Abril": 0,"Junio-Julio": 0,"Nov-Dic": 0,}

    def obtener_texto_para_lista(self):
        estado = " (Inhabilitado)" if not self.habilitado else ""
        return f"{self.nombre} (NSS: {self.nss}){estado}"

    def obtener_conteo_vacaciones_individual(self, periodo):
        return self.vacaciones_solicitadas_individual.get(periodo, 0)

    def registrar_vacaciones_individual(self, periodo):
        if self.vacaciones_solicitadas_individual.get(periodo, 0) < 3:
            self.vacaciones_solicitadas_individual[periodo] += 1
            return True
        return False

  
class ManejadorVacaciones:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_vacaciones = None
        self.combobox_trabajadores = None

    def vacaciones_uno(self):
        global contadorun, boton_vacu
        contadorun += 1
        if contadorun >= 3:
            if boton_vacu:
                boton_vacu.config(state=tk.DISABLED)
                messagebox.showinfo("Límite Alcanzado", "El período Enero-Febrero ha alcanzado el límite de solicitudes")

    def vacaciones_dos(self):
        global contadordo, boton_vacd
        contadordo += 1
        if contadordo >= 3:
            if boton_vacd:
                boton_vacd.config(state=tk.DISABLED)
                messagebox.showinfo("Límite Alcanzado", "El período Marzo-Abril ha alcanzado el límite de solicitudes")

    def vacaciones_tres(self):
        global contadortr, boton_vact
        contadortr += 1
        if contadortr >= 3:
            if boton_vact:
                boton_vact.config(state=tk.DISABLED)
                messagebox.showinfo("Límite Alcanzado", "El período Junio-Julio ha alcanzado el límite de solicitudes")

