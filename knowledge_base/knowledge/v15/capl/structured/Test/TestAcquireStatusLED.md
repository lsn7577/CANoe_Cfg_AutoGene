# TestAcquireStatusLED

> Category: `Test` | Type: `function`

## Syntax

```c
long TestAcquireStatusLED(dword ledBitMask);
```

## Description

Can be used in standalone mode to assign the test module state to an LED.

States:

## Parameters

| Name | Description |
|---|---|
| ledBitMask | The LED that wants to be used. Available bit masks under xlAcquireLED.The LED’s Keypad S1 and Keypad S2 cannot be used for test modules. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.6 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | Test nodes | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
