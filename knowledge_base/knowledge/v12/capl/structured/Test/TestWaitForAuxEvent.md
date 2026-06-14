# TestWaitForAuxEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForAuxEvent(dword aAuxEventId, dword aTimeout);
```

## Description

Waits for the signaling of the specified auxiliary event from a connected NodeLayer module.

Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// wait is resumed on check event
long result;
checkId = ChkStart_Timeout(1000);
result = TestWaitForAuxEvent(checkId, 2000);
```

## Availability

| Since Version |
|---|
