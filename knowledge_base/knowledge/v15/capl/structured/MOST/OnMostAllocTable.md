# OnMostAllocTable

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostAllocTable();
```

## Description

OnMostAllocTable is called as soon as the hardware interface detects a change in the MOST allocation table. The allocation table contains the reservation status of the synchronous MOST channels.

Supplemental information can be called up within this procedure by the mostEventChannel, mostEventTime and mostEventOrigTime functions.

Controller events are passed through CAPL nodes. Please use the Multibus Filter or MOST Filter to filter these events in node chains.

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1: MOST25 7.1 SP4: MOST150 7.2 SP3: MOST50 | 5.1: MOST25 7.1 SP4: MOST150 7.2 SP3: MOST50 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
