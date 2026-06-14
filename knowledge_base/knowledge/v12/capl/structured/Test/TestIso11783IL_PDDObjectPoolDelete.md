# TestIso11783IL_PDDObjectPoolDelete

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDObjectPoolDelete( dbNode node );
```

## Description

The function deletes the current device description object pool and sends an Object-pool Delete message to the Task Controller

Contrary to Iso11783IL_PDDDelete the connection to the Task Controller is not removed.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

error code

## Availability

| Since Version |
|---|
