# Iso11783IL_OPLoad

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLoad( char filename[] ); // form 1
```

## Description

The function loads an object pool file (*.iop). All other object pool access functions can only be used, if an object pool is loaded.

If the activation of the object pool was already done, the object pool is transmitted to the Virtual Terminal immediately. If not, this happens when the activation is done with Iso11873IL_OPActivate.

Optional a version designator for the object pool can be specified. The node layer tries to load the version with the Load Version command. If this is successful the object pool must not be transmitted to the Virtual Terminal.

This function is not necessary if a node was configured completely in the database (DBC):ISO11783IOPFilename and ISO11783IOPVersion are defined and VT21 message is assigned to the node.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPLoad( "ObjectPool.iop", "pool001"  );
Iso11783IL_OPActivate( );
```

## Availability

| Since Version |
|---|
