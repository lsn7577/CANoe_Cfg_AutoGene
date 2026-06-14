# linSetHeaderError

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linSetHeaderError(byte syncByte, byte idwithParity, byte StopAfterError)
```

## Description

With this function it is possible to set invalid parameters in a transmitted LIN header. These invalid parameters will be used until changed by another call to linSetHeaderError() for the same identifier (specified by the lower 6 bits of idWithParity). Setting the correct values with this function will of course disable all header errors for the specified id.

This function will not be supported with the CANCard XLe.

If the LIN hardware is not in Master mode calling this function will have no effect.

The invalid header is not reported on the transmitting channel. To get the error notified an additional channel has to be configured and connected to the transmitting channel.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

// Force an error in header of LIN frame with ID=0x33 by setting wrong protected ID

```c
on key 'h'
{
byte linID, protectedID, corParity, errParity, errPID;
// calculate protected ID with wrong parity bits
linID       = 0x33;                      // use frame ID=0x33
protectedID = linGetProtectedID(linID);  // get protected ID
corParity   = (protectedID & 0xC0) >> 6; // extract parity (0xC=0=11000000)
errParity   = (corParity ^ 0x2) & 0x3;   // calculate wrong parity using XOR
errPID      = linID | (errParity << 6);  // calculate PID with wrong parity
linSetHeaderError(0x55, errPID, 0);
}
...
or
...
// Force an error in header of LIN frame with ID=0x33 by setting wrong Synch byte
linSetHeaderError(0x50, linGetProtectedID(0x33), 0);
```

## Availability

| Since Version |
|---|
