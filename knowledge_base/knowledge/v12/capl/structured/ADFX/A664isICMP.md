# A664isICMP

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664isICMP (a664Frame aFrame, dbNode NodeName) (1)
```

## Description

This function returns the ICMP type and code for a packet. The intended use case is a check for an expected ICMP packet in an on-handler. The packet is checked according to the following rules:

## Availability

| Since Version |
|---|
