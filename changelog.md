# Pixel Consistency Changelog

## Pixel Consistency b0.7 WIP

### Coming Additions
- Entities
  - Horse (all variants)
  - [TODO: legs/anims] Baby Horse (all variants)
  - Horse Armor (all variants)
  - [TODO] Baby Horse Armor (all variants)
  - [TODO] Switch to ETF/EMF folders
  - [TODO] Cat
  - [TODO] Baby Cat
  - [TODO] Cat Collar
  - [TODO] Baby Cat Collar
  - [TODO] Spawner humanoid armor textures
  - [TODO] Separate fitted armor models
  - [TODO] Rename skins to textures
  - [TODO] Pixel consistent dragon egg is now in vanilla (24w33a)
  - [TODO] Make new tab textures in assets/minecraft/textures/gui/sprites/widget/ consistent
  - [TODO] Switch to Seamless? https://modrinth.com/mod/seamless

- Font
  - Unicode Basic Multilingual Plane
    - Pages 00-05
      - BASIC_LATIN
      - LATIN_1_SUPPLEMENT
      - LATIN_EXTENDED_A
      - LATIN_EXTENDED_B
      - IPA_EXTENSIONS
      - SPACING_MODIFIER_LETTERS
      - COMBINING_DIACRITICAL_MARKS
      - GREEK
      - CYRILLIC
      - CYRILLIC_SUPPLEMENTARY
      - ARMENIAN
      - HEBREW
    - Pages 1D and 1F
      - PHONETIC_EXTENSIONS
      - PHONETIC_EXTENSIONS_SUPPLEMENT
      - COMBINING_DIACRITICAL_MARKS_SUPPLEMENT
    - Pages 25-28
      - BOX_DRAWING
      - BLOCK_ELEMENTS
      - GEOMETRIC_SHAPES
      - MISCELLANEOUS_SYMBOLS
      - DINGBATS
      - MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A
      - SUPPLEMENTAL_ARROWS
      - BRAILLE_PATTERNS  
    - Page FF
      - HALFWIDTH_AND_FULLWIDTH_FORMS
      - SPECIALS
- Shaders
  - [TODO] Consistent Enchantment Glint Shader Overlay for below 1.20.5
  - Armor Enchantment Glint (`rendertype_armor_entity_glint`, elytra needs work)
  - Trident Enchantment Glint (`rendertype_entity_glint_direct`)
  - Item Enchantment Glint (`rendertype_glint`)

### Coming Fixes
- Tweak elder guardian and husk scale
- [TODO] Cold baby strider needs to frown harder
- [TODO] Fix wolf and baby wolf head rotations

# Pixel Consistency b0.6.1

b0.6 was missing a `bogged_inner_armor.jem` and a `bogged_outer_armor.jem`, resulting in a broken model for any bogged wearing armor.

This release fixes that in case you want to take on a consistent trial chamber! (more trial chamber consistency in the works)

### Fixes
- Bogged Inner & Outer Armor Layers

## Pixel Consistency b0.6

Celebrating 100 followers of Pixel Consistency! :D

This is a relatively small release, mainly to add support for all 1.20.5-1.21 new textures for supported entities, alongside arrows and a few other things.

Apologies for the delayed update, there are plenty of features in the works, but most are not stable enough for release yet.

### Additions
- Arrow
- Spectral Arrow
- Baby Wolf (all new variants)
- Wolf Armor
- Baby Wolf Armor
- Flow Armor Trim
- Bolt Armor Trim
- Flow Banner Pattern
- Guster Banner Pattern

### Fixes
- Wolf (all variants)
- Wolf Collar (uses new texture)
- Cobweb (new texture to fit block)
- Piglin Brute Outer Armor (now looks correct)
- Resize armor_inner UV (for future armor glint support)
- Remove Broken New World Screen Tab Textures

## Pixel Consistency b0.5

This is a big release, adding support for a lot of blocks, a few interesting entities and most GUI elements, as well as support for some outlines with the [Highlight](https://modrinth.com/mod/highlight) mod

### Additions:
- New Pack Icon
- Highlights:
  - Dragon Head
  - Signs (all variants)
  - Wither Skeleton Skull
- Entities:
  - Baby Wolf
  - Elder Guardian
  - End Crystal
  - Furnace Minecart
  - Mooshrooms (red and brown, due to mushroom)
  - Moobloom (modded)
  - Snow Golem
- Blocks:
  - Blockstates:
    - Big Dripleaf (4 models)
    - Calibrated Sculk Sensor
    - Mangrove Propagule
    - Potted Mangrove Propagule
    - Raised Rails:
      - Activator Rail (4 models)
      - Detector Rail (4 models)
      - Powered Rail (4 models)
      - Rail (2 models)
    - Sea Pickle (4 models)
    - Sunflower
  - Templates:
    - Coral Wall Fan (10 children)
    - Cross (68 children + 1 modded)
    - Flower Pot Cross (28 children)
    - Pointed Dripstone (10 children)
    - Stem Fruit (2 children)
    - Stem Growth (8 models, 2 children each)
    - Template Campfire (2 children)
    - Template Rail Raised (14 children)
    - Tinted Cross (8 children)
    - Tinted Flower Pot Cross (1 child)
- GUI:
  - Container:
    - Anvil (hammer)
    - Smithing Table (hammer)
  - Server List:
    - Join (2 textures)
  - Resource Pack List:
    - Select (2 textures)
    - Unselect (2 textures)
    - Widget (modded, recursive resources)
  - New World Screen:
    - Footer Separator
    - Header Separator
    - Light Dirt Background
    - Tab (2 textures)
    - Tab Selected (2 textures)
  - Options:
    - Options Background
  - World List:
    - Error (2 textures)
    - Join (2 textures)
    - Marked Join (2 textures)
    - Warning (2 textures)
- Particles:
  - Beacon Beam (incomplete)
  - End Gateway Beam (incomplete)

### Fixes:
- Allay (remodel base)
- Giant Armor (2 models, fixed UVs, incomplete)
- Husk (adult)
- Iron Golem (remodel waist)
- Piglin
- Skeleton Skull (separate texture)
- Vex (remodel base)
- Zombie Head (separate texture)
- Zombified Piglin

## Pixel Consistency b0.4.1

Due to changes to the build system, zipping the pack caused an issue

### Fixes:
- Baby:
  - Cow
  - Hoglin
  - Mooshroom
  - Piglin
  - Zoglin
  - Zombified Piglin

## Pixel Consistency b0.4

This release reformats the pack yet again (hopefully for the final time)

### Additions:
- Models:
  - Elder Guardian (no texture yet)
  - Rabbit
  - Baby Rabbit
  - Baby Moobloom (modded)
- Textures:
  - Armor Trims:
    - Dune
    - Eye
    - Host
    - Raiser
    - Rib
    - Sentry
    - Shaper
    - Silence
    - Snout
    - Spire
    - Tide
    - Vex
    - Ward
    - Wayfinder
    - Wild

### Fixes:
- Small Armor Stand (texture)
- Decorated Pot (minimize z-fighting)
- Spider Eyes
- Banner Base (failing to render)
- Baby Cow (horns)
- Baby Mooshroom (horns)

## Pixel Consistency b0.3

This release **requires ETF v5.2.1 and EMF v1.2.3** or up, due to many bug fixes and a couple of new features.
This includes a massive reformatting of the pack, a new [wiki](https://github.com/Thanos1716/pixel-consistency/wiki) and [Discord Server](https://discord.gg/x8n6RmP78V), plus a bunch of additions and fixes!

### Additions:
- Models:
  - Allay
  - Decorated Pot
  - Iron Golem
  - Minecarts:
    - Minecart with Chest
    - Minecart with Command Block (Animatica or MoreMcmeta to animate)
    - Minecart with TNT
  - Spawners:
    - Blaze
    - Cave Spider
    - Magma Cube
    - Silverfish
    - Skeleton
    - Spider
    - Zombie
  - Vex
  - Wandering Trader
- Textures:
  - Coast Armor Trim
  - Ghast (incomplete)
  - Shadow (incomplete)
  - Smithing Table Hammer (incomplete)

### Fixes:
- Baby Goat Horns
- Zoglin's Feet (on opposite sides to adult)
- Adult Axolotl Feet (z-fighting)
- Piglin Head
- Wither Skeleton Skull
- Bat (removed in favor of Mojang's new one)

## Pixel Consistency b0.2

This is a smaller release

### Additions:
- Dragon Head (incomplete)
- Magma Cube (2)
- Witch

### Fixes:
- Armor Trims (textures removed temporarily)
- Magma Cube (1, improved eyes)

## Pixel Consistency b0.1

Initial release for 1.20.X

### Additions:
- Armor Layers (inner and outer models, no trims yet):
  - Armor Stand
  - Drowned
  - Husk
  - Piglin
  - Piglin Brute
  - Pillager (modded)
  - Player (2 models)
  - Skeleton
  - Stray
  - Villager (modded)
  - Wither Skeleton
  - Zombie
  - Zombie Villager
  - Zombified Piglin
  - Baby:
    - Armor Stand
    - Drowned
    - Husk
    - Piglin
    - Villager (modded)
    - Zombie
    - Zombie Villager
    - Baby:
  - Armor Stand
  - Axolotl
  - Bee
  - Camel
  - Chicken
  - Cow
  - Drowned (2 models)
  - Fox
  - Goat
  - Hoglin
  - Husk
  - Llama (2 models)
  - Mooshroom
  - Panda
  - Pig (2 models)
  - Piglin
  - Polar Bear
  - Sheep (2 models)
  - Sniffer
  - Strider (2 models)
  - Trader Llama (2 models)
  - Turtle
  - Villager
  - Zoglin
  - Zombie
  - Zombie Villager
  - Zombified Piglin
- Block Entities:
  - Banner
  - Sign
- Other Entities:
  - Bat
  - Cave Spider
  - Elytra (incomplete)
  - Experience Orb (incomplete)
  - Llama Decor (adult)
  - Magma Cube (1)
  - Pillager
  - Slime (1 & 2)
  - Wither (incomplete)
  - Wither Skeleton
- Blocks:
  - Dragon Egg
  - Tripwire (10 models)
  - Tripwire Hook (4 models)
