# sysEndVariableStructUpdate

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysEndVariableStructUpdate(char namespace[], char variable[]); // form 1
```

## Description

Ends the update of several elements of a system variable of type struct or generic array.

Use this function and the corresponding sysBeginVariableStructUpdate to change several elements at the same time without the variable having an intermediate value where only some elements are changed.

## Return Values

0: no error, function successful

## Example

```c
sysEndVariableStructUpdate(sysvar::XCP::ECU_2::KL2);
```

## Availability

| Since Version |
|---|
