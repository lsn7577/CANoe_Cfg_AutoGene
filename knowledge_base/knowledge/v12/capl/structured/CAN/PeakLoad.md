# PeakLoad

> Category: `CAN` | Type: `function`

## Syntax

```c
long PeakLoad ()
CANx.PeakLoad
```

## Description

Returns the peakload of channel x.

Valid x values: 1…32

## Return Values

Peakload of channel x in percent.

## Example

```c
write ("CAN1 peakload = %d", CAN1.PeakLoad);
```

## Availability

| Since Version |
|---|
