from copy import deepcopy
import uuid

payload_template = {
  "input": {
    "workflow": {
      "251": {
        "inputs": {
          "ckpt_name": "2dn_Pony.safetensors"
        },
        "class_type": "CheckpointLoaderSimple"
      },
      "252": {
        "inputs": {
          "vae_name": "sdxl_vae.safetensors"
        },
        "class_type": "VAELoader"
      },
      "253": {
        "inputs": {
          "width": [
            "1116",
            0
          ],
          "height": [
            "1116",
            1
          ],
          "crop_w": 0,
          "crop_h": 0,
          "target_width": [
            "1116",
            0
          ],
          "target_height": [
            "1116",
            1
          ],
          "text_g": [
            "1106",
            0
          ],
          "text_l": [
            "1106",
            0
          ],
          "clip": [
            "545",
            1
          ]
        },
        "class_type": "CLIPTextEncodeSDXL"
      },
      "255": {
        "inputs": {
          "width": [
            "1116",
            0
          ],
          "height": [
            "1116",
            1
          ],
          "batch_size": [
            "1109",
            0
          ]
        },
        "class_type": "EmptyLatentImage"
      },
      "262": {
        "inputs": {
          "width": [
            "1116",
            0
          ],
          "height": [
            "1116",
            1
          ],
          "crop_w": 0,
          "crop_h": 0,
          "target_width": [
            "1116",
            0
          ],
          "target_height": [
            "1116",
            1
          ],
          "text_g": [
            "1110",
            0
          ],
          "text_l": [
            "1110",
            0
          ],
          "clip": [
            "545",
            1
          ]
        },
        "class_type": "CLIPTextEncodeSDXL"
      },
      "263": {
        "inputs": {
          "lora_name": "Organic_Sauce_epoch_13.safetensors",
          "strength_model": 0.6,
          "strength_clip": 0.6,
          "model": [
            "251",
            0
          ],
          "clip": [
            "251",
            1
          ]
        },
        "class_type": "LoraLoader"
      },
      "265": {
        "inputs": {
          "samples": [
            "955",
            0
          ],
          "vae": [
            "252",
            0
          ]
        },
        "class_type": "VAEDecode"
      },
      "272": {
        "inputs": {
          "clip_name": "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"
        },
        "class_type": "CLIPVisionLoader"
      },
      "419": {
        "inputs": {
          "model_name": "RealESRGAN_x2.pth"
        },
        "class_type": "UpscaleModelLoader"
      },
      "420": {
        "inputs": {
          "upscale_model": [
            "419",
            0
          ]
        },
        "class_type": "ImageUpscaleWithModel"
      },
      "424": {
        "inputs": {
          "pixels": [
            "1232",
            0
          ],
          "vae": [
            "252",
            0
          ]
        },
        "class_type": "VAEEncode"
      },
      "501": {
        "inputs": {
          "control_net_name": "SDXL/instantid/diffusion_pytorch_model.safetensors"
        },
        "class_type": "ControlNetLoader"
      },
      "512": {
        "inputs": {
          "text": [
            "1110",
            0
          ],
          "clip": [
            "263",
            1
          ]
        },
        "class_type": "CLIPTextEncode"
      },
      "545": {
        "inputs": {
          "lora_name": "tracksuit_guys_v4.safetensors",
          "strength_model": 0.75,
          "strength_clip": 0.75,
          "model": [
            "263",
            0
          ],
          "clip": [
            "263",
            1
          ]
        },
        "class_type": "LoraLoader"
      },
      "611": {
        "inputs": {
          "ipadapter_file": "ip-adapter-plus_sdxl_vit-h.safetensors"
        },
        "class_type": "IPAdapterModelLoader"
      },
      "616": {
        "inputs": {
          "samples": [
            "1255",
            0
          ],
          "vae": [
            "252",
            0
          ]
        },
        "class_type": "VAEDecode"
      },
      "791": {
        "inputs": {
          "weight": 0.2,
          "weight_type": "linear",
          "combine_embeds": "concat",
          "start_at": 0,
          "end_at": 0.8,
          "embeds_scaling": "V only",
          "model": [
            "545",
            0
          ],
          "ipadapter": [
            "611",
            0
          ],
          "image": [
            "1251",
            0
          ],
          "clip_vision": [
            "272",
            0
          ]
        },
        "class_type": "IPAdapterAdvanced"
      },
      "947": {
        "inputs": {
          "lora_name": "tracksuit_guys_v4.safetensors",
          "strength_model": 0.9,
          "strength_clip": 0.9,
          "model": [
            "263",
            0
          ],
          "clip": [
            "263",
            1
          ]
        },
        "class_type": "LoraLoader"
      },
      "955": {
        "inputs": {
          "add_noise": "enable",
          "noise_seed": 256,
          "steps": 25,
          "cfg": 4,
          "sampler_name": "dpmpp_2m",
          "scheduler": "karras",
          "start_at_step": 0,
          "end_at_step": 10000,
          "return_with_leftover_noise": "disable",
          "model": [
            "1221",
            0
          ],
          "positive": [
            "1221",
            1
          ],
          "negative": [
            "1221",
            2
          ],
          "latent_image": [
            "255",
            0
          ]
        },
        "class_type": "KSamplerAdvanced"
      },
      "1106": {
        "inputs": {
          "Text": "trk style, 1boy, (low-poly:1.2),painting, male focus, solo, black background, {JACKET_COLOR} jacket, ({DESCRIPTION}:1.2), (low contrast:1.2), (angry face, intense gaze:{AGRESSION}) rough man, simple background, (((soft light))), looking at viewer, upper body"
        },
        "class_type": "DF_Text_Box"
      },
      "1109": {
        "inputs": {
          "Value": 1
        },
        "class_type": "DF_Integer"
      },
      "1110": {
        "inputs": {
          "Text": "score_5, score_4, hood, low quality, (long neck:1.2), (( high contrast)), (( deep shadows)),  (((blushing))), ((red cheeks)), ((makeup)), chin dimple, (tattoos:1.2), ((red lips)), ((happy)), ((smile)), ((sad)), fat, (long neck:1.1), muscular, large body,((beautiful)), (red colors:1.2), red theme, red skin, old, (lazy eye), close-up, censored, watermark,"
        },
        "class_type": "DF_Text_Box"
      },
      "1114": {
        "inputs": {
          "upscale_by": 0.68,
          "upscale_method": "bicubic",
          "crop": "disabled",
          "image": [
            "420",
            0
          ]
        },
        "class_type": "DF_Image_scale_by_ratio"
      },
      "1116": {
        "inputs": {
          "width": 1024,
          "height": 1024,
          "aspect_ratio": "1:1 square 1024x1024",
          "swap_dimensions": "Off",
          "upscale_factor": 1,
          "batch_size": 1
        },
        "class_type": "CR SDXL Aspect Ratio"
      },
      "1117": {
        "inputs": {
          "weight": 0.7000000000000001,
          "weight_type": "linear",
          "combine_embeds": "concat",
          "start_at": 0,
          "end_at": 0.8,
          "embeds_scaling": "V only",
          "model": [
            "947",
            0
          ],
          "ipadapter": [
            "611",
            0
          ],
          "image": [
            "1251",
            0
          ],
          "clip_vision": [
            "272",
            0
          ]
        },
        "class_type": "IPAdapterAdvanced"
      },
      "1209": {
        "inputs": {
          "instantid_file": "SDXL/ip-adapter.bin"
        },
        "class_type": "InstantIDModelLoader"
      },
      "1210": {
        "inputs": {
          "control_net_name": "SDXL/instantid/diffusion_pytorch_model.safetensors"
        },
        "class_type": "ControlNetLoader"
      },
      "1211": {
        "inputs": {
          "provider": "CPU"
        },
        "class_type": "InstantIDFaceAnalysis"
      },
      "1221": {
        "inputs": {
          "ip_weight": 0.6,
          "cn_strength": 0.9,
          "start_at": 0,
          "end_at": 1,
          "noise": 0.7000000000000001,
          "combine_embeds": "average",
          "instantid": [
            "1209",
            0
          ],
          "insightface": [
            "1211",
            0
          ],
          "control_net": [
            "1210",
            0
          ],
          "image": [
            "1250",
            0
          ],
          "model": [
            "791",
            0
          ],
          "positive": [
            "253",
            0
          ],
          "negative": [
            "262",
            0
          ],
          "image_kps": [
            "1252",
            0
          ]
        },
        "class_type": "ApplyInstantIDAdvanced"
      },
      "1223": {
        "inputs": {
          "ip_weight": 0.7000000000000001,
          "cn_strength": 1,
          "start_at": 0,
          "end_at": 1,
          "noise": 0.9,
          "combine_embeds": "average",
          "instantid": [
            "1209",
            0
          ],
          "insightface": [
            "1211",
            0
          ],
          "control_net": [
            "1210",
            0
          ],
          "image": [
            "1232",
            0
          ],
          "model": [
            "1117",
            0
          ],
          "positive": [
            "262",
            0
          ],
          "negative": [
            "262",
            0
          ]
        },
        "class_type": "ApplyInstantIDAdvanced"
      },
      "1230": {
        "inputs": {
          "color": "{HEX_COLOR}",
          "width": 1400,
          "height": 1400,
          "invert": False,
          "mask_opacity": 1,
          "foreground_image": [
            "1231",
            0
          ],
          "foreground_mask": [
            "1236",
            0
          ]
        },
        "class_type": "Colored Image (mtb)"
      },
      "1231": {
        "inputs": {
          "transparency": True,
          "model": "u2net",
          "post_processing": False,
          "only_mask": False,
          "alpha_matting": False,
          "alpha_matting_foreground_threshold": 240,
          "alpha_matting_background_threshold": 10,
          "alpha_matting_erode_size": 10,
          "background_color": "none",
          "images": [
            "1246",
            0
          ]
        },
        "class_type": "Image Rembg (Remove Background)"
      },
      "1232": {
        "inputs": {
          "temperature": 10,
          "hue": 0,
          "brightness": 5,
          "contrast": -30,
          "saturation": -15,
          "gamma": 1,
          "image": [
            "265",
            0
          ]
        },
        "class_type": "ColorCorrect"
      },
      "1236": {
        "inputs": {
          "channel": "alpha",
          "image": [
            "1231",
            0
          ]
        },
        "class_type": "ImageToMask"
      },
      "1241": {
        "inputs": {
          "strength": 0.5,
          "start_percent": 0,
          "end_percent": 0.8,
          "positive": [
            "1223",
            1
          ],
          "negative": [
            "1223",
            2
          ],
          "control_net": [
            "1242",
            0
          ],
          "image": [
            "1232",
            0
          ]
        },
        "class_type": "ControlNetApplyAdvanced"
      },
      "1242": {
        "inputs": {
          "control_net_name": "SDXL/instantid/diffusion_pytorch_model.safetensors"
        },
        "class_type": "ControlNetLoader"
      },
      "1246": {
        "inputs": {
          "temperature": -5,
          "hue": 0,
          "brightness": 0,
          "contrast": -5,
          "saturation": 0,
          "gamma": 1,
          "image": [
            "616",
            0
          ]
        },
        "class_type": "ColorCorrect"
      },
      "1250": {
        "inputs": {
          "url_or_path": "https://r2r-comfyui.s3.amazonaws.com/users/771434c2-e2a1-47a2-bc3e-ebf9701a57c0.jpg"
        },
        "class_type": "LoadImageFromUrlOrPath"
      },
      "1251": {
        "inputs": {
          "url_or_path": "https://r2r-comfyui.s3.amazonaws.com/assets/ipAdapter.png"
        },
        "class_type": "LoadImageFromUrlOrPath"
      },
      "1252": {
        "inputs": {
          "url_or_path": "https://r2r-comfyui.s3.amazonaws.com/assets/keyPointImage.png"
        },
        "class_type": "LoadImageFromUrlOrPath"
      },
      "1254": {
        "inputs": {
          "filename_prefix": "final",
          "images": [
            "1230", # or this could be 1231 if transparent
            0
          ]
        },
        "class_type": "SaveImage"
      },
      "1255": {
        "inputs": {
          "add_noise": "enable",
          "noise_seed": 44,
          "steps": 30,
          "cfg": 4,
          "sampler_name": "dpmpp_2m",
          "scheduler": "karras",
          "start_at_step": 20,
          "end_at_step": 10000,
          "return_with_leftover_noise": "disable",
          "model": [
            "1223",
            0
          ],
          "positive": [
            "1241",
            0
          ],
          "negative": [
            "1241",
            1
          ],
          "latent_image": [
            "424",
            0
          ]
        },
        "class_type": "KSamplerAdvanced"
      }
    }
  }
}

def generate_payload(image_url, description, jacket_color, background_color, agression, strength):
    # Create a copy of the template to avoid modifying the original
    payload = deepcopy(payload_template)

    # Replacing the description with the description of the person
    payload["input"]["workflow"]["1106"]["inputs"]["Text"] = payload["input"]["workflow"]["1106"]["inputs"][
        "Text"
    ].replace("{DESCRIPTION}", f"{strength}, {description}")
    
    # Jacket Color
    payload["input"]["workflow"]["1106"]["inputs"]["Text"] = payload["input"]["workflow"]["1106"]["inputs"][
        "Text"
    ].replace("{JACKET_COLOR}", jacket_color)
    
    payload["input"]["workflow"]["1106"]["inputs"]["Text"] = payload["input"]["workflow"]["1106"]["inputs"][
        "Text"
    ].replace("{AGRESSION}", str(agression))
    
    # Setting bg color
    
    print(background_color)
    
    if (background_color == 'transparent'):
      payload["input"]["workflow"]["1254"]["inputs"]["images"] = ["1231", 0]
    else:
      payload["input"]["workflow"]["1230"]["inputs"]["color"] = background_color

    payload["input"]["workflow"]["1250"]["inputs"]["url_or_path"] = image_url

    return payload
