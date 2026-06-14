# sysSetVariableDWord

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableDWord(char namespace[], char variable[], dword value); // form 1
```

## Description

Sets the value of a variable of type unsigned 32 bit integer.

## Return Values

0: no error, function successful

## Example

```c
sysSetVariableDWord(sysvar::MyNamespace::UInt32Var, 1);
```

## Availability

| Since Version |
|---|
