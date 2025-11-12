# claude/claude_integration.py
"""
Integración con APIs de IA (Google Gemini y Anthropic Claude) para generación de contenido de presentaciones.
Soporta detección automática del proveedor disponible.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class ClaudeIntegration:
    """Clase para interactuar con APIs de IA (Claude o Gemini)"""
    
    def __init__(self, api_key=None, model=None, provider="auto"):
        """
        Inicializa la integración con la API de IA
        
        Args:
            api_key: Clave API (opcional, se busca en variables de entorno)
            model: Modelo a usar (opcional, se usa el predeterminado del proveedor)
            provider: Proveedor de IA ("claude", "gemini", o "auto" para detectar automáticamente)
        """
        self.provider = provider
        self.api_key = None
        self.model = model
        self.client = None
        
        if provider == "auto":
            gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            claude_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
            
            if gemini_key:
                self.provider = "gemini"
                self.api_key = gemini_key
            elif claude_key:
                self.provider = "claude"
                self.api_key = claude_key
            else:
                raise ValueError(
                    "No se encontró ninguna API key. "
                    "Por favor, configura GEMINI_API_KEY o ANTHROPIC_API_KEY en tu archivo .env"
                )
        else:
            if provider == "gemini":
                self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
                if not self.api_key:
                    raise ValueError("No se encontró GEMINI_API_KEY en las variables de entorno")
            elif provider == "claude":
                self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
                if not self.api_key:
                    raise ValueError("No se encontró ANTHROPIC_API_KEY en las variables de entorno")
        
        if self.provider == "gemini":
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.model = model or "gemini-2.5-flash"
            self.client = genai.GenerativeModel(self.model)
            print(f"✅ Usando Google Gemini ({self.model})")
        elif self.provider == "claude":
            from anthropic import Anthropic
            self.client = Anthropic(api_key=self.api_key)
            self.model = model or "claude-3-5-sonnet-20241022"
            print(f"✅ Usando Anthropic Claude ({self.model})")
    
    def generate_presentation_content(self, topic, num_slides=5, style="professional"):
        """
        Genera contenido para una presentación usando la IA configurada
        
        Args:
            topic: Tema de la presentación
            num_slides: Número de diapositivas a generar
            style: Estilo de la presentación
        
        Returns:
            str: Contenido generado en formato de texto estructurado
        """
        prompt = self._create_prompt(topic, num_slides, style)
        
        try:
            if self.provider == "gemini":
                response = self.client.generate_content(prompt)
                content = response.text
            elif self.provider == "claude":
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=4096,
                    messages=[{"role": "user", "content": prompt}]
                )
                content = message.content[0].text
            
            return content
            
        except Exception as e:
            raise Exception(f"Error al generar contenido con {self.provider}: {str(e)}")
    
    def _create_prompt(self, topic, num_slides, style):
        """Crea el prompt para la IA"""
        return f"""Genera el contenido para una presentación sobre "{topic}" con {num_slides} diapositivas.

Estilo: {style}

Formato de salida:
- Cada diapositiva debe empezar con "SLIDE N:" donde N es el número
- Luego el título de la diapositiva
- Seguido de viñetas con el contenido (usando guiones -)
- Deja una línea en blanco entre diapositivas

Ejemplo:
SLIDE 1: Título de la primera diapositiva
- Primera viñeta
- Segunda viñeta
- Tercera viñeta

SLIDE 2: Título de la segunda diapositiva
- Primera viñeta
- Segunda viñeta

Genera contenido relevante, conciso y bien estructurado. Incluye una diapositiva de introducción y una de conclusión.
"""
    
    def save_to_file(self, content, output_file):
        """
        Guarda el contenido generado en un archivo
        
        Args:
            content: Contenido a guardar
            output_file: Ruta del archivo de salida
        """
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            raise Exception(f"Error al guardar el archivo: {str(e)}")


# Funciones legacy para compatibilidad
def ask_claude(prompt, max_tokens=1000):
    """Función legacy - usar ClaudeIntegration en su lugar"""
    api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
    if not api_key:
        raise EnvironmentError("Set ANTHROPIC_API_KEY or CLAUDE_API_KEY env var.")
    
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def prompt_for_presentation(topic, slides=5):
    """
    Prompt que pide a la IA devolver JSON con la estructura de slides.
    """
    return f"""
Genera una presentación sobre "{topic}" con {slides} slides en formato JSON.
Cada slide debe ser un objeto con "title", "bullets" (lista) y opcional "image" (URL).
Devuelve **solo** JSON válido: [{{"title": "...", "bullets": ["..."]}}].
No expliques nada fuera del JSON.
"""


if __name__ == "__main__":
    # Prueba básica
    try:
        ai = ClaudeIntegration(provider="auto")
        print(f"✅ Integración inicializada correctamente")
        print(f"✅ Proveedor: {ai.provider}")
        print(f"✅ Modelo: {ai.model}")
        
        # Generar contenido de ejemplo
        content = ai.generate_presentation_content(
            topic="RPA con Python",
            num_slides=3,
            style="professional"
        )
        print("\n--- Contenido generado ---")
        print(content[:500] + "...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    def generate_presentation_content(self, topic, num_slides=5, style="professional"):
        """
        Genera contenido para una presentación usando Claude
        
        Args:
            topic: Tema de la presentación
            num_slides: Número de diapositivas a generar
            style: Estilo de la presentación (professional, casual, academic, etc.)
        
        Returns:
            str: Contenido generado en formato de texto estructurado
        """
        prompt = self._create_prompt(topic, num_slides, style)
        
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extraer el contenido de la respuesta
            content = message.content[0].text
            return content
            
        except Exception as e:
            raise Exception(f"Error al generar contenido con Claude: {str(e)}")
    
    def _create_prompt(self, topic, num_slides, style):
        """Crea el prompt para Claude"""
        return f"""Genera el contenido para una presentación sobre "{topic}" con {num_slides} diapositivas.

Estilo: {style}

Formato de salida:
- Cada diapositiva debe empezar con "SLIDE N:" donde N es el número
- Luego el título de la diapositiva
- Seguido de viñetas con el contenido (usando guiones -)
- Deja una línea en blanco entre diapositivas

Ejemplo:
SLIDE 1: Título de la primera diapositiva
- Primera viñeta
- Segunda viñeta
- Tercera viñeta

SLIDE 2: Título de la segunda diapositiva
- Primera viñeta
- Segunda viñeta

Genera contenido relevante, conciso y bien estructurado. Incluye una diapositiva de introducción y una de conclusión.
"""
    
    def save_to_file(self, content, output_file):
        """
        Guarda el contenido generado en un archivo
        
        Args:
            content: Contenido a guardar
            output_file: Ruta del archivo de salida
        """
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
        except Exception as e:
            raise Exception(f"Error al guardar el archivo: {str(e)}")


# Funciones legacy para compatibilidad
def ask_claude(prompt, max_tokens=1000):
    """Función legacy - usar ClaudeIntegration en su lugar"""
    api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")
    if not api_key:
        raise EnvironmentError("Set ANTHROPIC_API_KEY or CLAUDE_API_KEY env var.")
    
    client = Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def prompt_for_presentation(topic, slides=5):
    """
    Prompt que pide a Claude devolver JSON con la estructura de slides.
    """
    return f"""
Genera una presentación sobre "{topic}" con {slides} slides en formato JSON.
Cada slide debe ser un objeto con "title", "bullets" (lista) y opcional "image" (URL).
Devuelve **solo** JSON válido: [{{"title": "...", "bullets": ["..."]}}].
No expliques nada fuera del JSON.
"""


if __name__ == "__main__":
    # Prueba básica
    try:
        claude = ClaudeIntegration()
        print(f"✅ Claude Integration inicializado correctamente")
        print(f"✅ Modelo: {claude.model}")
        
        # Generar contenido de ejemplo
        content = claude.generate_presentation_content(
            topic="RPA con Python y Claude",
            num_slides=3,
            style="professional"
        )
        print("\n--- Contenido generado ---")
        print(content[:500] + "...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
