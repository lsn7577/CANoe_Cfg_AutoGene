# SysSetVariableIntArray

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long SysSetVariableIntArray(char namespace[], char variable[], int values[], long arraySize); // form 1
```

## Description

Sets the value of a variable of the int[] type.

## Return Values

0: no error, function successful

## Example

```c
long lVarArr[10];
...
sysSetVariableIntArray(sysvar::MyNamespace::IntArrayVar, lVarArr, elcount(lVarArr));
```

## Availability

| Up to Version |
|---|
