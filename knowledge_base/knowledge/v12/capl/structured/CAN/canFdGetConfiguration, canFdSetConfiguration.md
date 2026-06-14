# canFdGetConfiguration, canFdSetConfiguration

> Category: `CAN` | Type: `function`

## Syntax

```c
long canFdSetConfiguration(long channel, canSettings abrSettings, canSettings dbrSettings);
```

## Description

The CAN controller parameters for arbitration and data phase can be set or read

canFdSetConfiguration performs an automatic reset of the CAN controller.

## Return Values

1 = success0 = error

## Example

```c
int ret;
int channel = 1;
CANsettings abrSettings;

CANsettings dbrSettings;

abrSettings.baudrate = 1000000;
abrSettings.tseg1=5;
abrSettings.tseg2=2;
abrSettings.sjw=2;
abrSettings.sam=1;
abrSettings.flags = 0;

dbrSettings.baudrate = 4000000;
dbrSettings.tseg1=6;
dbrSettings.tseg2=3;
dbrSettings.sjw=2;
dbrSettings.sam=1;
dbrSettings.flags = 0;

write("Set 1 MB");
ret = canFdSetConfiguration(channel, abrSettings, dbrSettings);

if (ret)
{
write("Arbitration settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",abrSettings.baudrate, abrSettings.tseg1, abrSettings.tseg2, abrSettings.sjw, abrSettings.sam, abrSettings.flags);
write("Data settings: baud= %f, tseg1 = %d, tseg2= %d, sjw = %d, sam = %d, flags = 0x%x",dbrSettings.baudrate, dbrSettings.tseg1, dbrSettings.tseg2, dbrSettings.sjw, dbrSettings.sam, dbrSettings.flags);
}
```

## Availability

| Since Version |
|---|
