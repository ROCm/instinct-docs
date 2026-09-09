---
html_theme.sidebar_secondary.remove: true
---

<div class="id-landing-layout">
<div class="id-landing-main">

<input type="checkbox" id="id-sidebar-toggle" class="id-sidebar-toggle-input">
<label for="id-sidebar-toggle" class="id-sidebar-toggle-label" aria-label="Toggle site navigation">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>
</label>

<div class="id-hero-eyebrow">
  <span class="id-hero-eyebrow-rule"></span>AMD Instinct™ · Data Center GPU
</div>

# Systems &amp; Infrastructure Documentation

<p class="id-hero-lede">
Everything you need to <strong>deploy, validate, and operate</strong> AMD Instinct™ Data Center GPUs at scale — drivers, orchestration, cluster management, and acceptance testing for HPC and AI. For API and software-stack reference, see the <a href="https://rocm.docs.amd.com">ROCm documentation</a>.
</p>

<div class="id-hero-actions">
  <a class="id-btn id-btn-primary" href="https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/">
    Install the GPU driver
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  </a>
  <a class="id-btn id-btn-ghost" href="https://instinct.docs.amd.com/projects/system-acceptance/en/latest/">
    Customer Acceptance Guide
  </a>
</div>

<div class="id-hero-spacer"></div>

<!-- ════════════════ SYSTEM ADMINISTRATORS — primary, frequently updated ════════════════ -->

<div class="id-deck id-deck--primary">

<div class="id-deck-head">
  <div class="id-section-label">Start here</div>
  <h2 class="id-deck-title" id="system-administrators">System Administrators</h2>
  <p class="id-deck-sub">Deploy and run AMD Instinct GPUs on bare metal, in containers, and across clusters. These guides are the most frequently updated content on this site.</p>
</div>

<div class="id-group" open>
<a class="id-subhead" href="system-admin/bare-metal.html">Bare metal</a>
<div class="id-grid">

<a class="id-card" href="https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v2M15 2v2M9 20v2M15 20v2M20 9h2M20 14h2M2 9h2M2 14h2"/></svg></span>
  <span class="id-card-title">Instinct GPU Driver</span>
  <span class="id-card-desc">Install and configure the GPU, including logging and error codes.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/conceptual/partition.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/></svg></span>
  <span class="id-card-title">GPU Partitioning</span>
  <span class="id-card-desc">Split compute units and memory to partition a single GPU.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 14 16 10"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/></svg></span>
  <span class="id-card-title">AMD SMI</span>
  <span class="id-card-desc">Unified user-space tool to manage and monitor GPUs and drivers.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg></span>
  <span class="id-card-title">ROCm Validation Suite</span>
  <span class="id-card-desc">System validation and hardware diagnostics.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/system-acceptance/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/></svg></span>
  <span class="id-card-title">Customer Acceptance Guide</span>
  <span class="id-card-desc">Configure, validate, benchmark, and baseline Instinct GPUs.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/cvs/en/latest/index.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6 6h.01M6 18h.01"/></svg></span>
  <span class="id-card-title">Cluster Validation Suite</span>
  <span class="id-card-desc">Test scripts that validate AMD AI clusters end to end.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>
</div>

<div class="id-group" open>
<a class="id-subhead" href="system-admin/co-tools.html">Containers &amp; orchestration</a>
<div class="id-grid">

<a class="id-card" href="https://instinct.docs.amd.com/projects/gpu-operator/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg></span>
  <span class="id-card-title">GPU Operator</span>
  <span class="id-card-desc">Deploy and manage Instinct GPUs in Kubernetes clusters.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/network-operator/en/main/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/></svg></span>
  <span class="id-card-title">Network Operator</span>
  <span class="id-card-desc">Simplify AMD AINICs in Kubernetes environments.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/k8s-device-plugin/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/></svg></span>
  <span class="id-card-title">Device Plugin</span>
  <span class="id-card-desc">Register AMD GPUs with a Kubernetes container cluster.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/device-metrics-exporter/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="12" x2="12" y1="20" y2="10"/><line x1="18" x2="18" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="16"/></svg></span>
  <span class="id-card-title">Device Metrics Exporter</span>
  <span class="id-card-desc">Prometheus-format GPU metrics for HPC and AI environments.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/container-toolkit/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/></svg></span>
  <span class="id-card-title">AMD Container Toolkit</span>
  <span class="id-card-desc">Integrate Instinct GPUs with Docker and container runtimes.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/spur/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="6" rx="1"/><rect x="3" y="14" width="18" height="6" rx="1"/><path d="M7 7h.01M7 17h.01M12 7h4M12 17h4"/></svg></span>
  <span class="id-card-title">Spur</span>
  <span class="id-card-desc">AI-native job scheduler, drop-in compatible with Slurm, with GPU-first scheduling and Raft-based state.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>
</div>

<div class="id-group" open>
<a class="id-subhead" href="system-admin/index.html#cluster-cloud-virtualization">Cluster, cloud &amp; virtualization</a>
<div class="id-grid">

<a class="id-card" href="https://account.amd.com/en/forms/registration/enterpriseai-ea.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="16" height="20" x="4" y="2" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/></svg></span>
  <span class="id-card-title">Enterprise AI</span>
  <span class="id-card-desc">Tools to manage enterprise AI infrastructure at scale.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://amdresearch.github.io/omnistat/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg></span>
  <span class="id-card-title">Omnistat</span>
  <span class="id-card-desc">Profile GPU resource utilization across the cluster.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" x2="15.42" y1="13.51" y2="17.49"/><line x1="15.41" x2="8.59" y1="6.51" y2="10.49"/></svg></span>
  <span class="id-card-title">Cluster Networking</span>
  <span class="id-card-desc">Optimize the network for Instinct GPU applications.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/instinct-azure/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/></svg></span>
  <span class="id-card-title">Instinct on Azure</span>
  <span class="id-card-desc">Get started with AMD Instinct GPUs on Microsoft Azure.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/virt-drv/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/></svg></span>
  <span class="id-card-title">Virtualization Driver</span>
  <span class="id-card-desc">Explore the virtualization driver for Instinct GPUs.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://instinct.docs.amd.com/projects/amd-smi-virt/en/latest/">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/></svg></span>
  <span class="id-card-title">AMD SMI for Virtualization</span>
  <span class="id-card-desc">Manage and monitor virtualization-enabled AMD GPUs.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>
</div>

</div>

<!-- ════════════════ COMMON REFERENCE ════════════════ -->

<div class="id-deck">

<div class="id-deck-head">
  <h2 class="id-deck-title" id="common-reference">Common Reference</h2>
  <p class="id-deck-sub">Architecture, programming models, and technical collateral that span every deployment.</p>
</div>

<div class="id-grid">

<a class="id-card" href="https://rocm.docs.amd.com/en/latest/reference/gpu-arch/index.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v2M15 2v2M9 20v2M15 20v2M20 9h2M20 14h2M2 9h2M2 14h2"/></svg></span>
  <span class="id-card-title">Instinct Micro-architecture</span>
  <span class="id-card-desc">Hardware details for MI350, MI300, MI200, and MI100 accelerators.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/amdsmi/en/latest/index.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg></span>
  <span class="id-card-title">AMD SMI API Reference</span>
  <span class="id-card-desc">Full AMD SMI documentation covering all use cases.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/HIP/en/latest/index.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></span>
  <span class="id-card-title">HIP C++</span>
  <span class="id-card-desc">Learn the HIP programming model.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://rocm.docs.amd.com/projects/llvm-project/en/latest/conceptual/openmp.html">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="14 2 14 8 20 8"/><path d="M4 4a2 2 0 0 1 2-2h8l6 6v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/><path d="m9 13 2 2-2 2M15 13l-2 2 2 2"/></svg></span>
  <span class="id-card-title">OpenMP</span>
  <span class="id-card-desc">Explore the OpenMP programming model.</span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

<a class="id-card" href="https://docs.amd.com/v/u/en-US/ug1729-amd-instinct-accelerators">
  <span class="id-card-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg></span>
  <span class="id-card-title">Technical Information Portal</span>
  <span class="id-card-desc">NDA technical documentation and design collateral. <em>Login required.</em></span>
  <span class="id-card-go" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></span>
</a>

</div>

</div>

</div>
<!-- /.id-landing-main -->

<aside class="id-page-rail" aria-label="On this page">
  <div class="page-toc tocsection onthispage">
    <i class="fa-solid fa-list" aria-hidden="true"></i> On this page
  </div>
  <nav class="bd-toc-nav page-toc">
    <ul class="visible nav section-nav flex-column">
      <li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#system-administrators">System Administrators</a></li>
      <li class="toc-h2 nav-item toc-entry"><a class="reference internal nav-link" href="#common-reference">Common Reference</a></li>
      <li class="toc-h2 nav-item toc-entry"><a class="reference external nav-link" href="https://instinct.docs.amd.com/projects/gsid-verticals-docs/en/latest/">Industries &amp; Verticals</a></li>
    </ul>
  </nav>
</aside>

</div>
<!-- /.id-landing-layout -->

<!-- Industries/Verticals no longer gets featured landing placement — see docs/sphinx/_toc.yml.in,
     now a single external nav link to the gsid-verticals-docs project, like any other subpage. -->
