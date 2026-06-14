# A664InitMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664InitMessage (a664Message aMessage, dword srcIP, dword dstIP, word srcUDP, word dstUDP, word VLid, word payloadSize)
```

## Description

The complete Ethernet, IP- and UDP headers for an AFDX message are consistently set based on the given parameters. The payload area is initialized with 0.

## Parameters

| Name | Description |
|---|---|
| aMessage | The message object to be initialized. |
| srcIP | Source IP address to be used for the Eth and IP headers. |
| dstIP | Destination IP address to be used for the IP headers. |
| srcUDP | Source UDP port for the UDP header. |
| dstUDP | Destination UDP port for the UDP header. |
| VLid | VLId to be used for the destination Eth header (see selector EthVlId). |
| payloadSize | Size of the message payload after UDP header without counting the sequence number. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
