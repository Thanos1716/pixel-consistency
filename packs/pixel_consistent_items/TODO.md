
add christmas chest and trapped chest support 
check "texture_size" for models
create unique textures for the 8x8 banner patterns?


remove all particle texture references in models/item? (and any particle specific textures like for fences and fence gates)
run the pack through json cleaners and identify any unknown or useless keys
use "__comment" or "name" to define bone names?

[NOTE]: Neither Minecraft itself nor most other people structure resource packs like this, however this is a guide to how resource packs should be structured, taking into consideration simplicity, logic, size, readability and scriptability.
### Blockstates

Structure of blockstates is `blockstates/<block>.json` (hard coded?)

### Models

Structure of `models/block` is `models/block/<block>/<blockstate>.json`

Note: even if a block only has one blockstate this is still recommended because there is no "default" blockstate unlike predicates.

[TODO]: what about multi model blockstates like redstone idk

Structure of `models/item` is `models/item/<item>.json` (hard coded?)

Non default item models (those that only show up with predicates) should go in `models/item/<item>/<predicate>.json`

[TODO]: custom model data?????

For example the elytra:
- Normal elytra model would go in `models/item/elytra.json`
- Broken elytra model would go in `models/item/elytra/broken.json`

### Textures

[TODO]: structure of `textures/block`

Structure of `textures/item` should mirror the structure of `models/item`, where each `<item>.json` that has texture references becomes a folder with each of the relevant textures that it is the primary model for inside that folder

[TODO]: paletted permutations

For example the elytra:
- Normal elytra texture would go in `textures/item/elytra/layer0.png`
- Broken elytra texture would go in `textures/item/elytra/broken/layer0.png`

Template models that aren't directly used in the game should be in the _templates directory.

Textures from one model can be used by other models they are not primarily for, e.g the bottom texture of `minecraft:crafting_table` uses oak planks. In this case, the texture should go under the primary block and model. 

- Primary models should be considered the default, the first one added, or whatever makes the most sense, for example `minecraft:white_wool` would be the primary wool, and `minecraft:candle` would be the primary candle
  - In the case where there is no primary model, the first model when the sorted alphabetically should be used, for example `minecraft:anlger_pottery_sherd`. 
  - The `minecraft` namespace should always be considered primary if it exists.
- If an item model and a block model use the same texture, as a general rule the texture should be in `textures/block`

## Forge Separate Transforms

Forge & Polytone provide the opportunity for separate models depending on the transform of the item (known as `forge:separate_transforms`).
In this case, a resource pack should be created for each item use case and they should be converted into separate transforms programatically.

The generated pack(s) should be restructured with a `models/item/_transform` directory and a `models/item/_transform_packs` directory.

The models in `models/item/_transform` would not however contain any actual models, but rather only contain a `parent` key to the desired default model in `models/item/_transform_packs`.
This is to allow the easy switching out of certain packs for an end user, by simply overriding which pack the models in `models/item/_transform` reference. These can also be programatically generated.



The `models/item/<item>/<predicate>/<model_name>.json` should be the model to contain the `"loader": "forge:separate_transforms"` key, and its default parent should reference a model 
They will reference a `models/item/_packs/<pack_name>` directory containing each of the resource packs with their associated pack names.
this structure allows
