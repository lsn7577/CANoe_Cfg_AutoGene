# lookupSysvarInt

> Category: `Other` | Type: `function`

## Syntax

```c
sysvarInt * lookupSysvarInt(char sysvarPath[]); // form 1
```

## Description

Searches for a system variable definition. If the system variable is not found or has a wrong type, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid sysvar.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

## Return Values

The found system variable or an invalid object.

## Availability

| Since Version |
|---|
