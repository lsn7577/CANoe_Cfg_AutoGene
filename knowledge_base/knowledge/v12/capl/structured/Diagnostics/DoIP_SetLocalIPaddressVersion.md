# DoIP_SetLocalIPaddressVersion

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetLocalIPaddressVersion(dword addressIPVersion);
```

## Description

When no local IP address is given explicitly, select the local address according to the priority set with this function. For example, this will allow the selection of a specific address type when only the network adapter is configured.

## Return Values

Error code

## Example

```c
// Use the IPv6 address configured for the selected network adapter
char buffer[256];
DiagGetCommParameter( "DoIP.TESTER_Adapter", 0, buffer, elcount( buffer));
DoIP_SetTesterAdapter( buffer);
DoIP_SetLocalIPaddressVersion( 6);
```

## Availability

| Since Version |
|---|
