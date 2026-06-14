# TestIso11783IL_OPSetStringValue

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSetStringValue( dbNode node, dword objectID, char stringValue[] );
```

## Description

The functions set the string value of an object in the object pool. The object must exist in the object pool and must support a string value. If the Object Pool API is active, a Change String Value command is sent to the Virtual Terminal. This can be suppressed with Bit 0 in options.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
