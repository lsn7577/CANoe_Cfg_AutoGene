# TestIso11783IL_OPSave

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSave( dbNode node, char filename[] );
```

## Description

The function saves an object pool file (*.iop).

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
