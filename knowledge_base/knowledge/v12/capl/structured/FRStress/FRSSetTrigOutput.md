# FRSSetTrigOutput

> Category: `FRStress` | Type: `function`

## Syntax

```c
FRSSetTrigOutput (int triggermask, int triggerlevel);
```

## Description

Activates the trigger output of FRsstress. The trigger output can react to individual trigger lowerings or to a combination of sources.

## Parameters

| Name | Description |
|---|---|
| 1 | Trigger1 |
| 2 | Trigger2 |
| 4 | Trigger3 |
| 8 | Trigger4 |
| 16 | SW Trigger |
| 32 | External Trigger |

## Return Values

0: successful

## Availability

| Since Version |
|---|
