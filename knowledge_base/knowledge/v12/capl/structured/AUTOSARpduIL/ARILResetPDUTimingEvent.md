# ARILResetPDUTimingEvent

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILResetPDUTimingEvent (dbMessage, long TrueOrFalse);
```

## Description

Resets the event-timing to the values from the database. Possibly two timings (False and True) exist in parallel and are selected upon the current transmission mode of the PDU.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
