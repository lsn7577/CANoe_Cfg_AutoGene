# sysSetVariableInt

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableInt(char namespace[], char variable[], long value); // form 1
long sysSetVariableInt(SysVarName, long value); // form 2
```

## Description

Sets the value of a variable of a 32 bit integer type.

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

The user-defined CAPL function getSysVar returns any system variable of type Int. The function is therefore defined with the system variable type sysvarInt as the return value.

The system variable sv1 (defined with system variable type Int) represents any system variable depending on the counter of the getSysVar function.

The value of a system variable is set with the CAPL function sysSetVariableInt.

The value of the system variable is get with the CAPL function sysGetVariableInt and output in the Write Window.

Note

You must define the system variables FMW1::Key, DCM::SpeedSignal, and Engine::EngineStateSwitch in the System Variables Configuration dialog first.

```c
long lVar;
...
sysSetVariableInt(sysvar::MyNamespace::IntVar, lVar);
on key 'a'
{
  sysvarInt * sv1; //defines a local system variable 'sv1' with the system variable type 'sysvarInt'
  int  valueSysVar;
  sv1 = getSysVar(0);
  write("Variable is %s, Value is %d", sv1.name, @sv1);
  //@sv1++;
  sysSetVariableInt(sv1, @sv1+1);
  write("Variable is %s, Value is higher: %d", sv1.name, @sv1);
  sv1 = getSysVar(1);
  write("Variable is %s, Value is %d", sv1.name, @sv1);
  sv1 = getSysVar(2);
  valueSysVar = sysGetVariableInt(sv1);
  write("Variable is %s, Value is %d", sv1.name, valueSysVar);
}

sysvarInt * getSysVar(int aKey)
{
  switch (aKey)
  {
  case 0:
    return sysvar::FMW1::Key;
  case 1:
    return sysvar::DCM::SpeedSignal;
  default:
    return sysvar::Engine::EngineStateSwitch;
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
