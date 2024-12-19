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
    height: 5vw;
    object-fit: cover;
  }
  .small-sd-card.sd-card-body {
    width: 100%;
    height: 15%;
  }
  .small-sd-card {
    width: 45px;
    height: 0;
    display: none;
  }
  .bd-content .sd-card .sd-card-footer {
    border-top: none;
  }
</style>

# AMD Instinct Data Center GPU Documentation

Welcome to the documentation site for AMD Instinct Data Center GPUs. Targeted for system administrators and power users, this site provides comprehensive technical documentation, guides, and best practices for deploying and managing AMD Instinct Data Center GPUs. Content for GPU software development and applications including AI are located at [ROCm documentation](https://rocm.docs.amd.com).

## Installation and validation

::::{grid} 1 3 3 3
:margin 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Driver</h2>
</a>
<p class="paragraph">Install the Instinct Driver.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Instinct Virtualiazation Driver</h2>
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
  <h2 class="card-header">GPU Operators</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters. This project enables seamless configuration and operation of GPU-accelerated workloads, including machine learning, Generative AI, and other GPU-intensive applications.</p>
:::

::::

## Kubernetes

::::{grid} 1 3 3 3
:margin 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Driver</h2>
</a>
<p class="paragraph">Install the Instinct Driver.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Operators</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters. This project enables seamless configuration and operation of GPU-accelerated workloads, including machine learning, Generative AI, and other GPU-intensive applications.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">GPU Operators</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters. This project enables seamless configuration and operation of GPU-accelerated workloads, including machine learning, Generative AI, and other GPU-intensive applications.</p>
:::

::::  

## Telemetry

::::{grid} 1 3 3 3
:margin 2

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD-SMI</h2>
</a>
<p class="paragraph">The AMD System Management Interface (AMD SMI) library offers a unified tool for managing and monitoring GPUs.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD GPU Validation Suite</h2>
</a>
<p class="paragraph">The ROCm Validation Suite (RVS) is a system validation and diagnostics tool for monitoring, stress testing, detecting, and troubleshooting issues.</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ./images/generic.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://dcgpu.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">Instinct Datacenter Tool</h2>
</a>
<p class="paragraph">The Instinct Data Center tool (IDC) simplifies the administration of, and addresses key infrastructure challenges on Instinct GPUs in cluster and datacenter environments.</p>
:::

::::  
