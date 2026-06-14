# AfdxCompletePacket

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxCompletePacket( long packet );
```

## Description

This function completes a packet before sending it with AfdxOutputPacket. It calculates the fields that are marked with CompleteProtocol in the protocol overview, e.g. check sum, lengths, etc.

A frame needs to be completed prior to transmission. This is the case when one of the header fields is changed in an existing frame or the payload size is changed afterwards. With this function the check sum and length fields in the UDP and IPv4 header are calculated and filled in.

## Availability

| Since Version |
|---|
