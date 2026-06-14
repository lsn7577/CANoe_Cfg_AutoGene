# sysGetVariableMin

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableMin(SysVarName, long& minValue); // form 1
```

## Description

Retrieves the minimum of a variable of type integer or integer array.

The function can also be used for specific elements of a system variable of type struct or generic array. For this, add the element to the name of the variable. If you directly give the element name to the function instead of using strings, precede the name by sysvarMember:: instead of sysvar::.Example: sysvarMember::XCP::ECU_2::KL2.Curve2[0]

## Return Values

0: success

## Availability

| Since Version |
|---|
