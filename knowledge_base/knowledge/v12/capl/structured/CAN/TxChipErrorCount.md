# TxChipErrorCount

> Category: `CAN` | Type: `function`

## Syntax

```c
long TxChipErrorCount ()
CANx.TxChipErrorCount
```

## Description

Returns the current number of Tx errors in the CAN receiver of channel x.

Valid x values: 1…32

## Return Values

Current number of errors in the CAN receiver of channel x.

## Example

```c
write ("Number of Tx errors in receiver of CAN1 = %d", CAN1.TxChipErrorCount);
```

## Availability

| Since Version |
|---|
