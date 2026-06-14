# FDXConfigureSequenceCounting

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXConfigureSequenceCounting(long fdxClientHandle, long mode);
```

## Description

This function sets the behavior with which CANoe should fill out the field seqNrOrDgramLen in the FDX datagram header.

Prerequisite for the function is to configure UPD/IPv4 or UDP/IPv6 as transport layer for the FDX feature.

## Return Values

0: Successful function call

## Availability

| Since Version |
|---|
