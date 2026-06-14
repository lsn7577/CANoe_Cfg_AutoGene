# RxChipErrorCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long RxChipErrorCount ()
CANx.RxChipErrorCount
```

## Description

Returns the current Rx error count in the receiver of channel x.

Valid x values: 1…32

## Return Values

Current error count in the receiver of channel x.

## Example

```c
write ("Rx error count in the receiver of CAN1 
 = %d", CAN1.RxChipErrorCount);
```

## Availability

| Since Version |
|---|
