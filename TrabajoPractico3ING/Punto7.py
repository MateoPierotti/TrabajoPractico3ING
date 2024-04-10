# Interfaz para la creación de elementos multimedia
class MultimediaFactory:
    def create_image(self):
        pass
    
    def create_video(self):
        pass
    
    def create_audio(self):
        pass

# Clases concretas de fábricas
class JpegFactory(MultimediaFactory):
    def create_image(self):
        return JpegImage()
    
    def create_video(self):
        return JpegVideo()
    
    def create_audio(self):
        return JpegAudio()

class PngFactory(MultimediaFactory):
    def create_image(self):
        return PngImage()
    
    def create_video(self):
        return PngVideo()
    
    def create_audio(self):
        return PngAudio()

# Interfaz para elementos multimedia
class Image:
    def display(self):
        pass

class Video:
    def play(self):
        pass

class Audio:
    def play(self):
        pass

# Implementaciones concretas de elementos multimedia
class JpegImage(Image):
    def display(self):
        print("Displaying JPEG image")

class PngImage(Image):
    def display(self):
        print("Displaying PNG image")

class JpegVideo(Video):
    def play(self):
        print("Playing JPEG video")

class PngVideo(Video):
    def play(self):
        print("Playing PNG video")

class JpegAudio(Audio):
    def play(self):
        print("Playing JPEG audio")

class PngAudio(Audio):
    def play(self):
        print("Playing PNG audio")

# Ejemplo de uso
if __name__ == "__main__":
    factory = JpegFactory()  # Selecciona la fábrica de JPEG

    # Crear elementos multimedia
    # jpeg_image = factory.create_image()
    jpeg_video = factory.create_video()
    # jpeg_audio = factory.create_audio()

    # Utilizar los elementos multimedia
    # jpeg_image.display()
    jpeg_video.play()
    # jpeg_audio.play()

