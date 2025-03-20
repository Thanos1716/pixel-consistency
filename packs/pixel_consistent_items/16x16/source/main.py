#!/usr/bin/env python3
import numpy as np
from PIL import Image
import json
import os
import shutil

verbose = True

def load_json(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    return data

def save_json(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def get_data(path):
    img = Image.open(path).convert("RGBA")
    return np.array(img)


sides = [
    "angler_pottery_pattern",
    "archer_pottery_pattern",
    "arms_up_pottery_pattern",
    "blade_pottery_pattern",
    "brewer_pottery_pattern",
    "burn_pottery_pattern",
    "danger_pottery_pattern",
    "decorated_pot_side",
    "explorer_pottery_pattern",
    "friend_pottery_pattern",
    "heart_pottery_pattern",
    "heartbreak_pottery_pattern",
    "howl_pottery_pattern",
    "miner_pottery_pattern",
    "mourner_pottery_pattern",
    "plenty_pottery_pattern",
    "prize_pottery_pattern",
    "sheaf_pottery_pattern",
    "shelter_pottery_pattern",
    "skull_pottery_pattern",
    "snort_pottery_pattern"]

for left_side in sides:
    for right_side in sides:

        model_data = {
            "parent": "item/generated",
            "textures": {
                "layer0": "item/decorated_pot/decorated_pot_base",
                "layer1": f"item/decorated_pot/left/{left_side}",
                "layer2": f"item/decorated_pot/right/{right_side}"
            }
        }

        left_sherd = "_".join(left_side.split("_")[:-1]) + "_sherd"
        right_sherd = "_".join(right_side.split("_")[:-1]) + "_sherd"

        if left_side == "decorated_pot_side": left_sherd = "brick"
        if right_side == "decorated_pot_side": right_sherd = "brick"

        partial_model_dir_path = f"item/decorated_pot/{left_side}"
        partial_model_file_path = f"{partial_model_dir_path}/{right_side}"
        model_dir_path = f"assets/minecraft/models/{partial_model_dir_path}"
        model_file_path = f"{model_dir_path}/{right_side}"

        try:
            os.makedirs(f"../{model_dir_path}")
        except FileExistsError:
            pass

        save_json(f"../{model_file_path}.json", model_data)

        verbose and print(f"Created model {model_file_path}.json")

        cit_dir_path = f"assets/minecraft/optifine/cit/decorated_pot/{left_side}"
        cit_file_path = f"{cit_dir_path}/{right_side}"

        try:
            os.makedirs(f"../{cit_dir_path}")
        except FileExistsError:
            pass

        with open(f"../{cit_file_path}.properties", 'w') as f:

                f.write(
f"""type=item
matchItems=decorated_pot
model={partial_model_file_path}
nbt.BlockEntityTag.sherds.1=minecraft:{left_sherd}
nbt.BlockEntityTag.sherds.3=minecraft:{right_sherd}
"""
)

        verbose and print(f"Created CIT {cit_file_path}.properties")
