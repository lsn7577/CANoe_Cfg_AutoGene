# CANstressSetDisturbanceSequence

> Category: `CANstress` | Type: `function`

## Syntax

```c
void CANstressSetDisturbanceSequence (char sequence[], dword resolution);
```

## Description

Sets the disturbance sequence.

## Parameters

| Name | Description |
|---|---|
| sequence | Describes the sequence as a string of 0, 1, a, and u characters, whereby 0 stands for dominant, 1 for recessive, a for an analog disturbance and u for undisturbed. A disturbance sequence can contain up to 2048 characters. |
| resolution | Sets the resolution of the disturbance sequence. Possible values are 0 for bit times and 1 for BTL cycles. |

## Return Values

—

## Example

```c
CANstressSetDisturbanceSequence(“uuuu1111“, 0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
