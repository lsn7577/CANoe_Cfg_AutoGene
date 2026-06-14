# ChkCreate_Timeout, ChkStart_Timeout

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_Timeout (Duration aTimeout, char [] CaplCallback);
```

## Description

The check fires an event if the time has expired.

## Example

```c
// checks the maximum duration of a sequence of actions
checkId = ChkStart_Timeout (2000);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
