# canOutputErrorFrame

> Category: `CAN` | Type: `function`

## Syntax

```c
long canOutputErrorFrame(errorFrame, long dominant, long recessive);
```

## Description

Outputs an Error Frame to the CAN bus. The number of dominant bits and the number of trailing recessive bits are given as arguments.

## Return Values

1: OK

## Example

```c
canOutputErrorFrame(errorFrame, 12, 0); //output Error Frame with 12 dominant bits on CAN1
canOutputErrorFrame(CAN2.errorFrame, 6, 0); //output Error Frame with 6 dominant bits on CAN2
```

## Availability

| Since Version |
|---|
