import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class ImageGenerator:
    def __init__(self):
        # Carregar o modelo Stable Diffusion em precisão de ponto flutuante 16
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
        )
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = self.pipe.to(device)


    def generate_image(self, prompt, num_inference_steps=50):
        # Gerar a imagem
        with torch.no_grad():
            image = self.pipe(prompt, num_inference_steps=num_inference_steps).images[0]
        return image

    def save_image(self, image, filename="imagem_gerada.png"):
        # Salvar a imagem gerada
        image.save(filename)

    def show_image(self, filename="imagem_gerada.png"):
        # Exibir a imagem gerada
        img = Image.open(filename)
        img.show()

    def process_image(self, prompt):
        # Processar a imagem com base no prompt
        generated_image = self.generate_image(prompt)
        self.save_image(generated_image)
        self.show_image()
