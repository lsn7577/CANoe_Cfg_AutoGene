# sysSetAnalysisOnlyVariable

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
void sysSetAnalysisOnlyVariable(SysVarName, long anlyzLocal);
```

## Description

Determines whether the variable is meant to be used for analysis purposes.

If this is true (anlyzLocal is set to 1), and the variable is changed in a CAPL program in the Measurement setup, the value change is not transmitted to the real time part of CANoe, but used immediately in the analysis part. This is the default.

If it is false (anlyzLocal is set to 0), value changes are always transmitted to the real time part.

Direct access to values from system variables.

## Return Values

—

## Example

```c
sysSetAnalysisOnlyVariable(sysvar::MyNamespace::StringVar, 1);
```

## Availability

| Since Version |
|---|
