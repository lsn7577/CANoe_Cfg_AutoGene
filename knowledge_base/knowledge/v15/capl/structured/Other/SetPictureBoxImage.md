# SetPictureBoxImage

> Category: `Other` | Type: `function`

## Syntax

```c
setPictureBoxImage(panel, control, imagefile);
```

## Description

Replaces the image of the Panel Designer control during runtime:

Picture Box

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| control | Name of the control, restricted to 128 characters."" – references all controls on the panel. |
| iamgefile | Path and name of the image file. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | Picture Box | Picture Box | Picture Box | — | — | Picture Box |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
