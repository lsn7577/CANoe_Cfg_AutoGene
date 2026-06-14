# tlsAuthenticateAsServerVerifyClient

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
long tlsAuthenticateAsServerVerifyClient(dword socket, char certificate[]);
```

## Description

Starts the authentication handshake as server and verify the client certificate. Certificate common names have to match the entries in the Vector Security Manager. It is possible to copy the values from the Security Profile.

## Parameters

| Name | Description |
|---|---|
| socket | The socket handle. |
| certificate | You have to specify the common name of the server certificate. |

## Example

```c
void OnTcpListen( dword socket, long result)
{
  DWORD clientHandle;
  // Accept the connection
  clientHandle = TcpAccept( socket );

  tlsOpen(clientHandle);
  tlsAuthenticateAsServerVerifyClient(clientHandle, "ServerCertificateCommonName"); // certificate based TLS handshake

  if ((tlsGetLastError(clientHandle) != 0) &&
  (tlsGetLastError(clientHandle) != 997))
  {
    // an error occurred
    return;
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
