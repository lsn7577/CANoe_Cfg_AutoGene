# testGetWaitEventEnvVarData

> Category: `Test` | Type: `function`

## Syntax

```c
long testGetWaitEventEnvVarData(dword index, float & value); // form 1
```

## Description

Retrieves the environment variable value that has led to the resume of a joined wait statement.

## Return Values

0: Data access successful

## Example

```c
// add envVar event to the current set of “joined events” and get the envVar value
dword index = 0;
float evValue = 0;
TestJoinEnvVarEvent(MyEnvVar);
// ... other join events
index = TestWaitForAnyJoinedEvent(2000);

TestGetWaitEventEnvVarData(index, evValue);
```

## Availability

| Since Version |
|---|
