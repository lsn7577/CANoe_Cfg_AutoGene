# TestWaitForDiagKLineFrameTransmitted

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagKLineFrameTransmitted(dword timeout_ms); // form 1
```

## Description

Waits for the occurrence of a transmitted valid message. Should the message not occur before the expiration of the time timeout_ms, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
