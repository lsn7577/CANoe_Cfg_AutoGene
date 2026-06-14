# sysGetVariableSVType

> Category: `SystemVariables` | Type: `function`

## Syntax

```c
long sysGetVariableSVType(sysvar);
```

## Description

Gets the type of a system variable encoded as a long integer.

## Return Values

0: Invalid

## Example

```c
long t1, t2;
t1 = sysGetVariableSVType(lookupSysvar("mysysvar"));
t2 = sysGetVariableSVType(sysvar::mysysvar);
```

## Availability

| Since Version |
|---|
