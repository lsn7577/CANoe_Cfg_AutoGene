# sysGetVariableDWord

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
dword sysGetVariableDWord(char namespace[], char variable[]); // form 1
```

## Description

Returns the value of a variable of type unsigned 32 bit integer.

## Return Values

Value of the variable or 0 in case of error (form 1 and 2)

## Example

```c
sysGetVariableDWord(sysvar::MyNamespace::UInt32Var);
```

## Availability

| Since Version |
|---|
