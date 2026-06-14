# diagSetTimeout

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSetTimeout (DWORD timeout)
```

## Description

Specifies the request timeout.

A diagnostics response must start within this time, i.e. this corresponds to the P2 timeout.

## Parameters

| Name | Description |
|---|---|
| timeout | Timeout in msDefault: 1000 ms. |

## Return Values

Error code

## Example

```c
on start
{
  diagSetTimeout (200); // Set timeout to 200 ms
  diagSetTimeoutHandler("Request_Timeout");
}

on key '1'
{
  DiagRequest SimECU.ReadDataByIdentifier_Process req;
  diagSendRequest(req);
}

void Request_Timeout()
{
  write("No response received within expected time frame!");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
