# SetMapObjectText

> Category: `MapWindowAPI` | Type: `function`

## Syntax

```c
long SetMapObjectText( long handle, char text[] ); // form 1
long SetMapObjectText( long handle, char formattedText[], float value ); // form 2
```

## Description

Sets text (form 1) or formatted text (form 2) for a map object of the type text.

## Parameters

| Name | Description |
|---|---|
| handle | Reference of the map object. |
| text | Text which should be displayed. |
| formattedText | Text with a placeholder for a variable which should be displayed. |
| value | Variable which should be displayed in the text. |

## Example

```c
void DrawTextObject()
{
  long handle;
  float timeRemaining = 5.8;

  handle = CreateMapObject( 8 );

  // set position: Motorstraße/Hemminger Straße, D-70499 Stuttgart
  SetMapObjectPosition(handle, 48.825230, 9.095580);
  SetMapObjectText(handle, "Traffic Light: time remaining %5.1f s", timeRemaining);
  SetMapObjectFillColor(handle, makeRGB(0, 0, 0));
  DrawMapObject(handle);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14: form 1, 2 | — | — | 14 | 5.0 SP3: form 1, 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | — | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | — | — | ✔ | N/A |
