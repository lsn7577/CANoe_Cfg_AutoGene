# sysGetVariableDescriptionForValue

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableDescriptionForValue(SysVarName, long value, char buffer[], long bufferSize); // form 1
```

## Description

Retrieves a description for a value of a system variable of type long or long array. In this way, you can access the value table of the system variable.

## Return Values

0: no error, function successful

## Example

```c
char buffer[20];
sysGetVariableDescriptionForValue("Dynamic", "IntVar", 0, buffer, elcount(buffer));
```

## Availability

| Since Version |
|---|
