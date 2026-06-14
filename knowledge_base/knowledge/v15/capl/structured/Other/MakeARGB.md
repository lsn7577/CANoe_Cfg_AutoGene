# MakeARGB

> Category: `Other` | Type: `function`

## Syntax

```c
long MakeARGB(long Alpha, long Red, long Green, long Blue);
```

## Description

Calculates the color value from the alpha value and the three primary color components.

The value is interpreted as 4 bytes and the color results from which value is contained in which byte:

[0] = Alpha (transparency), [1] = Red, [2] = Green, [3] = Blue

See also availability for panel controls

## Parameters

| Name | Description |
|---|---|
| Alpha | The transparency of the color (0 - 255) 0: 0% opacity of the color, totally transparent 255: 100% opacity of the color |
| Red | Red color component (0 - 255) |
| Green | Green color component (0 - 255) |
| Blue | Blue color component (0 - 255) |

## Example

```c
MakeARGB(64, 255, 128, 0); // 25% opacity of orange color
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 SP4 | 8.5 SP4 | 13.0 | — | — | 2.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
