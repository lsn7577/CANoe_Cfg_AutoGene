# TestWaitForDiagKLineByteTransmitted

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagKLineByteTransmitted(dword timeout_ms); // form 1
```

## Description

Waits for the occurrence of a transmitted byte. Should the byte not occur before the expiration of the time timeout_ms, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
