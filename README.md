The releases are available and citable on Zenodo
[![DOI](https://zenodo.org/badge/690537412.svg)](https://zenodo.org/badge/latestdoi/690537412)


# JOIN-Software-v1 🔬

Image processing program optimized for microscopy images, especially those from 3D digital microscopes. This tool provides three essential functions:

**Stitch**: Combine multiple microscopy images to create panoramic or high-resolution images, ideal for 3D digital microscopy data to capture a broader field of view or more detailed information.

**Resize**: Adjust the size of your microscopy images by specifying scaling factors for width and height, ensuring they are perfectly suited for your analysis.

**Sharpen**: Enhance the intricate details and structures within your microscopy images, allowing for more precise analysis.

## Usage Instructions 🚀
#### Stitching
Select the Stitch option to create panoramic or high-resolution images.
Choose your folder containing the single images to stitch. The composed image will appear in the same folder at the end of the process as folder_name_stitched.tif.

#### Resizing
Utilize the Resize option to modify the dimensions of your microscopy images choosing a suitable scaling factor. Choose your folder containing the images you want to resize and choose a scaling factor for width and height between 0-1. A scaling factor for width of 0.2 is equal to scaling the image to 20% width. In some computers, pop-ups where you can enter the scaling factor will not appear in the screen but minimized with the program in the taskbar. The resized images will appear in your folder at the end of the process as name_resized{extension}in their own folder {folder_name}_Resized images.

#### Sharpening
Sharpen the details of your image. The sharpened image will appear in the same folder at the end of the process as name_sharpened.tif.


## Requirements 🛠️
Python 3 (https://www.python.org/downloads/)

``` python
pip install -r requirements.txt
```

## Installation 🔧
Github (https://github.com/AnnaFrances8/JOIN-Software-v1) > Code > Download zip > extract files > open JOIN-v1.py

If you need directly the .exe I can send you the .zip file by email (annafrances8@gmail.com).

## Notes 📋
The current process will be displayed in the Console window, which can be cleaned. 

Accepted extensions: .jpg, .tif

If the program does not respond, please wait, it is still running.

It may be necessary to refresh the folder to see the outputs.

More information available in: publication in progress.

## Interface ⚙️

See Interface screenshots folder.


## Author ✒️

**Anna Francès-Abellán** - [Annafrances8](https://github.com/AnnaFrances8)


## License 📄

This project is under the License Creative Commons Attribution 4.0 International - see the file LICENSE for details.
Permits almost any use subject to **providing credit** and license notice.

## Aknowledgements 🎁

Institut Català de Paleoecologia Humana i Evolució Social (IPHES).

Program INVESTIGO 2022.



