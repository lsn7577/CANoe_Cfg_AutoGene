# TestMostReadReg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestMostReadReg(long aChannel, long aChip, dword aOffset, dword aRegDataLen, unsigned long aTimeout);
```

## Description

Reads one or several chip registers in the MOST hardware and waits for the result. If the operation is successful, the written register values can be read out using TestMostRegGetData.

## Return Values

-101 to -129: Error codes like for mostReadReg, mostWriteReg

## Availability

| Since Version |
|---|
