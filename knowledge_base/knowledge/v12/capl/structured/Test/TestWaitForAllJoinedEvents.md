# TestWaitForAllJoinedEvents

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForAllJoinedEvents(dword aTimeout);
```

## Description

Waits for the current set of "joined events." The wait condition is resolved if all of the joined events were signaled.

Should not all events occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waits for the fulfillment of all conditions
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);
TestJoinTextEvent("ErrorFrame occurred!");
TestWaitForAllJoinedEvents(5000);
```

## Availability

| Since Version |
|---|
