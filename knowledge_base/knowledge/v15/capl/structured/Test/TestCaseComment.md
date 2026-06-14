# TestCaseComment

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseComment (char aComment[]);
TestCaseComment (char aComment[], message aMsg);
TestCaseComment (char aComment[], mostMessage aMsg);
TestCaseComment (char aComment[], mostAmsMessage aMsg);
TestCaseComment (char aComment[], mostRawMessage aMsg);
TestCaseComment (char aComment[], linFrame aMsg);
TestCaseComment (char aComment[], char aRawString[]);
TestCaseComment (char aComment[], gmLanMsg aMsg);
```

## Description

With this function within a test case a commentary can be taken over into the report. This comment can relate to a message that can also be output in the report.

The verdict of the test case is not be influenced.

## Parameters

| Name | Description |
|---|---|
| aComment | Commentary to be taken over into the report. |
| aMsg | CAN-, GMLAN-, LIN-, MOST-, MOST-AMS- or MOST system message to be taken over into the report. |
| aRawString | Here you may enter any ASCII characters. They will be added to the comment in the following way: <Hex value of the given character>(<ASCII display of the given charcter>). In ASCII display special characters will be replaced by '.'. |

## Return Values

—

## Example

```c
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
