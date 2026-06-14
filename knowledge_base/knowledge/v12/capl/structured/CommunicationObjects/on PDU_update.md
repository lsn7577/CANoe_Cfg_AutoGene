# on PDU_update

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on PDU_update <PDU>
```

## Description

The event procedure is called whenever the specified PDU is updated, regardless of whether its value has changed. You can use the event procedure only for PDUs of the new communication concept of CANoe.

## Example

```c
on PDU_Update Mirrors::MirrorAdjustment.consumerSide[CANoe,LeftMirror].StatusPdu
{
  write("Status %d at time %I64d", $this.health, this.ChangeTimeNS);
}
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| ChangeTimeNS Last time the value was changed, in nanoseconds since measurement start. | int64 | Read only |
| UpdateTimeNS Last time the value was updated, in nanoseconds since measurement start. | int64 | Read only |
| <SignalName> Value of the signal. Must be accessed with $this. | <data type of the signal> | Read only |
