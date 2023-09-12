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
Github(https://github.com/AnnaFrances8/JOIN-Software-v1) > Create > Download zip > extract files > open JOIN.py

If you need directly the .exe I can send you the .zip file by email (annafrances8@gmail.com).

## Notes 📋
Keep an eye on the Console window for progress updates during image processing.
If the tool appears unresponsive, please be patient, as it may still be in the processing stage.

More information available in: publication in progress.

## Interface ⚙️
![image](https://github.com/AnnaFrances8/JOIN-Software-v1/assets/141737377/21634cbb-60c3-488a-b221-02a3e321a3b2)

![image](https://github.com/AnnaFrances8/JOIN-Software-v1/assets/141737377/ed271c87-f330-4aca-91f7-39148913a14b)

![image](https://github.com/AnnaFrances8/JOIN-Software-v1/assets/141737377/79b9e63b-c023-428f-9fcd-de94663d2073)

![image](https://github.com/AnnaFrances8/JOIN-Software-v1/assets/141737377/89a96c3e-81fc-4902-98e1-054eee67b945)


## Author ✒️

**Anna Francès-Abellán** - [Annafrances8](https://github.com/AnnaFrances8)


## License 📄

This project is under the License Creative Commons Attribution 4.0 International - see the file LICENSE for details.
Permits almost any use subject to **providing credit** and license notice

## Aknowledgements 🎁

Institut Català de Paleoecologia Humana i Evolució Social (IPHES).
program INVESTIGO 2022 
![image](https://github.com/AnnaFrances8/JOIN-Software-v1/assets/141737377/4f71f0ea-8360-4961-bb48-e8a1b55d3b2b)


