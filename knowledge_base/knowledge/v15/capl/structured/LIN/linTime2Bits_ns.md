# linTime2Bits_ns

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linTime2Bits_ns(int64 time): // form 1
dword linTime2Bits_ns(dword channel, int64 time); // form 2
```

## Description

This function converts specified system times to bit times. The conversion is done using the current baud rate on the channel determined by the CAPL program context.

## Parameters

| Name | Description |
|---|---|
| time | System time to be converted [in ns]. |
| channel | Channel number, whose baud rate will be used. |

## Return Values

Resulting bit time.

## Example

Extract sync break length of LIN frames

```c
on linFrame *
{
..dword bitTimeSyncBreak;
  bitTimeSyncBreak = linTime2Bits_ns(this.breakLen);
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
