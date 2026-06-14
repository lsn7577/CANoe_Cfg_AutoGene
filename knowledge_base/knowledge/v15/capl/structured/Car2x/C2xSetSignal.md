# C2xSetSignal

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSetSignal( char *signalPath, int64 value); //form 1
long C2xSetSignal( char *signalPath, int64 value, char* stationName); //form 2
```

## Description

Sets a signal in a database defined packet.

## Parameters

| Name | Description |
|---|---|
| signalPath | Path to the signal value to be set in the packet. |
| value | New signal value. |
| stationName | Name of the sending station. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1 13.0: form 2 | — | — | — | 2.1 SP3: form 1 5.0: form 2 |
| Restricted To | — | Car2x: form 1 Car2x, Testnodes: form 2 | — | — | — | Car2x: form 1 Car2x, Testnodes: form 2 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
