# mostSetShutDownFlagUsage, mostGetShutDownFlagUsage

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetShutDownFlagUsage(long channel, long mode);
long mostGetShutDownFlagUsage(long channel);
```

## Description

For test purposes the stress network interface controller in the OptoLyzer G2 3150o is able to suppress the shutdown flag for the next node by calling.

mostSetShutDownFlagUsage with mode 0.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| mode | 0: clear shutdown flag 1: default mode |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
