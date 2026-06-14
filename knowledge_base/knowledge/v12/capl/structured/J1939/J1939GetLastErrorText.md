# J1939GetLastErrorText

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetLastErrorText( dword bufferSize, char buffer[] );
```

## Description

This function gets the description of the last occurred error.

## Return Values

number of characters that are copied to buffer

## Example

```c
dword size = 100;
char errText[size];

J1939GetLastErrorText( size, errText );
```

## Availability

| Since Version |
|---|
