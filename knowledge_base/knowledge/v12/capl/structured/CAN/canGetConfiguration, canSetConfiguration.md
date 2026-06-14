# canGetConfiguration, canSetConfiguration

> Category: `CAN` | Type: `function`

## Syntax

```c
long canGetConfiguration(long channel, canSettings settings);
```

## Description

The CAN controller parameters can be set or read.

canSetConfiguration performs an automatic reset of the CAN controller.

## Return Values

1 = success0 = error

## Example

```c
int ret;
int channel = 1;
canSettings settings;
settings.baudrate = 1000000;
settings.tseg1=5;
settings.tseg2=2;
settings.sjw=2;
settings.sam=1;
settings.flags = 0;

write("Set 1 MB");
ret = canSetConfiguration(channel, settings);

ret = canGetConfiguration(channel, settings);
if (ret)
{
   write("Settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",
             settings.baudrate, settings.tseg1, settings.tseg2, settings.sjw, settings.sam, settings.flags);
}
```

## Availability

| Since Version |
|---|
