# sysFilterRemoveNamespace

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysFilterRemoveNamespace(char namespace[]); // form 1
```

## Description

Removes a namespace from the variable filter. If no filterName is given, the namespace is removed from the default filter.

## Return Values

0: No error, function successful.

## Example

```c
long result;
//remove a namespace from the default filter.
result = sysFilterRemoveNamespace(“myNamespace”);
```

## Availability

| Since Version |
|---|
