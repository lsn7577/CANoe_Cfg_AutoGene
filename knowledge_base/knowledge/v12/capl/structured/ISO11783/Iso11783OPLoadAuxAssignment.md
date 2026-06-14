# Iso11783OPLoadAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoadAuxAssignment( dword ecuHandle, char filename[] );
```

## Description

This function loads the "Preferred Auxiliary Input Assignment" from an ini file. If the ECU is active the "Preferred Assignment Message" is sent immediately. Otherwise it is sent if the ECU gets active.

The "Preferred Assignment" must be saved with Iso11783OPSaveAuxAssignment before.

## Return Values

0 or error code

## Example

```c
Iso11783OPLoad( handle, "ObjectPool.iop", "pool001"  );
Iso11783OPLoadAuxAssignment( handle, "Sprayer.INI");
Iso11783OPActivate( handle);
```

## Availability

| Since Version |
|---|
