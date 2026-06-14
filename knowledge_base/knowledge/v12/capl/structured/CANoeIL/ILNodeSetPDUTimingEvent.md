# ILNodeSetPDUTimingEvent

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetPDUTimingEvent (dbMessage, long TrueOrFalse, long enable, long repetitionPeriod, long repetitionCount, long debounceDelay, long disturbanceCount, long flags)
```

## Description

Overrides the defined event timing from the database. Possibly two timings (False and True) exist in parallel and are selected upon the current transmission mode of the PDU.

Only when an enabled event timing exists, the PDU can be transmitted regardless of any cyclic timing if any transfer property of a signal or signal group is firing/triggering.

## Return Values

0: No error

## Availability

| Since Version |
|---|
