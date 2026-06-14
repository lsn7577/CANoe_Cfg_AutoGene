# GNSSContinueSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSContinueSpeed();
```

## Description

If the speed of the simulation was temporarily reset with the GNSSPauseSpeed function (set to zero), this function now restores the old speed.

## Return Values

error code

## Example

```c
GNSSContinueSpeed();
```

## Availability

| Since Version |
|---|
