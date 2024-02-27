# MC-Video2Structure *Dataset*
Functions to generate training data.

There are two datasets used in this project:

- **MC Blocks**: A dataset containing images (screenshots) of random views from a Minecraft world. This is used for training the *Block Segmentation Algorithm* (BSA), the *Block Depth Estimator* (BDE), and the *Camera Pose Estimator* (CPE). As such, each image has three different kinds of label: A greyscale image containing block labels for every pixel (BSA labels), a greyscale image containing depth information for every pixel (BDE labels), and the 5D position of the camera `{x, y, z, rot, pitch}` (CPE labels).
- **MC Structure Videos**: TBA

## General Setup

1. Install the python package [mcpi](https://github.com/martinohanlon/mcpi).

2. Create a default Minecraft (tested with version 1.19.4) server and install [Spigot](https://getbukkit.org/download/spigot).

3. Place the plugin [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice) in the plugin folder (don't mind that the plugin is made for an outdated Minecraft version).

4. Start the server via ```java -Xmx2G -jar spigot-*.jar nogui```.

    **Note**: If you are using WSL and you run Python with it, start the server also on WSL by allowing the Minecraft Port in your WSL firewall and starting the server with an added argument: ```java -Xmx2G -Djava.net.preferIPv4Stack=true -jar spigot-*.jar nogui```.

5. Make sure to have a void world running on the server. This can be archieved by creating a (Creative mode) Singleplayer world with the *Flat* world type and changing the preset to "Void". This world can then be copied to your server folder (and be sure to rename the world foldeer to "world").

6. Join the server and run `\tp 0.0 0.0 0.0` **in-game** to teleport you to world center (make sure to fly in creative mode). Now run `python example_coord_finder.py` **in a terminal**. If everything worked correctly, messages should appear in the chat showing you the mcpi relative coordinate offset. Write these coordinates in the `utils.py` file in the `SPAWN_OFFSET` tuple. If you move in your world and run the python script again, your correct coordinates (from the F degub menu) should appear in chat.

6. If everything worked correctly, you can now run `python example_build_world.py` which will create a random structure in the world. The argument for that file determines how big the created structure will be. Default is 3. Experiment around with it and clear everything up with `python example_clear_world.py <N BLOCKS>`.

## Generating **MC BLocks**

As said, there are three different uses for this dataset so three different labels will be produced.
The general outline of the dataset generation is the following:

- A python script will build a random structure and then record your coordinates every second while your run/ fly around in your world. After a specified amount of time, the script will create a *Minecraft Datapack* that your can install into your world which will teleport you to the recorded coordinates so you can take a screenshot and get teleported to the next location (to take again a screenshot and so on...)
- The screenshot loop will now be done **three times**: First in normal mode to record training data `X`. Then again with a *texture pack* for the BSA labels and lastly with a *shader pack* for the BDE labels. The labels for the CPE are already saved by the first step.

### Recording coordinates

Run `python create_mc_blocks.py <MINUTES TO RUN FOR>`. It will build a random structure and count down from 5 seconds. Position yourself where you want to start and then just walk and look around. The script will automatically save the camera pose every second. After the specified time period, a datapack is created TODO

## Generating **MC Structure Videos**

TBA

## Important note on current limitations

The first version of this project will have some major limitations that can be improved in further versions. Because the training data is generated this way, the model will currently only work with:

- a **void world** with the structure in the center,
- **no entities** in the world,
- no GUI shown and probably a set FOV, and
- a small selection of **18 blocks** (listed below).

Block list with their corresponding structure symbol, model id, and the id used by *mcpi* internally:

Block Name | Symbol | `id` | `mcpi id`
--- | --- | --- | ---
air          | ` ` [space] |  0 | 0
stone        | `s`         |  1 | 1
cobblestone  | `c`         |  2 | 4
slabs        | `b`         |  3 | 61 (retextured furnace)
bricks       | `X`         |  4 | 45
grass        | `D`         |  5 | 2
dirt         | `d`         |  6 | 3
sand         | `~`         |  7 | 12
planks       | `w`         |  8 | 16 (retextured coal ore)
log          | `L`         |  9 | 17
leaves       | `l`         | 10 | 56 (retextured diamond ore)
wool         | `%`         | 11 | 35
goldblock    | `-`         | 12 | 41
ironblock    | `=`         | 13 | 42
diamondblock | `+`         | 14 | 57
bookshelf    | `*`         | 15 | 47
obsidian     | `O`         | 16 | 49
glowstone    | `G`         | 17 | 89
melon        | `@`         | 18 | 103

For the structure files there are also place holders:

Place Holder | Symbol | `ids` mapped to
--- | --- | ---
[Building] Foundation | `F` | `[1, 2, 3, 4, 8, 11]`
[Building] Support    | `S` | `[9, 9, 9, 2, 3, 4]`
[Building] Wall       | `W` | `[1, 2, 4, 8, 11]`
[Building] Roof       | `R` | `[2, 4, 8, 8, 8]`
[Decoration] Interior | `$` | `[0, 0, 0, 0, 0, 0, 12, 13, 14, 15, 15, 15, 17, 17]`
[Decoration] Garden | `#` | `[0, 0, 0, 5, 5, 10, 15, 18, 18, 18]`