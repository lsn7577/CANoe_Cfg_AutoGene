# TestJoinTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinTextEvent(char[]aText)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Return Values

-3: Join error

## Example

```c
// waits for a specified text event
long result;
dword index = 0;
result = TestJoinTextEvent("ErrorFrame occurred!");
// ... other join events
TestJoinEnvVarEvent(MyEnvVar);
TestJoinSignalInRange(Velocity, 80, 100);

index = TestWaitForAnyJoinedEvent(2000);

// on ErrorFrame handler
on errorFrame
{
   TestSupplyTextEvent("ErrorFrame occurred!");
}
```

## Availability

| Since Version |
|---|
