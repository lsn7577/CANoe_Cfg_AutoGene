# C2xSetMapObjectBmpFilePath

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by SetMapObjectBmpFilePath. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long C2xSetMapObjectBmpFilePath( long handle, char filePath[] ); |  |  |  |
| Function | Sets the file path to a bitmap for a map object of the type bitmap. For transparency pure white color (RGB 255, 255, 255) is used. |  |  |  |
| Parameters | handle Reference of the map object |  |  |  |
| filePath Path of the bitmap file. You can set an absolute path (e.g. "C:\myCANoeConfig\bmp\circles.bmp") or a relative path (e.g. "bmp\circles.bmp"). If the relative option is used, the path is seen relative to the location of the CANoe configuration. If the bitmap file could not be found or load, the bitmap is displayed in the Map Window. |  |  |  |  |
| Return Values | 0 if success, else the set went wrong |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.1 | Car2x | — | • |  |
| Example void DrawBitmapObject(){ long handle; // both file paths lead to the same bitmap char filePathRelative[30] = "bmp\\TrafficLight.bmp"; char filePathAbsolute[50] = "C:\\myCANoeConfig\\bmp\\TrafficLight.bmp"; handle = C2xCreateMapObject( 7 ); // bitmap // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart C2xSetMapObjectPosition(handle, 48.825240, 9.095642); C2xSetMapObjectBmpFilePath(handle, filePathRelative); C2xSetMapObjectBmpCount(handle, 4); C2xSetMapObjectBmpIndex(handle, 1); // green traffic light C2xSetMapObjectSize(handle, 1.8, 4.2); C2xSetMapObjectHeading(handle, 87); C2xDrawMapObject(handle);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
