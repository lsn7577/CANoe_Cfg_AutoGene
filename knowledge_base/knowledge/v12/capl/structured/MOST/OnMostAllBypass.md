# OnMostAllBypass

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostAllBypass(long mode)
```

## Description

The event procedure OnMostAllBypass is called if the bypass of the MOST chip was opened or closed. The variable mode contains the new state.

Supplemental information can be called up within this procedure by the mostEventChannel, mostEventTime and mostEventOrigTime functions.

Controller events are passed through CAPL nodes. Please use the Multibus filter or MOST Filter to filter these events in node chains.

## Return Values

—

## Availability

| Since Version |
|---|
