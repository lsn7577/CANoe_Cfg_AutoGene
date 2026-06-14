# ipsecAssociationSetParameter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationSetParameter(long association, char[] parameter, char[] value); // form 1
long ipsecAssociationSetParameter(long association, char[] parameter, byte[] value); // form 2
long ipsecAssociationSetParameter(long association, char[] parameter, IP_Endpoint value); // form 3
long ipsecAssociationSetParameter(long association, char[] parameter, dword value); // form 4
```

## Description

Set the value of a parameter in a IPsec security association record. To modify the security association database it is necessary to call ipsecAssociationDatabaseUpdate.

A security association record can be created with ipsecAssociationInit or with ipsecAssociationDatabaseGetSpi.

## Parameters

| Name | Description |
|---|---|
| association | Handle to an association object. |
| source | Source endpoint of the security association. |
| destination | Destination endpoint of the security association. |
| UNSPEC | 0 |
| ESP | 1 |
| AH | 2 |
| ANY | 0 |
| TRANSPORT | 1 |
| TUNNEL | 2 |
| spi | Returns the security parameter index of the security association |
| espalgorithm | Returns the used esp algorithm. Possible values are: NONE AES AES128 AES192 AES256 |
| espkey | Returns the key of the esp algorithm |
| ahalgorithm | Returns the used esp algorithm. Possible values are: NULL SHA2_512 SHA512 AES192GMAC AES128GMAC SHA256 SHA2_256 SHA2_384 SHA384 SHA SHA1 AES256GMAC AESCMAC SHA1_160 NONE |
| ahkey | Returns the key of the esp algorithm |
| windowSize | replay window size in byte |
| 0 | extended sequence number disabled |
| 1 | extended sequence number enabled |
| value | The value to set in the security association record. |

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
