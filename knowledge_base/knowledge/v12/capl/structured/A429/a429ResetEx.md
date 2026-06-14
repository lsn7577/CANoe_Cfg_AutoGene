# a429ResetEx

> Category: `A429` | Type: `function`

## Syntax

```c
long a429ResetEx( long channel );
```

## Description

Re-initialize the selected channel with the active channel parameters. The active channel parameters are read with a429GetConfiguration and modified with a429SetConfiguration.

Note, that the channel is reset. The transmit queue and the hardware schedule table is emptied for this channel.

## Example

```c
on key 'r'
{
  if (a429ResetEx(RxChannel)) {
    write("reset channel '%d' OK", RxChannel);
  }
  else {
    write("reset channel '%d' failed", RxChannel);
  }

  if (a429ResetEx(TxChannel)) {
    write("reset channel '%d' OK", TxChannel);
  }
  else {
    write("reset channel '%d' failed", TxChannel);
  }
}
```

## Availability

| Since Version |
|---|
