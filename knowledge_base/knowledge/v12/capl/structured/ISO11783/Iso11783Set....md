# Iso11783Set...

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783SetAAC( char[] deviceName, long aac);
long Iso11783SetIG( char[] deviceName, long ig);
long Iso11783SetVS( char[] deviceName, long vs);
long Iso11783SetVSInstance( char[] deviceName, long vsi);
long Iso11783SetFct( char[] deviceName, long fct);
long Iso11783SetFctInstance( char[] deviceName, long fct );
long Iso11783SetECUInstance( char[] deviceName, long ecui );
long Iso11783SetMC( char[] deviceName, long mc);
long Iso11783SetIN( char[] deviceName, long in);
```

## Description

The function modifies a part of the device name.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
