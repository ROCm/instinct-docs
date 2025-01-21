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

Targeted for system administrators and power users, this site provides comprehensive technical documentation, guides, and best practices for deploying and managing AMD Instinct Data Center GPUs. Content for GPU software development and applications are located at [ROCm documentation](https://rocm.docs.amd.com).

## Beta status

This website is in beta status. The information here is accurate to our best efforts. The organization, layout and structure of this site will change rapidly. Feedback is appreciated via the [ROCm discussions forum](https://github.com/ROCm/ROCm/discussions).

## System deployment and configuration

::::::::{tab-set}

:::::::{tab-item} Instinct for AI
AI Stuff

::::::{tab-set}

:::::{tab-item} AI User

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

::::

:::::

:::::{tab-item} AI Developer

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

::::

:::::

::::::

:::::::

:::::::{tab-item} Instinct for HPC
HPC Stuff
:::::::

::::::::
