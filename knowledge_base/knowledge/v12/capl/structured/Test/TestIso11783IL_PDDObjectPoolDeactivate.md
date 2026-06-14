# TestIso11783IL_PDDObjectPoolDeactivate

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDObjectPoolDeactivate( dbNode node );
```

## Description

The function sends an Object-pool Deactivate message to the Task Controller and disconnects the connection to the Task Controller.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

error code

## Availability

| Since Version |
|---|
