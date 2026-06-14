# Iso11783OPSaveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSaveAuxAssignment( dword ecuHandle, char filename[] );
```

## Description

The function saves the current auxiliary input assignment as "Preferred Auxiliary Input Assignment" in an ini file.

With the function Iso11783OPLoadAuxAssignment the "Preferred Assignment" can be load and used again.

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );
[...]
Iso11783OPSaveAuxAssignment( handle, "Sprayer.INI");
[...]
```

## Availability

| Since Version |
|---|
