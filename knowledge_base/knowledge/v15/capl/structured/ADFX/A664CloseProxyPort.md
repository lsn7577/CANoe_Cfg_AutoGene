# A664CloseProxyPort

> Category: `ADFX` | Type: `function`

## Syntax

```c
long a664CloseProxyPort (WORD channel, DWORD outMsgId)
```

## Description

Method to close a specific socket port, which was generated using a664InitProxyPort.

This call is only required, if an existing message-pair or UDP-port combination needs to be modified.

On measurement end all existing proxy-ports are closed automatically.

## Parameters

| Name | Description |
|---|---|
| <channel> | AFDX-channel (1 to 16) to which socket packets should be mapped to (sent and observed). |
| <outMsgID> | messageID which is observed on AFDX-channel and transferred to the socket if detected. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
