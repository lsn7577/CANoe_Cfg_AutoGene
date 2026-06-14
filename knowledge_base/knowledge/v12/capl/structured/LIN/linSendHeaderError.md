# linSendHeaderError

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSendHeaderError(byte syncByte, byte idWithParity, byte StopAfterError)
```

## Description

This function sends a header with the current sync break, sync delimiter and interbyte space settings and the specified sync byte and id byte.

If the LIN hardware is not in Master mode calling this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// Force an error in header of LIN frame with ID=0x33 by setting wrong protected ID
on key 'h'
{
   byte linID, protectedID, corParity, errParity, errPID;
   // calculate protected ID with wrong parity bits
   linID = 0x33; // use frame ID=0x33
   protectedID = linGetProtectedID(linID); // get protected ID
   corParity = (protectedID & 0xC0) >> 6; // extract parity (0xC=0=11000000)
   errParity = (corParity ^ 0x2) & 0x3; // calculate wrong parity using XOR
   errPID = linID | (errParity << 6); // calculate PID with wrong parity
   linSendHeaderError(0x55, errPID, 0);
}
...
or
...
// Force an error in header of LIN frame with ID=0x33 by setting wrong Synch byte
linSendHeaderError(0x50, linGetProtectedID(0x33), 0);
```

## Availability

| Since Version |
|---|
