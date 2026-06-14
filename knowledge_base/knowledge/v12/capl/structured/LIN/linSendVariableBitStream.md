# linSendVariableBitStream

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSendVariableBitStream(byte dataBuffer[], int64 lengthInNS[], dword numberOfBits, dword roundUp)
```

## Description

Sends an arbitrary bit stream with bits of variable length on the LIN bus.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
// This function sends a disturbance of 1 second, followed by a pause of 1 second,
// followed by a disturbance of 7 seconds using the variable bit stream functionality
void SendDisturbances()
{
byte data[1] = { 2 };
int64 lengthInNS[3] = { 1000000000LL, 1000000000LL, 7000000000LL };
linSendVariableBitStream(data, lengthInNS, 3, 1, 1);  byte data[25];
}
```

## Availability

| Since Version |
|---|
