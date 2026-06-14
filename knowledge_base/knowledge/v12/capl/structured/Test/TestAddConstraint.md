# TestAddConstraint

> Category: `Test` | Type: `function`

## Syntax

```c
long TestAddConstraint (dword aAuxHandle);
```

## Description

Adds an event object or an event text as a constraint. Checks from the Test Service Library are suitable as event objects.

This function can be used within a test case and also on the main test level.

## Return Values

0: Constraint was added successfully

## Example

Add check as constraint

```c
dword checkId;
dword numCheckEvents;

// start the Error Frame observation
checkId = ChkStart_ErrorFramesOccured();
// Add check as constraint,
// that means that check violations are reported and
// the verdict of the test case is set to "failed"
TestAddConstraint(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// Remove check as constrait
TestRemoveConstraint(checkId);

// stop the check
ChkControl_Stop(checkId);
// reset stored values of the check
ChkControl_Reset(checkId);

// start the check again without adding as constraint,
// that means that Error Frames are observed, but violations
// are not reported and do not set the test case verdict to "failed"
ChkControl_Start(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// stop the check
ChkControl_Stop(checkId);

// analysis of check
numCheckEvents = ChkQuery_NumEvents(checkId);
if (numCheckEvents > 0)
TestStepFail("Error Frame occurred!");

// destroy check
ChkControl_Destroy(checkId);
```

## Availability

| Since Version |
|---|
