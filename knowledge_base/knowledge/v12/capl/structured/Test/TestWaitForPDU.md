# TestWaitForPDU

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForPDU (dbPDU aPDU, dword flags1, dword aTimeout); // form 1
```

## Description

Waits for the occurrence of the specified PDU. Should the PDU not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no PDU is specified the wait condition is resolved on any PDU.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

## Return Values

-6: Parse error, PDU is specified as string, but the name cannot be resolved or the PDU header ID cannot be found.

## Availability

| Since Version |
|---|
