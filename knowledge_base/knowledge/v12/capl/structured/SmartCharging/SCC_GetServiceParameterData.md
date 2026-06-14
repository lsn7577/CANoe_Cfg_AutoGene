# SCC_GetServiceParameterData

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetServiceParameterData ( long i1, long i2, char Name[], char ValueType[] )
```

## Description

Gets the name and value type of the parameter with the selected indices.

## Return Values

The name and value type of the parameter with the selected indices, where
For DIN 70121, ValueType is the actual content of the element <ValueType>. For ISO 15118, the subelement holding the parameter value is evaluated and ValueType is set accordingly. In both cases, there are the same possible results for ValueType, e.g. int, physicalValue, string.

## Availability

| Since Version |
|---|
