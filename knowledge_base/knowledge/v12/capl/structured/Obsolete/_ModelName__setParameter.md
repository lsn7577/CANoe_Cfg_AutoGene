# <ModelName>_setParameter

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long <ModelName>_setParameter( dword index, float values[], dword nrOfValues);
```

## Description

Copies the values from an array to a model parameter. The array size must not be smaller than the number of values the parameter has.

## Return Values

0: Success.

## Example

```c
float fArr[4];
...
// set parameter number 3 to the values to fArr
myControllerMdl_setParameter(3, fArr, elcount(fArr));
```

## Availability

| Since Version |
|---|
