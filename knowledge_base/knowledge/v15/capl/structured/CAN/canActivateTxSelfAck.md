# canActivateTxSelfAck

> Category: `CAN` | Type: `function`

## Syntax

```c
int canActivateTxSelfAck (int channel, int activate);
```

## Description

Activates/deactivates the transmit self ack feature in CANoe for the defined channel.

## Parameters

| Name | Description |
|---|---|
| channel | CAN channel |
| activate | 0 = deactivate 1 = activate |

## Example

```c
on key a'
{
  int channel
  int activate;
  // Activate TX Self-ACK for CAN channel 1
  channel = 1;
  activate = 1;
  canActivateTXSelfAck(channel, activate);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
