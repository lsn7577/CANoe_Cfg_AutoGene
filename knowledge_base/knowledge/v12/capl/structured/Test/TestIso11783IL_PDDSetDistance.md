# TestIso11783IL_PDDSetDistance

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDSetDistance( dbNode node, dword distance );
```

## Description

The distance covered is set with this function. The value is needed for the distance trigger and should be updated cyclically.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
