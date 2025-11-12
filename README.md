# 🎯 Proyecto RPA - Automatización de Presentaciones con IA

Sistema automatizado de generación de presentaciones PowerPoint profesionales utilizando Inteligencia Artificial. Soporta Google Gemini (gratuito) y Anthropic Claude, con conversión de LaTeX/PDF y múltiples temas de diseño.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Características Principales

- 🤖 **Generación automática con IA** - Google Gemini (gratis) o Claude AI
- 🎨 **4 Temas profesionales** - Modern Blue, Dark, Professional, Vibrant
- 🖥️ **Interfaz moderna** - CustomTkinter con tema oscuro y tabs organizadas
- 📄 **Conversión LaTeX/PDF** - Transforma documentos a PowerPoint
- 📝 **Conversión de texto** - Formato estructurado a presentaciones
- ⚡ **Detección automática** - Elige la API disponible automáticamente
- 🔄 **Procesamiento en segundo plano** - No bloquea la interfaz

##  Estructura del Proyecto

```
Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude/
├─ gui_app.py                 # 🖥️ Interfaz gráfica principal (CustomTkinter)
├─ test_complete.py           # 🧪 Suite completa de pruebas
├─ requirements.txt           # 📦 Dependencias del proyecto
├─ .env                       # 🔐 Configuración de API keys (no incluido)
├─ .env.example              # 📄 Plantilla de configuración
├─ LICENSE                    # 📜 Licencia MIT
├─ scripts/
│  ├─ latex_to_pptx.py       # Conversor LaTeX/PDF → PowerPoint
│  └─ text_to_pptx.py        # Conversor texto → PowerPoint (4 temas)
├─ claude/
│  └─ claude_integration.py  # Integración multi-proveedor de IA
└─ examples/
   └─ presentation.tex       # Ejemplo de presentación LaTeX Beamer
```

## 🚀 Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone https://github.com/Salvador0302/Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude.git
cd Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar API Key

Crea un archivo `.env` en la raíz del proyecto (puedes copiar `.env.example`):

**Opción 1: Google Gemini (GRATIS - Recomendado) ⭐**
1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Crea una nueva API key (gratis)
4. Agrega a `.env`:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

**Opción 2: Anthropic Claude (Requiere créditos) 💳**
1. Ve a [Anthropic Console](https://console.anthropic.com/)
2. Crea una cuenta y agrega créditos
3. Obtén tu API key
4. Agrega a `.env`:
```env
ANTHROPIC_API_KEY=tu_api_key_aqui
```

**Nota:** El sistema detecta automáticamente qué API usar. Si ambas están configuradas, usará Gemini por defecto.

## 💻 Uso

### Interfaz Gráfica (Recomendado)

Ejecuta la aplicación con interfaz moderna:

```bash
python gui_app.py
```

#### Funcionalidades de la interfaz:

**Pestaña 1: Generar con IA 🤖**
- Ingresa un tema y número de diapositivas
- Selecciona el estilo (profesional, educativo, creativo)
- Genera contenido automáticamente
- Visualiza y edita el contenido generado

**Pestaña 2: Editar Contenido ✏️**
- Carga contenido desde archivos .txt
- Edita manualmente el contenido
- Guarda borradores para usar después
- Convierte a PowerPoint con tema seleccionable

**Pestaña 3: Convertir PDF/LaTeX 📄**
- Convierte archivos PDF a PowerPoint
- Convierte archivos LaTeX Beamer a PowerPoint
- Selección de archivos con explorador
- Conversión automática con un clic

#### Temas Disponibles:
- 🔵 **Modern Blue** - Profesional con acentos azules (predeterminado)
- ⚫ **Dark** - Elegante con fondo oscuro
- 💼 **Professional** - Clásico corporativo
- 🌈 **Vibrant** - Colorido y dinámico

### Línea de Comandos

#### 1. Generar contenido con IA:
```python
from claude.claude_integration import ClaudeIntegration

# Detección automática de API (Gemini o Claude)
ai = ClaudeIntegration(provider="auto")

# Generar contenido
content = ai.generate_presentation_content(
    topic="Inteligencia Artificial y Machine Learning",
    num_slides=5,
    style="profesional"
)

# Guardar contenido
ai.save_to_file(content, "mi_presentacion.txt")
print(f"✅ Usando: {ai.provider} - Modelo: {ai.model}")
```

#### 2. Convertir texto a PowerPoint:
```python
from scripts.text_to_pptx import TextToPptxConverter

# Crear conversor con tema específico
converter = TextToPptxConverter(theme="modern_blue")
converter.convert("mi_presentacion.txt", "presentacion.pptx")
```

#### 3. Convertir LaTeX/PDF a PowerPoint:
```python
from scripts.latex_to_pptx import LatexToPptxConverter

converter = LatexToPptxConverter()
# Desde PDF:
converter.convert("documento.pdf", "presentacion.pptx")
# Desde LaTeX:
converter.convert("documento.tex", "presentacion.pptx")
```

### Ejecutar Tests

Verifica que todo funcione correctamente:

```bash
python test_complete.py
```

**Tests incluidos:**
- ✅ Test de integración con IA (Gemini/Claude)
- ✅ Test de conversión texto → PowerPoint
- ✅ Test de conversión LaTeX → PowerPoint
- ✅ Test de conversión PDF → PowerPoint

## 📖 Formato de Texto para Presentaciones

El contenido generado o manual debe seguir este formato estructurado:

```
Diapositiva 1: Título Principal de la Presentación
- Este será el título en la portada
- Puedes agregar un subtítulo aquí

Diapositiva 2: Primer Tema Importante
- Primera viñeta con contenido relevante
- Segunda viñeta con más información
- Tercera viñeta para completar la idea
- Cuarta viñeta opcional

Diapositiva 3: Segundo Tema Importante
- Punto clave número uno
- Punto clave número dos
- Punto clave número tres

Diapositiva 4: Conclusiones
- Resumen de puntos principales
- Llamado a la acción
- Contacto o referencias
```

**Notas importantes:**
- Cada diapositiva debe comenzar con `Diapositiva N:` seguido del título
- Usa guiones (`-`) para las viñetas
- La primera diapositiva será la portada
- Cada diapositiva puede tener entre 2-6 viñetas

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+** - Lenguaje principal
- **python-pptx** - Creación y manipulación de PowerPoint
- **Google Generative AI** - API de Gemini para generación de contenido
- **Anthropic** - API de Claude como alternativa
- **python-dotenv** - Gestión de variables de entorno
- **pdf2image** - Conversión de PDF a imágenes
- **Pillow (PIL)** - Procesamiento de imágenes

### Frontend
- **CustomTkinter** - Framework moderno para interfaces gráficas
- **tkinter** - GUI nativa de Python (base)

### Desarrollo
- **pytest** - Framework de testing (opcional)
- **poppler-utils** - Herramientas para procesamiento PDF

## 🎨 Temas de Presentación

El proyecto incluye 4 temas profesionales predefinidos:

| Tema | Descripción | Colores Principal |
|------|-------------|------------------|
| **modern_blue** | Profesional y limpio | Azul (#1E88E5) |
| **dark** | Elegante y sofisticado | Gris oscuro + Naranja |
| **professional** | Corporativo tradicional | Azul marino + Gris |
| **vibrant** | Dinámico y colorido | Púrpura + Verde |

Cada tema incluye:
- Diapositiva de portada personalizada
- Encabezados con color específico
- Viñetas estilizadas
- Diseño consistente en todas las diapositivas

## � Ejemplos de Uso

### Generar presentación con Claude AI

```python
from claude.claude_integration import ClaudeIntegration

claude = ClaudeIntegration()
content = claude.generate_presentation_content(
    topic="Inteligencia Artificial",
    num_slides=5,
    style="professional"
)
claude.save_to_file(content, "mi_presentacion.txt")
```

### Convertir texto a PowerPoint

```python
from scripts.text_to_pptx import TextToPptxConverter

converter = TextToPptxConverter()
converter.convert("entrada.txt", "salida.pptx")
```

### Convertir LaTeX a PowerPoint

```python
from scripts.latex_to_pptx import LatexToPptxConverter

converter = LatexToPptxConverter()
converter.convert("presentation.tex", "presentation.pptx")
```

## 📚 Ejemplos

El directorio `examples/` contiene:
- `presentation.tex`: Ejemplo de presentación en LaTeX Beamer
- Archivos generados por los scripts de conversión

## 🛠️ Tecnologías

- **Python 3.7+**
- **python-pptx**: Creación de archivos PowerPoint
- **anthropic**: API de Claude AI
- **python-dotenv**: Gestión de variables de entorno

## 📝 Formato de Entrada

### Formato de Texto
```
# Título Principal
Subtítulo
----
# Diapositiva 2
- Punto 1
- Punto 2
----
# Conclusión
Texto final
```

### LaTeX Beamer
```latex
\begin{frame}{Título}
    \begin{itemize}
        \item Punto 1
        \item Punto 2
    \end{itemize}
\end{frame}
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Salvador0302**

## 🙏 Agradecimientos

- Claude AI de Anthropic por la generación de contenido
- python-pptx por la manipulación de PowerPoint
- La comunidad de código abierto

---

⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!
