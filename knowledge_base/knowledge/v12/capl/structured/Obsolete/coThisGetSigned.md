# coThisGetSigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long coThisGetSigned( dword errCode[] );
```

## Description

The function returns a value with leading sign of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions.

## Return Values

—

## Example

```c
dword errCode[1];
long value;

value = coThisGetSigned( errCode );
```

## Availability

| Up to Version |
|---|
