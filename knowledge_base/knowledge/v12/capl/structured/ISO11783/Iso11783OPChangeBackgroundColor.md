# Iso11783OPChangeBackgroundColor

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeBackgroundColor( dword ecuHandle, dword objectID, dword color );
```

## Description

This function changes the background color of an object. The Change Background Color command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeBackgroundColor( handle, 1200, 5 );
```

## Availability

| Since Version |
|---|
