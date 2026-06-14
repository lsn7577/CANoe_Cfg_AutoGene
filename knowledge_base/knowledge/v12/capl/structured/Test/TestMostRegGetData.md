# TestMostRegGetData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestMostRegGetData(BYTE aBuffer[], long aBufferSize);
```

## Description

The TestMostRegGetData() function is used together with the TestMostReadReg and TestMostWriteReg functions.

After initiating one of these two functions, the resulting register value can be copied into a byte buffer. Ensure that the buffer size is as specified. A maximum of 16 bytes are transported with the MostReg result.

Note that the register values are only held ready for call-up until the next wait condition in the test program.

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
