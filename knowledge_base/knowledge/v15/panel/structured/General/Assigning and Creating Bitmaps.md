# Assigning and Creating Bitmaps

> Category: `Panel` | Subcategory: `General` | Type: `concept`

You can create and edit image files with any image processing program (e.g. Paint, Photoshop).

## Valid Formats

The Panel Designer supports PNG (support of alpha channel/transparency) and BMP.

Note

| Note When creating your own bitmaps be sure to save them as uncompressed Windows bitmaps. Some graphics drivers cannot process specially compressed bitmaps, which may result in undesirable optical effects or even system crashes. It is advisable to save all images belonging to a panel in a separate subdirectory. If you wish to forward a panel to another user you must also forward the image directory. |
|---|

## Create an Image Sequence

An image file for a n-stage switch always consists of n+1 rectangular partial bitmaps, each with the same height and width, arranged to be horizontally adjacent to one another.

In the first rectangle the inactive state is shown. This appears on the panel when no symbol has been assigned to the element. The Switch/Indicator shows the inactive state as long as the assigned symbol will be received.

The n switch values are located in the n partial bitmaps to the right of this.

Example of Two-Stage Switch

| Example of Two-Stage Switch |
|---|

## Transparent Color

For image files that do not have a transparent background, you must note the following information.

Image files whose transparency is active allow the background to appear through their areas of transparency color. That is, the transparency color remains invisible.

To draw a image file with transparency fill the areas that should be transparent with the color you have defined in the ribbon in the Transparency field or in the Properties Window in the Transparent Color field.The default setting of the transparency color is Blue (RGB 0,0,255).

Note

Use the default color Blue (RGB 0.0255) to create image files with transparent color. Then have not to choose always a new transparent color for each newly added bitmap in the Panel Designer.

Elements such as Button, Track Bar, Input/Output Box or Static Text do not appear through the transparency areas of Picture Box and Switch/Indicator if they are placed below them.When overlapping Picture Box and Switch/Indicator, the transparency remains active.

| Note Use the default color Blue (RGB 0.0255) to create image files with transparent color. Then have not to choose always a new transparent color for each newly added bitmap in the Panel Designer. |
|---|

## Image Size

Switch/Indicator and Picture Box support a image size (hight/width) of 32767 pixels. You can reduce the image size with every image processing program.

Example to reduce the image size for a image sequence with Windows Paint.

In the following example, the original file is 42273 x 420 pixels in size and contains 33 images (1 default image and 32 states). Each image has the dimensions 1281 x 420 pixels.

In Paint the image size should now be reduced to below 32767.

| Example to reduce the image size for a image sequence with Windows Paint. In the following example, the original file is 42273 x 420 pixels in size and contains 33 images (1 default image and 32 states). Each image has the dimensions 1281 x 420 pixels. In Paint the image size should now be reduced to below 32767. Divide 32767 by the number of images: 32767 / 33 = 992,93... Since the image size (overall image and single images) must not contain any floating-point numbers, the new maximum size of the overall image is 992 pixels * 33 = 32736 pixels. Select in Paint on the Home ribbon tab the Resize menu command. Select in the Resize and Skew dialog under Resize the Pixels option. Activate under Resize the Maintain aspect ratio option. Enter 32736 at Horizontal. 325 is automatically set for Vertical. Close the dialog with [OK]. Save the image file. |
|---|
