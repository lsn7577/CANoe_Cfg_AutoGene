# ipsecAssociationDatabaseGetSpi

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationDatabaseGetSpi(IP_Endpoint source, IP_Endpoint destination, char[] protocol, char[] mode);
```

## Description

With this function it is possible to create a security association in the security association database of the current network stack. The stack will assign a free SPI to the security association. After the creation it is possible to modify the security association record with ipsecAssociationSetParameter and the update the security association in the database by calling ipsecAssociationDatabaseUpdate.

## Parameters

| Name | Description |
|---|---|
| source | Source endpoint of the security association. |
| destination | Destination endpoint of the security association. |
| UNSPEC | 0 |
| ESP | 1 |
| AH | 2 |
| ANY | 0 |
| TRANSPORT | 1 |
| TUNNEL | 2 |

## Example

```c
on start
{
  dword socket;
  long association;
  dword addressCount;
  ip_Address adapterAddress[1];
  ip_Endpoint localEndpoint;

  // add a policy
  IpSecPolicyDatabaseAdd(ip_Endpoint(0.0.0.0:0), 0, ip_Endpoint(192.168.1.10:0), 24, "any", "out ipsec ah/transport//require");

  // create a security associaton in the database from the current node to the node 192.168.1.10
  ipGetAdapterAddress(1, adapterAddress, addressCount);
  localEndpoint.Address = adapterAddress[0];
  association = ipsecAssociationDatabaseGetSpi(localEndpoint, ip_Endpoint(192.168.1.10), "ah", "any");

  // set the ah algorithm and key
  ipsecAssociationSetParameter(association, "ahalgorithm", "sha");
  ipsecAssociationSetParameter(association, "ahkey", "0123456789ABCDEF");

  // update the security association in the database
  ipsecAssociationDatabaseUpdate(association);

  // release the association object when it isn't needed anymore
  ipsecAssociationRelease(association);

  // send data which maches the policy
  socket = udpOpen(ip_Endpoint(0.0.0.0:0));
  udpSendTo(socket, ip_Endpoint(192.168.1.10:23), "hello world", 11);
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
