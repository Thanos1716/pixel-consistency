<center><img src="https://cdn.modrinth.com/data/scjjjdC9/images/0fa9fbdb2b943aa60c3fd15fcbadfe39611cb781.png" alt="Pixel Consistency logo" width="100%"></center>

## About

### What is this?

The goal of this resourcepack is to make all textures in Minecraft have consistently sized pixels in-game.
In my opinion, this significantly improves the look and feel of Minecraft as a whole, and lends itself to a more coherent visual style.

An example of the baby turtle differences is shown below:

<center><img src="https://cdn.modrinth.com/data/scjjjdC9/images/744f221298bd85bffcf4d44e2ef1cbb1265cbcf9.png" alt="Difference between vanilla turtle and consistent turtle" width="100%"></center>

This project is currently in beta development at roughly 40% complete, but the majority of commonly observed inconsistencies have been fixed.

There may be issues, and not all pixel inconsistencies can be, or have been fixed yet.

### How do I get it to work?

This resourcepack is designed to work with [Fabulously Optimized](https://download.fo), an Optifine backwards-compatible Fabric based modpack with better support, more frequent updates, and more open development.

The vast majority of the features in this pack require <strong>client mods</strong>, so whilst a few will work in vanilla, most features will only work if you have one of the following installed:
 - [Fabulously Optimized](https://download.fo) (recommended)
 - [Entity Texture Features](https://modrinth.com/mod/entitytexturefeatures) & [Entity Model Features](https://modrinth.com/mod/entity-model-features) (manual installation)
 - Any modpack including ETF & EMF on Fabric or Forge
 - [Optifine](https://optifine.net/downloads) (not recommended)

<strong>If you use this resourcepack with Optifine, please be aware that <ins>not all features will work</ins>, and I do not provide support for it directly.</strong>

<!-- Either the [Modrinth Launcher](https://modrinth.com/app) or [Prism Launcher](https://prismlauncher.org/download/) are recommended. -->

## Features

Textures and models that are already pixel consistent in vanilla Minecraft are not listed.

Some models found in this resourcepack aren't fully pixel consistent, due to the Z-fighting issues that can occur when rendering two textures directly over the top of each other. In future there may be an option to use fully pixel consistent models, however at present they are not included because they don't look great.

For years, Minecraft's lack of respect for uniform pixel sizes has bothered me, I'm glad that Mojang are finally starting to acknowledge this with the addition of new models for the vex and bat, but they nowhere near cover everything that's inconsistent, so here I have made a list of everything that isn't and am doing my best to fix them one by one.

This project has taken too many hours, but I'm happy with how it's coming along.

### Entities

#### Babies and Small Variants

First on the chopping block, all the baby mobs just look like the adult mobs, but scaled down, and with big heads. One of the worst offenders in my opinion was the baby llama, which is scaled differently horizontally and vertically meaning its not even made of squares, but rectangles!

<details open> <summary>Baby Images</summary>
<img src="https://cdn.modrinth.com/data/scjjjdC9/images/8f030ffec9811eb2c2150b5e44083eeb19a02546.png" alt="Baby model collage">
</details>

<details> <summary>Baby Status</summary>

Baby Entity             | Fixed? | Notes
:-----------------------|:------:|:-
Small Armor Stand       | ✅      | Hips used to be wider, but poked through the armor layers
Baby Axolotl            | ✅      | Adult model has a Z-fghting issue
Baby Bee                | ✅      |
Baby Camel              | ✅      | The walking animation needs some work
Baby Cat                | ❌      | Waiting on adult
Baby Chicken            | ✅      |
Baby Cow                | ✅      | Consider adding back horns
Baby Donkey             | ❌      | Waiting on adult
Baby Drowned            | ✅      |
Baby Fox                | •      | Textures complete, scaling for feet incorrect
Baby Goat               | •      | Horns need work
Baby Hoglin             | ✅      |
Baby Horse              | ❌      | Waiting on adult
Baby Husk               | ✅      |
Baby Llama              | ✅      |
Baby Llama Decor        | ✅      |
Baby Mooshroom (Red)    | ✅      | Consider adding back horns
Baby Mooshroom (Brown)  | ✅      | Consider adding back horns
Baby Mule               | ❌      | Waiting on adult
Baby Ocelot             | ❌      | Waiting on adult
Baby Panda              | ✅      |
Baby Pig                | ✅      |
Baby Pig Saddle         | •      | Consider inflating to avoid Z-fighting
Baby Piglin             | ✅      |
Baby Polar Bear         | ✅      |
Baby Rabbit             | ❌      | Waiting on adult
Baby Sheep              | ✅      |
Baby Sheep Wool         | ✅      |
Baby Skeleton Horse     | ❌      | Waiting on adult
Baby Sniffer            | ✅      |
Baby Strider            | ✅      |
Baby Strider Saddle     | ✅      | Adult (possibly baby too) has a Z-fighting issue
Baby Trader Llama       | ✅      |
Baby Trader Llama Decor | ✅      |
Baby Turtle             | ✅      |
Baby Villager           | ✅      |
Baby Wolf               | ❌      |
Baby Zoglin             | ✅      |
Baby Zombie             | ✅      |
Baby Zombie Horse       | ❌      | Waiting on adult
Baby Zombie Villager    | ✅      |
Baby Zombified Piglin   | ✅      |

</details>

#### Armor Layers

In vanilla Minecraft, armor layers look quite odd in my opinion.
With the updated textures shown below, it can take a bit of getting used to, but it definitely looks better than vanilla.
There are also custom model support for piglins, villagers, wither skeletons and more, to make sure the armor layers fit all entities properly.

The armor layers information section (underneath the images) tells you what entities can spawn with, pick up (potentially) or have armor dispensed on them.

Custom armor layers is an EMF-only feature.

<details open> <summary>Armor Layers Images</summary>
<img src="https://cdn.modrinth.com/data/scjjjdC9/images/b1aaceed3f339454ac601e153904d7a6a44cbe94.png" alt="Armor layer renders of each type">
<img src="https://cdn.modrinth.com/data/scjjjdC9/images/3d645b7268dca35634cf0a54a8f123049e906c50.png" alt="Baby armor layer renders of each type">
</details>

<details> <summary>Armor Layers Information & Status</summary>

Entity           | Spawns | Pick up | Dispensed | Fixed? | Baby? | Trims? | Trims baby? | Notes
:----------------|:------:|:-------:|:---------:|:------:|:-----:|:------:|:-----------:|:-
Armor Stand      | ✔      | 🗶       | ✔         | ✅      | ✅     | ❌      | ❌           |
Drowned          | 🗶      | ✔       | 🗶         | ✅      | ✅     | ❌      | ❌           |
Giant            | 🗶      | 🗶       | 🗶         | ❌      | N/A   | ❌      | N/A         | Large texture, low priority
Husk             | ✔      | ✔       | 🗶         | ✅      | ✅     | ❌      | ❌           |
Piglin           | ✔      | ✔       | ✔         | ✅      | ✅     | ❌      | ❌           |
Piglin Brute     | 🗶      | 🗶       | ✔         | ✅      | N/A   | ❌      | N/A         |
Player           | 🗶      | •       | ✔         | ✅      | N/A   | ❌      | N/A         |
Player (Slim)    | 🗶      | •       | ✔         | ✅      | N/A   | ❌      | N/A         |
Skeleton         | ✔      | ✔       | 🗶         | ✅      | N/A   | ❌      | N/A         |
Stray            | ✔      | ✔       | 🗶         | ✅      | N/A   | ❌      | N/A         |
Wither Skeleton  | 🗶      | ✔       | 🗶         | ✅      | N/A   | ❌      | N/A         |
Zombie           | ✔      | ✔       | 🗶         | ✅      | ✅     | ❌      | ❌           |
Zombie Villager  | ✔      | ✔       | 🗶         | ✅      | ✅     | ❌      | ❌           |
Zombified Piglin | 🗶      | 🗶       | 🗶         | ✅      | ✅     | ❌      | ❌           |

##### Notes:

A piglin or piglin brute that enters the overworld and gets zombified will retain its armor\
A zombie villager that is cured will drop any armor it has on the ground\
A villager that has any armor when zombified will <ins>lose its armor</ins> (it will disappear)

</details>

#### Villager Armor Layers

Ever realize that you can put armor on villagers and pillagers? I didn't.

The following armor layers require the [Villager Armor Layer](https://modrinth.com/mod/villager-armor-layer) mod to work, because vanilla Minecraft doesn't render these layers normally. Currently only the ones discoverable in vanilla survival mode will be supported.

<details> <summary>Modded Armor Layers Information & Status</summary>

Entity           | Spawns | Pick up | Dispensed | Fixed? | Baby? | Trims? | Trims baby? | Notes
:----------------|:------:|:-------:|:---------:|:------:|:-----:|:------:|:-----------:|:-
Iron Golem       | 🗶      | 🗶       | 🗶         | ❌      | N/A   | ❌      | N/A         |
Pillager         | 🗶      | 🗶       | ✔         | ✅      | N/A   | ❌      | N/A         |
Villager         | 🗶      | 🗶       | ✔         | ✅      | ✅     | ❌      | ❌           |
Wandering Trader | 🗶      | 🗶       | 🗶         | ❌      | N/A   | ❌      | N/A         |
Witch            | 🗶      | 🗶       | 🗶         | ❌      | N/A   | ❌      | N/A         |

</details>

#### Other Living Entities

Here we have the miscellaneous living entities that don't really fit into any of the other categories (the miscellaneous non-living entities are further down).

<details> <summary>Other Living Entity Images</summary>
<img src="https://cdn.modrinth.com/data/scjjjdC9/images/656fabc53b375923e005dbb1886e23b31e7ec641.png" alt="Living entity model collage">
</details>

<details> <summary>Other Living Entity Status</summary>

Entity                  | Fixed? | Notes
:-----------------------|:------:|:-
Bat                     | •      | Updated by Mojang, after I did T.T
Cave Spider             | ✅      | Uses interesting UVs to get around spider/cave spider shared eye texture (fixable)
Charged Creeper Aura    | ❌      | Texture moves
Donkey                  | ❌      | Different scale to horse and mule
Drowned Overlay         | ❌      |
Elder Guardian          | ❌      | Large texture
Ghast                   | •      | Large texture
Giant                   | ❌      | Extremely large texture, very low priority
Horse                   | ❌      | Many textures at different scaling to horse and donkey
Llama Decor             | ✅      |
Magma Cube              | •      | Larger textures need work
Mule                    | ❌      | Different scale to horse and donkey
Phantom                 | ❌      | Changes size
Pig Saddle              | ❌      | Inflated
Pillager                | ✅      | Shrunk body overlay to make armor fit, could do retexturing in future?
Player Outer Layer      | •      | Should be configurable, EMF only
Player Slim Outer Layer | •      | Should be configurable, EMF only
Rabbit                  | ❌      | Many textures
Sheep Wool              | ✅      |
Skeleton Horse          | ❌      |
Slime                   | ✅      | Textures only
Snow Golem Pumpkin      | ❌      |
Stray Outer             | ❌      | Inflated
Trader Llama Decor      | ✅      |
Vex                     | •      | Updated by Mojang
Witch                   | ❌      |
Wither                  | •      | Double resolution created so far, wither can change size
Wither Armor            | ❌      | Texture moves
Wither Skeleton         | ✅      |
Zombie Horse            | ❌      |

</details>

### Block Entities

Who doesn't like some good banner art eh?

There are a few inconsistent block entities, most notably signs and banners. Unfortunately there is no support for sign text yet, but a mostly consistent model has been created and textured.

You might be concerned about the appearance of banner designs created by other people after being made pixel consistent, but thanks to many revisions, *most* banner designs are minimally impacted by being made pixel consistent, however some that make use of slight overlaps or differences in textures will likely not look as great.\
If you would like to see, there is a comparison below, and using the arrow keys in the gallery provides a clearer distinction.

Most of the banner patterns below can be found on [Planet Minecraft](https://planetminecraft.com/banners), however some I created myself.

<details open> <summary>Banner Images</summary>

Before                                                                                                                                          | After
:----------------------------------------------------------------------------------------------------------------------------------------------:|:-:
![Some banner designs that aren't pixel consistent](https://cdn.modrinth.com/data/scjjjdC9/images/1543eafe5c785e56f27eb1dd41bd7257ea40e8a0.png) | ![The same banner designs after being made pixel consistent](https://cdn.modrinth.com/data/scjjjdC9/images/a35a9cf605799a838d25fd6c564d677d4a0b187a.png)
![The full set of banner patterns in vanilla](https://cdn.modrinth.com/data/scjjjdC9/images/3e4da60eadadbad026c6b408e75e2c3cf6cb46a5.png)       | ![The full seto fo banner patterns pixel consistent](https://cdn.modrinth.com/data/scjjjdC9/images/81efc118d5ae01cb4861769d71821a0a11bffdb6.png)

</details>

<details> <summary>Block Entity Status</summary>

Entity                | Fixed? | Notes
:---------------------|:------:|:-
Dragon Head           | ❌      |
Banner                | ✅      |
Banner Patterns       | ✅      |
Hanging Sign Text     | ❌      |
Sign                  | ✅      | Increase sign width when sign text is supported
Sign Text             | ❌      |

</details>

### Other Entities

<details> <summary>Other Entity Status</summary>

Entity                      | Fixed? | Notes
:---------------------------|:------:|:-
Arrow                       | ❌      |
Dragon Fireball             | ❌      |
Elytra                      | ✅      | Model shrunk to size, but the size of the textures can't be easily modified since they use cape textures, needs more testing
End Crystal                 | ❌      | Pretty sure this model isn't consistent, though needs more testing because it's so bouncy
Experience Orbs             | •      | No model support yet, but textured to almost consistency
Fireball                    | ❌      |
Item Models                 | ❌      | Will need config support and to be disabled by default, will be a drastic overhaul to the look
Llama Spit                  | ❌      | Not actually inconsistent, just looks oddly blocky
Minecart With Chest         | ❌      |
Minecart With Hopper        | ❌      |
Minecart With Furnace       | ❌      |
Minecart With TNT           | ❌      |
Minecart With Command Block | ❌      |
Minecart With Other Blocks  | ❌      |
Spyglass Model              | ❌      |
Shulker Bullet              | ❌      |
Small Fireball              | ❌      |
Spectral Arrow              | ❌      |
Trident                     | ❌      |
Worn Creeper Head           | ❌      |
Worn Zombie Head            | ❌      |
Worn Player Head            | ❌      |
Worn Piglin Head            | ❌      |
Worn Dragon Head            | ❌      |
Worn Skeleton Skull         | ❌      |
Worn Wither Skeleton Skull  | ❌      |

</details>

### Blocks

<details> <summary>Block Status</summary>

Block          | Fixed? | Notes
:--------------|:------:|:-
Dragon Egg     | ✅      | Possibly a config to switch to the old shape, but correct texture scaling
Fire           | ❌      |
Lava           | ❌      |
Small Dripleaf | ❌      | Did work but accidentally deleted
Tripwire Hook  | ✅      |
Tripwire       | ✅      |
Water          | ❌      |

Note: Not many models have been checked, things like the `cross` model need to be reviewed.

</details>

### Particles

<details> <summary>Particle Status</summary>

Particle         | Fixed? | Notes
:----------------|:------:|:-
Beacon Beam      | ❌      |
End Crystal Beam | ❌      |
Guardian Beam    | ❌      |
Shadow           | ❌      |
Shulker Shriek   | ❌      |
Sonic Boom       | ❌      |

Many more inconsistent particles are missing.

</details>

<!-- ### GUI -->
<!-- The anvil hammer texture had? a double column of pixels? -->

### Spawner Entity Models

This heading refers to the tiny entity models that spin around inside a mob spawner.
Currently there is no way to support this, but it is something I would love to add in the future.

### Fresh Animations Support?

Fresh animations is not yet supported because of the drastic remodel of most edited mobs, however I am planning on adding support for it soon. This will likely take the form of a separate resourcepack.

## Links

This project is being hosted on [Modrinth](https://modrinth.com/resourcepack/pixel-consistency) and it's source can be found on [Github](https://github.com/Thanos1716/pixel-consistency).

If you have:

 - Discovered an inconsistent texture or model that is not listed,
 - Found a broken texture or model in this pack, or
 - Would like to request a feature

please raise an issue on the [issues](https://github.com/Thanos1716/pixel-consistency/issues) page.

### Curseforge

I will not be hosting this pack on Curseforge due to a combination of no Linux support for Minecraft in the Curseforge launcher (despite both Minecraft and Curseforge having a Linux client), no option to create an account without linking other services, and the general state that Curseforge is in.

<strong>Due to the reasons outlined above and although the license permits it, I would appreciate it if you don't upload direct copies of this pack to Curseforge.</strong> Any derivatives of it however, go wild!

## Credit

Thanks to Traben for developing both ETF and EMF, and for being very helpful when asking questions about CEM.

This resourcepack is partially inspired by [Better Vanilla Babies & Pixel Perfect Mobs](https://www.planetminecraft.com/texture-pack/better-vanilla-babies-optifine-1-14-4/) by DraminOver. No assets from that pack are used in this one.

## Licensing

This project is licensed under the permissive Creative Commons Zero 1.0 license in order to bring pixel consistency to as many people as possible, that means you can use any model in this pack however you like, you don't even have to give me credit, although that's always appreciated.

Note that the license CC0-1.0 applies to all of the models and most of the textures used in this pack. Some textures in this pack are modified versions of the vanilla assets, which are required to make the pack work, however no direct copies of assets under Mojang copyright are included. If you wish to use all of the CC0-1.0 assets without dealing with Mojang's assets, they can be found [here](https://github.com/Thanos1716/pixel-consistency/tree/main/source/cc0-assets/).

## Support Me

The best way to support me at the moment is by downloading my resourcepack!

I don't have any donation options available, but that is something I may consider setting up in the future. If this is something you would like, please [raise an issue](https://github.com/Thanos1716/pixel-consistency/issues).

If you are a resourcepack developer and enjoy my work, I would love it if you included any models from this pack in yours!

<!--------->
<!-- 🗶 ❌ -->
<!-- ✔ ✔️ -->
<!-- ✅ -->
# pixel-consistency
