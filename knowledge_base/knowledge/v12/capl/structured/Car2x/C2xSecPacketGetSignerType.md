# C2xSecPacketGetSignerType

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecPacketGetSignerType(long packetHandle);
```

## Description

Retrieves how the message signer information is included in the message. The information can be transmitted as digest (HashedId8), certificate or certificate chain.

## Return Values

0: unsecured

## Example

```c
switch (C2xSecPacketGetSignerType(packetHandle))
{
case 0: // unsecured
  // ...
  break;
case 1: // digest
  // ...
  break;
case 2: // certificate
  // ...
  break;
case 3: // certificate chain
  // ...
  break;
default: // error
  // ...
  break;
}
```

## Availability

| Since Version |
|---|
