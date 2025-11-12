# 🎯 Proyecto RPA - Automatización de Presentaciones con IA

Sistema automatizado de generación de presentaciones PowerPoint profesionales utilizando Inteligencia Artificial. Soporta Google Gemini (gratuito) y Anthropic Claude, con conversión de LaTeX/PDF y múltiples temas de diseño.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Características Principales

- 🤖 **Generación automática con IA** - Google Gemini (gratis) o Claude AI
- 🎨 **4 Temas profesionales** - Modern Blue, Dark, Professional, Vibrant
- 🖥️ **Interfaz gráfica** - CustomTkinter con tema oscuro y tabs organizadas
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
├─ .env.example               # 📄 Plantilla de configuración
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

Ejecuta la aplicación:

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
- GitHub: [@Salvador0302](https://github.com/Salvador0302)

## 🙏 Agradecimientos

Agradecimiento especial al **Profesor Kelvin (Alexander) Aquino Ynga** por su guía y enseñanzas en el desarrollo de este proyecto. Su apoyo fue fundamental para convertir esta idea en realidad.

- Google Gemini por proporcionar una API gratuita de IA
- Anthropic Claude AI por la excelente calidad de generación de contenido
- python-pptx por la librería de manipulación de PowerPoint
- CustomTkinter por el framework moderno de interfaces
- La comunidad de código abierto

---

⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!
