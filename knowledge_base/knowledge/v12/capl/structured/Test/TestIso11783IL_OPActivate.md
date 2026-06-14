# TestIso11783IL_OPActivate

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPActivate( dbNode node);
```

## Description

The function activates the Object Pool API. The initialization procedure with the Virtual Terminal is performed and the object pool is transmitted to the Virtual Terminal.

During the initialization procedure some information from the Virtual Terminal is requested. This can be suppressed with the options parameter. The requested information can be get with the function Iso11783IL_OPGetVTInfo.

This function is not necessary if a node was configured completely in the database (DBC):ISO11783IOPFilename and ISO11783IOPVersion are defined and VT21 message was assigned to the node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Function has been executed successfully

## Example

```c
TestIso11783IL_OPDeactivate(Sprayer, 0);
TestIso11783IL_OPSetProperty(Sprayer, "VTFunctionInstance", 1 );
TestIso11783IL_OPLoad(Sprayer, "Sprayer.iop", "Ver1" );
TestIso11783IL_OPActivate(Sprayer, 0);
```

## Availability

| Since Version |
|---|
