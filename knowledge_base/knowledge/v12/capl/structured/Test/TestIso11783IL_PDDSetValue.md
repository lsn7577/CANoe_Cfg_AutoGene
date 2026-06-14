# TestIso11783IL_PDDSetValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDSetValue( dbNode node, dbSignal signal, dword elementNumber, float value );
```

## Description

Sets the value of a process variable.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
