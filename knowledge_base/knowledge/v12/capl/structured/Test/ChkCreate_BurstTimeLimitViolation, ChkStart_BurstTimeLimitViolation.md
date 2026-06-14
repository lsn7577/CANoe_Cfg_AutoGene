# ChkCreate_BurstTimeLimitViolation, ChkStart_BurstTimeLimitViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_BurstTimeLimitViolation (char[] aBusName, duration aMaxTime);
```

## Description

Checks the maximum burst time on a bus.

## Example

```c
// observes the maximum burst time 3 ms
checkId = ChkStart_BurstTimeLimitViolation ("CAN", 3);
TestAddCondition(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
