# Anime-Decensoring

_Decensoring Hentai with Deep Neural Networks. Formerly named DeepMindBreak._

## This project is a continuation of a discontinued project.

A deep learning-based tool to automatically replace censored artwork in hentai with plausible reconstructions.

The user colors cencored regions green in an image editing program like GIMP or Photoshop. A neural network fills in the censored regions.

Anime-Decensoring has a pre-built binary for Windows 64-bit available [here](https://github.com/DoginUwU/Anime-Decensoring/releases/latest).

![Screenshot_1](https://user-images.githubusercontent.com/59850361/121423114-4fe16f80-c946-11eb-9866-261b54304b64.png)
![Censored, decensored](/readme_images/mermaid_collage.png)

## Features

- Decensoring images of ANY size
- Decensoring of ANY shaped censor (e.g. black lines, pink hearts, etc.)
- Higher quality decensors
- Support for mosaic decensors (Beta)
- User interface (Beta)

## Limitations

The decensorship is for color hentai images that have minor to moderate censorship of the penis or vagina. If a vagina or penis is completely censored out, decensoring will be ineffective.

It maybe does NOT work with:

- Black and white/Monochrome image
- Hentai with screentones (e.g. printed hentai)
- Real life porn
- Censorship of nipples
- Censorship of anus
- Animated gifs/videos

## To do

- Finish the user interface
- Update model with better quality data
- Add error log

# Installation

## Download Prebuilt Binaries
You can download the latest release [here](https://github.com/DoginUwU/Anime-Decensoring/releases/latest) or find all previous releases [here](https://github.com/DoginUwU/Anime-Decensoring/releases)
Binary only available for Windows 64-bit.

## Run Code Yourself
If you want to run the code yourself, you can clone this repo and download the model from https://drive.google.com/open?id=1byrmn6wp0r27lSXcT9MC4j-RQ2R04P1Z. Unzip the file into the /models/ folder.

### Dependencies (for running the code yourself)
- Python 3.6.7
- TensorFlow 1.10
- Keras 2.2.4
- Pillow
- h5py

No GPU required! Tested on Ubuntu 16.04 and Windows. Tensorflow on Windows is compatible with Python 3 and not Python 2. Tensorflow is not compatible with Python 3.7.

Tensorflow, Keras, Pillow, and h5py can all be installed by running in the command line

```
$ pip install -r requirements.txt
```

## Run Code Yourself on CPUs that don't support AVX instructions

CPUs that don't support AVX instructions may experience this error when using the above install instructions:

```
ModuleNotFoundError: No module named '_pywrap_tensorflow_internal'
```

Follow these alternate install instructions if that happens:

1. Start from a clean Python 3.6.7 install.
2. Download a version of tensorflow that do support AVX instructions from (https://github.com/fo40225/tensorflow-windows-wheel/tree/master/1.10.0/py36/CPU/sse2). I assume you picked tensorflow-1.10.0-cp36-cp36m-win_amd64.whl for 64-bit and the other for 32-bit computers.
3. Open the command line in the same directory as the file downloaded in step 2. Run

```
pip install tensorflow-1.10.0-cp36-cp36m-win_amd64.whl
```

or

```
pip install tensorflow-1.10.0-cp36-cp36m-win32.whl
```
depending on what you installed in step 2.
4. Open the command line in the directory of "DeepCreamPy-master" and run
```
pip install -r requirements.txt
```

Instructions are from https://github.com/deeppomf/DeepCreamPy/issues/26#issuecomment-434043166.


Follow me on Twitter [@DoginUwU](https://twitter.com/DoginUwU) for project updates.

Initial projects credits to [liaoxiong3x](https://github.com/liaoxiong3x/DeepCreamPy).

## License

This project is licensed under GNU Affero General Public License v3.0.

See [LICENSE.txt](LICENSE.txt) for more information about the license.

## Acknowledgements

Example mermaid image by Shurajo & AVALANCHE Game Studio under [CC BY 3.0 License](https://creativecommons.org/licenses/by/3.0/). The example image is modified from the original, which can be found [here](https://opengameart.org/content/mermaid).

Neural network code is modified from MathiasGruber's project [Partial Convolutions for Image Inpainting using Keras](https://github.com/MathiasGruber/PConv-Keras), which is an unofficial implementation of the paper [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723). [Partial Convolutions for Image Inpainting using Keras](https://github.com/MathiasGruber/PConv-Keras) is licensed under the MIT license.

User interface code is modified from Packt's project [Tkinter GUI Application Development Blueprints - Second Edition](https://github.com/PacktPublishing/Tkinter-GUI-Application-Development-Blueprints-Second-Edition). [Tkinter GUI Application Development Blueprints - Second Edition](https://github.com/PacktPublishing/Tkinter-GUI-Application-Development-Blueprints-Second-Edition) is licensed under the MIT license.

Data is modified from gwern's project [Danbooru2017: A Large-Scale Crowdsourced and Tagged Anime Illustration Dataset](https://www.gwern.net/Danbooru2017).
And [liaoxiong3x](https://github.com/liaoxiong3x/DeepCreamPy).

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for full license text of these projects.
