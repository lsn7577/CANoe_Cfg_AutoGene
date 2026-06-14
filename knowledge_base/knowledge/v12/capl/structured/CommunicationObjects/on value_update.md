# on value_update

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on value_update <value>
```

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

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| ChangeTimeNS Last time the value was changed, in nanoseconds since measurement start. | int64 | Read only |
| UpdateTimeNS Last time the value was updated, in nanoseconds since measurement start. | int64 | Read only |
