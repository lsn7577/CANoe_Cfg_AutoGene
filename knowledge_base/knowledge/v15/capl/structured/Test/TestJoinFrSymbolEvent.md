# TestJoinFrSymbolEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinFrSymbol ()
long TestJoinFrSymbol (dword aSymbolType, dword aChannelMask)
```

## Description

Completes the current set of "joined events" with the FlexRay symbol event.

This function does not wait.

## Parameters

| Name | Description |
|---|---|
| 0 | unknown |
| 1 | CAS |
| 2 | MTS |
| 3 | Wakeup |
| aChannelMask | Identifies the FlexRay channel of the communication controller. A value of 1 will wait for the symbol on channel A, 2 will wait for it on channel B and 3 on any channel (A/B). |

## Example

For an example see function TestWaitForFrSymbol.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
