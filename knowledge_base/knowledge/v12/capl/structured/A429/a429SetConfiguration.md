# a429SetConfiguration

> Category: `A429` | Type: `function`

## Syntax

```c
long a429SetConfiguration( long channel, a429settings mySettings );
```

## Description

This function sets the actual channel configuration. Internally the function a429ResetEx is called to apply the changes

## Example

```c
variables
{
  long RxChannel = 5;
  long TxChannel = 1;

  a429Settings ValidSetTx[2] = {
    { Bitrate = 100000, // default high-speed
    RxMinBitrate = 10500,
    RxMaxBitrate = 120000,
    MinGap = 32,
    Parity = a429OddParity,
    Flags = a429FlagsTx
    },
    { Bitrate = 12500, // default low-speed
    RxMinBitrate = 10500,
    RxMaxBitrate = 120000,
    MinGap = 32,
    Parity = a429OddParity,
    Flags = a429FlagsTx
    }
  };

  a429Settings ValidSetRx[2] = {
    { Bitrate      = 100000, // default high-speed
    RxMinBitrate = 97560,
    RxMaxBitrate = 102400,
    MinGap       = 32,
    Parity       = a429OddParity,
    Flags        = a429FlagsRx
    },
    { Bitrate = 12500, // default low-speed
    RxMinBitrate = 12188,
    RxMaxBitrate = 12810,
    MinGap = 32,
    Parity = a429OddParity,
    Flag = a429FlagsRx
    }
  };
}

// set channels to low speed
on key 'l'
{
  if (a429SetConfiguration(TxChannel, ValidSetTx[1])) {
    write("channel '%d' configured: OK", TxChannel);
  }
  else {
    write("channel '%d' not configured: FAILED", TxChannel);
  }
  if (a429SetConfiguration(RxChannel, ValidSetRx[1])) {
    write("channel '%d' configured: OK", RxChannel);
  }
  else {
    write("channel '%d' not configured: FAILED", RxChannel);
  }
}

// set channels to high speed
on key 'h'
{
  if (a429SetConfiguration(TxChannel, ValidSetTx[0])) {
    write("channel '%d' configured: OK", TxChannel);
  }
  else {
    write ("channel '%d' not configured: FAILED", TxChannel);
  }
  if (a429SetConfiguration(RxChannel, ValidSetRx[0])) {
    write("channel '%d' configured: OK", RxChannel);
  }
  else {
    write("channel '%d' not configured: FAILED", RxChannel);
  }
}
```

## Availability

| Since Version |
|---|
