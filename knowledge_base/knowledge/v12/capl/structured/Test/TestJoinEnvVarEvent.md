# TestJoinEnvVarEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinEnvVarEvent(dbEnvVar aEnvVar)
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

## Return Values

-3: Join error

## Example

```c
putValue (evMyEnvVar, 1);
TestJoinEnvVarEvent (evMyEnvVar);
TestWaitForAnyJoinedEvent (1000); // Does not wait, is immediately discontinued by an environment variable change!
```

## Availability

| Since Version |
|---|
