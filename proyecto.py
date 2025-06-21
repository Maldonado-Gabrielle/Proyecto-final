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

def vacaciones_cuatro(self):
        global contadorcu, boton_vacc
        contadorcu += 1
        if contadorcu >= 3:
            if boton_vacc:
                boton_vacc.config(state=tk.DISABLED)
                messagebox.showinfo("Límite Alcanzado", "El período Nov-Dic ha alcanzado el límite de solicitudes ")

    def _obtener_contador_global(self, periodo):
        global contadorun, contadordo, contadortr, contadorcu
        if periodo == "Enero-Febrero":
            return contadorun
        elif periodo == "Marzo-Abril":
            return contadordo
        elif periodo == "Junio-Julio":
            return contadortr
        elif periodo == "Nov-Dic":
            return contadorcu
        return 0

    def _actualizar_estado_botones_vacaciones(self):
        indice_seleccionado = self.combobox_trabajadores.current()
        trabajador_seleccionado = None
        global nombres_para_combobox_vacaciones

        texto_seleccionado = self.combobox_trabajadores.get()
        if texto_seleccionado and texto_seleccionado != "No hay empleados registrados aún":
            for t in lista_trabajadores_registrados:
                if t.obtener_texto_para_lista() == texto_seleccionado:
                    trabajador_seleccionado = t
                    break

        periodos_orden = ["Enero-Febrero", "Marzo-Abril", "Junio-Julio", "Nov-Dic"]
        global_buttons = [boton_vacu, boton_vacd, boton_vact, boton_vacc]

        for i, periodo in enumerate(periodos_orden):
            btn = global_buttons[i]
            if btn is None:
                continue

            contador_global_actual = self._obtener_contador_global(periodo)
            limite_global_alcanzado = (contador_global_actual >= 3)

            limite_individual_alcanzado = False
            if trabajador_seleccionado:
                limite_individual_alcanzado = (
                            trabajador_seleccionado.obtener_conteo_vacaciones_individual(periodo) >= 3)

            if not trabajador_seleccionado or not trabajador_seleccionado.habilitado or limite_global_alcanzado or limite_individual_alcanzado:
                btn.config(state=tk.DISABLED)
            else:
                btn.config(state=tk.NORMAL)
def _accion_combinada_vacacion(self, periodo, tu_funcion_original):
        seleccion_combobox_texto = self.combobox_trabajadores.get()

        if not seleccion_combobox_texto or seleccion_combobox_texto == "No hay empleados registrados aún" or \
                seleccion_combobox_texto == "Seleccione un empleado...":
            messagebox.showwarning("Error", "Por favor, seleccione un empleado primero.")
            return

        trabajador_seleccionado = None
        for t in lista_trabajadores_registrados:
            if t.obtener_texto_para_lista() == seleccion_combobox_texto:
                trabajador_seleccionado = t
                break

        if not trabajador_seleccionado:
            messagebox.showerror("Error", "No se pudo encontrar el empleado seleccionado.")
            return

        if not trabajador_seleccionado.habilitado:
            messagebox.showwarning("Inhabilitado",f"'{trabajador_seleccionado.nombre}' está inhabilitado y no puede solicitar vacaciones.")
            return

        contador_global_antes = self._obtener_contador_global(periodo)

        tu_funcion_original()

        if self._obtener_contador_global(periodo) >= 3 and contador_global_antes < 3:
            self._actualizar_estado_botones_vacaciones()
            return

        if trabajador_seleccionado.registrar_vacaciones_individual(periodo):
            mensaje_historial_simple = f"Vacación de {periodo} registrada para {trabajador_seleccionado.nombre}."
            historial_actividades.append(mensaje_historial_simple)
            messagebox.showinfo("Vacaciones Registradas",f"Vacaciones para '{trabajador_seleccionado.nombre}' registradas en '{periodo}'.\n"f"Este empleado lleva {trabajador_seleccionado.obtener_conteo_vacaciones_individual(periodo)} solicitudes \n")
        else:
            messagebox.showwarning("Límite Individual Alcanzado",f"'{trabajador_seleccionado.nombre}' ya ha alcanzado su límite de 3 solicitudes para el período '{periodo}'.")

        self._actualizar_estado_botones_vacaciones()

    def abrir_ventana_vacaciones(self):
        global boton_vacu, boton_vacd, boton_vact, boton_vacc
        global nombres_para_combobox_vacaciones

        self.ventana_principal.withdraw()

        self.ventana_vacaciones = tk.Toplevel(self.ventana_principal)
        self.ventana_vacaciones.title("Gestión de Vacaciones - Hospital XYZ")
        self.ventana_vacaciones.state('zoomed')
        self.ventana_vacaciones.configure(bg=COLOR_FONDO_CLARO)

        tk.Label(self.ventana_vacaciones, text="Fechas de Vacaciones Disponibles", font=FUENTE_TITULO, bg=COLOR_FONDO_CLARO, fg=COLOR_TEXTO_GENERAL).pack(pady=20)

        tk.Label(self.ventana_vacaciones, text="Seleccione un Empleado:", font=FUENTE_SUBTITULO, bg=COLOR_FONDO_CLARO,fg=COLOR_TEXTO_GENERAL).pack(pady=10)

        nombres_para_combobox_vacaciones = [t.obtener_texto_para_lista() for t in lista_trabajadores_registrados]
        if not nombres_para_combobox_vacaciones:
            nombres_para_combobox_vacaciones = ["No hay empleados registrados aún"]

        self.combobox_trabajadores = ttk.Combobox(self.ventana_vacaciones, values=nombres_para_combobox_vacaciones,state="readonly", font=FUENTE_ETIQUETA, width=40)
        self.combobox_trabajadores.pack(pady=10, ipadx=5, ipady=5)

        if nombres_para_combobox_vacaciones and nombres_para_combobox_vacaciones[
            0] != "No hay empleados registrados aún":
            self.combobox_trabajadores.current(0)
        else:
            self.combobox_trabajadores.set("No hay empleados registrados aún")
            self.combobox_trabajadores.config(state="disabled")

        self.combobox_trabajadores.bind("<<ComboboxSelected>>", lambda event: self._actualizar_estado_botones_vacaciones())

        tk.Label(self.ventana_vacaciones, text="Períodos de Solicitud de Vacaciones:", font=FUENTE_SUBTITULO, bg=COLOR_FONDO_CLARO, fg=COLOR_TEXTO_GENERAL).pack(pady=15)

        global boton_vacu, boton_vacd, boton_vact, boton_vacc
        boton_vacu = tk.Button(self.ventana_vacaciones, text="Enero - Febrero",command=lambda: self._accion_combinada_vacacion("Enero-Febrero", self.vacaciones_uno),font=FUENTE_BOTON_NORMAL, bg=COLOR_BOTON_ACCION, fg=COLOR_TEXTO_BOTON, width=25,height=1, relief="raised", bd=3)
        boton_vacu.pack(pady=7)

        boton_vacd = tk.Button(self.ventana_vacaciones, text="Marzo - Abril",command=lambda: self._accion_combinada_vacacion("Marzo-Abril", self.vacaciones_dos), font=FUENTE_BOTON_NORMAL, bg=COLOR_BOTON_ACCION, fg=COLOR_TEXTO_BOTON, width=25, height=1, relief="raised", bd=3)
        boton_vacd.pack(pady=7)

        boton_vact = tk.Button(self.ventana_vacaciones, text="Junio - Julio",command=lambda: self._accion_combinada_vacacion("Junio-Julio", self.vacaciones_tres),font=FUENTE_BOTON_NORMAL, bg=COLOR_BOTON_ACCION, fg=COLOR_TEXTO_BOTON, width=25,height=1, relief="raised", bd=3)
        boton_vact.pack(pady=7)

        boton_vacc = tk.Button(self.ventana_vacaciones, text="Noviembre - Diciembre",command=lambda: self._accion_combinada_vacacion("Nov-Dic", self.vacaciones_cuatro),font=FUENTE_BOTON_NORMAL, bg=COLOR_BOTON_ACCION, fg=COLOR_TEXTO_BOTON, width=25,height=1, relief="raised", bd=3)
        boton_vacc.pack(pady=7)

        self._actualizar_estado_botones_vacaciones()

        def volver_a_principal():
            self.ventana_vacaciones.destroy()
            self.ventana_principal.deiconify()

        tk.Button(self.ventana_vacaciones, text="Volver al Menú Principal", command=volver_a_principal, font=FUENTE_BOTON_NORMAL, bg=COLOR_BOTON_VOLVER, fg=COLOR_TEXTO_BOTON, width=20, height=1,relief="raised", bd=3).pack(pady=25)
        self.ventana_vacaciones.protocol("WM_DELETE_WINDOW", volver_a_principal)


def actualizar_combobox_para_turno(turno_seleccionado):
    global global_combobox_asistencia, global_label_trabajadores_listado

    nombres_trabajadores_turno = []
    for trabajador in lista_trabajadores_registrados:
        if trabajador.horario == turno_seleccionado and trabajador.habilitado:
            nombres_trabajadores_turno.append(trabajador.obtener_texto_para_lista())

    global_combobox_asistencia['values'] = nombres_trabajadores_turno

    if nombres_trabajadores_turno:
        global_combobox_asistencia.set("Seleccione un empleado...")
        global_combobox_asistencia.config(state="readonly")
        global_label_trabajadores_listado.config(text=f"Empleados en Turno {turno_seleccionado}:")
    else:
        global_combobox_asistencia.set("No hay empleados habilitados en este turno")
        global_combobox_asistencia.config(state="disabled")
        global_label_trabajadores_listado.config(text=f"No hay empleados habilitados en Turno {turno_seleccionado}")
