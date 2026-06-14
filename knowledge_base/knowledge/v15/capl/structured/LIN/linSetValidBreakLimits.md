# linSetValidBreakLimits

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetValidBreakLimits(dword breakMin16thBits, dword breakMax16thBits, dword delMin16thBits, dword delMax16thBits);
```

## Description

Sets limits for the accepted sync break and delimiter lengths. Any sync break and delimiter outside of this range is considered invalid, resulting in a receive error. Note that this function does not change the current sync break and delimiter length sent by a simulated master. This function can also be called in slave mode to test an external master.

This function does not change the header length restrictions of 47.6 bit times for LIN 2.x and 49 bit times for LIN 1.x. This means that a header can still be invalid even if the modified sync break and delimiter limits are met.

## Parameters

| Name | Description |
|---|---|
| breakMin16thBits | The minimum legal sync break length, specified in units of 1/16th bit times. Range: 152 (9.5 bit times) – 784 (49 bit times) |
| breakMax16thBits | The maximum legal sync break length, specified in units of 1/16th bit times. Range: 152 (9.5 bit times) – 784 (49 bit times), has to be greater than breakMin16thBits |
| delMin16thBits | The minimum legal sync delimiter length, specified in units of 1/16th bit times. Range: 1 – 784 (49 bit times) |
| delMax16thBits | The maximum legal sync delimiter length, specified in units of 1/16th bit times. Range: 1 – 784 (49 bit times), has to be greater than delMin16thBits |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 6.1 | — | — | — | 1.0 |
| Restricted To | LIN Real bus mode | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
