# TestRemoveConstraint

> Category: `Test` | Type: `function`

## Syntax

```c
long TestRemoveConstraint (dword aAuxHandle);
```

## Description

Removes an event object or an event text that was added as a constraint.

This function can be used both within a test case and also on the test module level.

## Return Values

0: Constraint was removed successfully

## Example

```c
dword checkId;
dword numCheckEvents;

// start the Error Frame observation
checkId = ChkStart_ErrorFramesOccured();
// Add check as constraint,
// that means that check violations are reported and
// the verdict of the test case is set to "failed"
TestAddConstrait(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// Remove check as constraint
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
