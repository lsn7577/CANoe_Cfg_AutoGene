# linGetMeasEdgeTimeDiffs

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetMeasEdgeTimeDiffs(dword arrSize, float timeDiffs[]);
```

## Description

This function retrieves the result of a falling edge difference measurement which has been started with linMeasEdgeTimeDiffs. Note that for each byte measured four time differences will be returned, although all of them might be 0 (if there had been only one falling edge in the measured byte). This means that time differences 0 to 3 contain the values for the first measured byte, time differences 4 to 7 contain the values for the second measured byte, etc.

The results are sorted in ascending order by the indices of the measured bytes.

## Parameters

| Name | Description |
|---|---|
| arrSize | The size of the timeDiffs array. |
| timeDiffs | The array which will receive the measured time differences. The unit of the measured times is nanoseconds. The first time difference of a byte always relates to the falling edge of the start bit. |

## Return Values

Returns the number of time differences copied into the timeDiffs-array.

## Example

See example for linMeasEdgeTimeDiffs.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
