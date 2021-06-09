# Anime-Decensoring

_Decensoring Hentai with Deep Neural Networks. Formerly named DeepMindBreak._

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
