# TestCaseDescription

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseDescription (char description[]);
```

## Description

With this function, a description test for a test case can be written into the report. The function can be called several times in a row, the transmitted texts are then added to one another without additional separation. The function may only be called within a test case and relates then to the respective test case.

To obtain line breaks (in form of <br /> tags) in the test report, "\n" may be inserted at any place.

## Return Values

—

## Example

Example 1

Example 2

See example: TestCaseTitle, TestCaseDescription, TestStep

```c
// add description with line break to report
TestCaseDescription("In this test case\nthe occurrence of Error Frames is tested.");
testcase CheckLockingOnCrash ()
{
   TestCaseTitle("TC 1.0", "Check unlock of central locking system on crash");
   TestCaseDescription("This test case simulates a crash during drive. The central locking system has to be unlocked on crash!");
   // Initialization of signals
   $CrashDetected = 0;
   $LockState = Locked;
   TestWaitForTimeout(200);

   TestCaseComment("Initialization of system completed");
   ...
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
