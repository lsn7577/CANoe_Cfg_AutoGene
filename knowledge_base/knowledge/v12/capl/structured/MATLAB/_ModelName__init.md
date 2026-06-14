# <ModelName>_init

> Category: `MATLAB` | Type: `function`

## Syntax

```c
long <ModelName>_init( dword enableTimer, dword enableEvents);
```

## Description

Initializes the CANoe runtime environment for the generated model DLL. This effectively overrides the default execution settings which were compiled into the DLL.

## Return Values

On success 0, otherwise a value unequal to zero.

## Example

```c
on start
{
modelTimer.SetCyclic(myTimeStep);
myControllerMdl_init(0,1);
}
```

## Availability

| Since Version |
|---|
