# linActivateCollisionResolution

> Category: `LIN` | Type: `function`

## Syntax

```c
long linActivateCollisionResolution(long etfId, long activate)
```

## Description

Activates or deactivates the Master node's automatic collision resolution of an event-triggered frame.

Per default the automatic collision resolution is active. If a collision occurs for any event-triggered frame, the Master resolves this collision by sending headers for all associated frames using the event-triggered frame slot. After all associated frames have sent new data, the Master sends the event-triggered frame header until the next collision occurs.

If the automatic collision resolution is deactivated, the Master always sends the event-triggered frame's header.

If the Master node is not simulated or no schedule tables are defined, then this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
