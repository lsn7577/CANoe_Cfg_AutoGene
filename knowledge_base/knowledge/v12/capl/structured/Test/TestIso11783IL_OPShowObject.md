# TestIso11783IL_OPShowObject

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPShowObject( dbNode node, dword objectID, dword show );
```

## Description

The function shows or hides an object. The Show Object command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
