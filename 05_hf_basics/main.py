from transformers import pipeline

pipe = pipeline("image-text-to-text", model="google/gemma-3-4b-it")

image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"
question = "What animal is on the candy?"

pipe(image=[image_url], text=[question])
