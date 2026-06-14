# Iso11783IL_FSGetVolumeInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSGetVolumeInfo( dword infoCount, dword retInfo[] );
```

## Description

This function returns information about the current volume. The current volume is the volume where the configuration is stored.

## Return Values

0: Function has been executed successfully

## Example

```c
dword info[3];

Iso11783IL_FSGetVolumeInfo( elCount(info), info );
write( "Total 
 size %d blocks", info[1] );
write( "Free size 
 %d blocks", info[2] );
```

## Availability

| Since Version |
|---|
