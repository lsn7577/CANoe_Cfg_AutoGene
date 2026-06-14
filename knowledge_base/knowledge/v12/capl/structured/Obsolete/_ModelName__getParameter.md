# <ModelName>_getParameter

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long <ModelName>_getParameter( dword index, float values[], dword nrOfValues);
```

## Description

Retrieves the values of a model parameter and copies them into an array. The array size must not be smaller than the number of values the parameter has.

## Return Values

0: Success.

## Example

```c
float fArr[4];
// get parameter number 3 and copy the values to fArr
myControllerMdl_getParameter(3, fArr, elcount(fArr));
```

## Availability

| Since Version |
|---|
