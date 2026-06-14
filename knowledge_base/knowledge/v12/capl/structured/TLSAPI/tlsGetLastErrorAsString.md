# tlsGetLastErrorAsString

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsGetLastErrorAsString(dword socket, char buffer[], dword bufferLength );
```

## Description

Retrieves the error message of the last operation that failed on a specified socket.

## Return Values

0: The error message was written into the text buffer. In case of an invalid error code, the error message has the format "Unknown error: x" assuming the last error code x for the specified socket.

## Example

```c
tlsOpen(clientHandle);
tlsAuthenticateAsServer(clientHandle, "Server1");

if ((tlsGetLastError(clientHandle) != 0) &&
   (tlsGetLastError(clientHandle) != 997))
{
  // an error occurred
  tlsGetLastErrorAsString(clientHandle, errorText, elcount(errorText));
  write( "tlsAuthenticateAsServer failed, %s (Result %d)", errorText,tlsGetLastError(clientHandle) );
  return;
}
```

## Availability

| Since Version |
|---|
