# OnMostSBC

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostSBC(long value)
```

## Description

A change is made to the Synchronous Bandwidth Register of the MOST chips, i.e. the distribution into synchronous/asynchronous transmission bandwidth. The 'value' parameter contains the new value of the Synchronous Bandwidth Register (see also Datasheet for the OS8104).

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
