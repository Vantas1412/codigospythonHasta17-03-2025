from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch

# Cargar el modelo preentrenado de Microsoft
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Función para predecir el texto LaTeX desde una imagen
def image_to_latex(image_path):
    image = Image.open(image_path).convert("RGB")  # Cargar imagen
    pixel_values = processor(images=image, return_tensors="pt").pixel_values  # Preprocesar

    with torch.no_grad():
        generated_ids = model.generate(pixel_values)  # Generar predicción

    predicted_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return predicted_text

# 📌 Ejemplo: Pasa una imagen con una fórmula matemática
image_path = "C:/recuperar/imagenes/formula.pngs"  # Reemplaza con la ruta de tu imagen
latex_code = image_to_latex(image_path)

print("Fórmula en LaTeX:", latex_code)
