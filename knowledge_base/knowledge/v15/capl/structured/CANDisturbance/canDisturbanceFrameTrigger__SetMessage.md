# canDisturbanceFrameTrigger::SetMessage

> Category: `CANDisturbance` | Type: `method`

## Syntax

```c
long canDisturbanceFrameTrigger::SetMessage(message msg, dword deviceID, dword validityMask);
```

## Description

Sets the frame for the trigger condition. The mask is filled automatically with the data of the frame. The used data can be configured with the validity mask.

## Parameters

| Name | Type | Description |
|---|---|---|
| msg |  | The frame data that should be used for the frame trigger. |
| deviceID |  | The device ID of the CAN Disturbance Interface. |
| Bit |  | Identifier CBFF* CEFF* FBFF* FEFF* |
| 0 | IDBase | ID28-18 |
| 1 |  | IDExtended — ID17-0 — ID17-0 |
| 2 |  | RemoteBase RTR SRR RRS SRR |
| 3 | IDE | IDE |
| 4 |  | RemoteExt — RTR — RRS |
| 5 | FDF | FDF |
| 6 |  | Reserved — r0 res res |
| 7 |  | BRS — BRS BRS |
| 8 |  | ESI — — ESI ESI |
| 9 | DLC | DLC0-DLC3 |
| 10 |  | Data D0-D7 D0-D7 D0-D63 D0-D63 |
| 11 |  | StuffCount — — StuffCount StuffCount |
| 12 | CRC | CRC (length depends on format and on DLC) |
| 13 | CRCDelimiter | CRCdel |
| 14 | ACKSlot | ACK |
| 15 | ACKDelimiter | ACKdel |
| 16 | EndOfFrame | EOF |

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
