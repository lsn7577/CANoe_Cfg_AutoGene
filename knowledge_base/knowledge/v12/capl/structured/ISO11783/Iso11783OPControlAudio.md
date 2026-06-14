# Iso11783OPControlAudio

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPControlAudio( dword ecuHandle, dword activations, dword frequency, dword onTime, dword offTime );
```

## Description

The function plays an acoustic signal on the Virtual Terminal. A Control Audio Device command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPControlAudio( 
 handle, 2, 2000, 100, 50 );
```

## Availability

| Since Version |
|---|
