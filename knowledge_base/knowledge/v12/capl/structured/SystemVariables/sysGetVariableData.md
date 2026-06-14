# sysGetVariableData

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableData(char namespace[], char variable[], byte buffer[], long& copiedBytes); // form 1
```

## Description

Returns the value of a variable of the type data, string, struct or generic array.

## Return Values

0: no error, function successful

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarData returns any system variable of type Data. The function is therefore defined with the system variable type sysvarData as the return value.

The system variable sv1 (defined with system variable type Data) represents any system variable depending on the counter of the getSysVarData function.

The value of a system variable is set with the CAPL function sysSetVariableData.

The value of the system variable is get with the CAPL function sysGetVariableData and output in the Write Window.

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

| Since Version |
|---|
