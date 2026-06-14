# linSetGlobalTimeoutPrevention

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetGlobalTimeoutPrevention(dword on);
```

## Description

Activates/deactivates the global timeout prevention for transceivers with a dominant timeout. If active, the cab/piggy will use an inbuilt transistor to keep the bus signal at a dominant level after the dominant timeout stopped the transceiver from transmitting a dominant signal.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
