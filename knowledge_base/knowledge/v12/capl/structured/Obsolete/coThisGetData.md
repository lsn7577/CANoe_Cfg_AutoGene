# coThisGetData

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coThisGetData( char buffer[], dword bufferSize, dword errCode[] );
```

## Description

The function returns the data of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions. The size of the data can be determined with coThisGetSize.

## Return Values

—

## Example

```c
dword errCode[1];
byte buffer[128];

coThisGetData( buffer, elCount(buffer), errCode );
```

## Availability

| Up to Version |
|---|
