# sysGetVariableFloat

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
double sysGetVariableFloat(char namespace[], char variable[]); // form 1
```

## Description

Returns the value of a variable of the double type.

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarFloat returns any system variable of type Float. The function is therefore defined with the system variable type sysvarFloat as the return value.

The system variable sv1 (defined with system variable type Float) represents any system variable depending on the counter of the getSysVarFloat function.

The value of a system variable is set with the CAPL function sysSetVariableFloat.

The value of the system variable is get with the CAPL function sysGetVariableFloat and output in the Write Window.

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

| Since Version |
|---|
