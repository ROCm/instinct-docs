# ROCm-Finance: ROCm toolkit for finance

ROCm-Finance pulls the trajectory of tomorrow into today: an open toolkit on the [ROCm](https://rocm.docs.amd.com/) stack that
delivers the GPU-native gradient boosting stacks the industry already trusts. XGBoost,
LightGBM, and ThunderGBM, tuned for [AMD Instinct](https://www.amd.com/en/products/accelerators/instinct.html)
accelerators so training, scoring, and scenario work land closer to real time than CPU-era
baselines could achieve.

ROCm-Finance collapses the distance between signal and decision. The same workloads that once
queued overnight now run in minutes. Risk, fraud, forecasting, and simulation pipelines step
into the high-bandwidth, multi-GPU computing ROCm was built to serve. ROCm-Finance provides production-oriented kernels, memory paths, and scaling behavior so your boosting jobs feel like
they arrived from the next generation, even on this week's cluster.

For more information on ROCm-Finance, including comparisons, prerequisites, install, and deep API
reference, see the [ROCm-Finance documentation](https://rocm.docs.amd.com/projects/rocm-finance/en/latest/index.html).

:::::{grid} 2 2 2 2

::::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Docs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./xgboost.html class="card-header-link">
  <h2 class="card-header">XGBoost</h2>
</a>
<p class="paragraph"> General-purpose GPU gradient boosting. Start here for many finance tabular workflows.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Docs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./lightgbm.html class="card-header-link">
  <h2 class="card-header">LightGBM</h2>
</a>
<p class="paragraph"> Leaf-wise training. Strong fit when dataset size drives the bottleneck.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Docs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./thundergbm.html class="card-header-link">
  <h2 class="card-header">ThunderGBM</h2>
</a>
<p class="paragraph"> GPU-oriented boosting for highly parallel, GPU-intensive training and simulation-style runs.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm/ROCm-Finance" class="card-header-link">
  <h2 class="card-header">GitHub</h2>
</a>
<p class="paragraph"> Source for ROCm-Finance and related packaging on GitHub.
</p>
::::

::::{grid-item-card}
:padding: 1
:img-top: ../images/ROCm-DS_Docs.jpg
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
:img-top: ../images/ROCm-DS_Docs.jpg
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href=./xgboost.html class="card-header-link">
  <h2 class="card-header">ROCm-Finance Blogs</h2>
</a>
<p class="paragraph"> Browse blogs detailing how to accelerate your finance boost workloads on AMD Instinct GPUs.
</p>
::::

:::::
