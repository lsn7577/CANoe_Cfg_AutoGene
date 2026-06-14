# linBits2Time_ns

> Category: `LIN` | Type: `function`

## Syntax

```c
int64 linBits2Time_ns(dword bitTimes);
int64 linBits2Time_ns(dword channel, dword bitTimes);
```

## Description

Converts specified bit time to an absolute time.

The absolute time is calculated using the current baud rate on the channel determined by the CAPL program context.

## Parameters

| Name | Description |
|---|---|
| bitTimes | Time in bits. |
| channel | Channel number, whose baud rate will be used. |

## Return Values

Absolute time in ns.

## Example

Convert header bit time of a LIN frame to ns

```c
on linFrame *
{
int64 headerTimeInNanoSeconds; // time in ns
headerTimeInNanoSeconds = linBits2Time_ns(this.LIN_HeaderTime);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 | 7.0 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
