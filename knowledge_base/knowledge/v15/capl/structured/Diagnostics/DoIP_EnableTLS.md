# DoIP_EnableTLS

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_EnableTLS(dword mode, char name[]);
```

## Description

Enables secure communication for DoIP tester or ECU simulation. If enabled, DoIP communication is carried out via TLS (Transport Layer Security).

## Parameters

| Name | Description |
|---|---|
| mode | 0: disable TLS, no secure communication. 1: enable TLS by routing activation response code (RARC) 0x07. 2: (tester only) enable TLS. Only secure connection is allowed. If ECU responds with RARC 0x10 on the first unsecure routing activation, the tester stops communication. 3: (tester only) enable TLS. Tester connects to ECU directly via TLS without establishing connection on unsecure port (e.g. 13400). |
| name | (ECU simulation) name of the server certificate, which must be used for TLS connection. It must be one of the certificates, available in the security profile, selected for the TCP/IP stack of the ECU simulation node. (Tester) name of the client certificate. Currently, client certificates are not supported for DoIP. The parameter is reserved for future use. It must be an empty string "". |

## Return Values

—

## Example

Example 1

Example 2

```c
on preStart
{
  // enable TLS for ECU simulation
  // use certificate 'Server1' (security profile 'DoIP over TLS Demo')
  DoIP_EnableTLS(1, "Server1");
}
on preStart
{
  // enable TLS for tester
  DoIP_EnableTLS(2, "");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 SP3 | — | — | — | 6 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
