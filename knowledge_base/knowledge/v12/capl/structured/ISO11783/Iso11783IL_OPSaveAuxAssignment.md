# Iso11783IL_OPSaveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSaveAuxAssignment( char filename[] ); // form 1
```

## Description

The function saves the current auxiliary input assignment as Preferred Auxiliary Input Assignment in an INI file.

With the function Iso11783IL_OPLoadAuxAssignment the Preferred Assignment can be load and used again.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPSaveAuxAssignment( "Sprayer.INI");
```

## Availability

| Since Version |
|---|
