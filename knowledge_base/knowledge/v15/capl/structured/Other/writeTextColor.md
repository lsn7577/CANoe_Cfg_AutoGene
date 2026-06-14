# writeTextColor

> Category: `Other` | Type: `function`

## Syntax

```c
void writeTextColor(dword sink,dword red, dword green, dword blue);
```

## Description

Sets the color for text of the specified page in the Write Window.

You can use the following constants for the target identifier:

// write sinksdword WRITE_SYSTEM = 0;dword WRITE_CAPL = 1;

In addition you can use one of the target identifiers returned by the function writeCreate.

The color settings have also an effect on the All tab of the Write Window.

## Parameters

| Name | Description |
|---|---|
| sink | The target identifier of the page on which the color settings should have an effect. |
| red | Specifies the intensity of the red color. |
| green | Specifies the intensity of the green color. |
| blue | Specifies the intensity of the blue color. |

## Return Values

—

## Example

```c
WriteTextColor(0,255,0,0);
WriteLineEx(0,1,"This is red text");
WriteTextBkgColor(0,0,255,0);
WriteLineEx(0,1,"This is red text with green background");
WriteTextColor(0,0,0,0);
WriteTextBkgColor(0,255,255,255);
WriteLineEx(0,1,"This is black text with white background");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
