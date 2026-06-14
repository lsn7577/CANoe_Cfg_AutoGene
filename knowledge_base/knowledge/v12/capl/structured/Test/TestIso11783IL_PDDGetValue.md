# TestIso11783IL_PDDGetValue

> Category: `Test` | Type: `function`

## Syntax

```c
float TestIso11783IL_PDDGetValue( dbNode node, dbSignal signal, dword elementNumber );
```

## Description

The function requests the value of a process variable.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

value of the process variable, 0 if the variable is not defined

## Availability

| Since Version |
|---|
