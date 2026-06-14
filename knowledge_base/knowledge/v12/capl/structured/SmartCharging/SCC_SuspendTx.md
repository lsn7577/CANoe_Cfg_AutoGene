# SCC_SuspendTx

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SuspendTx ( long NumberOfMessages )
```

## Description

Skips the sending of the following messages depending on the parameter value.

## Parameters

| Name | Description |
|---|---|
| Value | Behavior |
| -1 | Sending of all further messages is suspended. |
| 0 | Resume. Starting from current state messages are send. |
| >0 | The following NumberOfMessages are suspended. |

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
