# C2xSetMapObjectBmpFilePath

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetMapObjectBmpFilePath( long handle, char filePath[] );
```

## Description

Sets the file path to a bitmap for a map object of the type bitmap.

For transparency pure white color (RGB 255, 255, 255) is used.

## Return Values

0 if success, else the set went wrong

## Example

```c
void DrawBitmapObject()
{
  long handle;

  // both file paths lead to the same bitmap
  char filePathRelative[30] = "bmp\\TrafficLight.bmp";
  char filePathAbsolute[50] = "C:\\myCANoeConfig\\bmp\\TrafficLight.bmp";
  handle = C2xCreateMapObject( 7 ); // bitmap

  // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart
  C2xSetMapObjectPosition(handle, 48.825240, 9.095642);
  C2xSetMapObjectBmpFilePath(handle, filePathRelative);
  C2xSetMapObjectBmpCount(handle, 4);
  C2xSetMapObjectBmpIndex(handle, 1); // green traffic light
  C2xSetMapObjectSize(handle, 1.8, 4.2);
  C2xSetMapObjectHeading(handle, 87);
  C2xDrawMapObject(handle);
}
```

## Availability

| Since Version |
|---|
