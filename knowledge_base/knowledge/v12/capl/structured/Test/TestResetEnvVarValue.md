# TestResetEnvVarValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetEnvVarValue (dbEnvVar aEnvVar);
```

## Description

Resets the environment variable to initial value. If no initial value is available, the environment variable is set to 0 or "".

## Return Values

0: No error

## Example

```c
// check reaction of signal “LockState” after crash
@EnvErrorCrashDetected = 1;
TestWaitForTimeout(100);
if ($LockState !=  Unlocked)
    TestStepFail(“Doors are locked after crash is detected!”);

// reset the crash environment variable
TestResetEnvVarValue(EnvErrorCrashDetected);
TestWaitForTimeout(200);
```

## Availability

| Since Version |
|---|
