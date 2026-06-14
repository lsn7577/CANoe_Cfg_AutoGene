# sysGetVariableLongArray

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableLongArray(char namespace[], char variable[], long values[], long arraySize); // form 1
```

## Description

Returns the value of a variable of the int[] type.

If the actual array size of the system variable is larger than the array size given as parameter, all elements in the values array up to the array size given as parameter will receive the current values of the system variable. Elements in the values array beyond the array size given as parameter will remain unchanged.

If the actual array size of the system variable is smaller than the array size given as parameter, additional elements in the values array will be set to 0. Elements in the values array beyond the array size given as parameter will remain unchanged.

Never give as parameter an array size which is larger than real size of the values array, this would lead to unpredictable behavior.

## Return Values

0: no error, function successful

## Example

This example shows the use of system variable types as a return value of functions and as a local variable.

The user-defined CAPL function getSysVarIntArray returns any system variable of type IntArray. The function is therefore defined with the system variable type sysvarIntArray as the return value.

The system variable sv1 (defined with system variable type IntArray) represents any system variable depending on the counter of the getSysVarIntArray function.

The value of a system variable is set with the CAPL function sysSetVariableLongArray.

The value of the system variable is get with the CAPL function sysGetVariableLongArray and output in the Write Window.

You must define the system variables FMW1::KeyIntergerArray, DCM::SpeedSignalIntegerArray, and Engine::EngineIntegerArray in the System Variables Configuration dialog first.

```c
on key 'f'
{
  sysvarIntArray * sv1;
  long lVarArr [5] = {7, 7, 7, 7, 7};
  sv1 = getSysVarIntArray(0);
  write("Variable is %s%s, Value is %d", sv1.name, "[0]", @sv1[0]);
  sysSetVariableLongArray(sv1,lVarArr, elcount(lVarArr));
  write("Variable is %s%s, Value is: %d", sv1.name, "[0]",@sv1[0]);
  sv1 = getSysVarIntArray(1);
  write("Variable is %s%s, Value is %d", sv1.name, "[0]", @sv1[0]);
  sv1 = getSysVarIntArray(2);
  sysGetVariableLongArray (sv1, lVarArr, elcount(lVarArr));
  write("Variable is %s%s, Value is %d", sv1.name, "[0]",lVarArr[0]);
}

sysvarIntArray * getSysVarIntArray (int fKey)
{
  switch (fKey)
  {
  case 0:
    return sysvar::FMW1::KeyIntegerArray;
  case 1:
    return sysvar::DCM::SpeedSignalIntegerArray;
  default:
    return sysvar::Engine::EngineIntegerArray;
  }
}
```

## Availability

| Since Version |
|---|
