# TestIso11783IL_PDDSetParameter

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDSetParameter( dbNode node, char paramName[], float paramValue );
```

## Description

Changes an internal parameter of the PDD API.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
