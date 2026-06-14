# OnMostNetOn / OnMostInitReady

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostNetOn( )
```

## Description

The NetOn event (first "Stable Lock" after the loop has been woken up) has occurred on one of the configured MOST channels. The relevant channel or time stamp of this event can be called up with the mostEventChannel, mostEventTime and mostEventOrigTime functions.

In the MOST Specification 3V0 the NetOn event was renamed to InitReady. However, the meaning is still the same. The Trace Window displays this information in the disassembly column and the detail view. In CAPL there is an additional event procedure OnMostInitReady (since version 7.2). To assure the correct operation of existing CAPL programs, the event handler OnMostNetOn is still called.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

## Return Values

—

## Availability

| Since Version |
|---|
