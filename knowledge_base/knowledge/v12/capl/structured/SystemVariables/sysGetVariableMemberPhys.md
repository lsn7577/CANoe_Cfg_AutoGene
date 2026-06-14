# sysGetVariableMemberPhys

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableMemberPhys(char namespace[], char variableAndMemberName[], double& value); // form 1
```

## Description

Retrieves the physical value of a specific element of a variable of type struct or generic array.

Direct access to values from system variables

## Return Values

0: no error, function successful

## Example

```c
double val;
sysGetVariableMemberPhys(sysvarMember::XCP::ECU_2::KL2.Curve2[0], val);
```

## Availability

| Since Version |
|---|
