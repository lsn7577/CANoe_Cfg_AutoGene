# sysSetVariableFilterActive

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysSetVariableFilterActive(dword active); // form 1
```

## Description

Activates or deactivates a variable filter. If no filterName is given, the default filter is affected.

## Return Values

0: No error, function successful.

## Example

```c
long result;
//create the default filter as a Stop Filter.
result = sysCreateVariableFilter(0);
//deactivate the default filter.
result = sysSetVariableFilterActive(0);
```

## Availability

| Since Version |
|---|
