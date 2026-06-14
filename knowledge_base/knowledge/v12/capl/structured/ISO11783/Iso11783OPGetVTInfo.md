# Iso11783OPGetVTInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetVTInfo( dword ecuHandle, char key[] );
```

## Description

During initialization phase the Object Pool API request some information about the capabilities from Virtual Terminal. These information can be get with this function.

## Example

```c
LONG vtWidth;
vtWidth = Iso11783OPGetVTInfo( handle, "Width" );
```

## Availability

| Since Version |
|---|
