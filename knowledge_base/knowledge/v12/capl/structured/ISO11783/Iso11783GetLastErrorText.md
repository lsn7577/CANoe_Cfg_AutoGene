# Iso11783GetLastErrorText

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetLastErrorText( dword bufferSize, char buffer[] );
```

## Description

This function gets the description of the last occurred error.

## Return Values

Number of characters that are copied to buffer

## Example

```c
dword size = 100;
char errText[size];

Iso11783GetLastErrorText( size, errText );
```

## Availability

| Since Version |
|---|
