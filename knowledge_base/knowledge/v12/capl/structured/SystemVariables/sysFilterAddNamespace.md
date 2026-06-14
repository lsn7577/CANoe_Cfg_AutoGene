# sysFilterAddNamespace

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterAddNamespace(char namespace[]); // form 1
```

## Description

Adds a namespace to the variable filter. If no filterName is given, the namespace is added to the default filter.

## Return Values

0: No error, function successful.

## Example

```c
long result;
//create the default filter as a Stop Filter
result = sysCreateVariableFilter(0);
//add a namespace to the filter.
result = sysFilterAddNamespace(“myNamespace”);
```

## Availability

| Since Version |
|---|
