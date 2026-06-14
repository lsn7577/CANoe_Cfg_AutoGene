# Iso11783OPEnableObject

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPEnableObject( dword ecuHandle, dword objectID, dword enable );
```

## Description

The function activates or deactivates an input object. A Enable Object command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPEnableObject( 
 handle, 1200, 1 );
```

## Availability

| Since Version |
|---|
