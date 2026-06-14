# frSetPduFilter

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frSetPduFilter(frPDU message, long mode);
```

## Description

The function configures a filter for PDUs. With this filter it is possible to receive single PDUs with update bit = 0.

The function overrides the network hardware setting Show PDUs with disabled Update Bit (CANoe menu path: Configuration|Network Hardware...|FlexRay|Options).

The advantage of this filter is that only dedicated PDUs with disabled update bit are received instead of all PDUs with disabled update bit in the network.

## Return Values

—

## Availability

| Since Version |
|---|
