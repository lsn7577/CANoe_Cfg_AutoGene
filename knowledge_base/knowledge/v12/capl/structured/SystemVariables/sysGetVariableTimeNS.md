# sysGetVariableTimeNS

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
int64 sysGetVariableTimeNS(SysVarName);
```

## Description

Returns the time stamp of the last update to the variable value.

Direct access to values from system variables.

## Return Values

Time stamp of the last update to the variable value, in nanoseconds since measurement start.

## Example

```c
int64 timeStamp;
timeStamp = sysGetVariableTimeNS(sysvar::MyNamespace::FloatVar);
```

## Availability

| Since Version |
|---|
