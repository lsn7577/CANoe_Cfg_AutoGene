# TestWaitForValueUInt

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForValueUInt(COValue value, qword awaitedValue, dword timeoutMs)
```

## Description

Waits for a communication object value to reach a certain value. This function can only be used for communication object values with an unsigned integer data type. It cannot be used for system variables or bus system signals.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
ret = testWaitForValueUInt(ErrorSignal[LeftMirror], 1, 200);
```

## Availability

| Since Version |
|---|
