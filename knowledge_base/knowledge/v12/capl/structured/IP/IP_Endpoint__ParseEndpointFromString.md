# IP_Endpoint::ParseEndpointFromString

> Category: `IP` | Type: `function`

## Syntax

```c
long IP_Endpoint::ParseEndpointFromString(char endpoint[]);
```

## Description

Converts the character string to an endpoint and sets this endpoint to the IP endpoint value.

## Return Values

0: Success

## Example

```c
variables
{
  ip_Endpoint ipEndpoint;
}

on sysvar_update sysvar::Endpoint
{
  char endpointText[60];
  sysGetVariableString(this, endpointText, elcount(endpointText));
  ipEndpoint.ParseEndpointFromString(endpointText);
}
```

## Availability

| Since Version |
|---|
