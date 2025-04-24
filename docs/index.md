---
html_theme.sidebar_secondary.remove: true   
---
# AMD Instinct Data Center GPU Documentation

The AMD Instinct Documentation site provides comprehensive guides and technical documentation for system administrators and technical users deploying AMD Instinct Data Center GPUs in enterprise environments. This site focuses on large-scale deployment, cluster management, monitoring, and operational best practices for both HPC and AI workloads. For API documentation and core software stack details, please visit the [ROCm documentation](https://rocm.docs.amd.com).

::::::::::{dropdown} Industries/Verticals
:open:

::::::::{tab-set}

:::::::{tab-item} Computer Vision

::::{grid} 2 2 3 4

:::{grid-item-card}
:padding: 1
:img-top: ./images/models.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./vision/ai.html class="card-header-link">
  <h2 class="card-header">Models and applications</h2>
</a>
<p class="paragraph"> Design, develop, train, finetune, and infer your computer vision models on AMD Instinct GPUs.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/decoding.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./vision/decode.html class="card-header-link">
  <h2 class="card-header">Image and video decoding</h2>
</a>
<p class="paragraph"> Decode a wide variety of image and video formats leveraging the speed of AMD Instinct GPUs.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/processing.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./vision/preprocess.html class="card-header-link">
  <h2 class="card-header">Image processing</h2>
</a>
<p class="paragraph"> Eliminate the image preprocessing bottleneck in your computer vision workloads with AMD Instinct GPUs.
</p>
:::

::::

:::::

::::::

:::::::

:::::::{tab-item} Simulation & Modelling Apps
::::::{grid} 2 2 3 4

:::::{grid-item-card}
:padding: 1
:img-top: ./images/AnsysFluent-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps/ansys-fluent.html" class="card-header-link">
  <h2 class="card-header">Ansys Fluent</h2>
</a>
<p class="paragraph"> Ansys Fluent is a computational fluid dynamics (CFD) software that leverages AMD GPU acceleration through ROCm for high-performance simulations. The AMD partnership enables exascale-ready CFD solutions for complex engineering challenges.
</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/AnsysMech-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps\ansys-mechanical.html" class="card-header-link">
  <h2 class="card-header">Ansys Mechanical</h2>
</a>
<p class="paragraph"> Ansys Mechanical 2023R2+ supports MI200
</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/DevitoPRO-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps\devito.html" class="card-header-link">
  <h2 class="card-header">Devito Codes DevitoPRO</h2>
</a>
<p class="paragraph">DevitoPRO 4.8.2+ supports MI200 and MI300X.
</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/Starccm-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps\siemens.html" class="card-header-link">
  <h2 class="card-header">Siemens Simcenter STAR-CCM+</h2>
</a>
<p class="paragraph">Simcenter STAR-CCM+ 2402+ supports MI200.
</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/ECHELON-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps\stone-ridge.html" class="card-header-link">
  <h2 class="card-header">Stone Ridge Technology ECHELON</h2>
</a>
<p class="paragraph">ECHELON 2023.3+ supports MI200.
</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/FCharLES-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="isv-apps\cadence-fidelity.html" class="card-header-link">
  <h2 class="card-header">Cadence Fidelity LES Solver</h2>
</a>
<p class="paragraph">Fidelity LES Solver supports MI200.
</p>
:::::

::::::

:::::::

::::::::::

::::::::::{dropdown} System Administrators
:open:

::::::::{tab-set}

:::::{tab-item} Bare Metal

::::{grid} 2 2 3 4

:::{grid-item-card}
:padding: 1
:img-top: ./images/System-Administrators-Bare-Metal-AMD-GPU-Driver.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/" class="card-header-link">
  <h2 class="card-header">Instinct GPU Driver</h2>
</a>
<p class="paragraph">Install and configure the GPU. Learn about logging including error codes.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/System-Administrators-Bare-Metal-AMD-GPU-Partitioning.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.blogs.amd.com/software-tools-optimization/compute-memory-modes/README.html" class="card-header-link">
  <h2 class="card-header">GPU Partitioning</h2>
</a>
<p class="paragraph">Learn how to split the compute units and memory to partition a GPU.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/System-Administrators-Bare-Metal-AMD-AMD-SMI.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD SMI</h2>
</a>
<p class="paragraph">The AMD System Management Interface (AMD SMI) library offers a unified tool for managing and monitoring GPUs, particularly in high-performance computing environments. It provides a user-space interface that allows applications to control GPU operations, monitor performance, and retrieve information about the system’s drivers and GPUs.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/System-Administrators-Bare-Metal-AMD-Tools.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/" class="card-header-link">
  <h2 class="card-header">ROCmValidationSuite</h2>
</a>
<p class="paragraph">System validation and diagnosis</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/system-acceptance.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/system-acceptance/en/latest/" class="card-header-link">
  <h2 class="card-header">MI300X System Acceptance Tests</h2>
</a>
<p class="paragraph"> Test the correct functioning and optimal performance of server systems equipped with AMD Instinct MI300X GPU accelerators.</p>
:::

::::

:::::

:::::{tab-item} Kubernetes

::::{grid} 2 2 3 4

:::{grid-item-card}
:padding: 1
:img-top: ./images/gpu-operator.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Operator</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/device-plugin.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/k8s-device-plugin/en/latest/" class="card-header-link">
  <h2 class="card-header">Device Plugin</h2>
</a>
<p class="paragraph">Kubernetes (k8s) device plugin to enable registration of AMD GPU to a container cluster</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/device-metrics-exporter.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/device-metrics-exporter/en/latest/" class="card-header-link">
  <h2 class="card-header">Device Metrics Exporter</h2>
</a>
<p class="paragraph">The AMD Device Metrics Exporter enables Prometheus-format metrics collection for AMD GPUs in HPC and AI environments. </p>
:::

::::

:::::

:::::{tab-item} Cluster Management

::::{grid} 2 2 3 4

:::{grid-item-card}
:padding: 1
:img-top: ./images/omnistat.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://amdresearch.github.io/omnistat/" class="card-header-link">
  <h2 class="card-header">Omnistat</h2>
</a>
<p class="paragraph">Profile across the cluster.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/telemetry.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/" class="card-header-link">
  <h2 class="card-header">Cluster Networking</h2>
</a>
<p class="paragraph">Optimize the network for Instinct GPU applications </p>
:::

::::

:::::

:::::{tab-item} Cloud

::::{grid} 2 2 3 4

:::{grid-item-card}
:padding: 1
:img-top: ./images/instinct-azure.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/instinct-azure/latest/" class="card-header-link">
  <h2 class="card-header">Instinct on Azure</h2>
</a>
<p class="paragraph">Get started with AMD Instinct on Azure</p>
:::

::::

:::::

::::::::

::::::::::

::::::::::{dropdown} Common Reference
:open:

::::::{grid} 2 2 3 4

:::::{grid-item-card}
:padding: 1
:img-top: ./images/instinct-microarchitecture.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch.html" class="card-header-link">
  <h2 class="card-header">Instinct Micro-architecture</h2>
</a>
<p class="paragraph">Review hardware aspects of the AMD Instinct™ MI300, MI200 and MI100 series of GPU accelerators.</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/AMD-SMI-API-doc.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html" class="card-header-link">
  <h2 class="card-header">AMD SMI API Doc</h2>
</a>
<p class="paragraph">AMD SMI documentation covering all use cases.</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/hipcpp.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/HIP/en/latest/index.html" class="card-header-link">
  <h2 class="card-header">HIP C++</h2>
</a>
<p class="paragraph">Learn about HIP programming model.</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/virtualization_image.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/openmp.html" class="card-header-link">
  <h2 class="card-header">OpenMP</h2>
</a>
<p class="paragraph">Explore the OpenMP programming model.</p>
:::::

:::::{grid-item-card}
:padding: 1
:img-top: ./images/secure-docs.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://docs.amd.com/v/u/en-US/ug1729-amd-instinct-accelerators" class="card-header-link">
  <h2 class="card-header">Secure content</h2>
</a>
<p class="paragraph"> Additional NDA technical documentation, software, and design collateral for AMD Instinct products
Login Required -  Some content is available only to authorized users. </p>
:::::

::::::

::::::::::
