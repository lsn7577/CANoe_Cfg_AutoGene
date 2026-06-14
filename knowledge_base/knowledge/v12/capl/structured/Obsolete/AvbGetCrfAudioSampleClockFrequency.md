# AvbGetCrfAudioSampleClockFrequency

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword AvbGetCrfAudioSampleClockFrequency(dword listenerOrTalkerHandle, dword& retClockFrequency);
```

## Description

The function retrieves the audio sample clock frequency of the CRF stream received by the Listener or originated by the Talker.

The nominal frequency of the audio sample clock is the frequency returned by this function multiplied by the clock multiplier (see AvbGetCrfAudioSampleClockMultiplier).

## Return Values

0: The function completed successfully.

## Availability

| Up to Version |
|---|
