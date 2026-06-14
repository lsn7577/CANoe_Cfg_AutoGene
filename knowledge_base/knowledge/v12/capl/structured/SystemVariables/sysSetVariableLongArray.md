# sysSetVariableLongArray

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableLongArray(char namespace[], char variable[], long values[], long arraySize); // form 1
```

## Description

Sets the value of a variable of the int[] type.

The call will only succeed if the array size given as parameter is equal to the actual array size of the system variable (you cannot change that size dynamically). The current values of the system variable will then be set to the elements in the values array in the range from 0 to arraySize.

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
