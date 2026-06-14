# sysSetVariableFloatArray

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableFloatArray(char namespace[], char variable[], float values[], long arraySize); // form 1
```

## Description

Sets the value of a variable of the float[] type.

The call will only succeed if the array size given as parameter is equal to the actual array size of the system variable (you cannot change that size dynamically). The current values of the system variable will then be set to the elements in the values array in the range from 0 to arraySize.

Never give as parameter an array size which is larger than real size of the values array, this would lead to unpredictable behavior.

## Return Values

0: no error, function successful

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarFloatArray returns any system variable of type FloatArray. The function is therefore defined with the system variable type sysvarFloatArray as the return value.

The system variable sv1 (defined with system variable type FloatArray) represents any system variable depending on the counter of the getSysVarFloatArray function.

The value of a system variable is set with the CAPL function sysSetVariableFloatArray.

The value of the system variable is get with the CAPL function sysGetVariableFloatArray and output in the Write Window.

You must define the system variables FMW1::KeyFloatArray, DCM::SpeedSignalFloatArray, and Engine::EngineFloatArray in the System Variables Configuration dialog first.

```c
on key 'g'
{
  sysvarFloatArray * sv1;
  float fVarArr [5] = {7.3, 7.3, 7.3, 7.3, 7.3};
  sv1 = getSysVarFloatArray(0);
  write("Variable is %s%s, Value is %2.1lf", sv1.name, "[0]", @sv1[0]);
  sysSetVariableFloatArray(sv1,fVarArr, elcount(fVarArr));
  write("Variable is %s%s, Value is: %2.1lf", sv1.name, "[0]",@sv1[0]);
  sv1 = getSysVarFloatArray(1);
  write("Variable is %s%s, Valgue is %2.1lf", sv1.name, "[0]", @sv1[0]);
  sv1 = getSysVarFloatArray(2);
  sysGetVariableFloatArray (sv1, fVarArr, elcount(fVarArr));
  write("Variable is %s%s, Value is %2.1lf", sv1.name, "[0]",fVarArr[0]);
}

sysvarFloatArray * getSysVarFloatArray (int gKey)
{
  switch (gKey)
  {
  case 0:
    return sysvar::FMW1::KeyFloatArray;
  case 1:
    return sysvar::DCM::SpeedSignalFloatArray;
  default:
    return sysvar::Engine::EngineFloatArray;
  }
}
```

## Availability

| Since Version |
|---|
