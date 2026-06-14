# linActivateCollisionResolution

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateCollisionResolution(long etfId, long activate);
```

## Description

Activates or deactivates the Master node's automatic collision resolution of an event-triggered frame.

Per default the automatic collision resolution is active. If a collision occurs for any event-triggered frame, the Master resolves this collision by sending headers for all associated frames using the event-triggered frame slot. After all associated frames have sent new data, the Master sends the event-triggered frame header until the next collision occurs.

If the automatic collision resolution is deactivated, the Master always sends the event-triggered frame's header.

## Parameters

| Name | Description |
|---|---|
| etfId | Identifier of event-triggered frame. Value range: 0-59 |
| activate | 0: Disable 1: Enable |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
