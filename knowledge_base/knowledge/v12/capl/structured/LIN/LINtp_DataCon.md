# LINtp_DataCon

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_DataCon(long count);
```

## Description

This CAPL callback receives the number of data bytes successfully sent.

## Return Values

—

## Example

```c
void LINtp_DataCon(long count)
{
  write( "sent %d byte", count);
}
```

## Availability

| Since Version |
|---|
