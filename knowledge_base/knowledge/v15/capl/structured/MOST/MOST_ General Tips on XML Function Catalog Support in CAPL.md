# MOST: General Tips on XML Function Catalog Support in CAPL

> Category: `MOST` | Type: `notes`

## Description

Tips for using XML-based CAPL functions for the symbolic description of messages and parameters.

There are two different access formats when using XML function catalogs in CAPL:

mostAmsMessage AudioDiskPlayer.TrackPosition.Status msg;

msg.Track = 3;

mostAmsOutput(1, "AudioDiskPlayer.SourceActivity.StartResult(1,On)", 1);

testWaitForMostAMSMessage("AudioDiskPlayer.TrackPosition.Status(5)", 1, 200);

mostParamSet(msg, "Data.Record[].LastTrack", idx, 10);

Symbolic Identification of Messages | Symbolic Identification of Parameters | Input Assistance | MOST Database Support in CAPL

| Example mostAmsMessage AudioDiskPlayer.TrackPosition.Status msg; msg.Track = 3; |
|---|

| Example mostAmsOutput(1, "AudioDiskPlayer.SourceActivity.StartResult(1,On)", 1); testWaitForMostAMSMessage("AudioDiskPlayer.TrackPosition.Status(5)", 1, 200); mostParamSet(msg, "Data.Record[].LastTrack", idx, 10); |
|---|

| Version 15© Vector Informatik GmbH |
|---|
