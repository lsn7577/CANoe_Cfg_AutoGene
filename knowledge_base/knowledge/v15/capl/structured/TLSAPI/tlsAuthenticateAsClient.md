# tlsAuthenticateAsClient

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsAuthenticateAsClient(dword socket, char serverName[]); // from 1
long tlsAuthenticateAsClient(dword socket, char serverName[], char certificate[]); // form 2
```

## Description

Starts the authentication handshake as client. Certificate common names and Pre Shared Key names have to match the entries in the Vector Security Manager. It is possible to copy the values from the Security Profile.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| serverName | Name of the server as specified in the certificate of the server. The server name can be left blank (""). If the server name is left blank, the Server Name Indication (SNI) Extension of the TLS Handshake is not used. In case your TLS communication bases on certificates: If the server name is entered, you have to specify the common name of the server certificate. In case your TLS communication bases on PSKs: the server name must be the name of the Pre Shared Key. |
| certificate | The name of the client certificate. In case your TLS communication bases on certificates: This is only needed for bidirectional authentication, if the server verifies the client certificate (tlsAuthenticateAsServerVerifyClient). In case your TLS communication bases on PSKs: the certificate must be the name of the Pre Shared Key as well. |

## Example

```c
void OnTcpConnect( dword socket, long result)
{
  if (result == 0)
  {
    socket = tlsOpen(socket);
    // choose one of these three options:
    tlsAuthenticateAsClient(socket, "");// certificate based TLS handshake without SNI extension
    // or
    tlsAuthenticateAsClient(socket, "ServerCertificateCommonName"); // certificate based TLS handshake with SNI extension
    // or
    tlsAuthenticateAsClient(socket, " PreSharedKeyName ", “PreSharedKeyName”); // Pre Shared Key based TLS handshake

    if ((tlsGetLastError(socket) != 0) &&
    (tlsGetLastError(socket) != 997))
    {
      // an error occurred
      return;
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | — | 3.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
