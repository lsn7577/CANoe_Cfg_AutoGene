# canDisturbanceSequence::AppendToSequence

> Category: `CANDisturbance` | Type: `method`

## Syntax

```c
void canDisturbanceSequence::AppendToSequence(word segmentLength, char segmentValue);
```

## Description

Adds a segment to a sequence. If the maximum number of segments is reached, the function always returns 0.

Maximum number of segments: 4096

## Parameters

| Name | Description |
|---|---|
| segmentLength | The segment length in FPGA ticks |
| d | Dominant level |
| r | Recessive level (dominant level is not disturbed on bus) |
| R | Recessive stress level (dominant level is disturbed on bus) |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 10.0 SP3 recommended | — | — | — | 2.2 |
| Restricted To | — | CAN CAN Disturbance Interface | — | — | — | CAN CAN Disturbance Interface |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
