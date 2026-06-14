# OnDtlsServerConnect

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
void OnDtlsServerConnect(dword socket, ip_Endpoint endpoint, long result);
```

## Description

If the CAPL program implements this callback it is called on the DTLS server side when a DTLS client begins its TLS handshake.

When a DTLS client begins its handshake the server calls internally UdpConnect on the listening socket. After the socket is connected to the clients address the callback gets called to inform the user that a new socket for incoming DTLS connections has to be created.

## Parameters

| Name | Description |
|---|---|
| socket | The socket which is now connected to the client. |
| endpoint | The address and port to which this socket is now connected. |
| result | The result of the internal call to UdpConnect. |

## Return Values

—

## Example

```c
variables
{
  char data[1500];
}

on start
{
  dword socket;
  socket = UdpOpen(ip_Endpoint(0.0.0.0:0));
  UdpConnect(socket, ip_Endpoint(192.168.1.2:4433));
  socket = TlsOpen(socket);
  tlsAuthenticateAsClient(socket, "Server1");
}

void OnTlsHandshakeComplete(dword socket, long result)
{
  if(result == 0)
  {
    udpSend(socket, "Request", 7);
    udpReceiveFrom(socket, data, elcount(data));
  }
}

OnUdpReceiveFrom(dword socket, long result, dword address, dword port, char buffer[], dword size)
{
  // handle response
  // ...
  write("%BASE_FILE_NAME%: received: %s", buffer);
  tlsClose(socket, 1);
}
variables
{
  dword listeningSocket;
  char data[1500];
}

on start
{
  DtlsListen(ip_Endpoint(0.0.0.0:4433));
}

// create new socket to listen for next connection
void DtlsListen(ip_Endpoint endpoint)
{
  listeningSocket = UdpOpen(endpoint);
  listeningSocket = tlsOpen(listeningSocket);
  tlsAuthenticateAsServer(listeningSocket, "Server1");
}

void OnDtlsServerConnect(dword socket, ip_Endpoint endpoint, long result)
{
  if(result == 0)
  {
    DtlsListen(ip_Endpoint(0.0.0.0:4433));
  }
}

void OnTlsHandshakeComplete(dword socket, long result)
{
  if(result != 0)
  {
    write("%BASE_FILE_NAME%: Tls Handshake failed on socket %d. Socket gets closed. Result: %d", socket, result);
    udpClose(socket);
  }
  else
  {
    write("%BASE_FILE_NAME%: Tls Handshake complete on socket %d. Result: %d", socket, result);
    udpReceiveFrom(socket, data, elcount(data));
  }
}

OnUdpReceiveFrom(dword socket, long result, ip_Endpoint endpoint, char buffer[], dword size)
{
  write("%BASE_FILE_NAME%: received: %s", buffer);
  strncpy(data, buffer, elcount(data));
  strncat(data, " reflected", elcount(data));
  UdpSend(socket, data, strlen(data)); // reflect data
  tlsClose(socket, 1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
