# ChkQuery_EventTiming

> Category: `Test` | Type: `function`

## Syntax

```c
float ChkQuery_EventTiming (dword checkId);
check.QueryEventTiming();
```

## Description

Retrieves the timing value that has been violated in the LIN specific check.

## Return Values

< 0: Refers the query error codes

## Example

```c
testcase tcTSL_LINSyncBreak()
{
   dword checkId;
   float lastMeasuredSyncBreakLength;

   checkId = ChkStart_LINSyncBreakTimingViolation (18, 20);
   testWaitForTimeout(5000);
   ChkControl_Stop(checkId);

   lastMeasuredSyncBreakLength = ChkQuery_EventTiming(checkId);
   testStep("Evaluation", "Last measured sync break length is %.2f bits", lastMeasuredSyncBreakLength);
}
```

## Availability

| Since Version |
|---|
