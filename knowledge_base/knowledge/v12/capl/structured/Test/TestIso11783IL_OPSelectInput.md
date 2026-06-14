# TestIso11783IL_OPSelectInput

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSelectInput( dbNode node, dword objectID, dword select );
```

## Description

The function selects an input object. A Select Input command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
