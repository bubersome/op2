### **FFMPEG 转换视频文件：** 

1. 使用 FFmpeg 的命令行工具，并利用 VideoToolbox（苹果的硬件视频编码库）来加速编码。以下命令将从你的 MKV 文件中转换前一分钟到 MOV 格式，使用 VideoToolbox 的 h264 编码器：

   ```
   ffmpeg -ss 0 -t 60 -i /Volumes/Downloads/Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEBRip.DDP5.1.x264-Kitsune/Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEB-DL.DDP5.1.H.264-Kitsune.mkv -c:v h264_videotoolbox -c:a copy -sn -movflags +faststart output.mov
   ```

   ```
   ffmpeg -i /Volumes/Downloads/Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEBRip.DDP5.1.x264-Kitsune/Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEB-DL.DDP5.1.H.264-Kitsune.mkv -c:v h264_videotoolbox -c:a copy -sn -movflags +faststart output.mov
   ```

   

   解释一下命令的各个部分：

   - `-ss 0`: 开始时间，这里设置为从视频开始处。
   - `-t 60`: 持续时间，这里设置为60秒。
   - `-i`: 后面跟原始文件的路径。
   - `-c:v h264_videotoolbox`: 视频编码器使用 VideoToolbox 的 h264。
   - `-c:a copy`: 音频不转换编码，直接复制。
   - `-sn`: 不包括字幕轨道。
   - `-movflags +faststart`: 使得生成的 MOV 文件更适合网络流式播放。

2. **检查输出文件：** 转换完成后，检查输出文件 `output.mov` 确保转换是否成功且视频质量满意。





### 在Terminal中使用FFmpeg将一个视频文件从MKV格式转换为MOV格式，并使用NVIDIA CUDA进行硬件加速，你可以按照以下步骤进行操作：

1. **确保安装了FFmpeg**：首先需要确保你的系统中安装了支持CUDA的FFmpeg版本。可以通过在终端中输入`ffmpeg -version`来检查是否支持CUDA。

2. **准备文件路径**：由于你提供的路径是基于Windows的共享路径，如果你是在Linux或macOS上操作，可能需要先通过挂载或其它方法访问到这个路径。确保路径正确，并且可以从你的操作系统中访问到。

3. **执行转换命令**：使用以下FFmpeg命令来转换视频，利用CUDA加速：

   ```
   ffmpeg -hwaccel cuda -i "\\mac1T.1t.example.com\Downloads\Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEBRip.DDP5.1.x264-Kitsune\Dungeons.and.Dragons.Honor.Among.Thieves.2023.1080p.AMZN.WEB-DL.DDP5.1.H.264-Kitsune.mkv" -c:v h264_nvenc -preset fast -c:a copy output.mov
   ```

   说明：

   - `-hwaccel cuda`：启用CUDA硬件加速。
   - `-i`：后面跟输入文件的路径。
   - `-c:v h264_nvenc`：指定使用NVIDIA的H264编码器。
   - `-preset fast`：编码预设，`fast`为较快的编码速度，你也可以选择`slow`、`medium`等其他选项来权衡速度和质量。
   - `-c:a copy`：音频不转码，直接复制。
   - `output.mov`：输出文件的名称。

4. **执行命令**：在Terminal中执行上述命令，FFmpeg将开始转码过程，利用CUDA进行加速。





### NVENC编码器调用方式。下面是针对你提供的示例稍作修改的命令：

```
ffmpeg -hwaccel cuda -i "\\mac1T.1t.example.com\Downloads\Dune.Part.Two.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-FLUX.mkv" -c:v h264_nvenc -preset fast -c:a copy output2.mov
```

这里的改动包括：

1. **硬件加速器** (`-hwaccel`): 我将`cuda`改为`nvdec`。`nvdec`是NVIDIA的硬件解码器，用于加速视频解码过程，而`h264_nvenc`则用于编码。这样做可以确保解码和编码都通过NVIDIA硬件加速。
2. **编码器** (`-c:v`): 保持使用`h264_nvenc`，这是NVIDIA的硬件视频编码器。
3. **预设** (`-preset`): 使用`fast`预设，这是一个速度与质量之间的平衡。你可以根据需要选择不同的预设值，如`slow`, `medium`, `fast`, `faster`, `veryfast`, `superfast`, `ultrafast`，其中速度越快，压缩率可能越低，视频质量可能稍有降低。
4. **音频** (`-c:a`): 使用`copy`参数，意味着不对音频进行重新编码，而是直接复制。



### 转换为8位编码

如果你的目标是使用H.264并且可以接受8位视频（这对大多数用途来说已经足够），你可以在转码过程中添加一个滤镜来将视频从10位转换为8位。命令如下：

```
ffmpeg -hwaccel nvdec -i "\\mac1T.1t.example.com\Downloads\Dune.Part.Two.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-FLUX.mkv" -vf "format=pix_fmts=yuv420p" -c:v h264_nvenc -preset fast -c:a copy output2.mov

```

