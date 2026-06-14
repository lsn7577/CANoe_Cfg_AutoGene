# sysGetVariableLongLong

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
int64 sysGetVariableLongLong(char namespace[], char variable[]); // form 1
```

## Description

Returns the value of a variable of a 64 bit integer type.

The function can also be used for variables of type unsigned 64bit integer. You can simply cast the result to qword.

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

```c
sysGetVariableLongLong(sysvar::MyNamespace::Int64Var);
```

## Availability

| Since Version |
|---|
