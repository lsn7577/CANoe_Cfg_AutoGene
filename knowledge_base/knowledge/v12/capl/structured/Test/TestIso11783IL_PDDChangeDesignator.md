# TestIso11783IL_PDDChangeDesignator

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDChangeDesignator( dbNode node, word objectID, char asciiDesignator[] );
```

## Description

The function sends a Change Designator message with a new object designator to the Task Controller.

The first variant converts the ASCII designator string to an UTF-8 string if the supported version is 2 or higher.

In the second variant you can specify if the designator string shall encoded to UTF-8 or not.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

error code

## Availability

| Since Version |
|---|
