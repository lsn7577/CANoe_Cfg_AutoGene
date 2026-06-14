# Iso11783IL_OPChangeLineAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeLineAttribute( dword objectID, dword color, dword width, dword art ); // form 1
```

## Description

The function changes the properties of a line attribute object. A Change Line Attribute command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeLineAttribute( 1100, 10, 3, 0xaa );
```

## Availability

| Since Version |
|---|
