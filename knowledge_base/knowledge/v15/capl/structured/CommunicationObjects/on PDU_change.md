# on PDU_change

> Category: `CommunicationObjects` | Type: `event`

## Description

The event procedure is called whenever the specified PDU is changed, but not if it is simply updated without a value change. You can use the event procedure only for PDUs of the new communication concept of CANoe.

## Example

```c
on PDU_Change Mirrors::MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPdu
{
  write("Status %d at time %I64d", $this.health, this.ChangeTimeNS);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| ChangeTimeNS Last time the value was changed, in nanoseconds since measurement start. | int64 | Read only |
| UpdateTimeNS Last time the value was updated, in nanoseconds since measurement start. | int64 | Read only |
| <SignalName> Value of the signal. Must be accessed with $this. | <data type of the signal> | Read only |
