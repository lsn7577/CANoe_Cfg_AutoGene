# sysGetOrigTimeNS

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
int64 sysGetOrigTimeNS(SysVarName);
```

## Description

Returns the original time stamp of the last update to the variable value, before time synchronization may have changed it.

## Return Values

Original time stamp of the last update to the variable value in nanoseconds since measurement start.

## Example

```c
int64 timeStamp;
timeStamp = sysGetOrigTimeNS(sysvar::MyNamespace::FloatVar);
```

## Availability

| Since Version |
|---|
