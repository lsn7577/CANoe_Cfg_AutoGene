# OnLocalSecurityQueryLocalFreshness

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword OnLocalSecurityQueryLocalFreshness(dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
```

## Description

This callback handler is called when a node receives a secured PDU and when a node transmits a secured PDU.

It provides the possibility to build a CAPL based freshness. This freshness value is preferred to the internal Freshness Manager in the Vector Security Manager.

The internal freshness value is used if this callback is not implemented or returns an invalid value.

## Example

```c
/// This callback can be used to get provide a USER based freshness value
/// This callback is called BEFORE the cmac is calculated.
/// The freshness value is used to calculate the CMAC internally.
/// It is possible to specify an older or newer freshness value, the CMAC will be "correct" but the freshness is "wrong" (compared to the freshness of the system)
dword OnLocalSecurityQueryLocalFreshness(dword context, char pduName[], dword dataId, dword freshnessValueId, dword attemptNr, byte payload[], dword payloadLength, qword& freshness, dword& freshnessLength, qword truncatedRxFreshness, dword truncatedRxFreshnessBitLength)
{
  if ((dataId == 1) && (context == 0)) // check for PDU with data ID and     
  context [(0 = tx) (1 = rx)] to specify a freshness for
  {
    freshness = 7;  // new Freshness Value
    freshnessLength = 64; // new freshness length

    return 1; // use my values
  }
  return 0; // for all others use internal calculated freshness values
}
```

## Availability

| Up to Version |
|---|
