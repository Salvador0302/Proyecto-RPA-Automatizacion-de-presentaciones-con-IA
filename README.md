# 🎯 Proyecto RPA - Automatización de Presentaciones con IA# 🎯 Proyecto RPA - Automatización de Presentaciones con IA



Sistema automatizado de generación de presentaciones PowerPoint profesionales utilizando Inteligencia Artificial. Soporta Google Gemini (gratuito) y Anthropic Claude, con conversión de LaTeX/PDF y múltiples temas de diseño.Sistema automatizado de generación de presentaciones PowerPoint profesionales utilizando Inteligencia Artificial. Soporta Google Gemini (gratuito) y Anthropic Claude, con conversión de LaTeX/PDF y múltiples temas de diseño.



[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Gemini API](https://img.shields.io/badge/Gemini-Free-green)](https://makersuite.google.com/)

## ✨ Características Principales

## ✨ Características Principales

- 🤖 **Generación automática con IA** - Google Gemini (gratis) o Claude AI

- 🤖 **Generación automática con IA** - Google Gemini (gratis) o Claude AI- 🎨 **4 Temas profesionales** - Modern Blue, Dark, Professional, Vibrant

- 🎨 **4 Temas profesionales** - Modern Blue, Dark, Professional, Vibrant- 🖥️ **Interfaz moderna** - CustomTkinter con tema oscuro y tabs organizadas

- 🖥️ **Interfaz moderna** - CustomTkinter con tema oscuro y tabs organizadas- 📄 **Conversión LaTeX/PDF** - Transforma documentos a PowerPoint

- 📄 **Conversión LaTeX/PDF** - Transforma documentos a PowerPoint- 📝 **Conversión de texto** - Formato estructurado a presentaciones

- 📝 **Conversión de texto** - Formato estructurado a presentaciones- ⚡ **Detección automática** - Elige la API disponible automáticamente

- ⚡ **Detección automática** - Elige la API disponible automáticamente- 🔄 **Procesamiento en segundo plano** - No bloquea la interfaz

- 🔄 **Procesamiento en segundo plano** - No bloquea la interfaz

##  Estructura del Proyecto

## 📋 Estructura del Proyecto

```

```Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude/

Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude/├─ gui_app.py                 # 🖥️ Interfaz gráfica principal (CustomTkinter)

├─ gui_app.py                 # 🖥️ Interfaz gráfica principal (CustomTkinter)├─ test_complete.py           # 🧪 Suite completa de pruebas

├─ test_complete.py           # 🧪 Suite completa de pruebas├─ requirements.txt           # 📦 Dependencias del proyecto

├─ requirements.txt           # 📦 Dependencias del proyecto├─ .env                       # 🔐 Configuración de API keys (no incluido)

├─ .env                       # 🔐 Configuración de API keys (no incluido)├─ .env.example              # 📄 Plantilla de configuración

├─ .env.example              # 📄 Plantilla de configuración├─ LICENSE                    # 📜 Licencia MIT

├─ LICENSE                    # 📜 Licencia MIT├─ scripts/

├─ scripts/│  ├─ latex_to_pptx.py       # Conversor LaTeX/PDF → PowerPoint

│  ├─ latex_to_pptx.py       # Conversor LaTeX/PDF → PowerPoint│  └─ text_to_pptx.py        # Conversor texto → PowerPoint (4 temas)

│  └─ text_to_pptx.py        # Conversor texto → PowerPoint (4 temas)├─ claude/

├─ claude/│  └─ claude_integration.py  # Integración multi-proveedor de IA

│  └─ claude_integration.py  # Integración multi-proveedor de IA└─ examples/

└─ examples/   └─ presentation.tex       # Ejemplo de presentación LaTeX Beamer

   └─ presentation.tex       # Ejemplo de presentación LaTeX Beamer```

```

## 🚀 Instalación Rápida

## 🚀 Instalación Rápida

### 1. Clonar el repositorio

### 1. Clonar el repositorio

```bash

```bashgit clone https://github.com/Salvador0302/Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude.git

git clone https://github.com/Salvador0302/Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude.gitcd Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude

cd Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude```

```

### 2. Crear entorno virtual (recomendado)

### 2. Crear entorno virtual (recomendado)

```bash

```bashpython -m venv venv

python -m venv venv# Windows:

# Windows:venv\Scripts\activate

venv\Scripts\activate# Linux/Mac:

# Linux/Mac:source venv/bin/activate

source venv/bin/activate```

```

### 3. Instalar dependencias

### 3. Instalar dependencias

```bash

```bashpip install -r requirements.txt

pip install -r requirements.txt```

```

### 4. Configurar API Key

### 4. Configurar API Key

Crea un archivo `.env` en la raíz del proyecto (puedes copiar `.env.example`):

Crea un archivo `.env` en la raíz del proyecto (puedes copiar `.env.example`):

**Opción 1: Google Gemini (GRATIS - Recomendado) ⭐**

**Opción 1: Google Gemini (GRATIS - Recomendado) ⭐**1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)

1. Ve a [Google AI Studio](https://makersuite.google.com/app/apikey)2. Inicia sesión con tu cuenta de Google

2. Inicia sesión con tu cuenta de Google3. Crea una nueva API key (gratis)

3. Crea una nueva API key (gratis)4. Agrega a `.env`:

4. Agrega a `.env`:```env

```envGEMINI_API_KEY=tu_api_key_aqui

GEMINI_API_KEY=tu_api_key_aqui```

```

**Opción 2: Anthropic Claude (Requiere créditos) 💳**

**Opción 2: Anthropic Claude (Requiere créditos) 💳**1. Ve a [Anthropic Console](https://console.anthropic.com/)

1. Ve a [Anthropic Console](https://console.anthropic.com/)2. Crea una cuenta y agrega créditos

2. Crea una cuenta y agrega créditos3. Obtén tu API key

3. Obtén tu API key4. Agrega a `.env`:

4. Agrega a `.env`:```env

```envANTHROPIC_API_KEY=tu_api_key_aqui

ANTHROPIC_API_KEY=tu_api_key_aqui```

```

**Nota:** El sistema detecta automáticamente qué API usar. Si ambas están configuradas, usará Gemini por defecto.

**Nota:** El sistema detecta automáticamente qué API usar. Si ambas están configuradas, usará Gemini por defecto.

## 💻 Uso

## 💻 Uso

### Interfaz Gráfica (Recomendado)

### Interfaz Gráfica (Recomendado)

Ejecuta la aplicación con interfaz moderna:

Ejecuta la aplicación con interfaz moderna:

```bash

```bashpython gui_app.py

python gui_app.py```

```

#### Funcionalidades de la interfaz:

#### Funcionalidades de la interfaz:

**Pestaña 1: Generar con IA 🤖**

**Pestaña 1: Generar con IA 🤖**- Ingresa un tema y número de diapositivas

- Ingresa un tema y número de diapositivas- Selecciona el estilo (profesional, educativo, creativo)

- Selecciona el estilo (profesional, educativo, creativo)- Genera contenido automáticamente

- Genera contenido automáticamente- Visualiza y edita el contenido generado

- Visualiza y edita el contenido generado

**Pestaña 2: Editar Contenido ✏️**

**Pestaña 2: Editar Contenido ✏️**- Carga contenido desde archivos .txt

- Carga contenido desde archivos .txt- Edita manualmente el contenido

- Edita manualmente el contenido- Guarda borradores para usar después

- Guarda borradores para usar después- Convierte a PowerPoint con tema seleccionable

- Convierte a PowerPoint con tema seleccionable

**Pestaña 3: Convertir PDF/LaTeX 📄**

**Pestaña 3: Convertir PDF/LaTeX 📄**- Convierte archivos PDF a PowerPoint

- Convierte archivos PDF a PowerPoint- Convierte archivos LaTeX Beamer a PowerPoint

- Convierte archivos LaTeX Beamer a PowerPoint- Selección de archivos con explorador

- Selección de archivos con explorador- Conversión automática con un clic

- Conversión automática con un clic

#### Temas Disponibles:

#### Temas Disponibles:- 🔵 **Modern Blue** - Profesional con acentos azules (predeterminado)

- 🔵 **Modern Blue** - Profesional con acentos azules (predeterminado)- ⚫ **Dark** - Elegante con fondo oscuro

- ⚫ **Dark** - Elegante con fondo oscuro- 💼 **Professional** - Clásico corporativo

- 💼 **Professional** - Clásico corporativo- 🌈 **Vibrant** - Colorido y dinámico

- 🌈 **Vibrant** - Colorido y dinámico

### Línea de Comandos

### Línea de Comandos

#### 1. Generar contenido con IA:

#### 1. Generar contenido con IA:```python

```pythonfrom claude.claude_integration import ClaudeIntegration

from claude.claude_integration import ClaudeIntegration

# Detección automática de API (Gemini o Claude)

# Detección automática de API (Gemini o Claude)ai = ClaudeIntegration(provider="auto")

ai = ClaudeIntegration(provider="auto")

# Generar contenido

# Generar contenidocontent = ai.generate_presentation_content(

content = ai.generate_presentation_content(    topic="Inteligencia Artificial y Machine Learning",

    topic="Inteligencia Artificial y Machine Learning",    num_slides=5,

    num_slides=5,    style="profesional"

    style="profesional")

)

# Guardar contenido

# Guardar contenidoai.save_to_file(content, "mi_presentacion.txt")

ai.save_to_file(content, "mi_presentacion.txt")print(f"✅ Usando: {ai.provider} - Modelo: {ai.model}")

print(f"✅ Usando: {ai.provider} - Modelo: {ai.model}")```

```

#### 2. Convertir texto a PowerPoint:

#### 2. Convertir texto a PowerPoint:```python

```pythonfrom scripts.text_to_pptx import TextToPptxConverter

from scripts.text_to_pptx import TextToPptxConverter

# Crear conversor con tema específico

# Crear conversor con tema específicoconverter = TextToPptxConverter(theme="modern_blue")

converter = TextToPptxConverter(theme="modern_blue")converter.convert("mi_presentacion.txt", "presentacion.pptx")

converter.convert("mi_presentacion.txt", "presentacion.pptx")```

```

#### 3. Convertir LaTeX/PDF a PowerPoint:

#### 3. Convertir LaTeX/PDF a PowerPoint:```python

```pythonfrom scripts.latex_to_pptx import LatexToPptxConverter

from scripts.latex_to_pptx import LatexToPptxConverter

converter = LatexToPptxConverter()

converter = LatexToPptxConverter()# Desde PDF:

# Desde PDF:converter.convert("documento.pdf", "presentacion.pptx")

converter.convert("documento.pdf", "presentacion.pptx")# Desde LaTeX:

# Desde LaTeX:converter.convert("documento.tex", "presentacion.pptx")

converter.convert("documento.tex", "presentacion.pptx")```

```

### Ejecutar Tests

### Ejecutar Tests

Verifica que todo funcione correctamente:

Verifica que todo funcione correctamente:

```bash

```bashpython test_complete.py

python test_complete.py```

```

**Tests incluidos:**

**Tests incluidos:**- ✅ Test de integración con IA (Gemini/Claude)

- ✅ Test de integración con IA (Gemini/Claude)- ✅ Test de conversión texto → PowerPoint

- ✅ Test de conversión texto → PowerPoint- ✅ Test de conversión LaTeX → PowerPoint

- ✅ Test de conversión LaTeX → PowerPoint- ✅ Test de conversión PDF → PowerPoint

- ✅ Test de conversión PDF → PowerPoint

## 📖 Formato de Texto para Presentaciones

## 📖 Formato de Texto para Presentaciones

El contenido generado o manual debe seguir este formato estructurado:

El contenido generado o manual debe seguir este formato estructurado:

```

```Diapositiva 1: Título Principal de la Presentación

Diapositiva 1: Título Principal de la Presentación- Este será el título en la portada

- Este será el título en la portada- Puedes agregar un subtítulo aquí

- Puedes agregar un subtítulo aquí

Diapositiva 2: Primer Tema Importante

Diapositiva 2: Primer Tema Importante- Primera viñeta con contenido relevante

- Primera viñeta con contenido relevante- Segunda viñeta con más información

- Segunda viñeta con más información- Tercera viñeta para completar la idea

- Tercera viñeta para completar la idea- Cuarta viñeta opcional

- Cuarta viñeta opcional

Diapositiva 3: Segundo Tema Importante

Diapositiva 3: Segundo Tema Importante- Punto clave número uno

- Punto clave número uno- Punto clave número dos

- Punto clave número dos- Punto clave número tres

- Punto clave número tres

Diapositiva 4: Conclusiones

Diapositiva 4: Conclusiones- Resumen de puntos principales

- Resumen de puntos principales- Llamado a la acción

- Llamado a la acción- Contacto o referencias

- Contacto o referencias```

```

**Notas importantes:**

**Notas importantes:**- Cada diapositiva debe comenzar con `Diapositiva N:` seguido del título

- Cada diapositiva debe comenzar con `Diapositiva N:` seguido del título- Usa guiones (`-`) para las viñetas

- Usa guiones (`-`) para las viñetas- La primera diapositiva será la portada

- La primera diapositiva será la portada- Cada diapositiva puede tener entre 2-6 viñetas

- Cada diapositiva puede tener entre 2-6 viñetas

## 🛠️ Tecnologías Utilizadas

## 🛠️ Tecnologías Utilizadas

### Backend

### Backend- **Python 3.8+** - Lenguaje principal

- **Python 3.8+** - Lenguaje principal- **python-pptx** - Creación y manipulación de PowerPoint

- **python-pptx** - Creación y manipulación de PowerPoint- **Google Generative AI** - API de Gemini para generación de contenido

- **Google Generative AI** - API de Gemini para generación de contenido- **Anthropic** - API de Claude como alternativa

- **Anthropic** - API de Claude como alternativa- **python-dotenv** - Gestión de variables de entorno

- **python-dotenv** - Gestión de variables de entorno- **pdf2image** - Conversión de PDF a imágenes

- **pdf2image** - Conversión de PDF a imágenes- **Pillow (PIL)** - Procesamiento de imágenes

- **Pillow (PIL)** - Procesamiento de imágenes

### Frontend

### Frontend- **CustomTkinter** - Framework moderno para interfaces gráficas

- **CustomTkinter** - Framework moderno para interfaces gráficas- **tkinter** - GUI nativa de Python (base)

- **tkinter** - GUI nativa de Python (base)

### Desarrollo

### Desarrollo- **pytest** - Framework de testing (opcional)

- **pytest** - Framework de testing (opcional)- **poppler-utils** - Herramientas para procesamiento PDF

- **poppler-utils** - Herramientas para procesamiento PDF

## 🎨 Temas de Presentación

## 🎨 Temas de Presentación

El proyecto incluye 4 temas profesionales predefinidos:

El proyecto incluye 4 temas profesionales predefinidos:

| Tema | Descripción | Colores Principal |

| Tema | Descripción | Colores Principal ||------|-------------|------------------|

|------|-------------|------------------|| **modern_blue** | Profesional y limpio | Azul (#1E88E5) |

| **modern_blue** | Profesional y limpio | Azul (#1E88E5) || **dark** | Elegante y sofisticado | Gris oscuro + Naranja |

| **dark** | Elegante y sofisticado | Gris oscuro + Naranja || **professional** | Corporativo tradicional | Azul marino + Gris |

| **professional** | Corporativo tradicional | Azul marino + Gris || **vibrant** | Dinámico y colorido | Púrpura + Verde |

| **vibrant** | Dinámico y colorido | Púrpura + Verde |

Cada tema incluye:

Cada tema incluye:- Diapositiva de portada personalizada

- Diapositiva de portada personalizada- Encabezados con color específico

- Encabezados con color específico- Viñetas estilizadas

- Viñetas estilizadas- Diseño consistente en todas las diapositivas

- Diseño consistente en todas las diapositivas

## � Ejemplos de Uso

## 💡 Ejemplos de Uso Completos

### Generar presentación con Claude AI

### Ejemplo 1: Generar presentación completa con IA

```python

```pythonfrom claude.claude_integration import ClaudeIntegration

from claude.claude_integration import ClaudeIntegration

from scripts.text_to_pptx import TextToPptxConverterclaude = ClaudeIntegration()

content = claude.generate_presentation_content(

# Paso 1: Generar contenido con IA    topic="Inteligencia Artificial",

ai = ClaudeIntegration()    num_slides=5,

print(f"Usando: {ai.provider}")    style="professional"

)

content = ai.generate_presentation_content(claude.save_to_file(content, "mi_presentacion.txt")

    topic="Ciberseguridad en la Era Digital",```

    num_slides=6,

    style="profesional"### Convertir texto a PowerPoint

)

```python

# Paso 2: Guardar contenidofrom scripts.text_to_pptx import TextToPptxConverter

ai.save_to_file(content, "ciberseguridad.txt")

converter = TextToPptxConverter()

# Paso 3: Convertir a PowerPoint con temaconverter.convert("entrada.txt", "salida.pptx")

converter = TextToPptxConverter(theme="dark")```

converter.convert("ciberseguridad.txt", "ciberseguridad.pptx")

### Convertir LaTeX a PowerPoint

print("✅ Presentación creada exitosamente!")

``````python

from scripts.latex_to_pptx import LatexToPptxConverter

### Ejemplo 2: Usar múltiples temas

converter = LatexToPptxConverter()

```pythonconverter.convert("presentation.tex", "presentation.pptx")

from scripts.text_to_pptx import TextToPptxConverter```



temas = ["modern_blue", "dark", "professional", "vibrant"]## 📚 Ejemplos

contenido = "mi_contenido.txt"

El directorio `examples/` contiene:

for tema in temas:- `presentation.tex`: Ejemplo de presentación en LaTeX Beamer

    converter = TextToPptxConverter(theme=tema)- Archivos generados por los scripts de conversión

    converter.convert(contenido, f"presentacion_{tema}.pptx")

    print(f"✅ Creada presentación con tema: {tema}")## 🛠️ Tecnologías

```

- **Python 3.7+**

### Ejemplo 3: Convertir documento académico- **python-pptx**: Creación de archivos PowerPoint

- **anthropic**: API de Claude AI

```python- **python-dotenv**: Gestión de variables de entorno

from scripts.latex_to_pptx import LatexToPptxConverter

## 📝 Formato de Entrada

converter = LatexToPptxConverter()

### Formato de Texto

# Desde archivo LaTeX Beamer```

converter.convert("tesis_presentacion.tex", "tesis.pptx")# Título Principal

Subtítulo

# Desde PDF----

converter.convert("paper.pdf", "paper_slides.pptx")# Diapositiva 2

```- Punto 1

- Punto 2

## 📁 Archivos de Ejemplo----

# Conclusión

El directorio `examples/` contiene:Texto final

- **presentation.tex** - Plantilla de presentación LaTeX Beamer```

- Ejemplos de formato de texto estructurado

### LaTeX Beamer

## ❓ Preguntas Frecuentes (FAQ)```latex

\begin{frame}{Título}

**P: ¿Necesito pagar por usar el proyecto?**    \begin{itemize}

R: No, puedes usar Google Gemini que es completamente gratuito. Claude AI requiere créditos.        \item Punto 1

        \item Punto 2

**P: ¿Qué API es mejor, Gemini o Claude?**    \end{itemize}

R: Ambas funcionan bien. Gemini es gratis y genera buen contenido. Claude puede ser más detallado pero requiere pago.\end{frame}

```

**P: ¿Puedo cambiar los colores de los temas?**

R: Sí, puedes modificar los temas en `scripts/text_to_pptx.py` en el método `_get_theme_colors()`.## 🤝 Contribuciones



**P: ¿Funciona en Linux/Mac?**Las contribuciones son bienvenidas. Por favor:

R: Sí, el proyecto es multiplataforma. Solo asegúrate de instalar poppler-utils para conversión PDF.1. Fork el proyecto

2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)

**P: ¿Puedo usar mis propias plantillas de PowerPoint?**3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)

R: Actualmente el proyecto genera presentaciones desde cero. Puedes modificar el código para usar plantillas existentes.4. Push a la rama (`git push origin feature/AmazingFeature`)

5. Abre un Pull Request

## 🛠️ Troubleshooting

## 📄 Licencia

### Error: "No se encontró ninguna API key"

**Solución:** Asegúrate de crear el archivo `.env` con `GEMINI_API_KEY` o `ANTHROPIC_API_KEY`.Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.



### Error al convertir PDF## 👤 Autor

**Solución:** Instala poppler-utils:

- Windows: Descarga desde [poppler releases](https://github.com/oschwartz10612/poppler-windows/releases)**Salvador0302**

- Linux: `sudo apt-get install poppler-utils`

- Mac: `brew install poppler`## 🙏 Agradecimientos



### Error: "Module 'customtkinter' not found"- Claude AI de Anthropic por la generación de contenido

**Solución:** Ejecuta `pip install -r requirements.txt` para instalar todas las dependencias.- python-pptx por la manipulación de PowerPoint

- La comunidad de código abierto

### La interfaz no se ve moderna

**Solución:** Asegúrate de tener CustomTkinter >= 5.2.0 instalado.---



## 🤝 Contribuciones⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!


Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregada nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Salvador0302**
- GitHub: [@Salvador0302](https://github.com/Salvador0302)

## 🙏 Agradecimientos

- Google Gemini por proporcionar una API gratuita de IA
- Anthropic Claude AI por la excelente calidad de generación de contenido
- python-pptx por la librería de manipulación de PowerPoint
- CustomTkinter por el framework moderno de interfaces
- La comunidad de código abierto

## 🌟 Características Futuras

- [ ] Más temas de diseño personalizables
- [ ] Soporte para imágenes en las diapositivas
- [ ] Exportar a otros formatos (PDF, HTML)
- [ ] Integración con más proveedores de IA
- [ ] Editor WYSIWYG en la interfaz
- [ ] Plantillas personalizables por el usuario

---

⭐ **Si este proyecto te resulta útil, considera darle una estrella en GitHub!**

📧 **¿Tienes preguntas o sugerencias?** Abre un issue en el repositorio.
