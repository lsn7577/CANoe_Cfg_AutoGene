# ipsecAssociationDatabaseUpdate

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationDatabaseUpdate(long association);
```

## Description

With this function it is possible to update an existing security association in the security association database of the current network stack. This is necessary after modifying a security association record with ipsecAssociationSetParameter.

## Parameters

| Name | Description |
|---|---|
| association | Handle to an security association record object. |

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
