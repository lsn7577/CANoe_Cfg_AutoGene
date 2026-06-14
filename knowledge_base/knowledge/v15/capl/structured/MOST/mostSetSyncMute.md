# mostSetSyncMute

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncMute(long channel, long device, long mute);
```

## Description

Activates or deactivates the audio input or output of the bus interface.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| 0 | Line-In |
| 1 | Line-Out |
| 2 | S/PDIF In (VN2640 only) |
| 3 | S/PDIF Out (VN2640 only) |
| 0 | Active (mute off) |
| 1 | Inactive (mute on) |

## Return Values

See error codes

## Example

See CANoe online help MOST Access to Analog Audio Channels (Line In/ Headphone Out).

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 Not in StopMeasurement | MOST25 MOST50 MOST150 Not in StopMeasurement | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
