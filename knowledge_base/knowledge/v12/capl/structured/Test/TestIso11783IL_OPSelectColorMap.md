# TestIso11783IL_OPSelectColorMap

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSelectColorMap( dbNode node, dword colorMapID );
```

## Description

The function selects a color map object. A Select Color Map command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
