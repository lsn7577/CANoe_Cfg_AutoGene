# AvbSetCrfAudioSampleClockMultiplier

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword AvbSetCrfAudioSampleClockMultiplier(dword talkerHandle, dword clockMultiplier);
```

## Description

The function sets the audio sample clock multiplier of the CRF stream originat-ed by the Talker.

The nominal frequency of the audio sample clock is the clock frequency (see AvbSetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function.

## Return Values

0: The function completed successfully.

## Availability

| Up to Version |
|---|
