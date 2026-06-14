# TestIso11783IL_OPSetNumericValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSetNumericValue( dbNode node, dword objectID, long numericValue );
```

## Description

The function sets the numerical value of an object. The object must exist in the object pool and must support a numerical value. If the Object Pool API is active, a Change Numeric Value command is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
