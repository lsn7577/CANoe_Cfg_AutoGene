# sysGetVariableValueForDescription

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableValueForDescription(SysVarName, char description[], long& value); // form 1
```

## Description

Retrieves the value for a value description of a system variable of type long or long array. In this way, you can access the value table of the system variable.

## Return Values

0: no error, function successful

## Example

```c
long val;
sysGetVariableValueForDescription("Dynamic", "IntVar", "Zero", val);
```

## Availability

| Since Version |
|---|
