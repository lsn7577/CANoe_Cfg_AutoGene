# Iso11783OPLoadVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPLoadVersion( dword ecuHandle, char versionName[] );
```

## Description

The function loads an object pool, which is stored on the Virtual Terminal. A Load Version command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPLoadVersion( 
 handle, "POOL01A" );
```

## Availability

| Since Version |
|---|
