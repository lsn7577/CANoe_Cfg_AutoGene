# diagGetCommunicationErrorString

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetCommunicationErrorString( long communicationError, char descriptionOut, dword bufferLen);
```

## Description

Returns a description for the given communication error.

## Return Values

Number of characters written to the buffer.

## Example

```c
...
if (0 == TestWaitForDiagResponse( req, 2000))
{
  char errStr[100];
  err = DiagGetLastCommunicationError();
  DiagGetCommunicationErrorString( err, errStr, elcount(errStr));
  write("LastCommunicationError=%d - %s", err, errStr);
}
```

## Availability

| Since Version |
|---|
