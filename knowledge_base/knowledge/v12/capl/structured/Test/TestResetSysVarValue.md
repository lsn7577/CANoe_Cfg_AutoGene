# TestResetSysVarValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetSysVarValue (sysvar aSysVar);
```

## Description

Resets the system variable to initial value. If no initial value is defined, the system variable is not set.

## Return Values

0: No error

## Example

```c
// check reaction of signal “LockState” after crash
@sysvar::Error::SysVarCrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset the crash system variable
TestResetSysVarValue(sysvar::Error::SysVarCrashDetected);
TestWaitForTimeout(200);
```

## Availability

| Since Version |
|---|
