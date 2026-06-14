# mostSetMasterMode, mostGetMasterMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetMasterMode(long channel, long mode);
long mostGetMasterMode(long channel);
```

## Description

Configures the timing master as static or non-static master. A non-static master shuts the network down if there is for example no signal at its optical input, whereas a static master keeps the network running independently from the input signal.

mostSetMasterMode becomes operative with the next call of mostSetTimingMode.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| mode | 0: static master1: non-static master |

## Example

```c
// configure bus interface as non-static timing master
mostSetMasterMode(1, 1);
mostSetTimingMode(1, 1);
```

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
