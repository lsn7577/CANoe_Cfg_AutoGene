# TestWaitForSysVar

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSysVar(sysvar aSysVar, dword aTimeout);
```

## Description

Waits for the next system variable aSysVar. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Parameters

| Name | Description |
|---|---|
| Note Not available for a single element of a double or integer array. |  |

## Return Values

-2: Resume due to constraint violation.

## Example

```c
// waits for the occurrence of SysVar ‚MySysVar’
long result;
result = TestWaitForSysVar(sysvar::Test::MySysVar, 2000);
```

## Availability

| Since Version |
|---|
