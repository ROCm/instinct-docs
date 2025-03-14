<style>
  .small-sd-card-large.sd-card {}
  #buttonWrapper:hover {
    border-color: hsla(231, 99%, 66%, 1);
    transform: scale(1.05);
    background-color: var(--hover-background-colour);
  }
  h2 {
    margin: 0;
    font-size: 1.5em;
  }
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    box-sizing: border-box;
    width: 100%;
  }
  .date {
    font-size: 13px;
    font-weight: 300;
    line-height: 22.5px;
    text-transform: none;
    margin-bottom: 10px;
  }
  .paragraph {
    font-size: 16px;
    line-height: 24px;
    margin-bottom: 10px;
  }
  .small-sd-card-img-top.sd-card-img-top {
    width: 100%;
    height: 30%;
    object-fit: cover;
  }
  .small-sd-card.sd-card-body {
    width: 100%;
    height: 60%;
  }
  .small-sd-card {
    width: 145px;
    height: 0;
    display: none;
  }
  .bd-content .sd-card .sd-card-footer {
    border-top: none;
  }
</style>

# AMD Instinct Data Center GPU Documentation

The AMD Instinct Documentation site provides comprehensive guides and technical documentation for system administrators and technical users deploying AMD Instinct Data Center GPUs in enterprise environments. This site focuses on large-scale deployment, cluster management, monitoring, and operational best practices for both HPC and AI workloads. For API documentation and core software stack details, please visit the [ROCm documentation](https://rocm.docs.amd.com).

::::::::{tab-set}

:::::::{tab-item} AI

::::::{tab-set}

:::::{tab-item} AI Solutions Architect

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU AI Dev Hub</h2>
</a>
<p class="paragraph">Content for the user that works on running and building models efficiently. They are creating chat bots, using OpenAI APIs to build something, using vLLM to build another model, etc.
.</p>
:::

::::

:::::

:::::{tab-item} AI Core Developer

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Content placeholder</h2>
</a>
<p class="paragraph"> Content for user who works to understand the core libraries and optimize performance via low level coding (e.g. C++). How to guides for expert model builders and tips and tricks.
</p>
:::

::::

:::::

:::::{tab-item} Vision

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
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
:img-top: ./images/generic.jpg
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
:img-top: ./images/generic.jpg
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

:::::::{tab-item} HPC
::::::{tab-set}

:::::{tab-item} HPC Solutions Architect

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Content placeholder</h2>
</a>
<p class="paragraph">Content for the user that works on running and building models efficiently
.</p>
:::

::::

:::::

:::::{tab-item} HPC Core Developer

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Content placeholder</h2>
</a>
<p class="paragraph"> Content for user who works to understand the core libraries and optimize performance via low level coding (e.g. C++)
</p>
:::

::::

:::::

:::::{tab-item} Open Source Applications

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Content placeholder</h2>
</a>
<p class="paragraph"> Showcase our open source HPC partners (Kokkos, Trilinos, HPCToolkit, etc.)
</p>
:::

::::

:::::

:::::{tab-item} ISV Applications

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/AnsysFluent-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.blogs.amd.com/ecosystems-and-partners/ansys-fluent-performance/README.html" class="card-header-link">
  <h2 class="card-header">Ansys Fluent</h2>
</a>
<p class="paragraph"> Ansys Fluent Solver 2024R2+ supports MI200 and MI300.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/AnsysMech-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/amd/InfinityHub-CI/tree/main/ansys-mechanical" class="card-header-link">
  <h2 class="card-header">Ansys Mechanical</h2>
</a>
<p class="paragraph"> Ansys Mechanical 2023R2+ supports MI200
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/DevitoPRO-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://community.amd.com/t5/instinct-accelerators/devito-revolutionizes-high-performance-computing-for-the-oil-and/ba-p/625392" class="card-header-link">
  <h2 class="card-header">Devito Codes DevitoPRO</h2>
</a>
<p class="paragraph">DevitoPRO 4.8.2+ supports MI200 and MI300X.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/Starccm-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.blogs.amd.com/ecosystems-and-partners/Siemens/README.html" class="card-header-link">
  <h2 class="card-header">Siemens Sincenter STAR-CCM+</h2>
</a>
<p class="paragraph">Simcenter STAR-CCM+ 2402+ supports MI200.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/ECHELON-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.blogs.amd.com/ecosystems-and-partners/stone-ridge/README.html" class="card-header-link">
  <h2 class="card-header">Stone Ridge Technology ECHELON</h2>
</a>
<p class="paragraph">ECHELON 2023.3+ supports MI200.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/FCharLES-tile.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://www.cadence.com/en_US/home/resources/technical-briefs/fidelity-les-solver-tb.html" class="card-header-link">
  <h2 class="card-header">Cadence Fidelity LES Solver</h2>
</a>
<p class="paragraph">Fidelity LES Solver supports MI200.
</p>
:::

::::

:::::

::::::
:::::::

:::::::{tab-item} System Administrators

::::::{tab-set}

:::::{tab-item} Bare Metal

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Instinct Virtualization Driver</h2>
</a>
<p class="paragraph">Enable virtualization using SRIOV on Linux with KVM and VMWare.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Partitioning</h2>
</a>
<p class="paragraph">Learn how to split the compute units and memory to partition a GPU.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD SMI</h2>
</a>
<p class="paragraph"></p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Tools placeholder</h2>
</a>
<p class="paragraph">any Tools related to BM SYS admin</p>
:::

::::

:::::

:::::{tab-item} Virtualization

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Passthrough</h2>
</a>
<p class="paragraph">Enable virtualization using PCIe passthrough on Linux with KVM and VMWare.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">SRIOV</h2>
</a>
<p class="paragraph">Enable virtualization using SRIOV on Linux with KVM and VMWare.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Tools</h2>
</a>
<p class="paragraph">Placeholder for tools relevant to virtualization</p>
:::

::::

:::::

:::::{tab-item} Kubernetes

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Operator</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Device Plugin</h2>
</a>
<p class="paragraph">Kubernetes (k8s) device plugin to enable registration of AMD GPU to a container cluster</p>
:::

::::

:::::

:::::{tab-item} Cluster Management

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Telemetry</h2>
</a>
<p class="paragraph">Telemtry tools.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://amdresearch.github.io/omnistat/" class="card-header-link">
  <h2 class="card-header">Omnistat</h2>
</a>
<p class="paragraph">Profile across the cluster.</p>
:::

::::

:::::

:::::::

:::::::{tab-item} Core Reference Material
::::::{tab-set}

:::::{tab-item} GPU Architecture

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">MI300 series</h2>
</a>
<p class="paragraph">Enable virtualization using SRIOV on Linux with KVM and VMWare.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">MI200 Series</h2>
</a>
<p class="paragraph">Learn how to split the compute units and memory to partition a GPU.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">MI100 Series</h2>
</a>
<p class="paragraph"></p>
:::

::::

:::::

:::::{tab-item} System Management APIs

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD SMI API doc </h2>
</a>
<p class="paragraph">AMD SMI documentation covering all use cases.</p>
:::

::::

:::::

:::::::

::::::::
