# linETFSendOnSignalUpdate

> Category: `LIN` | Type: `function`

## Syntax

```c
long linETFSendOnSignalUpdate(long etfId, long active)
```

## Description

With this function it is possible to activate/deactivate the automatic responses on a certain event-triggered frame request in the case of a signal update on its associated frame(s). This concerns all Slave tasks publishing the responses to the specified event-triggered frame.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
