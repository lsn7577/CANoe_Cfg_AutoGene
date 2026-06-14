# OnMostTimingMode

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostTimingMode(long mode)
```

## Description

The OnMostTimingMode() event procedure is called if the timing mode of the MOST hardware has been changed.

Supplemental information can be called up within this procedure by the mostEventChannel, mostEventTime and mostEventOrigTime functions.

Controller events are passed through CAPL nodes. Please use the Multibus Filter or MOST Filter to filter these events in node chains.

## Parameters

| Name | Description |
|---|---|
| 0 | Timing Slave |
| 1 | Timing Master |

## Return Values

—

## Availability

| Since Version |
|---|
