# diagGetErrorString

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetErrorString (long errorCode, char bufferOut[], dword bufferLength)
```

## Description

Retrieves a text describing the error code.

## Return Values

Length of the text in bufferOut.

## Example

```c
on key 't'
{
  long retValue;
  char buffer[200];
  if ( 0 > (retValue=diagSetTarget("UDS_Diagnostic_Services"))) 
  {
    diagGetErrorString(retValue, buffer, elcount(buffer));
    write("Error: %s", buffer);
  }
}
```

## Availability

| Since Version |
|---|
