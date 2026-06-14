# A664InitProxyPort

> Category: `ADFX` | Type: `function`

## Syntax

```c
long a664InitProxyPort (WORD channel, DWORD ipAddr, WORD udpPort, DWORD outMsgId, DWORD inMsgId, WORD destPort, DWORD destIP, DWORD options)
```

## Description

Open a windows socket based server (Winsock Server) on a windows network adapter which is characterized by the IP address <ipAddr> and the UDP port <udpPort>. Additionally, a pair of AFDX messages from a specific channel <channel> is assigned to this socket. Data received from the client is further transferred with the defined Tx message <inMsgId>. Data originating from the Rx message <outMsgId> is transferred to the client. Calling a664CloseProxyPort closes the port.

An external application may be connected to this socket in order to realize protocols like TFTP or SNMP (via messages of SAP type).

Usually an external client connects to this socket and initiates transmission by sending an initial packet. The source IP address and source UDP port of those incoming requests are then used as the destination address parameters for the server’s responses.

However, in some use cases the data transfer is not requested by any client but is triggered from the server side (e.g. with SNMP traps). Therefore the function allows specifying the additional (optional) address parameters <destIP> and <destPort>.

Note: In order to map communication and points unambiguously a socket shall be assigned to a unique pair of channel <channel> and Rx message <outMsgId>.

## Example

```c
on key 'o'	// open ProxyPort
{
  long res = 0;
  WORD port = 10000;	// proxy sockets UDP port
  WORD channel = 1;	// use AFDX1 bus channel
  char buffer[48];		// buffer to retrieve local IP address

  res = GetIPAddress(buffer, elcount(buffer));  // get hosts IP address
  res = a664InitProxyPort(1, IpGetAddressAsNumber(buffer), port,
                NBF_SNMP_GETRESPONSEA.ID, SNMP_SCI.ID, 0, 0, 0);
  if (res == 0)
    writeEx(-3, 1, "ProxyPort available on IPaddr:%s and port:%d for 
            Afdx1", buffer, port);
  else
    writeEx(-3, 1, "Failure on opening ProxyPort for IPaddr:%s and 
            port:%d: #%d", buffer, port, res);
}
on key 'c'  // close ProxyPort
{
  long res;
  res = a664CloseProxyPort(1, NBF_SNMP_GETRESPONSEA.ID);
  writeEx(-3, 1, "a664CloseProxyPort: --> %d", res);
}
```

## Availability

| Since Version |
|---|
