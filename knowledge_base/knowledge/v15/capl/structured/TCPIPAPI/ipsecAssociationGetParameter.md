# ipsecAssociationGetParameter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long ipsecAssociationGetParameter(long association, char[] parameter, char[] value); // form 1
long ipsecAssociationGetParameter(long association, char[] parameter, byte[] value); // form 2
long ipsecAssociationGetParameter(long association, char[] parameter, IP_Endpoint value); // form 3
long ipsecAssociationGetParameter(long association, char[] parameter, dword value); // form 4
```

## Description

Get the value of a parameter from a IPsec security association record.

A security association record can be created with ipsecAssociationInit or with ipsecAssociationDatabaseGetSpi.

## Parameters

| Name | Description |
|---|---|
| association | Handle to an security association record object. |
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
| value | The returned value of the parameter. |

## Example

```c
on start
{
  long association;

  // create and init a security association record
  association = ipsecAssociationInit(ip_Endpoint(192.168.1.1), ip_Endpoint(192.168.1.10), "ah", "any", 30000);

  // print the parameter of the security association
  PrintSecurityAssociationAddressParameter(association, "source");
  PrintSecurityAssociationAddressParameter(association, "destination");
  PrintSecurityAssociationStringParameter(association, "protocol");
  PrintSecurityAssociationStringParameter(association, "mode");
  PrintSecurityAssociationNumberParameter(association, "spi");
  PrintSecurityAssociationStringParameter(association, "espAlgorithm");
  PrintSecurityAssociationStringParameter(association, "espKey");
  PrintSecurityAssociationStringParameter(association, "ahAlgorithm");
  PrintSecurityAssociationStringParameter(association, "ahKey");
  PrintSecurityAssociationNumberParameter(association, "windowSize");
  PrintSecurityAssociationNumberParameter(association, "esn");

  // release the association object when it isn't needed anymore
  ipsecAssociationRelease(association);
}

void PrintSecurityAssociationStringParameter(long handle, char parameterName[])
{
  char value[100];
  if(ipsecAssociationGetParameter(handle, parameterName, value) >= 0)
  {
    write("%s: %s", parameterName, value);
  }
}

void PrintSecurityAssociationAddressParameter(long handle, char parameterName[])
{
  char value[100];
  ip_Endpoint ep;
  if(ipsecAssociationGetParameter(handle, parameterName, ep) == 0)
  {
    ep.PrintEndpointToString(value);
    write("%s: %s", parameterName, value);
  }
}

void PrintSecurityAssociationNumberParameter(long handle, char parameterName[])
{
  dword value;
  if(ipsecAssociationGetParameter(handle, parameterName, value) == 0)
  {
    write("%s: %u", parameterName, value);
  }
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
