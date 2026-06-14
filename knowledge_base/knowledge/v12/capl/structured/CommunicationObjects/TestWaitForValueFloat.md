# TestWaitForValueFloat

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForValueFloat(COValue value, float awaitedValue, dword timeoutMs)
```

## Description

Waits for a communication object value to reach a certain value. This function can only be used for communication object values with a floating point data type. It cannot be used for system variables or bus system signals.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
ret = testWaitForValueFloat(MirrorStatus[CANoe].Temperature, 20.0, 200);
```

## Availability

| Since Version |
|---|
