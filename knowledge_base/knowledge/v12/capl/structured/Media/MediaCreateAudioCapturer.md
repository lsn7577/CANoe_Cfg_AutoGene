# MediaCreateAudioCapturer

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaCreateAudioCapturer();
```

## Description

Creates a streaming audio capturer which is a media source that captures audio from an input device, e.g. a microphone.

The audio capturer provides uncompressed audio in either PCM or IEEE floating-point format.

## Return Values

0: The function failed. Call MediaGetLastError to get a more specific error code.

## Availability

| Since Version |
|---|
