# AfdxCompletePacket

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxCompletePacket( long packet );
```

## Description

This function completes a packet before sending it with AfdxOutputPacket. It calculates the fields that are marked with CompleteProtocol in the protocol overview, e.g. check sum, lengths, etc.

A frame needs to be completed prior to transmission. This is the case when one of the header fields is changed in an existing frame or the payload size is changed afterwards. With this function the check sum and length fields in the UDP and IPv4 header are calculated and filled in.

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message that has been created with AfdxInitPacket. |

## Example

See example of AfdxResizeToken.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
