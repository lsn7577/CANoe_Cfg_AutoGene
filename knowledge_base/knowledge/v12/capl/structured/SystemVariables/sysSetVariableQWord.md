# sysSetVariableQWord

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableQWord(char namespace[], char variable[], qword value); // form 1
```

## Description

Sets the value of a variable of type unsigned 64bit integer.

## Return Values

0: no error, function successful

## Example

```c
sysSetVariableQWord(sysvar::MyNamespace::UInt64Var, 1);
```

## Availability

| Since Version |
|---|
