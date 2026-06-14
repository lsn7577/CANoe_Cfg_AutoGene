# CANstressWaitForPending

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressWaitForPending( dword timeout);
```

## Description

Waits until the CANstress hardware is in the state Pending.

## Parameters

| Name | Description |
|---|---|
| Note With timeout = 0 an infinite time is waited until the state Pending occurs. Thus the additional test procedure is blocked if the state Pending is not reached. |  |

## Return Values

0: If successful.

## Availability

| Since Version |
|---|
