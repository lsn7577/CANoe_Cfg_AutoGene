# TestCheckCondition

> Category: `Test` | Type: `function`

## Syntax

```c
long TestCheckCondition (dword aAuxHandle);
```

## Description

Checks whether the specified condition was already injured.

This function can be used both within a test case and also on test module level.

## Return Values

1: Condition was already injured at least once

## Example

Add check as condition

```c
// checks the maximum duration of a sequence of actions
checkId = ChkStart_Timeout (1000);
TestAddCondition(checkId);
TestWaitForTimeout(1500);
result = TestCheckCondition(checkId);
if (result == 1)
   TestStepFail("Timeout already occurred after 1500 ms.");
// sequence of different actions and waiting conditions
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
