# ILControlStart

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILControlStart ()
```

## Description

Cyclical sending starts; setting signals is now possible. Signal changes that occurred while the interaction layer was switched off (by ILControlStop or ILControlSimulationOff) are not considered on its activation.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
