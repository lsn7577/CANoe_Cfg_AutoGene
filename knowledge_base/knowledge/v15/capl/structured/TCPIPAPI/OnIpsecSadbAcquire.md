# OnIpsecSadbAcquire

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnIpsecSadbAcquire(ip_Endpoint source, ip_Endpoint destination, long policyHandle);
```

## Description

Get a parameter from a security policy record.

## Parameters

| Name | Description |
|---|---|
| source | Source endpoint for which the security association is acquired. |
| destination | Destination endpoint for which the security association is acquired. |
| policyHandle | Handle to the security policy which caused the acquire callback. |

## Return Values

—

## Example

```c
variables
{
  UdpSocket socket;
}

on start
{
  // add a policy
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.0:0), 24, "any", "out ipsec ah/transport//require");

  // open a udp socket
  socket = UdpSocket::Open(ip_Endpoint(0.0.0.0:0));
}

on key 's'
{
  //try to send data which maches the policy -> the first time will trigger OnIpsecSadbAcquire because there is no security association.
  // The first packet will be discareded because the policy requires IPsec.
  socket.SendTo(ip_Endpoint(192.168.1.10:12345), "hello world", 11);
}

// add a security policy in the acquire callback
void OnIpsecSadbAcquire(ip_Endpoint source, ip_Endpoint destination, long policyHandle)
{
  char protocol[20];
  char mode[20];
  long sa;
  char sourceEP[50];
  char remoteEP[50];

  source.PrintEndpointToString( sourceEP );
  destination.PrintEndpointToString( remoteEP );
  write("acquire a security association from source: %s to destination: %s", sourceEP, remoteEP);

  ipsecPolicyGetParameter(policyHandle, "protocol", protocol);
  ipsecPolicyGetParameter(policyHandle, "mode", mode);

  // create a security associaton in the database
  sa = IPsecAssociationDatabaseGetSpi(source, destination, protocol, mode);

  // set the ah algorithm and key
  ipsecAssociationSetParameter(sa, "ahalgorithm", "sha");
  ipsecAssociationSetParameter(sa, "ahkey", "0123456789ABCDEF");

  // update the security association in the database
  ipsecAssociationDatabaseUpdate(sa);

  // release the association object
  ipsecAssociationRelease(sa);
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
