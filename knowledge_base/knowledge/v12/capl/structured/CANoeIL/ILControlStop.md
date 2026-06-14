# ILControlStop

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILControlStop()
```

## Description

Sending is completely stopped. In this state the interaction layer is inoperative. Neither function calls, nor signal changes are considered during its inactivity and on its activation (by ILControlStart).

## Return Values

0: No error.

## Availability

| Since Version |
|---|
