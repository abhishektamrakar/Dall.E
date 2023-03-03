import os
import openai
openai.api_key = '####' # your api key
openai.Model.list()

openai.Image.create(
  prompt="A cute panda trying to cook some noodles in the space photorealistic 4k nikon",
  n=2,
  size="1024x1024"
)
