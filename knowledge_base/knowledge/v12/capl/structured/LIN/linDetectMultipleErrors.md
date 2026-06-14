# linDetectMultipleErrors

> Category: `LIN` | Type: `function`

## Syntax

```c
long linDetectMultipleErrors(long activate)
```

## Description

This function can be used to instruct LIN Hardware to enable/disable detection of more than one error per a LIN frame.

This function can be useful during tests of the stress functionality. For example, an inversion of bits in a frame response may lead to a receive error and checksum error simultaneously. By default only one error per frame is detected, but with this function the detection of both errors can be activated.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
