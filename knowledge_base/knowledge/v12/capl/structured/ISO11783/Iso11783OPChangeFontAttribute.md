# Iso11783OPChangeFontAttribute

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangeFontAttribute( dword ecuHandle, dword objectID, dword color, dword size, dword type, dword style );
```

## Description

The function changes the properties of a font attribute object. A Change Font Attribute command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangeFontAttribute( handle, 1100, 10, 3, 0, 0x01 );
```

## Availability

| Since Version |
|---|
