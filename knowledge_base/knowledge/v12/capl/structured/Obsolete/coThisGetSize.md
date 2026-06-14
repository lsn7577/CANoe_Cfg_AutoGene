# coThisGetSize

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coThisGetSize( dword errCode[] );
```

## Description

The function returns the size of the data of a SDO transfer in the event function coOnUploadResponse or coOnDownloadIndication. The call is only allowed in this event function.

## Return Values

—

## Example

```c
dword errCode[1];
dword size;

size = coThisGetSize( errCode );
```

## Availability

| Up to Version |
|---|
