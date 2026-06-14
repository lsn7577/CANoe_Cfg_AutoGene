# Iso11783IL_OPActivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPActivate( ); // form 1
```

## Description

The function activates the Object Pool API. The initialization procedure with the Virtual Terminal is performed and the object pool is transmitted to the Virtual Terminal.

During the initialization procedure some information from the Virtual Terminal is requested. This can be suppressed with the options parameter. The requested information can be get with the function Iso11783IL_OPGetVTInfo.

This function is not necessary if a node was configured completely in the database (DBC):ISO11783IOPFilename and ISO11783IOPVersion are defined and VT21 message was assigned to the node.

## Return Values

0: Function has been executed successfully

## Example

```c
void MoveToVtWithFunctionInstance1()
{
  Iso11783IL_OPDeactivate();
  Iso11783IL_OPSetProperty( "VTFunctionInstance", 1 );
  SetTimer( mMoveTimer, 1000 );
}

on timer mMoveTimer
{
  Iso11783IL_OPLoad( "Sprayer.iop" );
  Iso11783IL_OPActivate();
}
```

## Availability

| Since Version |
|---|
