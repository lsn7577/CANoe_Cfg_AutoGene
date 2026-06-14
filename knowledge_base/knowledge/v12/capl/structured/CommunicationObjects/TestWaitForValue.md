# TestWaitForValue

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForValue(COValue value, ValueType awaitedValue, dword timeoutMs)
```

## Description

Waits for a communication object value to reach a certain value. This function can only be used for communication object values with a complex data type (array or struct). It cannot be used for system variables or bus system signals.

## Return Values

-2: Resume due to constraint violation

## Example

```c
struct Mirrors::Position pos;
long ret;
pos.x = 100;
pos.y = 50;
ret = testWaitForValue(MirrorAdjustment.consumerSide[0,0].CurrentPosition, pos, 200);
```

## Availability

| Since Version |
|---|
