# linETFSetDirtyFlag

> Category: `LIN` | Type: `function`

## Syntax

```c
long linETFSetDirtyFlag(long assocId, long dirty)
```

## Description

With this function it is possible to set/clear the dirty flag of an associated frame. If the dirty flag of an associated frame is set when the corresponding event-triggered frame is being requested, then the LIN hardware will try to transmit the associated frame's data. The dirty flag gets reset automatically when the associated frame has been sent successfully – either via the event-triggered frame or unconditionally.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
