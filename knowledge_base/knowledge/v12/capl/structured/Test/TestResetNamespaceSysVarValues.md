# TestResetNamespaceSysVarValues

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetNamespaceSysVarValues (char aNamespace[]);
```

## Description

Resets all system variables of the given namespace and all sub-namespaces to their initial value. If no initial value is defined for a system variable, the system variable is not set.

aNamespace is not allowed to be empty. If system variables without namespace should be reset, TestResetSysVarValue has to be used.

## Return Values

0: No error

## Example

```c
// check the warning lights
@sysvar::Lights::SysVarWarningLights = 1;
TestWaitForTimeout(100);
if (@sysvar::Lights::SysVarWarningLightsDsp != 1)
    TestStepFail(“Warning lights do not flash!”);

// reset all “Lights” system variables
TestResetNamespaceSysVarValues(“Lights”);
TestWaitForTimeout(200);
```

## Availability

| Since Version |
|---|
