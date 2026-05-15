# ROCm-Finance: ROCm toolkit for finance

ROCm-Finance pulls the trajectory of tomorrow into today: an open toolkit on the [ROCm](https://rocm.docs.amd.com/) stack that
delivers GPU-native gradient-boosting stacks that the industry already trusts. XGBoost,
LightGBM, and ThunderGBM, tuned for [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html)
accelerators, so training, scoring, and simulation work land closer to real time than the CPU-era
baselines could achieve.

ROCm-Finance collapses the distance between signal and decision. The same workloads that once
queued overnight now run in minutes. Risk, fraud detection, forecasting, and simulation pipelines step
into the high-bandwidth GPU computing ROCm was built to serve. ROCm-Finance provides production-oriented kernels, memory paths, and scaling behavior so your boosting jobs feel like
they arrived from the next generation, even on this week's cluster.

For more information on ROCm-Finance, including comparisons, prerequisites, installation, and deep API
reference, see the [ROCm-Finance documentation](https://rocm.docs.amd.com/projects/rocm-finance/en/latest/index.html).

:::::{grid} 2 2 2 2

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-1.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./xgboost.html class="card-header-link">
  <h2 class="card-header">XGBoost</h2>
</a>
<p class="paragraph"> General-purpose GPU gradient boosting. Start here for high-performance workloads for data-intensive applications.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-2.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./lightgbm.html class="card-header-link">
  <h2 class="card-header">LightGBM</h2>
</a>
<p class="paragraph"> Leaf-wise training. Strong fit when sparsity abounds and dataset size drives the bottleneck.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-3.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./thundergbm.html class="card-header-link">
  <h2 class="card-header">ThunderGBM</h2>
</a>
<p class="paragraph"> GPU-oriented boosting for highly parallel, GPU-intensive training and simulation-style runs on high-dimensional datasets.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-4.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm/ROCm-Finance" class="card-header-link">
  <h2 class="card-header">GitHub</h2>
</a>
<p class="paragraph"> Source for all ROCm-Finance libraries on GitHub.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-5.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm/rocm-finance/tree/release/26.01/examples" class="card-header-link">
  <h2 class="card-header">Examples</h2>
</a>
<p class="paragraph"> Runnable examples on GitHub to explore the code.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/finance-6.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./finance-blogs.html class="card-header-link">
  <h2 class="card-header">ROCm-Finance Blogs</h2>
</a>
<p class="paragraph"> Browse blogs detailing how to accelerate your finance workloads using gradient boosting on AMD Instinct GPUs.
</p>
::::

:::::
