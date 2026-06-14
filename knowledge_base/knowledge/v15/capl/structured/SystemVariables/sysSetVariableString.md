# sysSetVariableString

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableString(char namespace[], char variable[], char value[]); // form 1
long sysSetVariableString(SysVarName, char value[]); // form 2
```

## Description

Sets the value of a variable of the String (char[]) type.

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

The user-defined CAPL function getSysVarString returns any system variable of type String. The function is therefore defined with the system variable type sysvarString as the return value.

The system variable sv1 (defined with system variable type String) represents any system variable depending on the counter of the getSysVarString function.

The value of a system variable is set with the CAPL function sysSetVariableString.

The value of the system variable is get with the CAPL function sysGetVariableString and output in the Write Window.

Note

You must define the system variables FMW1::KeyString, DCM::SpeedSignalString, and Engine::EngineString in the System Variables Configuration dialog first.

```c
sysSetVariableString(sysvar::MyNamespace::StringVar, "Vector");
on key 'd'
{
  sysvarString * svString1;
  char valueSysVarString[100];
  char buf[100];
  svString1 = getSysVarString(0);
  sysGetVariableString(svString1, buf, elcount(buf));
  write("Variable is %s, Value is %s", svString1.name, buf);
  sysSetVariableString(svString1, "OFF");
  sysGetVariableString(svString1, buf, elcount(buf));
  write("Variable is %s, Value is now: %s", svString1.name, buf);
  svString1 = getSysVarString(1);
  sysGetVariableString(svString1, buf, elcount(buf));
  write("Variable is %s, Value is %s", svString1.name, buf);
  svString1 = getSysVarString(2);
  sysGetVariableString(svString1, buf, elcount(buf));
  write("Variable is %s, Value is %s", svString1.name, buf);
}

sysvarString * getSysVarString(int cKey)
{
  switch (cKey)
  {
  case 0:
    return sysvar::FMW1::KeyString;
  case 1:
    return sysvar::DCM::SpeedSignalString;
  default:
    return sysvar::Engine::EngineStateString;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1/5.2: form 1 7.2 SP3: form 2 | 5.1/5.2: form 1 7.0: form 2 | 13.0 | 13.0: form 1 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since version 7.2 SP3) | ✔ (since version 7.0) | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
