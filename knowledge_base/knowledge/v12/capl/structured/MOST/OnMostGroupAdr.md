# OnMostGroupAdr

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostGroupAdr(long groupadr)
```

## Description

The group address of the hardware interface to the MOST bus has changed. The value of the new group address is in the groupadr parameter.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
