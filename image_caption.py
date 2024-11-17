import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests
import matplotlib.pyplot as plt
from io import BytesIO

# Step 1: Load the pre-trained model, image processor, and tokenizer
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

# Step 2: Define a function to preprocess images
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    return feature_extractor(images=image, return_tensors="pt").pixel_values

# Step 3: Define a function to generate captions
def generate_caption(image_tensor, max_length=16):
    with torch.no_grad():
        output_ids = model.generate(image_tensor, max_length=max_length, num_beams=4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption

# Step 4: Load and display an image from a local path or URL
def load_image(image_path=None, image_url=None):
    if image_path:
        image = Image.open(image_path).convert("RGB")
    elif image_url:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        raise ValueError("Provide either an image path or an image URL.")
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    return image

# Step 5: Run the entire pipeline
def main(image_path=None, image_url=None):
    # Load and display the image
    image = load_image(image_path=image_path, image_url=image_url)

    # Preprocess the image
    image_tensor = feature_extractor(images=image, return_tensors="pt").pixel_values

    # Generate and print the caption
    caption = generate_caption(image_tensor)
    print("Generated Caption:", caption)

# Replace 'path/to/your/image.jpg' with your actual image path or provide an image URL.
main(image_path=r"C:\\Users\\AISHWARYA\\OneDrive\\Pictures\\Saved Pictures\\blackbag.jpg") # For local image
