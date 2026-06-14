# Iso11783IL_OPChangeEndPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeEndPoint( dword objectID, dword width, dword height, dword direction ); // form 1
```

## Description

The function changes the length and alignment of a line object. A Change End Point command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeEndPoint( 1200, 50, 20, 0 );
```

## Availability

| Since Version |
|---|
