# hipDF

hipDF enables GPU accelerated DataFrames and DataFrame operations. This library, built on top of ROCm™, enables
large scale data processing on AMD Instinct™ GPUs, allowing you to perform many data manipulation operations
at breakneck speeds. Built on the familiar [Apache Arrow](https://arrow.apache.org/) memory format and using
APIs similar to the well known Python [Pandas library](https://pandas.pydata.org/), hipDF allows you to not
only build accelerated data processing workloads, but accelerate your existing Pandas applications with minimal
effort.

By adopting the well-known cuDF API on AMD hardware, hipDF ensures compatibility and ease of use across various
computing environments. This API compatibility enables existing cuDF workloads to be effortlessly transitioned
to run on supported AMD devices, allowing you to use the ROCm platform for your data processing tasks.

hipDF is currently in an Early Access state and is intended as a preview to the production ready release
planned for later this year.

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Docs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/hipDF/" class="card-header-link">
  <h2 class="card-header">Documentation</h2>
</a>
<p class="paragraph"> Installation instructions, how-to guides, and API reference material can all be found on the ROCm Documentation site.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ../images/hipDF.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm-DS/hipDF" class="card-header-link">
  <h2 class="card-header">Github</h2>
</a>
<p class="paragraph"> View the hipDF source code on Github.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Blogs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./ROCmDS-Blogs.html class="card-header-link">
  <h2 class="card-header">Blogs</h2>
</a>
<p class="paragraph"> View blog posts related to ROCm-DS and hipDF.
</p>
:::

::::
