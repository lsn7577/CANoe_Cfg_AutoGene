# sysSetVariableFloat

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableFloat(char namespace[], char variable[], float value); // form 1
long sysSetVariableFloat(SysVarName, float value); // form 2
```

## Description

Sets the value of a variable of the double type.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| value | New value of the variable. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

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
float fVar;
...
sysSetVariableFloat(sysvar::MyNamespace::FloatVar, fVar);
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
| Since Version | 5.1/5.2: form 1 7.2 SP3: form 2 | 5.1/5.2: form 1 7.0: form 2 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since version 7.2 SP3) | ✔ (since version 7.0) | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
