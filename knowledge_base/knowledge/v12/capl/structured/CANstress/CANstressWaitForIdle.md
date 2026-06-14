# CANstressWaitForIdle

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressWaitForIdle( dword timeout );
```

## Description

Waits until the CANstress hardware is in the state Idle.

## Parameters

| Name | Description |
|---|---|
| Note With timeout = 0 an infinite time is waited until the state Idle occurs. Thus the additional test procedure is blocked if the state Idle is not reached. |  |

## Return Values

0: If successful.

## Availability

| Since Version |
|---|
