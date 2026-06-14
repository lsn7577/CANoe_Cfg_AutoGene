# sysSetVariableLongLong

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableLongLong(char namespace[], char variable[], int64 value); // form 1
```

## Description

Sets the value of a variable of a 64 bit integer type.

The function can also be used for variables of type unsigned 64bit integer. You can simply cast the value to int64.

## Return Values

0: no error, function successful

## Example

```c
int64 llVar;
...
sysSetVariableLongLong(sysvar::MyNamespace::Int64Var, llVar);
```

## Availability

| Since Version |
|---|
