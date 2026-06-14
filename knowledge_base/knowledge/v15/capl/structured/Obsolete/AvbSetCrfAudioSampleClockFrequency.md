# AvbSetCrfAudioSampleClockFrequency

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Set property TimestampRate on the media type (retrievable via AvbGetMediaType) and call AvbSetMediaType. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | dword AvbSetCrfAudioSampleClockFrequency(dword talkerHandle, dword clockFrequency); |  |  |  |
| Function | The function sets the audio sample clock frequency of the CRF stream originated by the Talker. Note The nominal frequency of the audio sample clock is the frequency set by this function multiplied by the clock multiplier (see AvbSetCrfAudioSampleClockMultiplier). | Note The nominal frequency of the audio sample clock is the frequency set by this function multiplied by the clock multiplier (see AvbSetCrfAudioSampleClockMultiplier). |  |  |
| Note The nominal frequency of the audio sample clock is the frequency set by this function multiplied by the clock multiplier (see AvbSetCrfAudioSampleClockMultiplier). |  |  |  |  |
| Parameters | talkerHandle The handle of the Talker. |  |  |  |
| clockFrequency The audio sample clock frequency of the CRF stream to set. The supported values see AvbGetCrfAudioSampleClockFrequency. |  |  |  |  |
| Return Values | 0: The function completed successfully. |  |  |  |
| >0: Error code |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP2-9.0 SP5 | Ethernet | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
