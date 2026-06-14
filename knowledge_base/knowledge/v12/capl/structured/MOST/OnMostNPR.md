# OnMostNPR

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostNPR(long npr)
```

## Description

The Node Position Register of the MOST chip, i.e. the position of the device in the MOST ring, has changed. The parameter value contains the new value of the Node Position Register.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
