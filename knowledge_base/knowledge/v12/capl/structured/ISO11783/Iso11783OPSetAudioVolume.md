# Iso11783OPSetAudioVolume

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSetAudioVolume( dword ecuHandle, dword volume );
```

## Description

The function sets the audio volume of the Virtual Terminal. A Set Audio Volume command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPSetAudioVolume( handle, 100 );
```

## Availability

| Since Version |
|---|
