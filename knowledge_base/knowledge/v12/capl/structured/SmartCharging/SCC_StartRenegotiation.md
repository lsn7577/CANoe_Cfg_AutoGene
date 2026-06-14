# SCC_StartRenegotiation

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_StartRenegotiation ( )
```

## Description

Initiates a renegotiation procedure while inside the charge loop.

The charge point may initiate a renegotiation procedure by sending an EVSENotification with the value ReNegotiation (see SCC_SetEVSENotification).

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
