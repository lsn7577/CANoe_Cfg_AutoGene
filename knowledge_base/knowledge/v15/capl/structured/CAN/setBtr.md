# setBtr

> Category: `CAN` | Type: `function`

## Syntax

```c
long setBtr(long channel, byte btr0, byte btr1);
```

## Description

Sets another baud rate. The values do not become active until the next call of the function resetCan.

It should be noted that these values depend on the CAN controller used.

## Parameters

| Name | Description |
|---|---|
| 0 | All controllers |
| 1 - 32 | channel 1 - 32 |
| BTR0 | Value of Bit Timing Register 0. |
| BTR1 | Value of Bit Timing Register 1. |

## Return Values

Always 1

## Example

```c
...
setBtr(0, 0x00, 0x3a); // 500 kBaud for 82C200
resetCan(); // activate
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
