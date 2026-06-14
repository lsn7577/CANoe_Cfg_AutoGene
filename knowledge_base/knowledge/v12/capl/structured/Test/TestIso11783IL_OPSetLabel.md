# TestIso11783IL_OPSetLabel

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSetLabel( dbNode node, dword objectID, dword stringVarIdD, dword fontType, dword graphID );
```

## Description

A Set Label command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
