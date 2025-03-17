import os
from moviepy.editor import ImageSequenceClip, VideoFileClip
from PIL import Image

def redimensionar_imagenes(imagenes, tamaño=(854, 480)):
    imagenes_redimensionadas = []
    for img_path in imagenes:
        try:
            img = Image.open(img_path)
            if img.size != tamaño:  
                img = img.resize(tamaño)
                nuevo_path = img_path.replace(".", "_resized.")
                img.save(nuevo_path)
                imagenes_redimensionadas.append(nuevo_path)
            else:
                imagenes_redimensionadas.append(img_path)
        except Exception as e:
            print(f"Error al procesar {img_path}: {e}")
    return imagenes_redimensionadas

def crear_video(imagenes, nombre_video="presentacion.mp4", audio_origen="audio.mp4"):
    imagenes_redimensionadas = redimensionar_imagenes(imagenes)

    if not imagenes_redimensionadas:
        print("No se pudieron procesar imágenes.")
        return

    try:
        audio = VideoFileClip(audio_origen).audio
        duracion_total = audio.duration
        duracion_por_imagen = duracion_total / len(imagenes)

        clip = ImageSequenceClip(imagenes_redimensionadas, durations=[duracion_por_imagen] * len(imagenes))
        clip = clip.set_audio(audio)

        clip.write_videofile(nombre_video, fps=5, codec="libx264", audio_codec="aac")
        print(f" Video '{nombre_video}' creado con audio.")

    except Exception as e:
        print(f"Error al crear el video: {e}")

direccion = "C:/Users/Usuario/Pictures/Screenshots/MenfiTarea/"
formato = "pagina"
extension = "png"

imagenes = [os.path.join(direccion, f"{formato}{i}.{extension}") for i in range(1, 6)]

crear_video(imagenes, audio_origen=os.path.join(direccion, "Audio.mp4"))
