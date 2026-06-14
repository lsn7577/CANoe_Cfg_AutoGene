# xlSetLED

> Category: `Other` | Type: `function`

## Syntax

```c
dword xlSetLED(dword ledBitMask, dword ledMode);
```

## Description

Sets the LEDs specified by ledBitMask to the operation mode specified by ledMode. A successful call of xlAcquireLED is necessary before the operation mode of an LED can be set with this function.

This function is only supported on VN8900 devices.

Note that for every successful call of xlAcquireLED on a specific LED, you have to call xlReleaseLED to release this LED again.

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
| Operation Mode | Numeric Value |
| No Change | 0x00000000 |
| LED Off | 0x00000001 |
| LED On Red | 0x00000002 |
| LED Blinking Red | 0x00000004 |
| LED On Green | 0x00000008 |
| LED Blinking Green | 0x00000010 |
| LED On Orange | 0x00000020 |
| LED Blinking Orange | 0x00000040 |
| Note For the LEDs S1 and S2 only the No Change, LED Off and LED On Green operation modes are valid. |  |

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
