# TestJoinAuxEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinAuxEvent(dword aAuxEventId)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Return Values

-3: Join error

## Example

```c
// wait is resumed on check event
dword index = 0;
dword checkId = 0;
checkId = ChkStart_Timeout(1000);
TestJoinAuxEvent(checkId);
// … other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");

index = TestWaitForAnyJoinedEvent(2000);
```

## Availability

| Since Version |
|---|
