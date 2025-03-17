import os
from moviepy.editor import ImageSequenceClip, VideoFileClip, concatenate_videoclips, AudioFileClip
from PIL import Image

def redimensionar_imagen(imagen, tamaño=(854, 480)):
    try:
        img = Image.open(imagen)
        if img.size != tamaño:
            base, ext = os.path.splitext(imagen)
            nuevo_path = f"{base}_resized{ext}"
            img = img.resize(tamaño)
            img.save(nuevo_path)
            return nuevo_path
        return imagen
    except Exception as e:
        print(f"Error al procesar {imagen}: {e}")
        return None

def crear_video(imagen, audio_origen, nombre_video):
    imagen_redimensionada = redimensionar_imagen(imagen)
    if not imagen_redimensionada:
        print("No se pudo procesar la imagen.")
        return None

    try:
        audio = AudioFileClip(audio_origen)
        clip = ImageSequenceClip([imagen_redimensionada], fps=1).set_duration(audio.duration)
        clip = clip.set_audio(audio)

        clip.write_videofile(nombre_video, fps=3, codec="libx264", audio_codec="aac")
        print(f"Video '{nombre_video}' creado con audio.")

        clip.close()
        audio.close()
        return nombre_video
    except Exception as e:
        print(f"Error al crear el video: {e}")
        return None

def unir_videos(lista_videos, video_final="video_completo.mp4"):
    try:
        clips = [VideoFileClip(video) for video in lista_videos]
        video_unido = concatenate_videoclips(clips, method="compose")
        video_unido.write_videofile(video_final, codec="libx264", audio_codec="aac")
        print(f"Video final '{video_final}' creado exitosamente.")

        for clip in clips:
            clip.close()
    except Exception as e:
        print(f"Error al unir los videos: {e}")

direccion = "C:/Users/Usuario/Pictures/Screenshots/MenfiTarea/"
num_videos = 6
extension_imagen = "jpeg"
extension_audio = "mp3"

videos_generados = []

for i in range(1, num_videos + 1):
    imagen = os.path.join(direccion, f"tarea{i}.{extension_imagen}")
    audio = os.path.join(direccion, f"audio{i}.{extension_audio}")
    nombre_video = os.path.join(direccion, f"video{i}.mp4")
    video_generado = crear_video(imagen, audio, nombre_video)
    if video_generado:
        videos_generados.append(video_generado)

if videos_generados:
    unir_videos(videos_generados, os.path.join(direccion, "video_final.mp4")) 
