# Iso11783IL_TIMSetServerHeartbeatCounter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetServerHeartbeatCounter(byte hearbeatCounter); // form 1
long Iso11783IL_TIMSetServerHeartbeatCounter(dbNode server, byte hearbeatCounter); // form 2
```

## Description

Sets the heartbeat counter of message TIM_ServerStatus_Msg. The next status message uses the new heartbeat counter value.

If the new value is less than 251 (0xFB), then the counter is incremented as usual (after reaching the value 250 (0xFA) the counter restarts with value 0 again).

If the new value is 251 (0xFB), then after a single transmission of the status message with the value 251 the counter is reset to value 0 and incremented as usual.

If the new value of the counter is 252 or greater, then the status message is always sent with the same heartbeat counter value.

## Parameters

| Name | Type | Description |
|---|---|---|
| server |  | TIM server simulation node to apply the function. |
| 251 | 0xFB | Reset of Heartbeat counter |
| 252, 253 | 0xFC, 0xFD | Reserved values |
| 254 | 0xFE | Error condition on sender |
| 255 | 0xFF | Graceful shutdown |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
