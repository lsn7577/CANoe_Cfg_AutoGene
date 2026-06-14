# coThisGetUnsigned

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coThisGetUnsigned( dword errCode[] );
```

## Description

The function returns a value with no leading sign of an object in the event functions coOnUploadResponse or coOnDownloadIndication. The call is only allowed in these event functions.

## Return Values

Value of the object entry

## Example

```c
dword errCode[1];
dword value;

value = coThisGetUnsigned( errCode );
```

## Availability

| Up to Version |
|---|
