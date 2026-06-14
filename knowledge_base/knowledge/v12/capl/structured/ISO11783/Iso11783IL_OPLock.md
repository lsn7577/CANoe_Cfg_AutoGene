# Iso11783IL_OPLock

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPLock( dword lock, dword maskID, dword timeout ); // form 1
```

## Description

The function locks the screen updates on the Virtual Terminal. A Lock command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPLock( 1200, 1, 500 );
```

## Availability

| Since Version |
|---|
