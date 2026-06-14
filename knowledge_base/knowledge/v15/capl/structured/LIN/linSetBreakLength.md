# linSetBreakLength

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetBreakLength(dword syncBreakLen, dword syncDelLen); // form 1
dword linSetBreakLength(float syncBreakLen, float syncDelLen); // form 2
```

## Description

With this function it is possible to change length of break/synch symbol parts. Particularly the length of its synch break (dominant bits) and its synch delimiter (recessive bits).

The version using float parameters allows setting the break and delimiter lengths in increments of 1/16th bits, but the unit still is bit times (i.e. linSetBreakLength(14.5, 2.5) will set a break length of 14 8/16th bit times and a delimiter length of 2 8/16th bit times). Note that setting non-integer break and delimiter lengths is not supported by every hardware.

## Parameters

| Name | Description |
|---|---|
| syncBreakLen | Synch break length in bit times. Default value: 18 Value range: 10..30 |
| syncDelLen | Synch delimiter length in bit times. Default value: 2 Value range: 1..30 |
| Values required for a LIN compliant header: | syncBreakLength >= 13 syncDelimiterLength >= 1 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | — | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
