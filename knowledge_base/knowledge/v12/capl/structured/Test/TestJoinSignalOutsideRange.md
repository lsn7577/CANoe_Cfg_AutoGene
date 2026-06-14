# TestJoinSignalOutsideRange

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinSignalOutsideRange (Signal aSignal, float aLowLimit, float aHighLimit); // form 1
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

By default this condition will be checked immediately when the set of joined events is evaluated by TestWaitForAllJoinedEvents or TestWaitForAnyJoinedEvent and may not wait for a value change. It is also possible to delay the checking of the condition until the next message with the given signal arrives.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

-3: Join error.

## Example

```c
// waits until the value of signal ‚Velocity’ is outside the given range
long result;
dword index = 0;
result = TestJoinSignalOutsideRange(Velocity, 30, 50);
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);
```

## Availability

| Since Version |
|---|
