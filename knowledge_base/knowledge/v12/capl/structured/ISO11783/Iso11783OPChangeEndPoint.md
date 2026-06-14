# Iso11783OPChangeEndPoint

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeEndPoint( dword ecuHandle, dword objectID, dword width, dword height, dword direction );
```

## Description

The function changes the length and alignment of a line object. A Change End Point command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeEndPoint( handle, 1200, 50, 20, 0 );
```

## Availability

| Since Version |
|---|
