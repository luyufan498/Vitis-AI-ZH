<div align="center">
  <img width="100%" height="100%" src="docs/images/Vitis-AI.png">
</div>

<br />
Xilinx&reg; Vitis&trade; AI 是一套用于在 Xilinx 硬件平台上部署人工智能网络的工具栈。 目前，用于部署 Vitis AI 硬件平台包括 Xilinx 的移动端芯片（例如：ZCU102/104） 和 Alveo 加速计算卡。



Vitis AI 主要由优化后的IP、工具、库、模型以及示例设计组成。 Vitis AI 的主要特点是其高效性和易用性，这有助于释放 Xilinx FPGA 和 ACAP 的AI 加速潜力。 
  
<br />
<br />

<div align="center">
  <img width="45%" height="45%" src="docs/images/Vitis-AI-arch.png">
</div>

<br />
Vitis AI 的关键的组件：

* **AI Model Zoo**  - 一套全面的预优化模型，可随时部署在 Xilinx 设备上。一套可以直接取用的模型，免去自行训练核编译的痛苦过程。
* **AI Optimizer** - 一个可选的模型优化器，可以需要部署在Xilinx设备上的模型进行剪枝，最多可以将模型压缩90%。（注：AI Optimizer 非免费工具，使用此工具需要获得商业许可证，即commercial licenses）。
* **AI Quantizer** - 一个强大的量化器，支持模型量化、校准和微调。由于FPGA上运行AI模型需要使用定点型，因此如果用户想要设计核修改自己的模型，就需要使用这个工具，来量化自己的模型。
* **AI Compiler** - Vitis AI的编译器。将量化模型编译为高效的指令集和数据流。实际的工作把具体的AI模型转化成DPU可以跑的指令流。
* **AI Profiler** - Vitis AI 的分析工具，主要配合Vitis开发平台使用。用于深入分析人工智能网络的效率和利用率。
* **AI Library** - 一个高层次的C++ API库，主要用于具体云端和移动端的AI应用的开发。
* **DPU** - DPU 即 Deep Learning Processor Unit 深度学习处理单元，一个高效的可扩展的软IP。用户可以根据不同的应用的需要来修改和定制这个IP核。

**了解更多:** [Vitis AI 官网介绍](https://www.xilinx.com/products/design-tools/vitis/vitis-ai.html)  

## 关于汉化
- 目前汉化版对应的官方版本：Vitis 1.4 
- 加入汉化组：316587241

## [See What's New](docs//learn/release_notes.md)
- [历史更新信息（英文）](docs//learn/release_notes.md)
- 支持了新的平台, 包括 Versal ACAP platforms VCK190, VCK5000 和 Kria SoM 
- 更好的 Pytorch 和 Tensorflow 模型支持: Pytorch 版本支持范围 1.5-1.7.1, 提升了Tensorflow 2.x models 的量化
- 全新的模型：4D 雷达检测， 图像激光雷达传感器融合、3D 检测和分割、多任务、深度估计、超分辨率汽车、智能医疗和工业视觉应用
- 用于部署具有多个子图的模型的新 Graph Runner API
- DPUCADX8G (DPUv1)deprecated with DPUCADF8H (DPUv3Int8)
- DPUCAHX8H (DPUv3E) and DPUCAHX8L (DPUv3ME) release with xo
- Classification & Detection WAA examples for Versal (VCK190)

## 准备开始

目前有两种方式来安装用于运行Vitis AI的 Docker 容器。
- 直接运行预先搭建好的的容器： [xilinx/vitis-ai](https://hub.docker.com/r/xilinx/vitis-ai/tags)
- 本地根据Docker recipes来新建一个容器：[Docker Recipes](setup/docker)

**注：**
**Docker**，如果是第一次接触Docker可以简单理解为一个轻量化的虚拟化技术，用于隔离宿主机的运行环境。
**Docker Image**，镜像，类似于虚拟机中的镜像，或者一个WIN中的还原点。
**Container**，容器，可以理解为运行中的虚拟机。需要注意容器和镜像是不同的东西，类似于基于一个镜像可以创建很多个虚拟机，一个Image可以创建多个contrainer。
因此从Docker网站上下载的是一个 Viti AI 的镜像，所有的Vitis AI的环境已经安装好了，我们运行这个镜像就会产生一个容器，这个容器相当于一个正在运行的Ubuntu系统，我们只需要进入这个系统的环境就能够使用Vitis AI的各种工具了。使用Docker可以避免繁琐的环境配置过程。关于Docker的严谨解释请参考官网：https://docs.docker.com/get-started/overview/



### 安装
 - [安装Docker](docs/quick-start/install/install_docker/README.md) - 如果没有安装Docker需要先安装Docker

 - [解决Docker需要sudo执行的问题](https://docs.docker.com/install/linux/linux-postinstall/)

 - 确保你有至少 **100GB** 的硬盘空间

 - 克隆Vitis AI的官方Github仓库到本体，来为后续执行做准备。
    ```bash
    git clone --recurse-submodules https://github.com/Xilinx/Vitis-AI  

    cd Vitis-AI
    ```

**注1:** 下面所有的命令只适用于该版本的Vitis AI。 更多历史版本的细节： [Run Docker Container](docs/quick-start/install/install_docker/load_run_docker.md)

**注2:** 中国境内如果因为网络问题导致git没速度，可以使用下载压缩包解压到本地的方式来运行

#### 使用预先配置好的Vitis AI镜像文件

使用以下命令下载Vitis AI的Docker镜像。注意该命令下载的是CPU版本。
```
docker pull xilinx/vitis-ai-cpu:latest  
```

使用以下命令运行这个Docker:
```
./docker_run.sh xilinx/vitis-ai-cpu:latest
```
#### 通过Recipe（开发环境配置清单）来搭建Docker环境

Xilinx一共提供了两个版本的recipe：CPU 版本 和 GPU 版本。如果你有合适的N卡（亮机卡用不了）和CUDA支持可以选择GPU recipe，否则请选择 CPU recipe 方式。

**CPU Docker**

使用下面的命令来创建CPU docker：
```
cd setup/docker
./docker_build_cpu.sh
```
运行CPU docker:
```
./docker_run.sh xilinx/vitis-ai-cpu:latest
```
**GPU Docker**

使用下面的命令来创建GPU docker：
```
cd setup/docker
./docker_build_gpu.sh
```
运行GPU docker:
```
./docker_run.sh xilinx/vitis-ai-gpu:latest
```
**./docker_run.sh** 这个脚本是一个参考脚本，用户可以根据需要自行修改这个脚本来实现自己需要的功能。


### 在Docker中安装补丁和更新

你可以用下面的方法在 Conda 环境中安装 Anaconda packages： 

```
Vitis-AI /workspace > sudo conda install -n vitis-ai-caffe https://www.xilinx.com/bin/public/openDownload?filename=unilog-1.3.2-h7b12538_35.tar.bz2
```
对于下载文件:

```sh
sudo conda install -n vitis-ai-caffe ./<conda_package>.tar.bz2
 ```

**使用Alveo运行Vitis AI时打开X11的图形支持**

如果您使用 Alveo 卡运行 Vitis AI docker 并希望使用 X11 支持图形（例如，VART 中的某些演示应用程序和 Alveo 的 Vitis-AI-Library 需要显示图像或视频），请将以下行添加到*docker_run.sh* 脚本中的 *docker_run_params* 变量定义：

~~~
-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/tmp/.Xauthority \
~~~

并且在Docker启动之后，运行下面命令行：
~~~
cp /tmp/.Xauthority ~/
sudo chown vitis-ai-user:vitis-ai-group ~/.Xauthority
~~~

请注意，在运行此脚本之前，如果您使用基于 Windows 的 ssh 终端连接到远程服务器，请确保您有本地 X11 服务器正在运行，或者如果您使用的时Linux桌面版，你需要在命令窗口运行**xhost +** 命令。 在windows下使用ssh连接到远程服务器时，如果你用的是GUI工具，你需要在工具中启用 *X11转发* 或者类似选项，如果你用的是命令行，你需要加上 *-X* 参数。

 ### 从例程入门Vitis AI
  - [VART](demo/VART/README.md) 
  - [Vitis AI Library](demo/Vitis-AI-Library/README.md)


## 使用Vitis AI编程

Vitis AI 提供了一组统一的高级 C++/Python 编程 API，用于移动端到云端的跨平台的 AI 应用程序，包括用于 Alveo 的 DPU，以及用于 Zynq Ultrascale+ MPSoC 和 Zynq-7000 的 DPU。使用Vitis AI可以轻松地将 AI 应用程序从云端移植到边缘，反之亦然。
[VART Samples](demo/VART)中的10个示例可以帮助您熟悉未定义的编程API。

| ID | Example Name          | Models              | Framework  | Notes                                                                     |
|----|-----------------------|---------------------|------------|---------------------------------------------------------------------------|
| 1  | resnet50              | ResNet50            | Caffe      | Image classification with VART C\+\+ APIs\.                   |
| 2  | resnet50\_pt          | ResNet50            | Pytorch    | Image classification with VART extension C\+\+ APIs\.         |
| 3  | resnet50\_ext         | ResNet50            | Caffe      | Image classification with VART extension C\+\+ APIs\.         |
| 4  | resnet50\_mt\_py      | ResNet50            | TensorFlow | Multi\-threading image classification with VART Python APIs\. |
| 5  | inception\_v1\_mt\_py | Inception\-v1       | TensorFlow | Multi\-threading image classification with VART Python APIs\. |
| 6  | pose\_detection       | SSD, Pose detection | Caffe      | Pose detection with VART C\+\+ APIs\.                         |
| 7  | video\_analysis       | SSD                 | Caffe      | Traffic detection with VART C\+\+ APIs\.                      |
| 8  | adas\_detection       | YOLO\-v3            | Caffe      | ADAS detection with VART C\+\+ APIs\.                         |
| 9  | segmentation          | FPN                 | Caffe      | Semantic segmentation with VART C\+\+ APIs\.                  |
| 10 | squeezenet\_pytorch   | Squeezenet          | Pytorch    | Image classification with VART C\+\+ APIs\.                   |

更多教程, 请参考 [Vitis AI User Guide](https://www.xilinx.com/html_docs/vitis_ai/1_4/index.html)


## 参考资料
- [Vitis AI Overview](https://www.xilinx.com/products/design-tools/vitis/vitis-ai.html)
- [Vitis AI User Guide](https://www.xilinx.com/html_docs/vitis_ai/1_4/index.html)
- [Vitis AI Model Zoo with Performance & Accuracy Data](models/AI-Model-Zoo)
- [Vitis AI 教程](https://github.com/Xilinx/Vitis-Tutorials/tree/master/Machine_Learning)
- [开发者文章](https://developer.xilinx.com/en/get-started/ai.html)
- [安装和运行Vitis AI的系统需求](docs/learn/system_requirements.md)
- [Vitis AI的常见问答](docs/quick-start/faq.md)
- [Vitis AI 论坛](https://forums.xilinx.com/t5/AI-and-Vitis-AI/bd-p/AI)
- [第三方源](docs/reference/Thirdpartysource.md)
- [模型](docs/models.md)
- [Amazon AWS EC2 F1](https://aws.amazon.com/marketplace/pp/B077FM2JNS)
- [Xilinx Virtex UltraScale+ FPGA VCU1525 Acceleration Development Kit](https://www.xilinx.com/products/boards-and-kits/vcu1525-a.html)
- [AWS F1 Application Execution on Xilinx Virtex UltraScale Devices](https://github.com/aws/aws-fpga/blob/master/SDAccel/README.md)
- [Release Notes](docs/release-notes/1.x.md)
- [UG1023](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2017_4/ug1023-sdaccel-user-guide.pdf)
- [ML Suite Overview](docs/ml-suite-overview.md)
- [Webinar on Xilinx FPGA Accelerated Inference](https://event.on24.com/wcc/r/1625401/2D3B69878E21E0A3DA63B4CDB5531C23?partnerref=Mlsuite)
- [ML Suite Lounge](https://www.xilinx.com/products/boards-and-kits/alveo/applications/xilinx-machine-learning-suite.html)
- [Models](https://www.xilinx.com/products/boards-and-kits/alveo/applications/xilinx-machine-learning-suite.html#gettingStartedCloud)
- [whitepaper here](https://www.xilinx.com/support/documentation/white_papers/wp504-accel-dnns.pdf)

