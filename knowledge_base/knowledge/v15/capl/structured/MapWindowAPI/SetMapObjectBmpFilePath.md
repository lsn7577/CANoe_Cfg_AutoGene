# SetMapObjectBmpFilePath

> Category: `MapWindowAPI` | Type: `function`

## Syntax

```c
long SetMapObjectBmpFilePath( long handle, char filePath[] );
```

## Description

Sets the file path to a bitmap for a map object of the type bitmap.

For transparency pure white color (RGB 255, 255, 255) is used.

## Parameters

| Name | Description |
|---|---|
| handle | Reference of the map object. |
| filePath | Path of the bitmap file. You can set an absolute path (e.g. "C:\myCANoeConfig\bmp\circles.bmp") or a relative path (e.g. "bmp\circles.bmp"). If the relative option is used, the path is seen relative to the location of the CANoe configuration. If the bitmap file could not be found or load, the bitmap is displayed in the Map Window. |

## Example

```c
void DrawBitmapObject()
{
  long handle;

  // both file paths lead to the same bitmap
  char filePathRelative[30] = "bmp\\TrafficLight.bmp";
  char filePathAbsolute[50] = "C:\\myCANoeConfig\\bmp\\TrafficLight.bmp";
  handle = CreateMapObject( 7 ); // bitmap

  // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart
  SetMapObjectPosition(handle, 48.825240, 9.095642);
  SetMapObjectBmpFilePath(handle, filePathRelative);
  SetMapObjectBmpCount(handle, 4);
  SetMapObjectBmpIndex(handle, 1); // green traffic light
  SetMapObjectSize(handle, 1.8, 4.2);
  SetMapObjectHeading(handle, 87);
  DrawMapObject(handle);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | — | — | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | — | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | — | — | ✔ | N/A |
