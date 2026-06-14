# OnTlsHandshakeComplete

> Category: `TLSAPI` | Type: `function`

## Syntax

```c
void OnTlsHandshakeComplete(dword socket, long result);
```

## Description

If the CAPL program implements this callback it is called when a TLS handshake is completed.

## Return Values

—

## Example

```c
void OnTlsHandshakeComplete(dword socket, int result)
{
  LONG retVal;
  if (result == 0)
  {
    gConnectionSecured = 1;

    //
    // Send first message
    //
    retVal = TcpSend( socket, "The TLS connection is up", 25 );
    
if (retVal != 0)
    {
      // an error occurred
      return;
    }

    //
    // Receive
    //
    TcpReceive( socket, gRecBuffer, elcount(gRecBuffer) );
  }
}
```

## Availability

| Since Version |
|---|
