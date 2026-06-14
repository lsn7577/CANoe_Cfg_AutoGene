# TestCaseComment

> Category: `Test` | Type: `function`

## Syntax

```c
TestCaseComment (char aComment[]);
```

## Description

With this function within a test case a commentary can be taken over into the report. This comment can relate to a message that can also be output in the report.

The verdict of the test case is not be influenced.

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

| Since Version |
|---|
