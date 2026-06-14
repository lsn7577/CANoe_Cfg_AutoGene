# SetMediaFile

> Category: `Other` | Type: `function`

## Syntax

```c
SetMediaFile(panel, control, mediafile);
```

## Description

Replaces the media file of the Panel Designer control during runtime:

Media Player

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Parameters

| Name | Description |
|---|---|
| panel | Panel name, restricted to 128 characters."" – references all loaded panelsIf you open a panel the first time, the panel is loaded. If you close the panel, it remains loaded. |
| control | Name of the control, restricted to 128 characters."" – references all controls on the panel. |
| mediafile | Path and name of the media file. |

## Return Values

—

## Example

Setting media file using absolute path.

Setting media file using relative path. The media file is in the Videos folder and this folder is parallel to the panel folder.

```c
on key 'x'
{
SetMediaFile("Movie", "Media Player", "D:\\Example\\MediaPlayerProject\\Videos\\song.mpg");
}
on key 'y'
{
SetMediaFile("Movie", "Media Player", "..\\Videos\\song.mpg");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 | 7.5 | 13.0 | — | — | 1.0 |
| Restricted To | Media Player | Media Player | Media Player | — | — | Media Player |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
