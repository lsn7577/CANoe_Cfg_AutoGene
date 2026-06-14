# OnMostAllocTable

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostAllocTable()
```

## Description

OnMostAllocTable is called as soon as the hardware interface detects a change in the MOST allocation table. The allocation table contains the reservation status of the synchronous MOST channels.

Supplemental information can be called up within this procedure by the mostEventChannel, mostEventTime and mostEventOrigTime functions.

Controller events are passed through CAPL nodes. Please use the Multibus Filter or MOST Filter to filter these events in node chains.

## Return Values

—

## Availability

| Since Version |
|---|
