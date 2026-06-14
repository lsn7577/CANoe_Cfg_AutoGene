# OnMostAllBypass

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostAllBypass(long mode);
```

## Description

The event procedure OnMostAllBypass is called if the bypass of the MOST chip was opened or closed. The variable mode contains the new state.

Supplemental information can be called up within this procedure by the mostEventChannel, mostEventTime and mostEventOrigTime functions.

Controller events are passed through CAPL nodes. Please use the Multibus filter or MOST Filter to filter these events in node chains.

## Parameters

| Name | Description |
|---|---|
| mode | 0: The bypass is opened.1: The bypass is closed. The MOST hardware is transparent to other devices on the ring. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
