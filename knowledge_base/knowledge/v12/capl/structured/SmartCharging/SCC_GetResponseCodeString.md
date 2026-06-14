# SCC_GetResponseCodeString

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetResponseCodeString ( char ResponseCode[] )
```

## Description

Gets the response code.

## Return Values

Queries the response code string (to the output buffer). This allows for evaluating its actual semantics, whereas each callback only returns a binary value indicating OK or FAILED.

## Availability

| Since Version |
|---|
