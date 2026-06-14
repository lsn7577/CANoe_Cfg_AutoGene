# sysFilterAddVariable

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterAddVariable(sysVar variable); // form 1
```

## Description

Adds a variable a variable filter. If no filterName is given, the variable will be added to the default filter.

## Parameters

| Name | Description |
|---|---|
| Note If a struct member is specified, the whole struct will be added. |  |

## Return Values

0: No error, function successful.

## Example

```c
long result;
//create default filter as Stop Filter
result = sysCreateVariableFilter(0);
//add a variable that should be stopped by the filter
result = sysFilterAddVariable(sysvar::myNamespace::myVariable);
```

## Availability

| Since Version |
|---|
