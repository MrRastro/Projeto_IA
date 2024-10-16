import PIL.Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from googletrans import Translator

class ImageDescriber:
    def __init__(self):
        # Carregar o processador e o modelo
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.translator = Translator()

    def load_image(self, image_path):
        # Carregar a imagem
        return PIL.Image.open(image_path)

    def generate_description(self, img):
        # Preparar a imagem
        inputs = self.processor(images=img, return_tensors="pt")

        # Gerar a descrição
        out = self.model.generate(**inputs, max_length=50)
        description = self.processor.decode(out[0], skip_special_tokens=True)
        return description

    def translate_description(self, description):
        # Traduzir para o português
        return self.translator.translate(description, dest='pt').text

    def process_image(self, image_path):
        # Processar a imagem para gerar e traduzir a descrição
        img = self.load_image(image_path)
        description = self.generate_description(img)
        translated_description = self.translate_description(description)
        return translated_description
