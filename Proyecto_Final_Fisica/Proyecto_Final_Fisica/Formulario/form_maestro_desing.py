import tkinter  as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import Utileria.util_ventana as util_ventana
import Utileria.util_imagenes as util_img
from Formulario.form_calculo_resistencia import FormularioCalculoResistencia

class FormularioMaestroDesing(tk.Tk):
    
    
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./Imagenes/logo.png",(560,136))
        self.perfil = util_img.leer_imagen("./Imagenes/perfil2.png",(100,100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        #configuracion inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap("./Imagenes/logo.ico")
        w,h = 1024 , 600
        util_ventana.centrar_ventana(self,w,h)
        
    def paneles(self):
        ##Crear paneles como : barra superior, menu lateral, y cuerpo principal
        self.barra_superior = tk.Frame(self,bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP,fill='both')
        
        
        #menu lateral
        self.menu_lateral = tk.Frame(self,bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT,fill='both', expand=False)
       
        #cuerpo principal
        self.cuerpo_principal = tk.Frame(self,bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT,fill='both', expand=True)
        
    def controles_barra_superior(self):
        #configuracion de la barra superior
        
        font_awesome = font.Font(family='FontAwesome',size=12)
        #etiqueta de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="RESISTENCIAS")
        self.labelTitulo.config(fg="#fff", font=("Roboto",15),bg = COLOR_BARRA_SUPERIOR,pady=10,width=16)
        self.labelTitulo.pack(side=tk.LEFT)
        
        #boton del menu lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
        
        #Etiqueta de informacion 
        #self.labelTitulo = tk.Label(self.barra_superior,text="GAAAA")
        #self.labelTitulo.config(fg ="#fff",font=("Roboto",10), bg = COLOR_BARRA_SUPERIOR ,padx=10,width=20)
        #self.labelTitulo.pack(side=tk.RIGHT)
        
    def controles_menu_lateral(self):
        ##configuracion del menu lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome',size=15) 
        self.labelPerfil = tk.Label(self.menu_lateral,image=self.perfil,bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP,pady=10)
        
        ##botones del menu lateral
        self.buttonResistencias = tk.Button(self.menu_lateral)
        self.buttonInformacionAplicacion = tk.Button(self.menu_lateral)
        self.buttonEjercicios = tk.Button(self.menu_lateral)
        self.buttonInformacioTeorica = tk.Button(self.menu_lateral)
           
        buttons_info =[
            ("Resistencias","\uf2db",self.buttonResistencias,self.abrir_panel_en_contruccion),
            ("Info App","\uf108",self.buttonInformacionAplicacion,self.abrir_panel_en_contruccion),
            ("Ejercicios","\uf02d",self.buttonEjercicios,self.abrir_panel_en_contruccion),
            ("Info Teorica","\uf129",self.buttonInformacioTeorica,self.abrir_panel_en_contruccion)
        ]
        
        for text,icon,button,comando in buttons_info:
            self.configurar_boton_menu(button,text,icon,font_awesome,ancho_menu,alto_menu,comando)

            
    def configurar_boton_menu(self,button,text,icon,font_awesome,ancho_menu,alto_menu, comando):
        button.config(text=f"      {icon}  {text}",anchor ="w",font=font_awesome,
                      bd=0,bg=COLOR_MENU_LATERAL,fg="white",width=ancho_menu,height=alto_menu,
                      command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
        
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')
        
    def toggle_panel(self):
        # Contraer barra lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)   
    
    def abrir_panel_en_contruccion(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioCalculoResistencia(self.cuerpo_principal)
        
    def limpiar_panel(self,panel):
        for widget in panel.winfo_children():
            widget.destroy()
    