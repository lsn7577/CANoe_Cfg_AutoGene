# sysGetVariableFloat

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
double sysGetVariableFloat(char namespace[], char variable[]); // form 1
double sysGetVariableFloat(SysVarName); // form 2
long sysGetVariableFloat(char namespace[], char variable[], double& value); // form 3
long sysGetVariableFloat(SysVarName, double& value); // form 4
```

## Description

Returns the value of a variable of the double type.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space (form 1). |
| variable | Name of the variable (form 1). |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |
| value | Receives the current value of the variable. |

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

Example 1

Example 2

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarFloat returns any system variable of type Float. The function is therefore defined with the system variable type sysvarFloat as the return value.

The system variable sv1 (defined with system variable type Float) represents any system variable depending on the counter of the getSysVarFloat function.

The value of a system variable is set with the CAPL function sysSetVariableFloat.

The value of the system variable is get with the CAPL function sysGetVariableFloat and output in the Write Window.

Note

You must define the system variables FMW1::KeyFloat, DCM::SpeedSignalFloat, and Engine::EngineFloat in the System Variables Configuration dialog first.

```c
on key 'c'
{
  sysvarFloat * svFloat1;  //defines a local system variable 'sv1Float' with the system variable type 'sysvarFloat'
  float valueSysVar;
  svFloat1 = getSysVarFloat(0);
  //@svFloat1 = 1.5;
  write("Variable is %s, Value is %7.3f", svFloat1.name, @svFloat1);
  //@svFloat1 = @svFloat1*2.5;
  sysSetVariableFloat(svFloat1, @svFloat1*2.5);
  write("Variable is %s, Value is higher: %7.3f", svFloat1.name, @svFloat1);
  svFloat1 = getSysVarFloat(1);
  write("Variable is %s, Value is %7.3f", svFloat1.name, @svFloat1);
  svFloat1 = getSysVarFloat(2);
  valueSysVar = sysGetVariableFloat(svFloat1);
  write("Variable is %s, Value is %d", svFloat1.name, valueSysVar);
}

sysvarFloat * getSysVarFloat(int cKey)
{
  switch (cKey)
  {
  case 0:
    return sysvar::FMW1::KeyFloat;
  case 1:
    return sysvar::DCM::SpeedSignalFloat;
  default:
    return sysvar::Engine::EngineFloat;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1/5.2: form 1 7.2 SP3: form 2-4 | 5.1/5.2: form 1 7.0: form 2 7.2 SP3: form 3-4 | 13.0 | 13.0: form 2 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since version 7.2 SP3) | ✔ (since version 7.0) | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
