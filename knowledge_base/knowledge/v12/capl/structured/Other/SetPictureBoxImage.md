# SetPictureBoxImage

> Category: `Other` | Type: `function`

## Syntax

```c
setPictureBoxImage(panel, control, imagefile);
```

## Description

Replaces the image of the Panel Designer Picture Box control during runtime.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

Setting image file using absolute path.

Setting image file using relative path. The image is in the Images folder and this folder is parallel to the panel folder.

```c
on key 'x'
{
SetPictureBoxImage("Movie", "Picture Box", "D:\\Example\\PictureBoxProject\\Images\\Picture.bmp");
}
on key 'y'
{
SetPictureBoxImage("Movie", "Picture Box", "..\\Images\\Picture.bmp");
}
```

## Availability

| Since Version |
|---|
