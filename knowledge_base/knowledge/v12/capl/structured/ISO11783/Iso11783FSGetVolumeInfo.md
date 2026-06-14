# Iso11783FSGetVolumeInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSGetVolumeInfo( dword infoCount, dword retInfo[] );
```

## Description

This function returns information about the current volume. The current volume is the volume where the configuration is stored.

## Return Values

0 or error code

## Example

```c
dword info[3];

Iso11783FSGetVolumeInfo( elCount(info), info );
write( "Total 
 size %d blocks", info[1] );
write( "Free size 
 %d blocks", info[2] );
```

## Availability

| Since Version |
|---|
