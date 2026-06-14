# Iso11783OPShowObject

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPShowObject( dword ecuHandle, dword objectID, dword show );
```

## Description

The function shows or hides an object. The Show Object command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPShowObject( 
 handle, 1200, 1 );
```

## Availability

| Since Version |
|---|
