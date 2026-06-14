# DoIP_SetLocalIPaddressVersion

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetLocalIPaddressVersion(dword addressIPVersion);
```

## Description

When no local IP address is given explicitly, select the local address according to the priority set with this function. For example, this will allow the selection of a specific address type when only the network adapter is configured.

## Parameters

| Name | Description |
|---|---|
| addressIPVersion | 0: Use IPv6 address if no IPv4 address is available (default) 4: Use only IPv4 address 6: Use only IPv6 address other: reserved |

## Return Values

Error code

## Example

```c
// Use the IPv6 address configured for the selected network adapter
char buffer[256];
DiagGetCommParameter( "DoIP.TESTER_Adapter", 0, buffer, elcount( buffer));
DoIP_SetTesterAdapter( buffer);
DoIP_SetLocalIPaddressVersion( 6);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | — | — | — | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
