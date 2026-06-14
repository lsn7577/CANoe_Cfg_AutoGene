# SCC_AuthorizationReq

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_AuthorizationReq ( byte SessionID[] )
```

## Description

The callback is called as soon as an Authorization Request is received.

The challenge optionally transmitted in this request can be queried with SCC_GetGenChallenge.

## Return Values

—

## Availability

| Since Version |
|---|
