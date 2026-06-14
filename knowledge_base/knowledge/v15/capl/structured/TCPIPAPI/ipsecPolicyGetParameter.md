# ipsecPolicyGetParameter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecPolicyGetParameter(long policy, char[] parameter, char[] value); // form 1
long ipsecPolicyGetParameter(long policy, char[] parameter, IP_Endpoint value); // form 2
long ipsecPolicyGetParameter(long policy, char[] parameter, dword value); // form 3
```

## Description

Get a parameter from a security policy record.

## Parameters

| Name | Description |
|---|---|
| policy | Handle to a security policy record object. |
| Source | Returns the source selector. |
| Destination | Returns the destination selector. |
| UNSPEC | 0 |
| ESP | 1 |
| AH | 2 |
| ANY | 0 |
| TRANSPORT | 1 |
| TUNNEL | 2 |
| DEFAULT | 0 |
| USE | 1 |
| REQUIRE | 2 |
| DISCARD | 0 |
| NONE | 1 |
| IPSEC | 2 |
| ENTRUST | 3 |
| BYPASS | 4 |
| value | The returned value of the parameter. |

## Example

```c
on start
{
  dword socket;

  // add a policy
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.0:0), 24, "any", "out ipsec ah/transport//require");

  // try to send data which maches the policy -> this will trigger OnIpsecSadbAcquire
  socket = udpOpen(ip_Endpoint(0.0.0.0:0));
  udpSendTo(socket, ip_Endpoint(192.168.1.10:12345), "hello world", 11);
}

void PrintSecurityPolicyParameter(long handle, char parameterName[])
{
  char value[100];
  ip_Endpoint ep;
  if(ipsecPolicyGetParameter(handle, parameterName, value) >= 0)
  {
    write("%s: %s", parameterName, value);
  }
  else if(ipsecPolicyGetParameter(handle, parameterName, ep) >= 0)
  {
    ep.PrintEndpointToString(value);
    write("%s: %s", parameterName, value);
  }
}

void OnIpsecSadbAcquire(ip_Endpoint source, ip_Endpoint destination, long policyHandle)
{
  PrintSecurityPolicyParameter(policyHandle, "source");
  PrintSecurityPolicyParameter(policyHandle, "destination");
  PrintSecurityPolicyParameter(policyHandle, "protocol");PrintSecurityPolicyParameter(policyHandle, "mode");
  PrintSecurityPolicyParameter(policyHandle, "level");
  PrintSecurityPolicyParameter(policyHandle, "policytype");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP3 | — | — | — | 4.0 SP3 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
