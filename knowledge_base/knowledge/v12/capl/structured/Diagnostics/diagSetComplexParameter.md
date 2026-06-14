# diagSetComplexParameter

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetComplexParameter (diagResponse obj, char parameterName[], DWORD iteration, char subParameter[], double numValue)
```

## Description

Sets one of the sub-parameters within a complex parameter to the specified (numeric or symbolic) value.

For this first the complex parameter, that is, the name of the iteration, must be specified; then the number of repetitions of the sub-parameter list that is the goal, and then the sub-parameter in the iteration itself.

## Return Values

Error code.

## Availability

| Since Version |
|---|
