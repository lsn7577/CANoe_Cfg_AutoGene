# resetFlexRayCCEx

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long resetFlexRayCCEx (int channel, int wuChMask, int wuCount, int wuTxIdle, int wuTxLow, char[] cfg);
```

## Description

This function initializes the FlexRay Communication Controller (CC) and generates the specified wake-up pattern before reintegration in the cluster or the start-up.

## Parameters

| Name | Description |
|---|---|
| channel | FlexRay channel (cluster number) |
| 1 | Channel A |
| 2 | Channel B |
| wuCount | Number of repetitions (2 – 63) of the wake-up symbol in a wake-up pattern. |
| wuTxIdle | This number designates the number of idle bits in a wake-up symbol. According to protocol specification, this should result in 18 µs. |
| wuTxLow | This number designates the number of low bits in a wake-up symbol. According to protocol specification, this should result in 6 µs. |
| cfg | Character data array. This is currently not used and is of no importance. |

## Return Values

—

## Example

Example 1

The following program resets the FlexRay interface of the attached channel and sends a wake-up (if network is idle), when the <W> key is pressed.

Example 2

```c
on key 'w'
{
   int wuChMask = 3;    // send wake-up on both channels
   int wuCount  = 4;    // send symbol 2 times (range 2-63)
   int wuTxIdle = 180;  // idle time of symbol in bit (range 0-255)
   int wuTxLow = 60;    // low time of symbol in bit (range 0-63)
   CHAR cfg[1];         // <cfg> -> not used yet
   resetFlexRayCCEx(%CHANNEL%,wuChMask,wuCount,wuTxIdle,wuTxLow,cfg);
   Write("FlexRay CC %d is reset and sending a wakeup.", %CHANNEL%);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
