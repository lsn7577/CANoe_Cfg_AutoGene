# AvbGetCrfAudioSampleClockMultiplier

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword AvbGetCrfAudioSampleClockMultiplier(dword listenerOrTalkerHandle, dword& retClockMultiplier);
```

## Description

The function retrieves the audio sample clock multiplier of the CRF stream received by the Listener or originated by the Talker.

The nominal frequency of the audio sample clock is the clock frequency (see AvbGetCrfAudioSampleClockFrequency) multiplied by the multiplier returned by this function.

## Return Values

0: The function completed successfully.

## Availability

| Up to Version |
|---|
