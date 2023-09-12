# JOIN-Software-v1 🔬

Image processing program optimized for microscopy images, especially those from 3D digital microscopes. This tool provides four essential functions:

**Stitch**: Combine multiple microscopy images to create panoramic or high-resolution images, ideal for 3D digital microscopy data to capture a broader field of view or more detailed information.

**Resize**: Adjust the size of your microscopy images by specifying scaling factors for width and height, ensuring they are perfectly suited for your analysis.

**Remove Background**: Eliminate background noise and distractions from your microscopy images, enhancing the clarity of your sample. Perfect for publication figures.

**Sharpen**: Enhance the intricate details and structures within your 3D microscopy images, allowing for more precise analysis.

## Usage Instructions 🚀
#### Stitching
Select the Stitch option to create panoramic or high-resolution images.
Choose a folder containing the individual microscopy images you want to combine, particularly useful for 3D digital microscope captures.
The composed image will appear in the same folder at the end of the process as **folder_name**_stitched.tif.
#### Resizing
Utilize the Resize option to modify the dimensions of your microscopy images.
Select a folder containing the images you wish to resize.
Specify the desired scaling factors for width and height (within the range of 0 to 1).
For instance, a width scaling factor of 0.2 will reduce the image width to 20% of the original size.
The resized images will be saved in the same folder with filenames like **name**_resized{extension}, ensuring they are tailored to your requirements.
#### Background Removal
Choose the Remove Background option to eliminate background from your microscopy images.
The processed images, now free from background, will be saved in the same folder with filenames like **name**_no_background.tif.
#### Sharpening
Opt for the Sharpen option to enhance the intricate details and structures in your 3D microscopy images, allowing for more precise analysis.
The sharpened images will be saved in the same folder with filenames like **name**_sharpened.tif, ensuring your data is ready for in-depth examination.


## Requirements 🛠️
Python 3 (https://www.python.org/downloads/)

``` python
pip install opencv-python
```
``` python
pip install pillow  # for the PIL (Pillow) library
```
``` python
pip install opencv-python  # for OpenCV
```
``` python
pip install numpy  # for NumPy
```
``` python
pip install rembg  # for rembg
```


## Installation 🔧


## Notes 📋
Keep an eye on the Console window for progress updates during image processing.
If the tool appears unresponsive, please be patient, as it may still be in the processing stage.








## Ejecutando las pruebas ⚙️




## Despliegue 📦



## Construido con 🛠️


## Contribuyendo 🖇️



## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌


## Author ✒️

* **Anna Francès-Abellán** - [Annafrances8](https://github.com/AnnaFrances8)

 

## License 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Aknowledgements 🎁




