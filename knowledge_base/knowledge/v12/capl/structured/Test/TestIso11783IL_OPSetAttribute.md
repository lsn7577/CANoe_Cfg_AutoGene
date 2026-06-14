# TestIso11783IL_OPSetAttribute

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPSetAttribute( dbNode node, dword objectID, dword attributeID, long value );
```

## Description

The function sets an attribute value of an object. The object must exist in the object pool and support the attribute ID. If the Object Pool API is active, the Change Attribute command (175) is sent to the Virtual Terminal. This can be suppress with Bit 0 in options.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
