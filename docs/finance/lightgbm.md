# LightGBM (ROCm-Finance)

LightGBM is how ROCm-Finance answers scale: leaf-wise training that shines when dataset size—wide
feature stores, long histories, dense microstructure matrices—would otherwise push
decisions into the next shift. On Instinct, that wall between overnight queues and minutes
thins out; the same boosting idiom, routed through ROCm's high-bandwidth, multi-GPU environment.

Reach for LightGBM when volume is the bottleneck, and you still want gradient boosting semantics
with GPU-native backing.

::::{grid} 2 2 2 2

:::{grid-item-card}
:padding: 1
:img-top: ../images/finance-6.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://rocm.docs.amd.com/projects/lightgbm/en/latest/" class="card-header-link">
  <h2 class="card-header">Documentation</h2>
</a>
<p class="paragraph"> Installation instructions, how-to guides, and API reference material are available on the ROCm Documentation site.
</p>
:::

:::{grid-item-card}
:padding: 1
:img-top: ../images/finance-2.png
:class-img-top: small-sd-card-img-top
:class-body: small-sd-card
:class: small-sd-card
+++
<a href="https://github.com/ROCm/LightGBM/" class="card-header-link">
  <h2 class="card-header">Github</h2>
</a>
<p class="paragraph"> View the LightGBM source code on Github.
</p>
:::

::::
