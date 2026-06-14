# sysGetVariableFloatArray

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableFloatArray(char namespace[], char variable[], float values[], long arraySize); // form 1
```

## Description

Returns the value of a variable of the float[] type.

If the actual array size of the system variable is larger than the array size given as parameter, all elements in the values array up to the array size given as parameter will receive the current values of the system variable. Elements in the values array beyond the array size given as parameter will remain unchanged.

If the actual array size of the system variable is smaller than the array size given as parameter, additional elements in the values array will be set to 0. Elements in the values array beyond the array size given as parameter will remain unchanged.

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
