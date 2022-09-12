import torch
import sys
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
from torch import autocast
from PIL import Image
from pathlib import Path

(_, prompt, raw_seed, raw_steps, out_name) = sys.argv

height = 512
width = 512
seed = int(raw_seed)
steps = int(raw_steps)

device = torch.device('cuda')
lms = LMSDiscreteScheduler(
    beta_start=0.00085,
    beta_end=0.012,
    beta_schedule="scaled_linear"
)
pipe = StableDiffusionPipeline.from_pretrained('../stable-diffusion-v1-4', scheduler=lms, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to(device)
pipe.enable_attention_slicing()

generator = torch.Generator("cuda").manual_seed(seed)

Path('./output/').mkdir(exist_ok=True)

with autocast("cuda"):
    images = pipe(prompt, store_each_step=True, num_inference_steps=steps, generator=generator, height=height, width=width).images

    for i in range(steps):
        images[i][0].save(f'./output/{out_name}-{i+1}.png', 'PNG')
