# TestMostWriteReg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestMostWriteReg(long aChannel, long aChip, dword aOffset, dword aRegDataLen, BYTE aRegData[], unsigned long aTimeout);
```

## Description

Writes one or several chip registers in the MOST hardware and waits for the result. If the operational is successful, the written register values can be read out using TestMostRegGetData.

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
