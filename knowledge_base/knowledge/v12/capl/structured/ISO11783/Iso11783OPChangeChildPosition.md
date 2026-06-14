# Iso11783OPChangeChildPosition

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeChildPosition( dword ecuHandle, dword parentID, dword objectID, long x, long y );
```

## Description

The function changes the absolute position of an object inside its parent object. A Change Child Position command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeChildPosition( handle, 1000, 1200, 10, 10 );
```

## Availability

| Since Version |
|---|
