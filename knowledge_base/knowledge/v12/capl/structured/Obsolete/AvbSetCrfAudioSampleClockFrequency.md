# AvbSetCrfAudioSampleClockFrequency

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword AvbSetCrfAudioSampleClockFrequency(dword talkerHandle, dword clockFrequency);
```

## Description

The function sets the audio sample clock frequency of the CRF stream originated by the Talker.

The nominal frequency of the audio sample clock is the frequency set by this function multiplied by the clock multiplier (see AvbSetCrfAudioSampleClockMultiplier).

## Return Values

0: The function completed successfully.

## Availability

| Up to Version |
|---|
