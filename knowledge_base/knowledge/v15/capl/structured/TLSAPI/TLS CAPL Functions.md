# TLS CAPL Functions

> Category: `TLSAPI` | Type: `notes`

| TLS The TLS API provides functions for encrypting a socket connection (see TCP/IP CAPL Functions). |
|---|

| Functions | Short Description |
|---|---|
| tlsOpen | Opens a TLS socket. |
| tlsClose | Closes a TLS socket. |
| tlsAuthenticateAsClient | Starts the authentication handshake as client. |
| tlsAuthenticateAsServer | Starts the authentication handshake as server. |
| tlsAuthenticateAsServerVerifyClient | Starts the authentication handshake as server and verify the client certificate. |
| tlsGetLastError | Returns the TLS error code of the last operation that failed on a specified TLS socket. |
| tlsGetLastErrorAsString | Retrieves the error message of the last operation that failed on a specified TLS socket. |
| Callbacks | Short Description |
| OnDtlsServerConnect | It is called when a new DTLS client connects to the DTLS server. |
| OnTlsHandshakeComplete | It is called when a TLS socket completes its handshake. |
| OnTlsClose | It is called when the peer closes the tls connection while a receive call is pending. |

| Version 15© Vector Informatik GmbH |
|---|
