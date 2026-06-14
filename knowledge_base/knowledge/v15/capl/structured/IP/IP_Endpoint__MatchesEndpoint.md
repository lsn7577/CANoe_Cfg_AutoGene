# IP_Endpoint::MatchesEndpoint

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Endpoint::MatchesEndpoint(IP_Endpoint ipEndpoint); // form 1
long IP_Endpoint::MatchesEndpoint(IP_Endpoint ipEndpoint, long prefix); // form 2
```

## Description

Compares two endpoints whereas wildcards matches always. If no transport protocol type is set or the port number is set to 0 this is considered as wildcard. Additionally, the IP address must match according to MatchesAddress.

With form 2 only the network address of the IP address will be considered.

## Parameters

| Name | Description |
|---|---|
| ipEndpoint | An IP endpoint that may contain wildcards. |
| prefix | Prefix in number of bits. Only the first bits specified by prefix are considered. |

## Example

Example 1

Example 2

Example 3

```c
on start
{
  IP_Endpoint 192.168.1.1:4000 ep1;
  IP_Endpoint 192.168.1.2:4000 ep2;
  if (ep1.MatchesEndPoint( ep2 ) == 1)
  {
    write( "Endpoints match!" );
  }
}
on start
{
  IP_Endpoint 192.168.1.1:4000 ep1;
  IP_Endpoint 192.168.1.2:4000 ep2;
  if (ep1.MatchesEndPoint( ep2, 24 ) == 1)
  {
    write( "Endpoints match!" );
  }
}
on start
{
  IP_Endpoint 192.168.1.1:4000 ep1;
  IP_Endpoint 192.168.1.1:4000 ep2;
  if (ep1 == ep2)
  {
    write( "Endpoints are equal!" );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | 13.0: form 1 | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
