# FRSSetTrigElem

> Category: `FRStress` | Type: `function`

## Syntax

```c
long FRSSetTrigElem( long triggerCondition, long triggerElement, long triggerValue);
```

## Description

Adds a numerical trigger value to the respective trigger condition. A complex trigger condition can be created through multiple calls.

## Parameters

| Name | Description |
|---|---|
| triggerCondition | Values: 1-4 |
| 1 | PPI |
| 2 | NFI |
| 3 | SFI |
| 4 | SUPFI |
| 5 | FrameId |
| 6 | PayloadLength |
| 7 | HeaderCR |
| 8 | cycleCount |
| 9 | BSS1 |
| 10 | BSS2 |
| 11 | BSS3 |
| 12 | BSS4 |
| 13 | BSS5 |
| 14 | TrailerBSS1 |
| 15 | TrailerBSS2 |
| 16 | TrailerBSS3 |
| 17 | TrailerCRCByte1 |
| 18 | TrailerCRCByte2 |
| 19 | TrailerCRCByte |
| 20 | FES |
| triggerValue | Numerical value of the respective frame field. The respective maximum values must be noted. For example, the Payload Length must not exceed the maximum value of 127 words. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.2 | — | — | — | 1.1 |
| Restricted To | — | FlexRay Digital, analog, Scope mode | — | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
