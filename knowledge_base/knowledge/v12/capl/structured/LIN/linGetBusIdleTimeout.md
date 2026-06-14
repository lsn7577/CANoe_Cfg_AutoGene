# linGetBusIdleTimeout

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetBusIdleTimeout()
```

## Description

This function returns the currently set bus idle timeout. Depending on the protocol version, the timeout will be specified in bit times (LIN 1.x and Cooling) or in milliseconds (all others).

## Return Values

On success, returns the bus idle timeout, otherwise zero.

## Availability

| Since Version |
|---|
