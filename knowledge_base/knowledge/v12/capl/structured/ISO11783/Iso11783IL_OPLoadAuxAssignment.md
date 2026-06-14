# Iso11783IL_OPLoadAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLoadAuxAssignment( char filename[] ); // form 1
```

## Description

This function loads the Preferred Auxiliary Input Assignment from an INI file. If the ECU is active the Preferred Assignment Message is sent immediately. Otherwise it is sent if the ECU gets active.

The Preferred Assignment must be saved with Iso11783IL_OPSaveAuxAssignment before.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPLoad( "ObjectPool.iop", "pool001"  );
Iso11783IL_OPLoadAuxAssignment( "Sprayer.INI");
Iso11783IL_OPActivate( );
```

## Availability

| Since Version |
|---|
