# ChkControl_Reset

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkControl_Reset(dword aCheckId);
check.Reset();
```

## Description

The status (stored values) of the check is initialized. The check does not have to be stopped for this function to work.

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

// reset stored values of the check
ChkControl_Reset(checkId);

// start the check again without adding as condition
ChkControl_Start(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// stop the check
ChkControl_Stop(checkId);

// analysis of check
numCheckEvents = ChkQuery_NumEvents(checkId);
if (numCheckEvents > 0)
   TestStepFail("Error Frame occurred!");
```

## Availability

| Since Version |
|---|
