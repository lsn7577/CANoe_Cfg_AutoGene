# IP_Endpoint::MatchesEndpoint

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::MatchesEndpoint(IP_Endpoint ipEndpoint); // form 1
```

## Description

Compares two endpoints whereas wildcards matches always. If no transport protocol type is set or the port number is set to 0 this is considered as wildcard. Additionally, the IP address must match according to MatchesAddress.

With form 2 only the network address of the IP address will be considered.

## Return Values

0: No match

## Example

```c
on start
{
  IP_Endpoint 192.168.1.1:4000 ep1;
  IP_Endpoint 192.168.1.1:4000 ep2;
  if (ep1 == ep2)
  {
    write( "Endpoints are equal!" );
  }
}
```

## Availability

| Since Version |
|---|
