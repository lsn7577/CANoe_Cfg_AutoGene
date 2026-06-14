# ChkControl_Start

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkControl_Start(dword aCheckId);
check.Start();
```

## Description

Begin or continue checking the event condition. May work on a check stopped earlier, or on a check only created previously (e.g. in 'on preStart'). Ignored for active checks.

## Return Values

0: successful

## Example

```c
dword checkId;
dword numCheckEvents;

// start the Error Frame observation
checkId = ChkStart_ErrorFramesOccured();
// Add check as condition,
// that means that check violations are reported and
// the verdict of the test case is set to "failed"
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
// Remove check as condition
TestRemoveCondition(checkId);

// stop the check
ChkControl_Stop(checkId);

// reset stored values of the check
ChkControl_Reset(checkId);
// start the check again without adding as condition,
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
