# AfdxInitPacket

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxInitPacket( long msgID, char msgName[], long initSignals ); // form 1
```

## Description

Any access to an AFDX message requires a valid handle. This function returns such a handle and enables the user to manipulate or transmit the message in subsequent calls to AFDX CAPL functions. This function allocates internal buffer memory and initializes the corresponding protocol fields. The level of initialization depends on the selected function signature.

Form 1: When an AFDX DBC is used this function may be called for a message in this DBC with either the message ID or the message name. Note that the message attributes from the DBC file are used for initialization too.

Form 2: When the complete addressing information is available this function signature provides a convenient way to create the handle.

Form 3: If you want to create another instance of an existing AFDX message (either previously created with AfdxInitPacket or signaled with the callback <OnAfdxPacket>) this function signature should be used. Addressing information, attributes and payload contents are duplicated for the new handle.

Form 4: This function signature returns a handle to an "empty" message (all fields are set to "0").

Form 5-7: With these function signatures it is possible to create a message based on either a raw byte stream or an initialized structure. The specified initialization data is copied to the target message "as is".

## Example

Form 1

Snippet placed in e.g. on preStart system function

Form 2

```c
variables
{
  // create packet handle
  long gMSG1;
}

// instantiate message MSG1
gMSG1 = AfdxInitPacket( 0, "AFDX_MSG_OUT_1", 0 );
if (gMSG1 == 0)
{
  write( "Creating packet failed, result %d", AfdxGetLastError() );
}
variables
{
  // static configuration for message MSG1
  const dword k_MSG1_SrcIP  = 0x0A0A0401; // source IP address = 10.10.4.1
  const dword k_MSG1_DstIP  = 0xE0E03908; // destination IP address = 224.224.57.8
  const dword k_MSG1_SrcUDP = 35420; // source UDP port
  const dword k_MSG1_DstUDP = 35420; // destination UDP port
  const dword k_VLID1       = 14600; // VL ID
  const dword k_MSG1_MxFrSz = 784; // maximum frame size

  // create packet handle
  long gMSG1;
}
// instantiate packet MSG1
gMSG1 = AfdxInitPacket( k_MSG1_SrcIP, k_MSG1_DstIP, k_MSG1_SrcUDP, k_MSG1_DstUDP, k_VLID1, k_MSG1_MxFrSz );
if (gMSG1 == 0)
{
  write( "Creating packet failed, result %d", AfdxGetLastError() );
}
```

## Availability

| Since Version |
|---|
