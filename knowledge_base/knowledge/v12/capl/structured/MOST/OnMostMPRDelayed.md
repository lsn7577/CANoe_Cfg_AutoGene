# OnMostMPRDelayed

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostMPRDelayed(long mpr)
```

## Description

The value of the maximum position register in the MOST chip has not changed since the last network change event (NCE) for t_MPRDelayed (see MOST Spec 2V3 – 3.9 Timing Definitions). The mpr parameter indicates the value of the maximum position register.

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
