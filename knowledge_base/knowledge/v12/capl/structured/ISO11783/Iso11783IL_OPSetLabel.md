# Iso11783IL_OPSetLabel

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetLabel( dword objectID, dword stringVarIdD, dword fontType, dword graphID ); // form 1
```

## Description

A Set Label command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPSetLabel( 
 1200, 1250, 1, 1260 );
```

## Availability

| Since Version |
|---|
