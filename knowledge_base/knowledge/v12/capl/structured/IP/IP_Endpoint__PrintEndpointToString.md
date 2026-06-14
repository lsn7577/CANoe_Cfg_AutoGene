# IP_Endpoint::PrintEndpointToString

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::PrintEndpointToString(char endpoint[]);
```

## Description

Converts the endpoint to a character string.

## Return Values

0: Success

## Example

```c
void OnReceiveFrom( UdpSocket socket, long result, IP_Endpoint senderEndpoint, byte buffer[], dword size)
{
  char endpointText[60];
  senderEndpoint.PrintEndpointToString(endpointText);
  write("packet from %s received", endpointText );
}
```

## Availability

| Since Version |
|---|
