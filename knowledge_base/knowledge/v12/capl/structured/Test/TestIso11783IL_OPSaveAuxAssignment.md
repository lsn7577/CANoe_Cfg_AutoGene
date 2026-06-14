# TestIso11783IL_OPSaveAuxAssignment

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSaveAuxAssignment( dbNode node, char filename[] );
```

## Description

The function saves the current auxiliary input assignment as Preferred Auxiliary Input Assignment in an INI file.

With the function Iso11783IL_OPLoadAuxAssignment the "Preferred Assignment" can be load and used again.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
