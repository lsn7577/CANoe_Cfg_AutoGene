# Iso11783IL_OPControlAudio

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPControlAudio( dword activations, dword frequency, dword onTime, dword offTime ); // form 1
```

## Description

The function plays an acoustic signal on the Virtual Terminal. A Control Audio Device command is sent to the Virtual Terminal.

## Example

```c
Iso11783IL_OPControlAudio( 
 2, 2000, 100, 50 );
```

## Availability

| Since Version |
|---|
