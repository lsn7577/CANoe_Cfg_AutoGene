# sysGetVariableQWord

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
qword sysGetVariableQWord(char namespace[], char variable[]); // form 1
```

## Description

Returns the value of a variable of type unsigned 64 bit integer.

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

```c
sysGetVariableQWord(sysvar::MyNamespace::UInt64Var);
```

## Availability

| Since Version |
|---|
