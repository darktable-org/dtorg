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

## File Formats That Are Not Supported

The following formats are explicitly not supported:

- Apple ProRAW DNGs
- CinemaDNG lossless (Blackmagic, some DJI, etc.) and lossy (Blackmagic)
- DNG 1.7 using JPEG XL (Adobe enhanced, Samsung Expert RAW)
- Fujifilm lossy RAFs
- Nikon high efficiency NEFs
- Phase One other than IIQ L
- Sony downsized lossless ARWs ("M" for full-frame, "S" for full-frame & APS-C)

If you are having problems opening a file and the camera is supported, make sure you are not using one of these formats.

## Supported Cameras

NOTE: this table does not list the availability of freely available sample at [raw.pixls.us](https://raw.pixls.us/). Please refer to [this post](https://discuss.pixls.us/t/raw-samples-wanted/5420) for the up-to-date information. There currently are [![count of unique cameras in the archive](https://raw.pixls.us/button-cameras.svg)](https://raw.pixls.us/) unique cameras, [![total count of unique samples](https://raw.pixls.us/button-samples.svg)](https://raw.pixls.us/) unique samples.

### [Please contribute samples!](https://discuss.pixls.us/t/raw-samples-wanted/5420)

The table has the following fields:

- **Model, Aliases:** The name of the camera with at least basic support in darktable
- **WB Presets:** If darktable has white balance presets for the camera so you can choose things like "Daylight" and "Fluorescent" in the temperature module
- **Noise Profile:** If darktable has a noise profile so you can use the profiled denoise module with the camera

The table is based on the source code from the 5.2.x branch.

### Canon

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| EOS 1000D               | EOS Digital Rebel XS, EOS Kiss Digital F, EOS Kiss F                                          | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 100D                | EOS Kiss X7, EOS Rebel SL1                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 10D                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| EOS 1100D               | EOS Kiss X50, EOS Rebel T3                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 1200D               | EOS Kiss X70, EOS Rebel T5                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 1300D               | EOS Kiss X80, EOS Rebel T6                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 2000D               | EOS 1500D, EOS Kiss X90, EOS Rebel T7                                                         | ❌ No       | ✅ Yes         | RawSpeed |
| EOS 200D                | EOS Kiss X9, EOS Rebel SL2                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 20D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 250D                | EOS 200D Mark II, EOS Kiss X10, EOS Rebel SL3                                                 | ❌ No       | ✅ Yes         | LibRaw   |
| EOS 300D                | EOS Digital Rebel, EOS Kiss Digital                                                           | ✅ Yes      | ❌ No          | RawSpeed |
| EOS 30D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 350D                | EOS 350D, EOS Digital Rebel XT, EOS Kiss Digital N                                            | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 4000D               | EOS 3000D, EOS Rebel T100                                                                     | ❌ No       | ❌ No          | RawSpeed |
| EOS 400D                | EOS Digital Rebel XTi, EOS Kiss Digital X                                                     | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 40D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 450D                | EOS Digital Rebel XSi, EOS Kiss Digital X2, EOS Kiss X2                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 500D                | EOS Kiss X3, EOS Rebel T1i                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 50D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 550D                | EOS Kiss X4, EOS Rebel T2i                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5D                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5D Mark II          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5D Mark III         |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5D Mark IV          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5DS                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 5DS R               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 600D                | EOS Kiss X5, EOS Rebel T3i                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 60D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 650D                | EOS Kiss X6i, EOS Rebel T4i                                                                   | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 6D                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 6D Mark II          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 700D                | EOS Kiss X7i, EOS Rebel T5i                                                                   | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 70D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 750D                | EOS Kiss X8i, EOS Rebel T6i                                                                   | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 760D                | EOS 8000D, EOS Rebel T6s                                                                      | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 77D                 | EOS 9000D                                                                                     | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 7D                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 7D Mark II          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 800D                | EOS Kiss X9i, EOS REBEL T7i, EOS Rebel T7i                                                    | ❌ No       | ✅ Yes         | RawSpeed |
| EOS 80D                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS 850D                | EOS Kiss X10i, EOS Rebel T8i                                                                  | ❌ No       | ✅ Yes         | LibRaw   |
| EOS 90D                 |                                                                                               | ❌ No       | ✅ Yes         | LibRaw   |
| EOS D2000C              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EOS D30                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EOS D60                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M10                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| EOS M100                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M2                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| EOS M200                |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| EOS M3                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M5                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M50                 | EOS Kiss M                                                                                    | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS M50 Mark II         | EOS Kiss M2                                                                                   | ❌ No       | ✅ Yes         | LibRaw   |
| EOS M6                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS M6 Mark II          |                                                                                               | ❌ No       | ✅ Yes         | LibRaw   |
| EOS R                   |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R10                 |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R100                |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| EOS R3                  |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R5                  |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R5 C                |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| EOS R50                 |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R6                  |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R6 Mark II          |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R7                  |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS R8                  |                                                                                               | ❌ No       | ✅ Yes         | LibRaw   |
| EOS RP                  |                                                                                               | ✅ Yes      | ✅ Yes         | LibRaw   |
| EOS Ra                  |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| EOS-1D                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EOS-1D Mark II          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1D Mark II N        |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| EOS-1D Mark III         |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1D Mark IV          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1D X                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1D X Mark II        |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1D X Mark III       |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| EOS-1Ds                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1Ds Mark II         |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| EOS-1Ds Mark III        |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| IXY 220F                | IXUS 125 HS, PowerShot ELPH 110 HS                                                            | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot A3200 IS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot A610          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot A620          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot A630          |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot A640          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot A650          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot A710 IS       |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| PowerShot A720 IS       |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G1            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot G1 X          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G1 X Mark II  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G1 X Mark III |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot G10           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G11           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G12           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G15           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G16           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G2            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G3            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G3 X          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G5            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G5 X          |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G5 X Mark II  |                                                                                               | ❌ No       | ✅ Yes         | LibRaw   |
| PowerShot G6            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot G7 X          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G7 X Mark II  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G7 X Mark III |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| PowerShot G9            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot G9 X          |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot G9 X Mark II  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot Pro1          |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S100          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot S110          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot S120          |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot S3 IS         |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S30           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S40           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot S45           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S50           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S60           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S70           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot S90           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot S95           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot SD450         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX1 IS        |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| PowerShot SX10 IS       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX100 IS      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot SX110 IS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX130 IS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX160 IS      |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot SX20 IS       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX220 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX230 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX240 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX260 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX30 IS       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX40 HS       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX50 HS       |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot SX510 HS      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| PowerShot SX530 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| PowerShot SX60 HS       |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PowerShot SX70 HS       |                                                                                               | ❌ No       | ❌ No          | LibRaw   |
| PowerShot SX710 HS      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### DJI

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| FC220                   |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| FC3170                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### Epson

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| R-D1                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| R-D1s                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| R-D1x                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Fujifilm

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| FinePix E550            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix E900            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix F550EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix F600EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix F700            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix F770EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix F900EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix HS10 HS11       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix HS20EXR         |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix HS30EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix HS50EXR         |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| FinePix S1              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix S100FS          |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S200EXR         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix S2Pro           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S3Pro           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix S5000           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S5200           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S5500           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S5600           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S5Pro           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix S6000fd         |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S6500fd         |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S7000           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S9500           | FinePix S9000                                                                                 | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix S9600           | FinePix S9600fd                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| FinePix SL1000          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| FinePix X10             |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| FinePix X100            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GFX 100                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| GFX 50R                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| GFX 50S                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| GFX100                  |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| GFX100 II               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GFX100S                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GFX100S II              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| GFX50S II               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-A1                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-A10                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-A2                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| X-A3                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-A5                    |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X-A7                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-E1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-E2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-E2S                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-E3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-E4                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-H1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-H2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-H2S                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-M1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-M5                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-Pro1                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-Pro2                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-Pro3                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-S1                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-S10                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-S20                   |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X-T1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T10                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T100                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X-T2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T20                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T200                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| X-T3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T30                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T30 II                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-T4                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X-T50                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X100F                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X100S                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X100T                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X100V                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X100VI                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X20                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| X30                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X70                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| XF1                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| XF10                    |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| XQ1                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| XQ2                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### GITUP

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| GIT2                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| GIT2P                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### GoPro

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| FUSION                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| HERO5 Black             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| HERO6 Black             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| HERO7 Black             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Hasselblad

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| CF132                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| CFV                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| CFV-50                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| H3D                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| H4D-50                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| H5D-40                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| H5D-50c                 | CFV-50c                                                                                       | ❌ No       | ❌ No          | RawSpeed |
| L1D-20c                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| X1D                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X1D II 50C              | CFV II 50C, X1D II 50C                                                                        | ❌ No       | ❌ No          | RawSpeed |
| X2D 100C                | CFV 100C, X2D 100C                                                                            | ❌ No       | ❌ No          | RawSpeed |

### ImBack

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| ImB35mm                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Kodak

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| DCS Pro 14N             |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DCS Pro 14nx            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DCS Pro SLR/n           |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DCS460D                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DCS520C                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DCS560C                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DCS760C                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EOS DCS 1               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EOS DCS 3               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EasyShare Z981          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EasyShare Z990          |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| P850 ZOOM               |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| P880                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| ProBack645              |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| Z1015 IS                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |

### LG

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| D855                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| H815                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Nexus 5X                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| US996                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| VS995                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### LGE

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Nexus 5                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Nexus 5X                |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### Leaf

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Aptus 22                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Credo 40                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |

### Leica Camera AG

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| R8 - Digital Back DMR   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| R9 - Digital Back DMR   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |

### Leica

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| C (Typ 112)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| C-Lux                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| CL                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D-LUX (Typ 109)         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D-LUX 3                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D-LUX 4                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D-LUX 5                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D-LUX 6                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D-Lux 7                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| D-Lux 8                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Digilux 2               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| Digilux 3               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| M (Typ 240)             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| M (Typ 262)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M Monochrom (Typ 246)   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M-D (Typ 262)           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M10                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| M10 Monochrom           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M10-D                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M10-P                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M10-R                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M11                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| M11 Monochrom           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M11-D                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M11-P                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| M8                      |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| M9                      |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| Q (Typ 116)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Q2                      |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Q2 Monochrom            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Q3                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Q3 43                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| S (Typ 007)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| S2                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| S3                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| SL (Typ 601)            |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| SL2                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| SL2-S                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| SL3                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| SL3-S                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| T (Typ 701)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| TL                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| TL2                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| V-LUX (Typ 114)         |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| V-LUX 1                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| V-Lux 4                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| V-Lux 5                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X (Typ 113)             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X Vario (Typ 107)       |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X-U (Typ 113)           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X1                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| X2                      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### Mamiya

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| ZD                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Minolta

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| DiMAGE 5                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE 7                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE 7Hi              |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE 7i               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE A1               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE A2               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DiMAGE A200             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DiMAGE G500             |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| DiMAGE Z2               |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| Dynax 5D                | Alpha 5D, Alpha Sweet Digital, Maxxum 5D                                                      | ✅ Yes      | ✅ Yes         | RawSpeed |
| Dynax 7D                | Alpha 7D, Alpha-7 Digital, Maxxum 7D                                                          | ✅ Yes      | ❌ No          | RawSpeed |

### Nikon

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| 1 AW1                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 J1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 J2                    |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| 1 J3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 J4                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| 1 J5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 S1                    |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| 1 S2                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| 1 V1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 V2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 1 V3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| COOLPIX B700            |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| COOLPIX P1000           | COOLPIX P1100                                                                                 | ✅ Yes      | ✅ Yes         | RawSpeed |
| COOLPIX P950            |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Coolpix A               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Coolpix A1000           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Coolpix P330            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Coolpix P340            |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| Coolpix P6000           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Coolpix P7000           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Coolpix P7100           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Coolpix P7700           |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Coolpix P7800           |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D1                      |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D100                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D1H                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D1X                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D200                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D2H                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D2Hs                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D2X                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D2Xs                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D3                      |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D300                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3000                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D300S                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3100                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3200                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3300                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3400                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D3500                   |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| D3S                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D3X                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D4                      |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D40                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D40X                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D4S                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5                      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| D50                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D500                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5000                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5100                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5200                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5300                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5500                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D5600                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D6                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| D60                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D600                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D610                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D70                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D700                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D7000                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D70s                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| D7100                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D7200                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D750                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D7500                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D780                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D80                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D800                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D800E                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D810                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D850                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| D90                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Df                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E5400                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E5700                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E8700                   |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| LS-5000                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Z 30                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Z 5                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Z 50                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z 6                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z 6_2                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z 7                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z 7_2                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z 8                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Z 9                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| Z f                     |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| Z fc                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Z50_2                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Z5_2                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Z6_3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |

### Nokia

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Lumia 1020              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### OM System

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| OM-1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| OM-1 Mark II            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| OM-3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| OM-5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| TG-7                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Olympus

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| C5050Z                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| C5060WZ                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| C7070WZ                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| C8080WZ                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-1                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-10                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-20                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E-3                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-30                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-300                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-330                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-400                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-410                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-420                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-450                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E-5                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-500                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-510                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-520                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-600                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-620                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M10                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M10 Mark II           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M10 Mark III          | E-M10 Mark IIIs                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M10 Mark IV           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M1MarkII              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M1MarkIII             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M1X                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E-M5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M5 Mark II            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-M5 Mark III           |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-P1                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| E-P2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-P3                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-P5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-P7                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL1                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL10                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| E-PL2                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL3                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL5                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL6                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL7                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL8                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PL9                   |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| E-PM1                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| E-PM2                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| PEN-F                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| SH-2                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| SP350                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| SP500UZ                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| SP510UZ                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| SP570UZ                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Stylus1                 | Stylus1                                                                                       | ❌ No       | ❌ No          | RawSpeed |
| TG-4                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| TG-5                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| TG-6                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| XZ-1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| XZ-10                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| XZ-2                    |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### OnePlus

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| ONEPLUS A6003           |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| One                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| OnePlus Nord 3 5G       |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### Panasonic

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| DC-FZ10002              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-FZ82                 | DC-FZ80, DC-FZ80D, DC-FZ82D, DC-FZ85, DC-FZ85D                                                | ❌ No       | ❌ No          | RawSpeed |
| DC-G100                 | DC-G100D, DC-G110                                                                             | ❌ No       | ❌ No          | RawSpeed |
| DC-G9                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-G95                  | DC-G90, DC-G91, DC-G95D, DC-G97, DC-G99, DC-G99D                                              | ❌ No       | ✅ Yes         | RawSpeed |
| DC-G9M2                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-GF9                  | DC-GX800, DC-GX850                                                                            | ❌ No       | ✅ Yes         | RawSpeed |
| DC-GH5                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-GH5M2                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-GH5S                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-GH6                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-GX880                | DC-GF10, GF90                                                                                 | ❌ No       | ❌ No          | RawSpeed |
| DC-GX9                  | DC-GX7MK3                                                                                     | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-LX100M2              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-S1                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-S1H                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-S1R                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DC-S1RM2                |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DC-S5                   | DC-S5D                                                                                        | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-S5M2                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-S5M2X                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DC-S9                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DC-TZ202                | DC-TZ200, DC-TZ200D, DC-TZ202D, DC-TZ220, DC-TZ220D, DC-ZS200, DC-ZS200D, DC-ZS220, DC-ZS220D | ❌ No       | ❌ No          | RawSpeed |
| DC-TZ90                 | DC-FZ91, DC-FZ92, DC-FZ93, DC-TZ91, DC-ZS70                                                   | ❌ No       | ✅ Yes         | RawSpeed |
| DC-TZ96                 | DC-TZ95, DC-TZ95D, DC-TZ99, DC-ZS80, DC-ZS99                                                  | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-CM1                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-FX150               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ100               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ1000              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-FZ150               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ18                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-FZ200               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-FZ2000              | DMC-FZ2500                                                                                    | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ28                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-FZ30                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-FZ300               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-FZ330               |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-FZ35                | DMC-FZ38                                                                                      | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-FZ45                | DMC-FZ40                                                                                      | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ50                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-FZ70                | DMC-FZ72                                                                                      | ❌ No       | ❌ No          | RawSpeed |
| DMC-FZ8                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-G1                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-G10                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-G2                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-G3                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-G5                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-G6                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-G7                  | DMC-G70                                                                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-G8                  | DMC-G80, DMC-G81, DMC-G85                                                                     | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GF1                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GF2                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-GF3                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GF5                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-GF6                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-GF7                 |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-GF8                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-GH1                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-GH2                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GH3                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GH4                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GM1                 | DMC-GM1S                                                                                      | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GM5                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GX1                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GX7                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GX8                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-GX85                | DMC-GX7MK2, DMC-GX80                                                                          | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-L1                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-L10                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DMC-LF1                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-LX1                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-LX100               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-LX15                | DMC-LX10, DMC-LX9                                                                             | ❌ No       | ✅ Yes         | RawSpeed |
| DMC-LX2                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-LX3                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-LX5                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-LX7                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-TZ100               | DMC-TX1, DMC-TZ101, DMC-TZ110, DMC-ZS100, DMC-ZS110                                           | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-TZ60                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DMC-TZ61                | DMC-ZS40                                                                                      | ❌ No       | ❌ No          | RawSpeed |
| DMC-TZ71                | DMC-TZ70, DMC-ZS50                                                                            | ✅ Yes      | ✅ Yes         | RawSpeed |
| DMC-TZ81                | DMC-TZ80, DMC-TZ85, DMC-ZS60                                                                  | ❌ No       | ❌ No          | RawSpeed |

### Paralenz

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Dive Camera             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Pentax

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| *ist D                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| *ist DL                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| *ist DL2                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| *ist DS                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| 645D                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| 645Z                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Caplio GX100            |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| K-01                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-1                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-1 Mark II             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-3                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-3 II                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-3 Mark III            |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| K-3 Mark III Monochrome |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| K-30                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-5                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-5 II                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-5 II s                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-50                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-500                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| K-7                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-70                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-S1                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-S2                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-m                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-r                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K-x                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K100D                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K100D Super             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K10D                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K110D                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K2000                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| K200D                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| K20D                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| KF                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| KP                      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| MX-1                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Q                       |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| Q-S1                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| Q10                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| Q7                      |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |

### Phase One

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| IQ140                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| IQ150                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| IQ180                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| P20+                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| P25+                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| P30                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| P45                     | P45+                                                                                          | ❌ No       | ❌ No          | RawSpeed |
| P65+                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Raspberrypi

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| RP_imx477               |                                                                                               | ❌ No       | ✅ Yes         | Unknown  |

### Ricoh

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| GR                      |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GR II                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GR III                  | GR III HDF                                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| GR IIIx                 | GR IIIx HDF                                                                                   | ✅ Yes      | ✅ Yes         | RawSpeed |

### Samsung

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| EK-GN120                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| EX1                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| EX2F                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| G920F                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| G935F                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| GX-1S                   |                                                                                               | ✅ Yes      | ❌ No          | Unknown  |
| GX10                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| GX20                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NX mini                 |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| NX1                     |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NX10                    |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NX100                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NX1000                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NX11                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX1100                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX20                    |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX200                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX2000                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| NX210                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX30                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| NX300                   | NX300M                                                                                        | ✅ Yes      | ❌ No          | RawSpeed |
| NX3000                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX3300                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| NX5                     |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NX500                   |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| WB2000                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### Sigma

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| BF                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DP1                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DP1 Merrill             |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| fp                      |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| fp L                    |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| sd Quattro              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| sd Quattro H            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Sinar

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| Hy6                     |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| eVolution 75            |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Sjcam

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| SJ6 LEGEND              |                                                                                               | ❌ No       | ❌ No          | RawSpeed |

### Sony

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| DSC-F828                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DSC-HX99                | DSC-HX95                                                                                      | ❌ No       | ❌ No          | RawSpeed |
| DSC-R1                  |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DSC-RX0                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSC-RX0M2               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DSC-RX1                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX10                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M2             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M3             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M4             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M5             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M5A            |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M6             |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX100M7             | DSC-RX100M7A                                                                                  | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX10M2              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX10M3              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX10M4              |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSC-RX1R                |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSC-RX1RM2              |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A100               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A200               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A230               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A290               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DSLR-A300               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A330               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A350               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A380               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A390               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A450               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A500               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| DSLR-A550               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A560               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| DSLR-A580               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A700               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A850               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| DSLR-A900               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCA-68                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCA-77M2               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCA-99M2               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| ILCE-1                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-1M2                |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-3000               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| ILCE-3500               |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| ILCE-5000               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-5100               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6000               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6100               | ILCE-6100A                                                                                    | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-6300               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6400               | ILCE-6400A                                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6500               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6600               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-6700               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7C                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7CM2               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7CR                |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| ILCE-7M2                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7M3                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7M4                |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7R                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7RM2               |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7RM3               | ILCE-7RM3A                                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7RM4               | ILCE-7RM4A                                                                                    | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7RM5               |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-7S                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| ILCE-7SM2               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| ILCE-7SM3               |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-9                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-9M2                |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-9M3                |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
| ILCE-QX1                | UMC-R10C                                                                                      | ❌ No       | ❌ No          | RawSpeed |
| ILME-FX3                | ILME-FX3A                                                                                     | ❌ No       | ❌ No          | RawSpeed |
| ILME-FX30               |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NEX-3                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-3N                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| NEX-5                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-5N                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-5R                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-5T                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-6                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-7                   |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-C3                  |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| NEX-F3                  |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| SLT-A33                 |                                                                                               | ✅ Yes      | ❌ No          | RawSpeed |
| SLT-A35                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A37                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A55                 | SLT-A55                                                                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A57                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A58                 |                                                                                               | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A65                 | SLT-A65                                                                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A77                 | SLT-A77                                                                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| SLT-A99                 | SLT-A99                                                                                       | ✅ Yes      | ✅ Yes         | RawSpeed |
| ZV-1                    | ZV-1A                                                                                         | ❌ No       | ✅ Yes         | RawSpeed |
| ZV-E1                   |                                                                                               | ❌ No       | ❌ No          | RawSpeed |
| ZV-E10                  |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |

### YI TECHNOLOGY

| Model                   | Aliases                                                                                       | WB Presets | Noise Profile | Decoder  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ---------- | ------------- | -------- |
| M1                      |                                                                                               | ❌ No       | ✅ Yes         | RawSpeed |
