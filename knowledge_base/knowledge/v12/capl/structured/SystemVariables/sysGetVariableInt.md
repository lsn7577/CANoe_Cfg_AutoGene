# sysGetVariableInt

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableInt(char namespace[], char variable[]); // form 1
```

## Description

Returns the value of a variable of a 32 bit integer type.

The function can also be used for variables of type unsigned integer. You can simply cast the result to dword.

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVar returns any system variable of type Int. The function is therefore defined with the system variable type sysvarInt as the return value.

The system variable sv1 (defined with system variable type Int) represents any system variable depending on the counter of the getSysVar function.

The value of a system variable is set with the CAPL function sysSetVariableInt.

The value of the system variable is get with the CAPL function sysGetVariableInt and output in the Write Window.

You must define the system variables FMW1::Key, DCM::SpeedSignal, and Engine::EngineStateSwitch in the System Variables Configuration dialog first.

```c
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

| Since Version |
|---|
