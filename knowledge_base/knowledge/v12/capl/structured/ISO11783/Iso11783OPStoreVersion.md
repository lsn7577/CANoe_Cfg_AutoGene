# Iso11783OPStoreVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPStoreVersion( dword ecuHandle, char versionName[] );
```

## Description

The function stores the current object pool on the Virtual Terminal. A Store Version command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPStoreVersion( 
 handle, "POOL01A" );
```

## Availability

| Since Version |
|---|
