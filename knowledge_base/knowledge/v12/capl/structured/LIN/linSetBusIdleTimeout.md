# linSetBusIdleTimeout

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetBusIdleTimeout(dword timeout)
```

## Description

This function sets a new bus idle timeout. Depending on the protocol version, the timeout will be specified in bit times (LIN 1.x and Cooling) or in milliseconds (all others).

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
