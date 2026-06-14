# TestIso11783IL_PDDDelete

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDDelete( dbNode node );
```

## Description

Deletes the process data directory and disconnects from the Task Controller.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
