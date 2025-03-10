# AMD Instinct Data Center GPU Documentation

Targeted for system administrators and power users, this site provides comprehensive technical documentation, guides, and best practices for deploying and managing AMD Instinct Data Center GPUs. Content for GPU software development and applications are located at [ROCm documentation](https://rocm.docs.amd.com).

## System deployment and configuration

::::{grid} 1 2 2 2
:margin 2

:::{grid-item-card}
:padding: 2
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/" class="card-header-link">
  <h2 class="card-header">Instinct Driver</h2>
</a>
<p class="paragraph">Configure systems with the amdgpu driver built for Instinct GPUs</p>
:::

:::{grid-item-card}
:padding: 2
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/" class="card-header-link">
  <h2 class="card-header">Cluster Networking</h2>
</a>
<p class="paragraph">Optimize the network for Instinct GPU applications </p>
:::

:::{grid-item-card}
:padding: 2
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/system-acceptance/en/latest/" class="card-header-link">
  <h2 class="card-header">System Acceptance Test Guide</h2>
</a>
<p class="paragraph">Detailed instructions to test the proper functioning and optimal performance of server systems equipped with AMD Instinct MI300X GPU accelerators. </p>
:::

::::  

## Kubernetes

::::{grid} 1 2 2 2
:margin 2

:::{grid-item-card}
:padding: 2
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm/k8s-device-plugin" class="card-header-link">
  <h2 class="card-header">AMD Kubernetes Device Plugin</h2>
</a>
<p class="paragraph">Kubernetes (k8s) device plugin to enable registration of AMD GPU to a container cluster</p>
:::

:::{grid-item-card}
:padding: 1
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/gpu-operator/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD GPU Operator</h2>
</a>
<p class="paragraph">The AMD GPU Operator simplifies the deployment and management of AMD Instinct GPU accelerators within Kubernetes clusters.</p>
:::

::::  

## Telemetry

::::{grid} 1 2 2 2
:margin 2

:::{grid-item-card}
:padding: 2
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://instinct.docs.amd.com/projects/device-metrics-exporter/en/latest/" class="card-header-link">
  <h2 class="card-header">AMD Device Metrics Exporter</h2>
</a>
<p class="paragraph">AMD Device Metrics Exporter enables Prometheus-format metrics collection for AMD GPUs in HPC and AI environments. </p>
:::

::::  

:::{note}
 The organization, layout and structure of this site is
 under active development and may change frequently. Feedback is appreciated via the
 [ROCm discussions forum](https://github.com/ROCm/ROCm/discussions).
:::
