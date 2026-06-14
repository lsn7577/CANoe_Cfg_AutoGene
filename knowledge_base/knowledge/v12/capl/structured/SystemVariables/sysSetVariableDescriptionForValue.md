# sysSetVariableDescriptionForValue

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableDescriptionForValue(char namespace[], char variable[], long value, char description[]);
```

## Description

Sets a description for a particular value of a system variable of type long or long array. In this way, you can define a value table for a variable which you have created with sysDefineVariableInt/sysDefineVariableIntArray.

## Return Values

0: no error, function successful

## Example

```c
sysSetVariableDescriptionForValue("Dynamic", "IntVar", 0, "Zero");
```

## Availability

| Since Version |
|---|
