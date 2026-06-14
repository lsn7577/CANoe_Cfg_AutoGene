# TestResetNamespaceSysVarValues

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetNamespaceSysVarValues (char aNamespace[]);
```

## Description

Resets all system variables of the given namespace and all sub-namespaces to their initial value. If no initial value is defined for a system variable, the system variable is not set.

aNamespace is not allowed to be empty. If system variables without namespace should be reset, TestResetSysVarValue has to be used.

## Parameters

| Name | Description |
|---|---|
| aNamespace | Namespace which system variables should be reset. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
