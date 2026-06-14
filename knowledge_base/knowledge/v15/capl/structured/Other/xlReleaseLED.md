# xlReleaseLED

> Category: `Other` | Type: `function`

## Syntax

```c
dword xlReleaseLED(dword ledBitMask);
```

## Description

Releases the specified LEDs after they were successfully acquired with a call of xlAcquireLED.

This function is supported by the following device: VN8900 (driver version > 7.5)

## Parameters

| Name | Description |
|---|---|
| LED | Numeric Value |
| Module (M) | 0x001 |
| CAN Channel 1 | 0x008 |
| CAN Channel 2 | 0x010 |
| CAN Channel 3 | 0x020 |
| CAN Channel 4 | 0x040 |
| FlexRay Channel 1 A | 0x080 |
| FlexRay Channel 1 B | 0x100 |
| Keypad S1 | 0x200 |
| Keypad S2 | 0x400 |

## Example

See xlAcquireLED

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP6 | 7.2 SP6 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
