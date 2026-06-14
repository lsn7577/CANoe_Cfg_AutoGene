# sysBeginVariableStructUpdate

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysBeginVariableStructUpdate(char namespace[], char variable[]); // form 1
```

## Description

Starts the update of several elements of a system variable of type struct or generic array.

Use this function and the corresponding sysEndVariableStructUpdate to change several elements at the same time without the variable having an intermediate value where only some elements are changed. Each call must be followed by a call to sysEndVariableStructUpdate, else the variable value will not change.

## Return Values

0: no error, function successful

## Example

```c
sysBeginVariableStructUpdate(sysvar::XCP::ECU_2::KL2);
```

## Availability

| Since Version |
|---|
