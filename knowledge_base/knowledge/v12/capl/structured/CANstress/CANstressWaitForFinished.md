# CANstressWaitForFinished

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressWaitForFinished( dword timeout );
```

## Description

Waits until the CANstress hardware is in the state Finished.

## Parameters

| Name | Description |
|---|---|
| Note With timeout = 0 an infinite time is waited until the state Finished occurs. Thus the additional test procedure is blocked if the state Finished is not reached. |  |

## Return Values

0: If successful.

## Availability

| Since Version |
|---|
