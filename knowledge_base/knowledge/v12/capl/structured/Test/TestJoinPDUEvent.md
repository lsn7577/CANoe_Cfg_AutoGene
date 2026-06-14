# TestJoinPDUEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinPDUEvent (dbPDU aPDU, dword flags1); // form 1
```

## Description

Completes the current set of joined events with the transmitted event. This function does not wait.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

## Return Values

-6: Parse error, PDU is specified as string, but the name cannot be resolved or the PDU header ID cannot be found.

## Availability

| Since Version |
|---|
