# MakeRGB

> Category: `Other` | Type: `function`

## Syntax

```c
long MakeRGB(long Red, long Green, long Blue);
```

## Description

Calculates the color value from the three primary color components.

The value is interpreted as 4 bytes and the color results from which value is contained in which byte:

[0] = ignored, [1] = Red, [2] = Green, [3] = Blue

See also availability for panel controls

## Parameters

| Name | Description |
|---|---|
| Red | Red color component (0 - 255) |
| Green | Green color component (0 - 255) |
| Blue | Blue color component (0 - 255) |

## Example

```c
MakeRGB(255, 128, 0); // orange color
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
