# Iso11783OPSetLabel

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetLabel( dword ecuHandle, dword objectID, dword stringVarIdD, dword fontType, dword graphID );
```

## Description

A Set Label command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPSetLabel( 
 handle, 1200, 1250, 1, 1260 );
```

## Availability

| Since Version |
|---|
