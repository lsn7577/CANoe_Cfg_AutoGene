# DoIP_GetLastResponseCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_GetLastResponseCode();
```

## Description

Returns the last negative response code received from the peer.

## Return Values

1: No response code received yet , or this error does not have a specific response code

## Example

```c
void DoIP_ErrorInd( int error)
{
  write( "received error %d with error code %d", error, DoIP_GetLastResponseCode());
}
```

## Availability

| Since Version |
|---|
