# BusLoad

> Category: `CAN` | Type: `function`

## Syntax

```c
long BusLoad ()
CANx.BusLoad
```

## Description

Returns the current busload of channel x.

Valid x values: 1…32

## Return Values

Current busload of channel x in percent.

## Example

```c
write ("CAN1 busload = %d", CAN1.BusLoad);
```

## Availability

| Since Version |
|---|
