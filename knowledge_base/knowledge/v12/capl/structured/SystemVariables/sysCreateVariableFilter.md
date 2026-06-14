# sysCreateVariableFilter

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysCreateVariableFilter(long filterType); // form 1
```

## Description

Creates a new variable filter behind the node calling the function. If no filterName is given, the default filter with an empty name is created.

## Return Values

0: No error, function successful.

## Example

```c
long result;
//create the default filter as a Stop Filter.
result = sysCreateVariableFilter(0);
```

## Availability

| Since Version |
|---|
