# sysFilterRemoveVariable

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterRemoveVariable(sysVar variable); // form 1
```

## Description

Removes a variable from a variable filter. If no filterName is given, the variable will be removed from the default filter.

## Parameters

| Name | Description |
|---|---|
| Note If a struct member is specified, the whole struct will be removed. |  |

## Return Values

0: No error, function successful.

## Example

```c
long result;
//remove a variable from the default filter
result = sysFilterRemoveVariable(sysvar::myNamespace::myVariable);
```

## Availability

| Since Version |
|---|
