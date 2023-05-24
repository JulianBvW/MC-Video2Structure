# MC-Video2Structure
University project for extracting 3D minecraft house structures from 2D videos.

## Setup

### Dataset Generation

To interact with the minecraft world from python, the package [mcpi](https://github.com/martinohanlon/mcpi) is used. This will connect to a [Spigot](https://getbukkit.org/download/spigot) Server using the plugin [RaspberryJuice](https://github.com/zhuowei/RaspberryJuice).

Start the server using ```java -Xmx2G -Djava.net.preferIPv4Stack=true -jar spigot-*.jar nogui``` (the second argument is needed when starting the server from WSL2; open firewall for IPv4 in that case first) and follow the README in the Dataset folder.

### Model training

TBA

## Roadmap

- [ ] Dataset Generation
  - [ ] MC Blocks
  - [ ] MC Structure Videos
- [ ] Model Training
  - [ ] Camera Pose Estimator
  - [ ] Depth Estimator
  - [ ] Block Segmentation
  - [ ] Inner Structure Reader
  - [ ] Outer Structure Reader
