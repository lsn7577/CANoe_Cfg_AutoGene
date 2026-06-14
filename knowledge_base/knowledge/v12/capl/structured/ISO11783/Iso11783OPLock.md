# Iso11783OPLock

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLock( dword ecuHandle, dword lock, dword maskID, dword timeout );
```

## Description

The function locks the screen updates on the Virtual Terminal. A Lock command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPLock( handle, 1200, 1, 500 );
```

## Availability

| Since Version |
|---|
