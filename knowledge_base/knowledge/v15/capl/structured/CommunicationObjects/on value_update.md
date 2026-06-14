# on value_update

> Category: `CommunicationObjects` | Type: `event`

## Description

The event procedure is called whenever the specified value is updated, regardless of whether the value has changed. You can use the event procedure for all values of communication objects, including e.g. signal and event values, LatestCall or LatestReturn of methods, service states, etc.

## Example

```c
on value_update MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition
{
  write("New position received: (%d,%d)", $this.x.phys, $this.y.phys);
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
