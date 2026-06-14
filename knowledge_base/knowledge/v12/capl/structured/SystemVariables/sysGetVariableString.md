# sysGetVariableString

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableString(char namespace[], char variable[], char buffer[], long bufferSize); // form 1
```

## Description

Returns the value of a variable of the String (char[]) type.

## Return Values

0: no error, function successful

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarString returns any system variable of type String. The function is therefore defined with the system variable type sysvarString as the return value.

The system variable sv1 (defined with system variable type String) represents any system variable depending on the counter of the getSysVarString function.

The value of a system variable is set with the CAPL function sysSetVariableString.

The value of the system variable is get with the CAPL function sysGetVariableString and output in the Write Window.

You must define the system variables FMW1::KeyString, DCM::SpeedSignalString, and Engine::EngineString in the System Variables Configuration dialog first.

```c
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

| Since Version |
|---|
