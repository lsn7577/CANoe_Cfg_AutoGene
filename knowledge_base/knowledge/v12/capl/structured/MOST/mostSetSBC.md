# mostSetSBC

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSBC (long channel, long sbcvalue)
```

## Description

This function sets the "Synchronous Bandwidth Control (SBC) Register" of the MOST hardware chip to the given value.

The function is only practically applicable if the hardware connected to the channel is in master mode.

The newly set value is only accepted once a "DeAllocate" message re-releases all synchronous channel assignments.

## Availability

| Since Version |
|---|
