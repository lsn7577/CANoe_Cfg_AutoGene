# ChkQuery_EventReason

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_EventReason (dword checkId);
```

## Description

Retrieves the exact reason of firing event in the LIN specific check.

## Parameters

| Name | Description |
|---|---|
| CheckId | Identifier of the queried Check. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 7.0 SP5: method | 13.0 | — | 14 | 1.0 |
| Restricted To | — | LIN | LIN | — | LIN | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
