# A664InitMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitMessage (a664Message aMessage, dword srcIP, dword dstIP, word srcUDP, word dstUDP, word VLid, word payloadSize)
```

## Description

The complete Ethernet, IP- and UDP headers for an AFDX message are consistently set based on the given parameters. The payload area is initialized with 0.

## Availability

| Since Version |
|---|
