# GNSSPauseSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSPauseSpeed();
```

## Description

This function temporarily sets the speed to zero. The GNSS receiver thus remains in place where it is, but continues to send position data. This also applies to playing back a position file.

You can use the GNSSContinueSpeed function to accept the old speed again.

## Return Values

error code

## Example

```c
GNSSPauseSpeed();
```

## Availability

| Since Version |
|---|
