# OnMostMacAdr

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostMacAdr(int64 macAdr)
```

## Description

The MAC address (48 bit) of the hardware interface to the MOST bus has changed.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the MOST Application Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
