# TestIso11783IL_OPSetProperty

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSetProperty( dbNode node, char propertyName[], long newValue );
```

## Description

The function sets a property of the Object Pool API, i.e. the supported Virtual Terminal version.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Unction has been executed successfully

## Availability

| Since Version |
|---|
