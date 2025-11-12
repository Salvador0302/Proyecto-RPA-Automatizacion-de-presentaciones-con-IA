"""
Script de prueba completo para el proyecto RPA
Prueba la integración con Gemini, generación de contenido y conversión a PPTX
"""
import os
import sys

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from claude.claude_integration import ClaudeIntegration
from scripts.text_to_pptx import TextToPptxConverter
from scripts.latex_to_pptx import LatexToPptxConverter


def test_claude_api():
    """Prueba 1: Conexión con Claude API"""
    print("\n" + "="*60)
    print("🧪 PRUEBA 1: Verificando conexión con Claude API")
    print("="*60)
    
    try:
        claude = ClaudeIntegration()
        print("✅ API key cargada correctamente")
        print(f"✅ Modelo configurado: {claude.model}")
        return claude
    except ValueError as e:
        print(f"❌ Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None


def test_generate_presentation(claude):
    """Prueba 2: Generar contenido con Claude"""
    print("\n" + "="*60)
    print("🧪 PRUEBA 2: Generando contenido con Claude AI")
    print("="*60)
    
    topic = "Python y Automatización RPA"
    print(f"📝 Tema: {topic}")
    print("⏳ Generando presentación (esto puede tardar unos segundos)...")
    
    try:
        content = claude.generate_presentation_content(
            topic=topic,
            num_slides=5,
            style="professional"
        )
        
        if content:
            print("✅ Contenido generado exitosamente")
            print("\n--- Vista previa (primeros 300 caracteres) ---")
            print(content[:300] + "...")
            
            # Guardar el contenido
            output_file = "examples/test_claude_output.txt"
            claude.save_to_file(content, output_file)
            print(f"✅ Contenido guardado en: {output_file}")
            return content, output_file
        else:
            print("❌ No se pudo generar contenido")
            return None, None
            
    except Exception as e:
        print(f"❌ Error al generar contenido: {e}")
        return None, None


def test_text_to_pptx(text_file):
    """Prueba 3: Convertir texto a PowerPoint"""
    print("\n" + "="*60)
    print("🧪 PRUEBA 3: Convirtiendo texto a PowerPoint")
    print("="*60)
    
    try:
        converter = TextToPptxConverter()
        output_file = "examples/test_output.pptx"
        
        print(f"📄 Archivo de entrada: {text_file}")
        print(f"📊 Archivo de salida: {output_file}")
        print("⏳ Convirtiendo...")
        
        converter.convert(text_file, output_file)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file) / 1024  # KB
            print(f"✅ Presentación creada exitosamente")
            print(f"✅ Tamaño del archivo: {file_size:.2f} KB")
            print(f"✅ Ubicación: {output_file}")
            return True
        else:
            print("❌ El archivo PPTX no se creó")
            return False
            
    except Exception as e:
        print(f"❌ Error en la conversión: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_latex_to_pptx():
    """Prueba 4: Convertir LaTeX a PowerPoint"""
    print("\n" + "="*60)
    print("🧪 PRUEBA 4: Convirtiendo LaTeX a PowerPoint")
    print("="*60)
    
    latex_file = "examples/presentation.tex"
    output_file = "examples/presentation_from_latex.pptx"
    
    if not os.path.exists(latex_file):
        print(f"⚠️  Archivo {latex_file} no encontrado, saltando esta prueba")
        return False
    
    try:
        converter = LatexToPptxConverter()
        print(f"📄 Archivo de entrada: {latex_file}")
        print(f"📊 Archivo de salida: {output_file}")
        print("⏳ Convirtiendo...")
        
        converter.convert(latex_file, output_file)
        
        if os.path.exists(output_file):
            file_size = os.path.getsize(output_file) / 1024  # KB
            print(f"✅ Presentación creada exitosamente")
            print(f"✅ Tamaño del archivo: {file_size:.2f} KB")
            print(f"✅ Ubicación: {output_file}")
            return True
        else:
            print("❌ El archivo PPTX no se creó")
            return False
            
    except Exception as e:
        print(f"❌ Error en la conversión: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Ejecuta todas las pruebas"""
    print("\n" + "🚀"*30)
    print("   INICIANDO PRUEBAS COMPLETAS DEL PROYECTO RPA")
    print("🚀"*30)
    
    results = {
        "API Connection": False,
        "Content Generation": False,
        "Text to PPTX": False,
        "LaTeX to PPTX": False
    }
    
    # Prueba 1: API
    claude = test_claude_api()
    if claude:
        results["API Connection"] = True
        
        # Prueba 2: Generación de contenido
        content, text_file = test_generate_presentation(claude)
        if content and text_file:
            results["Content Generation"] = True
            
            # Prueba 3: Conversión a PPTX
            if test_text_to_pptx(text_file):
                results["Text to PPTX"] = True
    
    # Prueba 4: LaTeX a PPTX
    if test_latex_to_pptx():
        results["LaTeX to PPTX"] = True
    
    # Resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN DE PRUEBAS")
    print("="*60)
    
    for test_name, passed in results.items():
        status = "✅ PASÓ" if passed else "❌ FALLÓ"
        print(f"{status} - {test_name}")
    
    total_passed = sum(results.values())
    total_tests = len(results)
    
    print("\n" + "="*60)
    print(f"🎯 Resultado: {total_passed}/{total_tests} pruebas exitosas")
    print("="*60)
    
    if total_passed == total_tests:
        print("\n🎉 ¡TODAS LAS PRUEBAS PASARON! El proyecto funciona correctamente.")
    else:
        print("\n⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")
    
    print("\n📁 Archivos generados en la carpeta 'examples/':")
    print("   - test_claude_output.txt (contenido generado por Claude)")
    print("   - test_output.pptx (presentación desde texto)")
    print("   - presentation_from_latex.pptx (presentación desde LaTeX)")


if __name__ == "__main__":
    main()
