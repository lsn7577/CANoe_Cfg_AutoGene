# ChkControl_Destroy

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkControl_Destroy(dword aCheckId);
```

## Description

The check is destroyed and cannot be accessed anymore. Its resources are freed.

## Return Values

0: successful

## Example

```c
dword checkId;
dword numCheckEvents;

// start the Error Frame observation
checkId = ChkStart_ErrorFramesOccured();
// Add check as condition
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// Remove check as condition
TestRemoveCondition(checkId);

// stop the check
ChkControl_Stop(checkId);

// destroy check
ChkControl_Destroy(checkId);
```

## Availability

| Since Version |
|---|
