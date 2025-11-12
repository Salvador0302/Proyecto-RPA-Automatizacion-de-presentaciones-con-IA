"""
Interfaz gráfica MODERNA para el generador de presentaciones con IA
Usando CustomTkinter para un diseño profesional y actual
"""
import customtkinter as ctk
from tkinter import messagebox, filedialog
import os
import sys
import threading

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from claude.claude_integration import ClaudeIntegration
from scripts.text_to_pptx import TextToPptxConverter
from scripts.latex_to_pptx import LatexToPptxConverter

# Configuración de apariencia
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"


class ModernPresentationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.title("🚀 Generador de Presentaciones con IA")
        self.geometry("1000x800")
        
        # Centrar la ventana
        self.center_window()
        
        # Variables
        self.ai_instance = None
        self.current_content = ""
        
        # Configurar el grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Crear la interfaz
        self.create_header()
        self.create_main_content()
        self.create_footer()
        
        # Inicializar IA
        self.initialize_ai()
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_header(self):
        """Crea el encabezado de la aplicación"""
        header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        # Título principal
        title_label = ctk.CTkLabel(
            header_frame,
            text="🤖 Generador de Presentaciones con IA",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=10)
        
        # Subtítulo
        subtitle_label = ctk.CTkLabel(
            header_frame,
            text="Crea presentaciones profesionales usando Inteligencia Artificial",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        subtitle_label.pack()
    
    def create_main_content(self):
        """Crea el contenido principal con tabs"""
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Tabs
        self.tabview = ctk.CTkTabview(main_frame, corner_radius=10)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Crear tabs
        self.tab_generate = self.tabview.add("🤖 Generar con IA")
        self.tab_edit = self.tabview.add("✏️ Editar Contenido")
        self.tab_convert = self.tabview.add("📊 Convertir a PPTX")
        
        # Configurar cada tab
        self.setup_generate_tab()
        self.setup_edit_tab()
        self.setup_convert_tab()
    
    def setup_generate_tab(self):
        """Configura el tab de generación con IA"""
        # Configurar grid
        self.tab_generate.grid_columnconfigure(0, weight=1)
        
        # Frame de estado de IA
        status_frame = ctk.CTkFrame(self.tab_generate, fg_color="transparent")
        status_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(
            status_frame,
            text="Estado de la IA:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).pack(anchor="w")
        
        self.ai_status_label = ctk.CTkLabel(
            status_frame,
            text="⏳ Inicializando...",
            font=ctk.CTkFont(size=13),
            text_color="orange"
        )
        self.ai_status_label.pack(anchor="w", pady=(5, 0))
        
        # Separador
        ctk.CTkFrame(self.tab_generate, height=2, fg_color="gray30").grid(
            row=1, column=0, sticky="ew", padx=20, pady=10)
        
        # Formulario de generación
        form_frame = ctk.CTkFrame(self.tab_generate, fg_color="transparent")
        form_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
        form_frame.grid_columnconfigure(0, weight=1)
        
        # Tema
        ctk.CTkLabel(
            form_frame,
            text="📝 Tema de la presentación:",
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.topic_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Ej: Inteligencia Artificial y Machine Learning",
            height=40,
            font=ctk.CTkFont(size=13)
        )
        self.topic_entry.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        self.topic_entry.insert(0, "Inteligencia Artificial y Machine Learning")
        
        # Frame para parámetros en línea
        params_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        params_frame.grid(row=2, column=0, sticky="ew", pady=(0, 15))
        params_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Número de slides
        slides_container = ctk.CTkFrame(params_frame, fg_color="transparent")
        slides_container.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        ctk.CTkLabel(
            slides_container,
            text="📊 Número de slides:",
            font=ctk.CTkFont(size=13, weight="bold")
        ).pack(anchor="w")
        
        self.slides_var = ctk.StringVar(value="5")
        self.slides_spinbox = ctk.CTkEntry(
            slides_container,
            textvariable=self.slides_var,
            width=80,
            height=35
        )
        self.slides_spinbox.pack(anchor="w", pady=(5, 0))
        
        # Estilo de contenido
        style_container = ctk.CTkFrame(params_frame, fg_color="transparent")
        style_container.grid(row=0, column=1, sticky="ew", padx=(0, 10))
        
        ctk.CTkLabel(
            style_container,
            text="🎨 Estilo de contenido:",
            font=ctk.CTkFont(size=13, weight="bold")
        ).pack(anchor="w")
        
        self.style_combo = ctk.CTkComboBox(
            style_container,
            values=["professional", "casual", "academic", "creative"],
            width=150,
            height=35
        )
        self.style_combo.pack(anchor="w", pady=(5, 0))
        self.style_combo.set("professional")
        
        # Tema de PowerPoint
        theme_container = ctk.CTkFrame(params_frame, fg_color="transparent")
        theme_container.grid(row=0, column=2, sticky="ew")
        
        ctk.CTkLabel(
            theme_container,
            text="🎨 Tema de PowerPoint:",
            font=ctk.CTkFont(size=13, weight="bold")
        ).pack(anchor="w")
        
        self.theme_combo = ctk.CTkComboBox(
            theme_container,
            values=["modern_blue", "dark", "professional", "vibrant"],
            width=150,
            height=35
        )
        self.theme_combo.pack(anchor="w", pady=(5, 0))
        self.theme_combo.set("modern_blue")
        
        # Botón generar
        self.generate_btn = ctk.CTkButton(
            form_frame,
            text="🤖 Generar Contenido con IA",
            command=self.generate_content,
            height=45,
            font=ctk.CTkFont(size=15, weight="bold"),
            state="disabled"
        )
        self.generate_btn.grid(row=3, column=0, pady=(10, 0))
        
        # Barra de progreso
        self.progress_generate = ctk.CTkProgressBar(form_frame, mode="indeterminate")
        self.progress_generate.grid(row=4, column=0, sticky="ew", pady=(15, 0))
        self.progress_generate.grid_remove()  # Ocultar inicialmente
    
    def setup_edit_tab(self):
        """Configura el tab de edición de contenido"""
        self.tab_edit.grid_columnconfigure(0, weight=1)
        self.tab_edit.grid_rowconfigure(1, weight=1)
        
        # Título
        ctk.CTkLabel(
            self.tab_edit,
            text="✏️ Edita o carga tu contenido aquí",
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(20, 10))
        
        # Área de texto
        self.content_textbox = ctk.CTkTextbox(
            self.tab_edit,
            font=ctk.CTkFont(family="Consolas", size=12),
            wrap="word"
        )
        self.content_textbox.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))
        
        # Botones de acción
        buttons_frame = ctk.CTkFrame(self.tab_edit, fg_color="transparent")
        buttons_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))
        
        ctk.CTkButton(
            buttons_frame,
            text="📄 Cargar Archivo",
            command=self.load_text_file,
            height=40,
            width=150
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            buttons_frame,
            text="💾 Guardar",
            command=self.save_content,
            height=40,
            width=150
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            buttons_frame,
            text="🗑️ Limpiar",
            command=self.clear_content,
            height=40,
            width=150,
            fg_color="red",
            hover_color="darkred"
        ).pack(side="left", padx=5)
    
    def setup_convert_tab(self):
        """Configura el tab de conversión"""
        self.tab_convert.grid_columnconfigure(0, weight=1)
        
        # Título
        ctk.CTkLabel(
            self.tab_convert,
            text="📊 Convierte tu contenido a PowerPoint",
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Opción 1: Texto a PPTX
        option1_frame = ctk.CTkFrame(self.tab_convert)
        option1_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)
        option1_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(
            option1_frame,
            text="📝 Opción 1: Convertir Texto a PowerPoint",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))
        
        ctk.CTkLabel(
            option1_frame,
            text="Convierte el contenido del editor a una presentación PowerPoint profesional.",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        ).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))
        
        ctk.CTkButton(
            option1_frame,
            text="📊 Texto → PPTX",
            command=self.convert_text_to_pptx,
            height=50,
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=2, column=0, padx=20, pady=(0, 15))
        
        # Separador
        ctk.CTkFrame(self.tab_convert, height=2, fg_color="gray30").grid(
            row=2, column=0, sticky="ew", padx=20, pady=15)
        
        # Opción 2: LaTeX/PDF a PPTX
        option2_frame = ctk.CTkFrame(self.tab_convert)
        option2_frame.grid(row=3, column=0, sticky="ew", padx=20, pady=10)
        option2_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(
            option2_frame,
            text="📄 Opción 2: Convertir LaTeX/PDF a PowerPoint",
            font=ctk.CTkFont(size=15, weight="bold")
        ).grid(row=0, column=0, sticky="w", padx=20, pady=(15, 5))
        
        ctk.CTkLabel(
            option2_frame,
            text="Convierte archivos LaTeX (.tex) o PDF existentes a PowerPoint.",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        ).grid(row=1, column=0, sticky="w", padx=20, pady=(0, 15))
        
        ctk.CTkButton(
            option2_frame,
            text="📄 LaTeX/PDF → PPTX",
            command=self.convert_latex_to_pptx,
            height=50,
            font=ctk.CTkFont(size=14, weight="bold")
        ).grid(row=2, column=0, padx=20, pady=(0, 15))
        
        # Barra de progreso
        self.progress_convert = ctk.CTkProgressBar(self.tab_convert, mode="indeterminate")
        self.progress_convert.grid(row=4, column=0, sticky="ew", padx=20, pady=(15, 10))
        self.progress_convert.grid_remove()  # Ocultar inicialmente
    
    def create_footer(self):
        """Crea el footer con información de estado"""
        footer_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        footer_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=(10, 20))
        
        self.status_label = ctk.CTkLabel(
            footer_frame,
            text="✅ Listo para generar",
            font=ctk.CTkFont(size=13),
            text_color="green"
        )
        self.status_label.pack(side="left")
        
        # Créditos
        credits_label = ctk.CTkLabel(
            footer_frame,
            text="💡 Proyecto RPA | Powered by Gemini/Claude AI",
            font=ctk.CTkFont(size=11),
            text_color="gray60"
        )
        credits_label.pack(side="right")
    
    # ========== MÉTODOS DE FUNCIONALIDAD ==========
    
    def initialize_ai(self):
        """Inicializa la conexión con la IA"""
        def init_thread():
            try:
                self.ai_instance = ClaudeIntegration(provider="auto")
                provider = self.ai_instance.provider.upper()
                model = self.ai_instance.model
                
                self.after(0, lambda: self.ai_status_label.configure(
                    text=f"✅ {provider} conectado ({model})",
                    text_color="green"
                ))
                self.after(0, lambda: self.generate_btn.configure(state="normal"))
                
            except Exception as e:
                self.after(0, lambda: self.ai_status_label.configure(
                    text=f"❌ Error: {str(e)}",
                    text_color="red"
                ))
                self.after(0, lambda: messagebox.showwarning(
                    "Advertencia",
                    f"No se pudo conectar con la IA:\n{str(e)}\n\n"
                    "Puedes cargar contenido desde un archivo o usar la conversión LaTeX/PDF."
                ))
        
        threading.Thread(target=init_thread, daemon=True).start()
    
    def generate_content(self):
        """Genera contenido usando la IA"""
        topic = self.topic_entry.get().strip()
        if not topic:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un tema")
            return
        
        try:
            num_slides = int(self.slides_var.get())
        except ValueError:
            messagebox.showwarning("Advertencia", "El número de slides debe ser un número")
            return
        
        style = self.style_combo.get()
        
        # Deshabilitar botón y mostrar progreso
        self.generate_btn.configure(state="disabled")
        self.progress_generate.grid()
        self.progress_generate.start()
        self.status_label.configure(text="⏳ Generando contenido con IA...", text_color="orange")
        
        def generate_thread():
            try:
                content = self.ai_instance.generate_presentation_content(
                    topic=topic,
                    num_slides=num_slides,
                    style=style
                )
                
                self.after(0, lambda: self.on_content_generated(content))
                
            except Exception as e:
                self.after(0, lambda: self.on_generation_error(str(e)))
        
        threading.Thread(target=generate_thread, daemon=True).start()
    
    def on_content_generated(self, content):
        """Callback cuando el contenido se genera exitosamente"""
        self.progress_generate.stop()
        self.progress_generate.grid_remove()
        self.generate_btn.configure(state="normal")
        
        self.content_textbox.delete("1.0", "end")
        self.content_textbox.insert("1.0", content)
        
        self.status_label.configure(text="✅ Contenido generado exitosamente", text_color="green")
        
        # Cambiar al tab de edición
        self.tabview.set("✏️ Editar Contenido")
        
        messagebox.showinfo("Éxito", "Contenido generado correctamente.\nPuedes editarlo antes de convertir.")
    
    def on_generation_error(self, error_msg):
        """Callback cuando hay un error en la generación"""
        self.progress_generate.stop()
        self.progress_generate.grid_remove()
        self.generate_btn.configure(state="normal")
        self.status_label.configure(text="❌ Error al generar contenido", text_color="red")
        messagebox.showerror("Error", f"No se pudo generar el contenido:\n{error_msg}")
    
    def load_text_file(self):
        """Carga contenido desde un archivo de texto"""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                self.content_textbox.delete("1.0", "end")
                self.content_textbox.insert("1.0", content)
                
                self.status_label.configure(
                    text=f"✅ Archivo cargado: {os.path.basename(file_path)}",
                    text_color="green"
                )
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{str(e)}")
    
    def save_content(self):
        """Guarda el contenido actual en un archivo"""
        content = self.content_textbox.get("1.0", "end").strip()
        if not content:
            messagebox.showwarning("Advertencia", "No hay contenido para guardar")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Guardar contenido",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.status_label.configure(
                    text=f"✅ Guardado: {os.path.basename(file_path)}",
                    text_color="green"
                )
                messagebox.showinfo("Éxito", f"Contenido guardado en:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    def clear_content(self):
        """Limpia el contenido del área de texto"""
        if messagebox.askyesno("Confirmar", "¿Deseas limpiar todo el contenido?"):
            self.content_textbox.delete("1.0", "end")
            self.status_label.configure(text="🗑️ Contenido limpiado", text_color="gray")
    
    def convert_text_to_pptx(self):
        """Convierte el texto actual a PowerPoint"""
        content = self.content_textbox.get("1.0", "end").strip()
        if not content:
            messagebox.showwarning("Advertencia", "No hay contenido para convertir")
            return
        
        output_path = filedialog.asksaveasfilename(
            title="Guardar presentación",
            defaultextension=".pptx",
            filetypes=[("PowerPoint", "*.pptx"), ("Todos los archivos", "*.*")]
        )
        
        if not output_path:
            return
        
        # Guardar contenido temporalmente
        temp_file = "temp_content.txt"
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear archivo temporal:\n{str(e)}")
            return
        
        theme = self.theme_combo.get()
        
        self.progress_convert.grid()
        self.progress_convert.start()
        self.status_label.configure(text="⏳ Convirtiendo a PowerPoint...", text_color="orange")
        
        def convert_thread():
            try:
                converter = TextToPptxConverter(theme=theme)
                converter.convert(temp_file, output_path)
                
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                
                self.after(0, lambda: self.on_conversion_success(output_path))
                
            except Exception as e:
                self.after(0, lambda: self.on_conversion_error(str(e)))
        
        threading.Thread(target=convert_thread, daemon=True).start()
    
    def convert_latex_to_pptx(self):
        """Convierte un archivo LaTeX o PDF a PowerPoint"""
        input_path = filedialog.askopenfilename(
            title="Seleccionar archivo LaTeX o PDF",
            filetypes=[
                ("Archivos LaTeX", "*.tex"),
                ("Archivos PDF", "*.pdf"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if not input_path:
            return
        
        output_path = filedialog.asksaveasfilename(
            title="Guardar presentación",
            defaultextension=".pptx",
            filetypes=[("PowerPoint", "*.pptx"), ("Todos los archivos", "*.*")]
        )
        
        if not output_path:
            return
        
        self.progress_convert.grid()
        self.progress_convert.start()
        self.status_label.configure(text="⏳ Convirtiendo LaTeX/PDF...", text_color="orange")
        
        def convert_thread():
            try:
                converter = LatexToPptxConverter()
                converter.convert(input_path, output_path)
                
                self.after(0, lambda: self.on_conversion_success(output_path))
                
            except Exception as e:
                self.after(0, lambda: self.on_conversion_error(str(e)))
        
        threading.Thread(target=convert_thread, daemon=True).start()
    
    def on_conversion_success(self, output_path):
        """Callback cuando la conversión es exitosa"""
        self.progress_convert.stop()
        self.progress_convert.grid_remove()
        self.status_label.configure(text="✅ Presentación creada exitosamente", text_color="green")
        
        result = messagebox.askyesno(
            "Éxito",
            f"Presentación creada exitosamente:\n{output_path}\n\n¿Deseas abrir el archivo?"
        )
        
        if result:
            os.startfile(output_path)
    
    def on_conversion_error(self, error_msg):
        """Callback cuando hay un error en la conversión"""
        self.progress_convert.stop()
        self.progress_convert.grid_remove()
        self.status_label.configure(text="❌ Error en la conversión", text_color="red")
        messagebox.showerror("Error", f"No se pudo crear la presentación:\n{error_msg}")


def main():
    """Función principal"""
    app = ModernPresentationApp()
    app.mainloop()


if __name__ == "__main__":
    main()
