# GBT27930IL_DelayRxMessage

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_DelayRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword delay); // form 1
```

## Description

A message described in the function is only forwarded to the simulation node after the defined delay. As a result, the simulated node reacts to the message only after this delay.

You can also define a system variable which is set if the specified message is received.

To revert this command you can use GBT27930IL_ResetDelayedRxMessage or GBT27930IL_ResetAllDelayedRxMessage.

## Return Values

0: Function has been executed successfully

## Example

```c
—
```

## Availability

| Since Version |
|---|
