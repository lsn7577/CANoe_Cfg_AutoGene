# canFlushTxQueue

> Category: `CAN` | Type: `function`

## Syntax

```c
long canFlushTxQueue(long channel);
```

## Description

Flushes the Tx queue for the defined channel.

## Return Values

0: Interface doesn’t support flush of Tx queue

## Example

```c
on key 'f'
{
  int result;
  //flush Tx queue for CAN channel 1

  result = canFlushTxQueue(1);
  if(result == 1)
    write("Tx queue flushed ");
  else
    write("Tx queue flush failed Result =%d ", result);
}
```

## Availability

| Since Version |
|---|
