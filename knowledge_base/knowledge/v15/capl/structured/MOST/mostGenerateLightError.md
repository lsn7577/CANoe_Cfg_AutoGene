# mostGenerateLightError

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateLightError(long channel, long lightofftime, long lightontime, long repeat);
```

## Description

Starts (repeat > 0) or stops (repeat = 0) generation of Light-ON-OFF transitions.

For OptoLyzerOL3150o: The stress network interface controller (NIC) must have active bypass or bypass opened (see mostSetStressNodeParameter).

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| lightofftime | Time during which no light is emitted (in ms). |
| lightontime | Time during which modulated light is emitted (in ms). |
| 0 | Stop Light-Off-On transitions |
| >0 | Number of Light-Off-On transitions |
| 0xFFFF | Generate Light-Off-On transitions continually |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | — | — | — | —✔ |
| Restricted To | MOST25 MOST150 After measurement start Not in Stopmeasurement | MOST25 MOST150 After measurement start Not in Stopmeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
