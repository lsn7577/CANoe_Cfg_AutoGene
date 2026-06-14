# ILNodeSetPDUTimingCyclic

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeSetPDUTimingCyclic (dbMessage, long TrueOrFalse, long offset, long period, long disturbanceCount, long flags)
```

## Description

Overrides the defined cyclic-timing from the database. Possibly two timings (False and True) exist in parallel and are selected upon the current transmission mode of the PDU.

## Return Values

0: No error

## Availability

| Since Version |
|---|
