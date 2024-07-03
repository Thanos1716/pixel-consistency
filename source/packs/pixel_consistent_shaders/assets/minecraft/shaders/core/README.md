# Shaders
## Enchantment Glint Shaders

There are a number of core shaders that control the enchantment glint on various entities and items.
These shaders go by the following names (with .fsh, .vsh and .json extensions), and as of 1.21 do the listed things:

- `rendertype_armor_entity_glint`: armor_outer, armor_inner and elytra entity models
- `rendertype_armor_glint`: likely unused
- `rendertype_entity_glint_direct`: trident entity model
- `rendertype_entity_glint`: likely unused
- `rendertype_glint_direct`: was previously used for most gui items, but now seems unused
- `rendertype_glint_translucent`: likely unused
- `rendertype_glint`

The `likely unused` shaders are set to render at 10 times the normal brightness, in order to make spotting a use case for them more likely. If you see an oddly bright enchantment glint, please report it to the GitHub or Discord, thanks :)

The `pixelate` function simply applies a pixelation filter by rounding the coordinates of the fragment to the nearest multiple of the scale.

The `transformPixelate` function simply applies a matrix transformation before pixelating the fragment, given an inverted matrix it's used to make the pixels line up with the texture.

The `textureSize` function is used to get the size of the texture atlas that the shader is being applied to, allowing to pixelate consistently when the texture atlas changes size.

Presently there is a variable in each of the used fragment shaders called `textureGlintRatio`. It is currently hard coded to be the ratio between the most likely size of the base texture and the size of the enchantment glint texture. This can be wrong, for example in the case of `rendertype_armor_entity_glint`, the elytra texture is much smaller than the armor overlay textures. Resizing the elytra texture would be infeasible due to the cape textures from Mojang being of a specific size, and shrinking the armor textures would be effectively impossible, due to the number of differently shaped mobs (especially the Giant). Unfortunately this means that armor layers are favored and the elytra cannot have a pixel consistent enchantment glint unless I can find a way to not hard-code textureGlintRatio.
If *anyone* knows a way to pass the sizes of these textures into the shader, please let me know :D

At some point reused functions should probably be extracted into an `include` shader.