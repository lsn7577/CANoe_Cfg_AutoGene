# coThisGetFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
float coThisGetFloat( dword errCode[] );
```

## Description

The function returns a floating point value of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions.

## Return Values

—

## Example

```c
dword errCode[1];
float value;

value = coThisGetFloat( errCode );
```

## Availability

| Up to Version |
|---|
