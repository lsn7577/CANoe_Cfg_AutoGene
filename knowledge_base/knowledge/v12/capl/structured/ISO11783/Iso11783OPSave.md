# Iso11783OPSave

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSave( dword ecuHandle, char filename[] );
```

## Description

The function saves an object pool file (*.iop).

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );

Iso11783OPSave( 
 handle, "ObjectPool.iop");
```

## Availability

| Since Version |
|---|
