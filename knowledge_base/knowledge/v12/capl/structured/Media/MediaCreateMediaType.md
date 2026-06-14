# MediaCreateMediaType

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaCreateMediaType ();
```

## Description

Creates an empty media type. After usage use MediaReleaseMediaType to release the media type.

## Return Values

0: The function failed. Call MediaGetLastError to get a more specific error code.

## Availability

| Since Version |
|---|
