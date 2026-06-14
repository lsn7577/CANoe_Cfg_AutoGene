# SomeIpRemoveValue

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpRemoveValue( dword objectHandle, char valuePath[]);
```

## Description

This function can be used to remove a value in the object specified in the objectHandle parameter. The value is removed in this case via symbolic access paths.

The function may be used on entries of dynamic arrays or optional values which shall be removed. In the case of arrays successive entries are moved forward.

## Return Values

0: The function was successfully executed

## Availability

| Since Version |
|---|
