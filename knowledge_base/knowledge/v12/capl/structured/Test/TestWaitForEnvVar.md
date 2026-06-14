# TestWaitForEnvVar

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForEnvVar(dbEnvVar aEnvVar, dword aTimeout);
```

## Description

Waits for the description of the specified environment variable (aEnvVar or with the name aEnvVarName). Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waiting point is discontinued immediately
long result;
putValue (evMyEnvVar, 1);
result = TestWaitForEnvVar (evMyEnvVar, 1000); // Does not wait, is immediately discontinued by an environment variable change!
```

## Availability

| Since Version |
|---|
