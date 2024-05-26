---
title: camera support
Date: 2022-08-06 14:15:10+02:00
author: Victor Forsiuk
lede: lede-camera-support.jpg
lede_author: <a href="https://jo.dreggn.org/home/">jo</a>
menu: "footer"
---

This is an auto-generated list of the state of support of different camera models. Cameras that produce DNG files should be supported even if they are not on the list but samples are still appreciated.

If your particular camera is not on the list or is missing some form of support please check for an open bug report and if one doesn't exist create one and attach sample files. For details on the kinds of things that are needed see these two blog posts:

- [What's involved with adding support for new cameras](/2012/10/whats-involved-with-adding-support-for-new-cameras/)
- [Profiling sensor and photon noise](/2012/12/profiling-sensor-and-photon-noise/)

You don't need to go through these steps yourself necessarily but instead attach enough sample files to the bug report so we can do it ourselves.

The following formats are explicitly not supported:

- Apple ProRAW DNGs
- CinemaDNG lossless (Blackmagic, some DJI, etc.) and lossy (Blackmagic)
- DNG 1.7 using JPEG XL (Adobe enhanced, Samsung Expert RAW)
- Fujifilm lossy RAFs
- Nikon high efficiency NEFs
- OM System 14-bit high resolution ORFs
- Sony downsized lossless ARWs ("M" for full-frame, "S" for full-frame & APS-C)

The table has the following fields:

- **Camera:** The name of the camera with at least basic support in darktable
- **WB Presets:** If darktable has white balance presets for the camera so you can choose things like "Daylight" and "Fluorescent" in the temperature module
- **Noise Profile:** If darktable has a noise profile so you can use the profiled denoise module with the camera

NOTE: this table does not list the availability of freely available sample at [raw.pixls.us](https://raw.pixls.us/). Please refer to [this post](https://discuss.pixls.us/t/raw-samples-wanted/5420) for the up-to-date information. There currently are [![count of unique cameras in the archive](https://raw.pixls.us/button-cameras.svg)](https://raw.pixls.us/) unique cameras, [![total count of unique samples](https://raw.pixls.us/button-samples.svg)](https://raw.pixls.us/) unique samples.

### [Please contribute samples!](https://discuss.pixls.us/t/raw-samples-wanted/5420)

The following table is based on the source code on darktable's master branch as of 2024-05-25.

| Maker           | Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| --------------- | ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Canon           | EOS 1000D               | EOS Digital Rebel XS, EOS Kiss Digital F, EOS Kiss F                                          | Yes        | Yes           | RawSpeed |
| Canon           | EOS 100D                | EOS Kiss X7, EOS Rebel SL1                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 10D                 |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | EOS 1100D               | EOS Kiss X50, EOS Rebel T3                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 1200D               | EOS Kiss X70, EOS Rebel T5                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 1300D               | EOS Kiss X80, EOS Rebel T6                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 2000D               | EOS 1500D, EOS Kiss X90, EOS Rebel T7                                                         | No         | Yes           | RawSpeed |
| Canon           | EOS 200D                | EOS Kiss X9, EOS Rebel SL2                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 20D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 250D                | EOS Kiss X10, EOS Rebel SL3, EOS 200D Mark II                                                 | No         | Yes           | LibRaw   |
| Canon           | EOS 300D                | EOS Digital Rebel, EOS Kiss Digital                                                           | Yes        | No            | RawSpeed |
| Canon           | EOS 30D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 350D                | EOS 350D, EOS Digital Rebel XT, EOS Kiss Digital N                                            | Yes        | Yes           | RawSpeed |
| Canon           | EOS 4000D               | EOS 3000D, EOS Rebel T100                                                                     | No         | No            | RawSpeed |
| Canon           | EOS 400D                | EOS Digital Rebel XTi, EOS Kiss Digital X                                                     | Yes        | Yes           | RawSpeed |
| Canon           | EOS 40D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 450D                | EOS Digital Rebel XSi, EOS Kiss Digital X2, EOS Kiss X2                                       | Yes        | Yes           | RawSpeed |
| Canon           | EOS 500D                | EOS Kiss X3, EOS Rebel T1i                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 50D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 550D                | EOS Kiss X4, EOS Rebel T2i                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5D                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5D Mark II          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5D Mark III         |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5D Mark IV          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5DS                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 5DS R               |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 600D                | EOS Kiss X5, EOS Rebel T3i                                                                    | Yes        | Yes           | RawSpeed |
| Canon           | EOS 60D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 650D                | EOS Kiss X6i, EOS Rebel T4i                                                                   | Yes        | Yes           | RawSpeed |
| Canon           | EOS 6D                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 6D Mark II          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 700D                | EOS Kiss X7i, EOS Rebel T5i                                                                   | Yes        | Yes           | RawSpeed |
| Canon           | EOS 70D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 750D                | EOS Kiss X8i, EOS Rebel T6i                                                                   | Yes        | Yes           | RawSpeed |
| Canon           | EOS 760D                | EOS 8000D, EOS Rebel T6s                                                                      | Yes        | Yes           | RawSpeed |
| Canon           | EOS 77D                 | EOS 9000D                                                                                     | Yes        | Yes           | RawSpeed |
| Canon           | EOS 7D                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 7D Mark II          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 800D                | EOS Kiss X9i, EOS REBEL T7i, EOS Rebel T7i                                                    | No         | Yes           | RawSpeed |
| Canon           | EOS 80D                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS 850D                | EOS Kiss X10i, EOS Rebel T8i                                                                  | No         | Yes           | LibRaw   |
| Canon           | EOS 90D                 |                                                                                               | No         | Yes           | LibRaw   |
| Canon           | EOS D2000C              |                                                                                               | No         | No            | RawSpeed |
| Canon           | EOS D30                 |                                                                                               | No         | No            | RawSpeed |
| Canon           | EOS D60                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M10                 |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | EOS M100                |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M2                  |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | EOS M200                |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS M3                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M5                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M50                 | EOS KISS M                                                                                    | Yes        | Yes           | LibRaw   |
| Canon           | EOS M50 Mark II         | EOS KISS M2                                                                                   | No         | Yes           | LibRaw   |
| Canon           | EOS M6                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS M6 Mark II          |                                                                                               | No         | Yes           | LibRaw   |
| Canon           | EOS R                   |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R10                 |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R100                |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS R3                  |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS R5                  |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R50                 |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R6                  |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R6 Mark II          |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R7                  |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS R8                  |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS Ra                  |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS RP                  |                                                                                               | Yes        | Yes           | LibRaw   |
| Canon           | EOS-1D                  |                                                                                               | No         | No            | RawSpeed |
| Canon           | EOS-1D Mark II          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1D Mark II N        |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | EOS-1D Mark III         |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1D Mark IV          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1D X                |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1D X Mark II        |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1D X Mark III       |                                                                                               | No         | No            | LibRaw   |
| Canon           | EOS-1Ds                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1Ds Mark II         |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | EOS-1Ds Mark III        |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | IXY 220F                | IXUS 125 HS, PowerShot ELPH 110 HS                                                            | No         | Yes           | RawSpeed |
| Canon           | PowerShot A3200 IS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot A610          |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot A620          |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot A630          |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot A640          |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot A650          |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot A710 IS       |                                                                                               | Yes        | No            | Unknown  |
| Canon           | PowerShot A720 IS       |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G1            |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot G1 X          |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G1 X Mark II  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G1 X Mark III |                                                                                               | No         | Yes           | RawSpeed |
| Canon           | PowerShot G10           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G11           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G12           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G15           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G16           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G2            |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G3            |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G3 X          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G5            |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G5 X          |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G5 X Mark II  |                                                                                               | No         | Yes           | LibRaw   |
| Canon           | PowerShot G6            |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot G7 X          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G7 X Mark II  |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G7 X Mark III |                                                                                               | No         | No            | LibRaw   |
| Canon           | PowerShot G9            |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot G9 X          |                                                                                               | No         | Yes           | RawSpeed |
| Canon           | PowerShot G9 X Mark II  |                                                                                               | No         | Yes           | RawSpeed |
| Canon           | PowerShot Pro1          |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S100          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot S110          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot S120          |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot S3 IS         |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S30           |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S40           |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot S45           |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S50           |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S60           |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S70           |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot S90           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot S95           |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot SD450         |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX1 IS        |                                                                                               | Yes        | No            | RawSpeed |
| Canon           | PowerShot SX10 IS       |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX100 IS      |                                                                                               | No         | Yes           | RawSpeed |
| Canon           | PowerShot SX110 IS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX130 IS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX160 IS      |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot SX20 IS       |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX220 HS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX230 HS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX240 HS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX260 HS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX30 IS       |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX40 HS       |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX50 HS       |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot SX510 HS      |                                                                                               | No         | Yes           | RawSpeed |
| Canon           | PowerShot SX530 HS      |                                                                                               | No         | No            | RawSpeed |
| Canon           | PowerShot SX60 HS       |                                                                                               | Yes        | Yes           | RawSpeed |
| Canon           | PowerShot SX70 HS       |                                                                                               | No         | No            | LibRaw   |
| Canon           | PowerShot SX710 HS      |                                                                                               | No         | No            | RawSpeed |
| DJI             | FC220                   |                                                                                               | No         | Yes           | Unknown  |
| DJI             | FC3170                  |                                                                                               | No         | Yes           | Unknown  |
| Epson           | R-D1                    |                                                                                               | No         | No            | RawSpeed |
| Epson           | R-D1s                   |                                                                                               | No         | No            | RawSpeed |
| Epson           | R-D1x                   |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix E550            |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix E900            |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix F550EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix F600EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix F700            |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix F770EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix F900EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix HS10 HS11       |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix HS20EXR         |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix HS30EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix HS50EXR         |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | FinePix S1              |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix S100FS          |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S200EXR         |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix S20Pro          |                                                                                               | Yes        | No            | Unknown  |
| Fujifilm        | FinePix S2Pro           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S3Pro           |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix S5000           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S5200           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S5500           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S5600           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S5Pro           |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix S6000fd         |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S6500fd         |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S7000           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S9100           |                                                                                               | Yes        | No            | Unknown  |
| Fujifilm        | FinePix S9500           | FinePix S9000                                                                                 | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix S9600           |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | FinePix SL1000          |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | FinePix X10             |                                                                                               | No         | Yes           | RawSpeed |
| Fujifilm        | FinePix X100            |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | GFX 100                 |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | GFX 50R                 |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | GFX 50S                 |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | GFX100 II               |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | GFX100S                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | GFX50S II               |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-A1                    |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-A10                   |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-A2                    |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | X-A3                    |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-A5                    |                                                                                               | No         | Yes           | RawSpeed |
| Fujifilm        | X-A7                    |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-E1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-E2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-E2S                   |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-E3                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-E4                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-H1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-H2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-H2S                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-M1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-Pro1                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-Pro2                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-Pro3                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-S1                    |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-S10                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-S20                   |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-T1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T10                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T100                  |                                                                                               | No         | Yes           | RawSpeed |
| Fujifilm        | X-T2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T20                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T200                  |                                                                                               | Yes        | No            | RawSpeed |
| Fujifilm        | X-T3                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T30                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T30 II                |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X-T4                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X-T5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X100F                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X100S                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X100T                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X100V                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X100VI                  |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | X20                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | X30                     |                                                                                               | No         | Yes           | RawSpeed |
| Fujifilm        | X70                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Fujifilm        | XF1                     |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | XF10                    |                                                                                               | No         | Yes           | RawSpeed |
| Fujifilm        | XQ1                     |                                                                                               | No         | No            | RawSpeed |
| Fujifilm        | XQ2                     |                                                                                               | No         | No            | RawSpeed |
| GITUP           | GIT2                    |                                                                                               | No         | No            | RawSpeed |
| GITUP           | GIT2P                   |                                                                                               | No         | No            | RawSpeed |
| GoPro           | FUSION                  |                                                                                               | No         | No            | RawSpeed |
| GoPro           | HERO5 Black             |                                                                                               | No         | No            | RawSpeed |
| GoPro           | HERO6 Black             |                                                                                               | No         | No            | RawSpeed |
| GoPro           | HERO7 Black             |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | CF132                   |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | CFV                     |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | CFV-50                  |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | H3D                     |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | H4D-50                  |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | H5D-40                  |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | H5D-50c                 | CFV-50c                                                                                       | No         | No            | RawSpeed |
| Hasselblad      | L1D-20c                 |                                                                                               | No         | Yes           | Unknown  |
| Hasselblad      | X1D                     |                                                                                               | No         | No            | RawSpeed |
| Hasselblad      | X1D II 50C              | CFV II 50C, X1D II 50C                                                                        | No         | No            | RawSpeed |
| Hasselblad      | X2D 100C                | CFV 100C, X2D 100C                                                                            | No         | No            | RawSpeed |
| ImBack          | ImB35mm                 |                                                                                               | No         | No            | RawSpeed |
| Kodak           | DCS Pro 14N             |                                                                                               | Yes        | No            | RawSpeed |
| Kodak           | DCS Pro 14nx            |                                                                                               | No         | No            | RawSpeed |
| Kodak           | DCS Pro SLR/n           |                                                                                               | Yes        | No            | RawSpeed |
| Kodak           | DCS460D                 |                                                                                               | No         | No            | RawSpeed |
| Kodak           | DCS520C                 |                                                                                               | No         | No            | RawSpeed |
| Kodak           | DCS560C                 |                                                                                               | Yes        | No            | RawSpeed |
| Kodak           | DCS760C                 |                                                                                               | No         | No            | RawSpeed |
| Kodak           | EasyShare Z981          |                                                                                               | No         | No            | RawSpeed |
| Kodak           | EasyShare Z990          |                                                                                               | No         | No            | RawSpeed |
| Kodak           | EOS DCS 1               |                                                                                               | No         | No            | RawSpeed |
| Kodak           | EOS DCS 3               |                                                                                               | No         | No            | RawSpeed |
| Kodak           | P850 ZOOM               |                                                                                               | Yes        | No            | Unknown  |
| Kodak           | P880                    |                                                                                               | No         | No            | RawSpeed |
| Kodak           | ProBack645              |                                                                                               | Yes        | No            | Unknown  |
| Kodak           | Z1015 IS                |                                                                                               | Yes        | No            | RawSpeed |
| Leaf            | Aptus 22                |                                                                                               | No         | No            | RawSpeed |
| Leaf            | Credo 40                |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | C (Typ 112)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | C-Lux                   |                                                                                               | No         | No            | RawSpeed |
| Leica Camera AG | R8 - Digital Back DMR   |                                                                                               | Yes        | No            | Unknown  |
| Leica Camera AG | R9 - Digital Back DMR   |                                                                                               | Yes        | No            | Unknown  |
| Leica           | CL                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | D-LUX (Typ 109)         |                                                                                               | No         | No            | RawSpeed |
| Leica           | D-LUX 3                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | D-LUX 4                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | D-LUX 5                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | D-LUX 6                 |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | D-Lux 7                 |                                                                                               | No         | Yes           | RawSpeed |
| Leica           | Digilux 2               |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | Digilux 3               |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | M (Typ 240)             |                                                                                               | Yes        | Yes           | RawSpeed |
| Leica           | M (Typ 262)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | M Monochrom (Typ 246)   |                                                                                               | No         | No            | RawSpeed |
| Leica           | M-D (Typ 262)           |                                                                                               | No         | No            | RawSpeed |
| Leica           | M10                     |                                                                                               | No         | Yes           | RawSpeed |
| Leica           | M10 Monochrom           |                                                                                               | No         | No            | RawSpeed |
| Leica           | M10-D                   |                                                                                               | No         | No            | RawSpeed |
| Leica           | M10-P                   |                                                                                               | No         | No            | RawSpeed |
| Leica           | M10-R                   |                                                                                               | No         | No            | RawSpeed |
| Leica           | M11                     |                                                                                               | No         | No            | RawSpeed |
| Leica           | M11 Monochrom           |                                                                                               | No         | No            | RawSpeed |
| Leica           | M11-P                   |                                                                                               | No         | No            | RawSpeed |
| Leica           | M8                      |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | M9                      |                                                                                               | Yes        | No            | RawSpeed |
| Leica           | Q (Typ 116)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | Q2                      |                                                                                               | Yes        | Yes           | RawSpeed |
| Leica           | Q2 Monochrom            |                                                                                               | No         | No            | RawSpeed |
| Leica           | Q3                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | S (Typ 007)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | S2                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | S3                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | SL (Typ 601)            |                                                                                               | No         | Yes           | RawSpeed |
| Leica           | SL2                     |                                                                                               | No         | No            | RawSpeed |
| Leica           | SL2-S                   |                                                                                               | No         | No            | RawSpeed |
| Leica           | SL3                     |                                                                                               | No         | No            | RawSpeed |
| Leica           | T (Typ 701)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | TL                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | TL2                     |                                                                                               | No         | No            | RawSpeed |
| Leica           | V-LUX (Typ 114)         |                                                                                               | No         | No            | RawSpeed |
| Leica           | V-LUX 1                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | V-Lux 4                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | V-Lux 5                 |                                                                                               | No         | No            | RawSpeed |
| Leica           | X (Typ 113)             |                                                                                               | No         | No            | RawSpeed |
| Leica           | X Vario (Typ 107)       |                                                                                               | No         | No            | RawSpeed |
| Leica           | X-U (Typ 113)           |                                                                                               | No         | No            | RawSpeed |
| Leica           | X1                      |                                                                                               | No         | No            | RawSpeed |
| Leica           | X2                      |                                                                                               | No         | Yes           | RawSpeed |
| LG              | D855                    |                                                                                               | No         | No            | RawSpeed |
| LG              | H815                    |                                                                                               | No         | No            | RawSpeed |
| LG              | Nexus 5X                |                                                                                               | No         | No            | RawSpeed |
| LG              | US996                   |                                                                                               | No         | No            | RawSpeed |
| LG              | VS995                   |                                                                                               | No         | No            | RawSpeed |
| LGE             | Nexus 5                 |                                                                                               | No         | Yes           | Unknown  |
| LGE             | Nexus 5X                |                                                                                               | No         | Yes           | Unknown  |
| Mamiya          | ZD                      |                                                                                               | No         | No            | RawSpeed |
| Minolta         | DiMAGE 5                |                                                                                               | Yes        | No            | Unknown  |
| Minolta         | DiMAGE 7                |                                                                                               | Yes        | No            | RawSpeed |
| Minolta         | DiMAGE 7Hi              |                                                                                               | Yes        | No            | RawSpeed |
| Minolta         | DiMAGE 7i               |                                                                                               | Yes        | No            | RawSpeed |
| Minolta         | DiMAGE A1               |                                                                                               | Yes        | No            | RawSpeed |
| Minolta         | DiMAGE A2               |                                                                                               | Yes        | No            | RawSpeed |
| Minolta         | DiMAGE A200             |                                                                                               | No         | No            | RawSpeed |
| Minolta         | DiMAGE G500             |                                                                                               | Yes        | No            | Unknown  |
| Minolta         | DiMAGE Z2               |                                                                                               | Yes        | No            | Unknown  |
| Minolta         | Dynax 5D                | Alpha 5D, Maxxum 5D                                                                           | Yes        | Yes           | RawSpeed |
| Minolta         | Dynax 7D                | Alpha 7D, Maxxum 7D                                                                           | Yes        | No            | RawSpeed |
| Nikon           | 1 AW1                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 J1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 J2                    |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | 1 J3                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 J4                    |                                                                                               | No         | No            | RawSpeed |
| Nikon           | 1 J5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 S1                    |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | 1 S2                    |                                                                                               | No         | No            | RawSpeed |
| Nikon           | 1 V1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 V2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | 1 V3                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Coolpix A               |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Coolpix A1000           |                                                                                               | No         | No            | RawSpeed |
| Nikon           | COOLPIX B700            |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | COOLPIX P1000           |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Coolpix P330            |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Coolpix P340            |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | Coolpix P6000           |                                                                                               | No         | No            | RawSpeed |
| Nikon           | Coolpix P7000           |                                                                                               | No         | No            | RawSpeed |
| Nikon           | Coolpix P7100           |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Coolpix P7700           |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | Coolpix P7800           |                                                                                               | No         | No            | RawSpeed |
| Nikon           | COOLPIX P950            |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | D1                      |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D100                    |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D1H                     |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D1X                     |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D200                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D2H                     |                                                                                               | No         | No            | RawSpeed |
| Nikon           | D2Hs                    |                                                                                               | No         | No            | RawSpeed |
| Nikon           | D2X                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D2Xs                    |                                                                                               | No         | No            | RawSpeed |
| Nikon           | D3                      |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D300                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3000                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D300S                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3100                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3200                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3300                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3400                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D3500                   |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | D3S                     |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D3X                     |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D4                      |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D40                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D40X                    |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D4S                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5                      |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | D50                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D500                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5000                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5100                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5200                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5300                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5500                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D5600                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D6                      |                                                                                               | No         | No            | RawSpeed |
| Nikon           | D60                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D600                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D610                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D70                     |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D700                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D7000                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D70s                    |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | D7100                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D7200                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D750                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D7500                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D780                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D80                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D800                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D800E                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D810                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D850                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | D90                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Df                      |                                                                                               | No         | No            | RawSpeed |
| Nikon           | E5400                   |                                                                                               | Yes        | No            | RawSpeed |
| Nikon           | E5700                   |                                                                                               | No         | No            | RawSpeed |
| Nikon           | E8700                   |                                                                                               | Yes        | No            | Unknown  |
| Nikon           | LS-5000                 |                                                                                               | No         | No            | RawSpeed |
| Nikon           | Z 30                    |                                                                                               | No         | No            | RawSpeed |
| Nikon           | Z 5                     |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | Z 50                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z 6                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z 6_2                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z 7                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z 7_2                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z 8                     |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | Z 9                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Nikon           | Z f                     |                                                                                               | No         | Yes           | RawSpeed |
| Nikon           | Z fc                    |                                                                                               | No         | No            | RawSpeed |
| Nokia           | Lumia 1020              |                                                                                               | No         | No            | RawSpeed |
| Olympus         | C5050Z                  |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | C5060WZ                 |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | C7070WZ                 |                                                                                               | No         | No            | RawSpeed |
| Olympus         | C8080WZ                 |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-1                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-10                    |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-20                    |                                                                                               | No         | No            | RawSpeed |
| Olympus         | E-3                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-30                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-300                   |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-330                   |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-400                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-410                   |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-420                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-450                   |                                                                                               | No         | No            | RawSpeed |
| Olympus         | E-5                     |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-500                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-510                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-520                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-600                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-620                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M10                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M10 Mark II           |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M10 Mark III          | E-M10 Mark IIIs                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M10 Mark IV           |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M1MarkII              |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M1MarkIII             |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M1X                   |                                                                                               | No         | No            | RawSpeed |
| Olympus         | E-M5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M5 Mark II            |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-M5 Mark III           |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-P1                    |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | E-P2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-P3                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-P5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-P7                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL1                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL10                  |                                                                                               | No         | No            | RawSpeed |
| Olympus         | E-PL2                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL3                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL5                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL6                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL7                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL8                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PL9                   |                                                                                               | No         | Yes           | RawSpeed |
| Olympus         | E-PM1                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | E-PM2                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | PEN-F                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | SH-2                    |                                                                                               | No         | No            | RawSpeed |
| Olympus         | SP350                   |                                                                                               | No         | No            | RawSpeed |
| Olympus         | SP500UZ                 |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | SP510UZ                 |                                                                                               | Yes        | No            | Unknown  |
| Olympus         | SP570UZ                 |                                                                                               | No         | No            | RawSpeed |
| Olympus         | Stylus1                 | Stylus1                                                                                       | No         | No            | RawSpeed |
| Olympus         | TG-4                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | TG-5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | TG-6                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | XZ-1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Olympus         | XZ-10                   |                                                                                               | Yes        | No            | RawSpeed |
| Olympus         | XZ-2                    |                                                                                               | No         | Yes           | RawSpeed |
| OM System       | OM-1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| OM System       | OM-1 Mark II            |                                                                                               | Yes        | Yes           | RawSpeed |
| OM System       | OM-5                    |                                                                                               | Yes        | Yes           | RawSpeed |
| OM System       | TG-7                    |                                                                                               | No         | No            | RawSpeed |
| OnePlus         | One                     |                                                                                               | No         | No            | RawSpeed |
| OnePlus         | ONEPLUS A6003           |                                                                                               | No         | Yes           | Unknown  |
| OnePlus         | OnePlus Nord 3 5G       |                                                                                               | No         | Yes           | Unknown  |
| Panasonic       | DC-FZ10002              |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-FZ82                 | DC-FZ80, DMC-FZ80, DMC-FZ85                                                                   | No         | No            | RawSpeed |
| Panasonic       | DC-G100                 | DC-G110                                                                                       | No         | No            | RawSpeed |
| Panasonic       | DC-G9                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-G95                  | DC-G90, DC-G91, DC-G95D, DC-G99, DC-G99D                                                      | No         | Yes           | RawSpeed |
| Panasonic       | DC-G9M2                 |                                                                                               | Yes        | No            | Unknown  |
| Panasonic       | DC-GF9                  | DC-GX800, DC-GX850                                                                            | No         | Yes           | RawSpeed |
| Panasonic       | DC-GH5                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-GH5M2                |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DC-GH5S                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DC-GX880                | DC-GF10, GF90                                                                                 | No         | No            | RawSpeed |
| Panasonic       | DC-GX9                  | DC-GX7MK3                                                                                     | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-LX100M2              |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-S1                   |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DC-S1H                  |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DC-S1R                  |                                                                                               | No         | Yes           | RawSpeed |
| Panasonic       | DC-S5                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DC-TZ202                | DC-TZ200, DC-TZ200D, DC-TZ202D, DC-TZ220, DC-TZ220D, DC-ZS200, DC-ZS200D, DC-ZS220, DC-ZS220D | No         | No            | RawSpeed |
| Panasonic       | DC-TZ90                 | DC-FZ91, DC-FZ92, DC-FZ93, DC-TZ91, DC-ZS70                                                   | No         | Yes           | RawSpeed |
| Panasonic       | DC-TZ96                 | DC-TZ95, DC-TZ95D, DC-ZS80                                                                    | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-CM1                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-FX150               |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ100               |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ1000              |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-FZ150               |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ18                |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-FZ200               |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-FZ2000              | DMC-FZ2500                                                                                    | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ28                |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-FZ30                |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-FZ300               |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-FZ330               |                                                                                               | No         | Yes           | RawSpeed |
| Panasonic       | DMC-FZ35                | DMC-FZ38                                                                                      | No         | Yes           | RawSpeed |
| Panasonic       | DMC-FZ45                | DMC-FZ40                                                                                      | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ50                |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-FZ70                | DMC-FZ72                                                                                      | No         | No            | RawSpeed |
| Panasonic       | DMC-FZ8                 |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-G1                  |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-G10                 |                                                                                               | No         | Yes           | RawSpeed |
| Panasonic       | DMC-G2                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-G3                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-G5                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-G6                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-G7                  | DMC-G70                                                                                       | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-G8                  | DMC-G80, DMC-G81, DMC-G85                                                                     | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GF1                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GF2                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-GF3                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GF5                 |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-GF6                 |                                                                                               | No         | Yes           | RawSpeed |
| Panasonic       | DMC-GF7                 |                                                                                               | No         | Yes           | RawSpeed |
| Panasonic       | DMC-GF8                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-GH1                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-GH2                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GH3                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GH4                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GM1                 | DMC-GM1S                                                                                      | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GM5                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GX1                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GX7                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GX8                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-GX85                | DMC-GX7MK2, DMC-GX80                                                                          | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-L1                  |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-L10                 |                                                                                               | No         | No            | RawSpeed |
| Panasonic       | DMC-LF1                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-LX1                 |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-LX100               |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-LX15                | DMC-LX10, DMC-LX9                                                                             | No         | Yes           | RawSpeed |
| Panasonic       | DMC-LX2                 |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-LX3                 |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-LX5                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-LX7                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-TZ100               | DMC-TX1, DMC-TZ101, DMC-TZ110, DMC-ZS100, DMC-ZS110                                           | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-TZ60                |                                                                                               | Yes        | No            | RawSpeed |
| Panasonic       | DMC-TZ61                | DMC-ZS40                                                                                      | No         | No            | RawSpeed |
| Panasonic       | DMC-TZ71                | DMC-TZ70, DMC-ZS50                                                                            | Yes        | Yes           | RawSpeed |
| Panasonic       | DMC-TZ81                | DMC-TZ80, DMC-TZ85, DMC-ZS60                                                                  | No         | No            | RawSpeed |
| Paralenz        | Dive Camera             |                                                                                               | No         | No            | RawSpeed |
| Pentax          | *ist D                  |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | *ist DL                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | *ist DL2                |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | *ist DS                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | 645D                    |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | 645Z                    |                                                                                               | No         | No            | RawSpeed |
| Pentax          | Caplio GX100            |                                                                                               | Yes        | No            | Unknown  |
| Pentax          | K-01                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-1                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-1 Mark II             |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-3                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-3 II                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-3 Mark III            |                                                                                               | No         | Yes           | RawSpeed |
| Pentax          | K-3 Mark III Monochrome |                                                                                               | No         | No            | RawSpeed |
| Pentax          | K-30                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-5                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-5 II                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-5 II s                |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-50                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-500                   |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | K-7                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-70                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-m                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-r                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-S1                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-S2                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K-x                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K100D                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K100D Super             |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K10D                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K110D                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K2000                   |                                                                                               | No         | No            | RawSpeed |
| Pentax          | K200D                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | K20D                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Pentax          | KF                      |                                                                                               | No         | No            | RawSpeed |
| Pentax          | KP                      |                                                                                               | No         | Yes           | RawSpeed |
| Pentax          | MX-1                    |                                                                                               | No         | No            | RawSpeed |
| Pentax          | Q                       |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | Q-S1                    |                                                                                               | No         | No            | RawSpeed |
| Pentax          | Q10                     |                                                                                               | Yes        | No            | RawSpeed |
| Pentax          | Q7                      |                                                                                               | Yes        | No            | RawSpeed |
| Phase One       | IQ140                   |                                                                                               | No         | No            | RawSpeed |
| Phase One       | IQ180                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Phase One       | P25+                    |                                                                                               | No         | No            | RawSpeed |
| Phase One       | P30                     |                                                                                               | No         | No            | RawSpeed |
| Phase One       | P45                     |                                                                                               | No         | No            | RawSpeed |
| Phase One       | P65+                    |                                                                                               | No         | No            | RawSpeed |
| Raspberrypi     | RP_imx477               |                                                                                               | No         | Yes           | Unknown  |
| Ricoh           | GR                      |                                                                                               | Yes        | Yes           | RawSpeed |
| Ricoh           | GR II                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Ricoh           | GR III                  | GR III HDF                                                                                    | Yes        | Yes           | RawSpeed |
| Ricoh           | GR IIIx                 | GR IIIx HDF                                                                                   | Yes        | Yes           | RawSpeed |
| Samsung         | EK-GN120                |                                                                                               | No         | No            | RawSpeed |
| Samsung         | EX1                     |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | EX2F                    |                                                                                               | No         | No            | RawSpeed |
| Samsung         | G920F                   |                                                                                               | No         | No            | RawSpeed |
| Samsung         | G935F                   |                                                                                               | No         | No            | RawSpeed |
| Samsung         | GX-1S                   |                                                                                               | Yes        | No            | Unknown  |
| Samsung         | GX10                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | GX20                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | NX mini                 |                                                                                               | No         | No            | RawSpeed |
| Samsung         | NX1                     |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | NX10                    |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | NX100                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | NX1000                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Samsung         | NX11                    |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX1100                  |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX20                    |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX200                   |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX2000                  |                                                                                               | No         | No            | RawSpeed |
| Samsung         | NX210                   |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX30                    |                                                                                               | No         | No            | RawSpeed |
| Samsung         | NX300                   | NX300M                                                                                        | Yes        | No            | RawSpeed |
| Samsung         | NX3000                  |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX3300                  |                                                                                               | No         | No            | RawSpeed |
| Samsung         | NX5                     |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | NX500                   |                                                                                               | Yes        | No            | RawSpeed |
| Samsung         | WB2000                  |                                                                                               | No         | Yes           | RawSpeed |
| Sigma           | fp                      |                                                                                               | No         | No            | RawSpeed |
| Sigma           | fp L                    |                                                                                               | No         | No            | RawSpeed |
| Sigma           | sd Quattro              |                                                                                               | No         | No            | RawSpeed |
| Sigma           | sd Quattro H            |                                                                                               | No         | No            | RawSpeed |
| Sinar           | eVolution 75            |                                                                                               | No         | No            | RawSpeed |
| Sjcam           | SJ6 LEGEND              |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSC-F828                |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSC-HX99                | DSC-HX95                                                                                      | No         | No            | RawSpeed |
| Sony            | DSC-R1                  |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSC-RX0                 |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSC-RX0M2               |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSC-RX1                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX10                |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M2             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M3             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M4             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M5             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M5A            |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M6             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX100M7             |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX10M2              |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX10M3              |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX10M4              |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSC-RX1R                |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSC-RX1RM2              |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A100               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A200               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A230               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A290               |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSLR-A300               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A330               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A350               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A380               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A390               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A450               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A500               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | DSLR-A550               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A560               |                                                                                               | No         | No            | RawSpeed |
| Sony            | DSLR-A580               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A700               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A850               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | DSLR-A900               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCA-68                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCA-77M2               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCA-99M2               |                                                                                               | No         | No            | RawSpeed |
| Sony            | ILCE-1                  |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-3000               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | ILCE-3500               |                                                                                               | No         | No            | RawSpeed |
| Sony            | ILCE-5000               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-5100               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6000               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6100               |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-6300               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6400               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6500               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6600               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-6700               |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-7                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7C                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7CM2               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7CR                |                                                                                               | No         | No            | RawSpeed |
| Sony            | ILCE-7M2                |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7M3                |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7M4                |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7R                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7RM2               |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7RM3               | ILCE-7RM3A                                                                                    | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7RM4               | ILCE-7RM4A                                                                                    | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7RM5               |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-7S                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | ILCE-7SM2               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | ILCE-7SM3               |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-9                  |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-9M2                |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-9M3                |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ILCE-QX1                |                                                                                               | No         | No            | RawSpeed |
| Sony            | ILME-FX3                |                                                                                               | No         | No            | RawSpeed |
| Sony            | ILME-FX30               |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | NEX-3                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-3N                  |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | NEX-5                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-5N                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-5R                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-5T                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-6                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-7                   |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-C3                  |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | NEX-F3                  |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | SLT-A33                 |                                                                                               | Yes        | No            | RawSpeed |
| Sony            | SLT-A35                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A37                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A55                 | SLT-A55                                                                                       | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A57                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A58                 |                                                                                               | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A65                 | SLT-A65                                                                                       | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A77                 | SLT-A77                                                                                       | Yes        | Yes           | RawSpeed |
| Sony            | SLT-A99                 | SLT-A99                                                                                       | Yes        | Yes           | RawSpeed |
| Sony            | ZV-1                    |                                                                                               | No         | Yes           | RawSpeed |
| Sony            | ZV-E1                   |                                                                                               | No         | No            | RawSpeed |
| Sony            | ZV-E10                  |                                                                                               | No         | Yes           | RawSpeed |
| YI TECHNOLOGY   | M1                      |                                                                                               | No         | Yes           | Unknown  |
