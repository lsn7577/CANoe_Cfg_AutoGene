# Iso11783OPLoad

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoad( dword ecuHandle, char filename[] );
```

## Description

The function loads an object pool file (*.iop). All other object pool access functions can only be used, if an object pool is loaded.

If the activation of the object pool was already done, the object pool is transmitted to the Virtual Terminal immediately. If not, this happens when the activation is done with Iso11783OPActivate.

Optional a version designator for the object pool can be specified. The node layer tries to load the version with the Load Version command. If this is successful the object pool must not be transmitted to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );

Iso11783OPLoad( handle, "ObjectPool.iop", "pool001"  );
ISo11783OPActivate( handle);
Iso11783ECUGoOnline(handle, gECUAddress );
```

## Availability

| Since Version |
|---|
