# MediaGetLastError

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaGetLastError();
```

## Description

Retrieves the calling CAPL program’s last-error code value of the Media API. This code represents a Windows HRESUL value typically in the value ranges reserved for the Windows Media Foundation (see error codes).

## Return Values

Error code

## Example

```c
dword retVal;
dword listenerHandle;
// open a listener
listenerHandle = AvbOpenListener();

// check if last function was successfully executed
if ((retVal = AvbGetLastError()) != 0)
{
  write("AVB IL error occured: Error code: %d", retVal);
}
```

## Availability

| Since Version |
|---|
