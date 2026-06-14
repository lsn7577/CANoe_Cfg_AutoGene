# Iso11783IL_OPChangeActiveMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeActiveMask( dword maskID ); // form 1
```

## Description

This function changes the active data mask. The Change Active Mask command is sent to the Virtual Terminal.

## Return Values

= 0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangeActiveMask( 1000 );
```

## Availability

| Since Version |
|---|
