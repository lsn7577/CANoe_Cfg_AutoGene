# Iso11783OPActivate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPActivate( dword ecuHandle);
```

## Description

The function activates the Object Pool API. The initialization procedure with the Virtual Terminal is performed and the object pool is transmitted to the Virtual Terminal.

During the initialization procedure some information from the Virtual Terminal is requested. This can be suppressed with the options parameter. The requested information can be get with the function Iso11783OPGetVTInfo.

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );

Iso11783OPLoad( handle, "ObjectPool.iop", 
 "pool001" );
Iso11783OPActivate( handle );
Iso11783ECUGoOnline(handle, gECUAddress );
```

## Availability

| Since Version |
|---|
