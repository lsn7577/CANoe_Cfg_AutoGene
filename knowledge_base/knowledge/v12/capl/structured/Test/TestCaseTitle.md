# TestCaseTitle

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseTitle (char identifier[], char title[]);
```

## Description

The title of a test case is acquired automatically from the test case name in the CAPL program. It can also be set explicitly together with a test case identifier with the help of this function. The function may only be called within a test case and relates then to the respective test case.

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

   TestCaseComment("Initialization of system completed.");
   ...
}
```

## Availability

| Since Version |
|---|
