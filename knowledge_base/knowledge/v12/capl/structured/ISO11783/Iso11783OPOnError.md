# Iso11783OPOnError

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnError( dword ecuHandle, long error, dword vtFunction );
```

## Description

The function is called by the node layer, when the object pool detects an error.

## Return Values

—

## Example

```c
void Iso11783OPOnError( dword handle, LONG error, dword vtFunction )
{
}
```

## Availability

| Since Version |
|---|
