# sysSetVariableData

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableData(char namespace[], char variable[], byte data[], long size); // form 1
long sysSetVariableData(SysVarName, byte data[], long size); // form 2
```

## Description

Sets the value of a variable of the type data, string, struct or generic array.

## Parameters

| Name | Description |
|---|---|
| namespace | Name of the name space. |
| variable | Name of the variable. |
| data | New values for the variable. |
| size | New size for the variable. Must not exceed the length of the data array. |
| SysVarName | Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". |

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarData returns any system variable of type Data. The function is therefore defined with the system variable type sysvarData as the return value.

The system variable sv1 (defined with system variable type Data) represents any system variable depending on the counter of the getSysVarData function.

The value of a system variable is set with the CAPL function sysSetVariableData.

The value of the system variable is get with the CAPL function sysGetVariableData and output in the Write Window.

Note

You must define the system variables FMW1::KeyData, DCM::SpeedSignalData, and Engine::EngineData in the System Variables Configuration dialog first.

```c
on key 'e'
{
  sysvarData * svData1;
  char valueSysVarData[100];
  byte buf[2];
  long size = 2;
  long copiedBytes;
  byte data[2] = {0xAF, 0xEF};
  svData1 = getSysVarData(0);
  sysGetVariableData(svData1, buf, copiedBytes);
  write("Variable is %s, Value is %x", svData1.name, buf[0]);
  sysSetVariableData(svData1, data, size);
  sysGetVariableData(svData1, buf, copiedBytes);
  write("Variable is %s, Value is now: %x", svData1.name, buf[0]);
  svData1 = getSysVarData(1);
  sysGetVariableData(svData1, buf, copiedBytes);
  write("Variable is %s, Value is %x", svData1.name, buf[0]);
  svData1 = getSysVarData(2);
  sysGetVariableData(svData1, buf, copiedBytes);
  write("Variable is %s, Value is %x", svData1.name, buf[0]);
}

sysvarData * getSysVarData(int eKey)
  {
  switch (eKey)
  {
  case 0:
    return sysvar::FMW1::KeyData;
  case 1:
    return sysvar::DCM::SpeedSignalData;
  default:
    return sysvar::Engine::EngineStateData;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 | 7.6 | 13.0 | 13.0 | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
