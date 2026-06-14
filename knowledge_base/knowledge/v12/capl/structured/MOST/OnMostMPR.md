# OnMostMPR

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostMPR(long value)
```

## Description

A change is made to the Maximum Position Register of the MOST chip, i.e. the number of devices in the MOST ring. The value parameter contains the new value of the Maximum Position Register.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
