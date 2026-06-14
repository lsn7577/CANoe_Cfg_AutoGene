# OnMostCriticalUnlock

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostCriticalUnlock()
```

## Description

A "Critical Unlock" was detected on one of the configured MOST channels. This event occurs if the lock status of the connected MOST hardware does not exhibit a "Lock" (see MOST Spec 2V3 - 3.2.2 NetInterface) after a "Stable Lock" for at least t_Unlock (see MOST Spec 2V3 – 3.9 Timing Definitions).The relevant channel or time stamp of this event can be called up with the mostEventChannel, mostEventTime and mostEventOrigTime functions.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
