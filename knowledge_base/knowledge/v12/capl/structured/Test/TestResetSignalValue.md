# TestResetSignalValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetSignalValue (Signal aSignal); // form 1
```

## Description

Resets the signal to initial value. The sending depends on the message send typ.

The reset-function does not contain a waiting time which guarantees that the signal is sent out on the bus. If a waiting time is desired, the TestWaitForTimeout function has additionally been executed.

## Return Values

0: No error

## Example

```c
// check reaction of signal “LockState” after crash
$CrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset test signals
TestResetSignalValue(CrashDetected);
TestResetSignalValue(LockState);
TestWaitForTimeout(200);
```

## Availability

| Since Version |
|---|
