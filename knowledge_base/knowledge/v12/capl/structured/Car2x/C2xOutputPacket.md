# C2xOutputPacket

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xOutputPacket( long packet) // form 1
```

## Description

This function sends a WLAN packet. (form 1)

This function sends a WLAN packet with a specific txPower. (form 2)

This method extends the existing OutputPacket function and allows to send a frame with a dedicated Tx-power. It can be used in combination with the existing (old) OutputPacket function, which still uses the default-txPower defined in the Setup-Dialog or by SetSendParameters.

Notes:

## Return Values

0 or error code

## Example

see also example of C2xInitPacket

```c
void SendGNPacket()
{
  long handle;   // handle to c2x message
  long counter = 0, txPower = 25;
  handle = C2xInitPacket("geo_cnh");    // Create a c2x message

  // If nothing went wrong...
  if (handle != 0 && txPower > -20)
  {
    counter++;
    C2xSetTokenInt(handle, "geo_cnh", "reserved", counter);   // Fill the message with the payload
    C2xOutputPacket(handle, txPower);   // transmit packet with decreasing txPower
    txPower--;
  }
}
```

## Availability

| Since Version |
|---|
