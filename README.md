# diffusion-animation

This script helps you generate a timelapse showing the progress Stable Diffusion makes from step to step.

## prerequisites

 * Python 3
 * [My diffusers fork](https://github.com/ayan4m1/diffusers)
 * [Stable Diffusion v1.4 Model](https://huggingface.co/CompVis/stable-diffusion-v1-4)
 * Conda `ldm` environment from [Stable Diffusion install guide](https://github.com/CompVis/stable-diffusion#requirements)

 To install my diffusers fork, clone it, then run `python setup.py install` inside the clone directory.

## usage

Ensure the SD model is in the parent directory to this script, i.e. `../stable-diffusion-v1-4/` should exist from the directory you run the script in. For example:

```
Desktop/
├─ diffusion-animation/
│  ├─ animate.py
├─ stable-diffusion-v1-4/
│  ├─ model_info.json
│  ├─ ...
```

Execute

> python animate.py "<prompt>" <seed> <steps> <filename>

The script will place files named `text-{x}.png` in the `./output` directory, where `{x}` is the step number associated with the image.

Until video output is working, please use an image-to-video stitching utility to make timelapse videos.

## roadmap

 * video/gif output
