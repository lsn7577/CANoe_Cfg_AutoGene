# Iso11783OPChangeActiveMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeActiveMask( dword ecuHandle, dword maskID );
```

## Description

This function changes the active data mask. The Change Active Mask command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeActiveMask( handle, 1000 );
```

## Availability

| Since Version |
|---|
