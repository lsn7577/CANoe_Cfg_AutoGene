# on value_change

> Category: `CommunicationObjects` | Type: `event`

## Syntax

```c
on value_change <value>
```

## Description

The event procedure is called whenever the specified value changes. It’s not called when the value is updated, but does not change. You can use the event procedure for all values of communication objects, including e.g. signal and event values, LatestCall or LatestReturn of methods, service states, etc.

## Example

```c
on value_change MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition
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
