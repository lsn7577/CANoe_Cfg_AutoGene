# Iso11783OPSelectColorMap

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSelectColorMap( dword ecuHandle, dword colorMapID );
```

## Description

The function selects a color map object. A Select Color Map command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPSelectColorMap( handle, 1400 );
```

## Availability

| Since Version |
|---|
