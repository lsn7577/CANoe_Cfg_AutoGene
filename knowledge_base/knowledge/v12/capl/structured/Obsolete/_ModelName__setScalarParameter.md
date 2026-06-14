# <ModelName>_setScalarParameter

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long <ModelName>_setScalarParameter( dword index, float value);
```

## Description

Sets a scalar model parameter to the given value.

## Return Values

0: Success.

## Example

The parameterization functions are deprecated. It is much easier to use the generated System variables directly.

Some parameters might not be configurable during measurement. This depends on the implementation of a Simulink block. If the <ModelName>_set functions are used in the preStart section of a CAPL program, all parameters will be configurable and will use the new values during measurement.

Parameterization requires the C-API for data exchange which is available since MATLAB R14.

<ModelName> = placeholder for Simulink model

```c
@myModel::Subsystem::Frequency = 1.0;
Instead of
myModel_setParamter(index, 1.0);
```

## Availability

| Since Version |
|---|
