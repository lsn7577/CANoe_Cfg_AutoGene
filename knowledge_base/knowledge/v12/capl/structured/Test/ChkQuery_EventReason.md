# ChkQuery_EventReason

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventReason (dword checkId);
check.QueryEventReason();
```

## Description

Retrieves the exact reason of firing event in the LIN specific check.

## Return Values

< 0: Refers the query error codes

## Example

```c
testcase tcTSL_LINReconfRequest()
{
   dword checkId;
   long rqViolationReason;

   checkId = ChkStart_LINReconfRequestFormatViolation();
   testWaitForTimeout(5000);
   ChkControl_Stop(checkId);

   rqViolationReason = ChkQuery_EventReason(checkId);
   if (rqViolationReason & 0x1)
   {
      testStep("Evaluation", "Initial NAD is out of range");
   }
   if (rqViolationReason & 0x2)
   {
      testStep("Evaluation", "NAD references undefined Slave");
   }
   if (rqViolationReason & 0x4)
   {
      testStep("Evaluation", "Supplier ID does not match");
   }
   if (rqViolationReason & 0x8)
   {
      testStep("Evaluation", "Function ID does not match");
   }
   if (rqViolationReason & 0x10)
   {
      testStep("Evaluation", "Variant ID does not match");
   }
}
```

## Availability

| Since Version |
|---|
