# TestIso11783IL_PDDUpdateDeviceDescription

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDUpdateDeviceDescription( dbNode node, char deviceCfgPath [] );
```

## Description

The function updates the current device description object pool at run-time.

Only the device object and objects of type DeviceValuePresentation of the specified file are transmitted.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

error code

## Availability

| Since Version |
|---|
