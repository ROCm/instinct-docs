<head>
  <meta charset="UTF-8">
  <meta name="description" content="GPU memory">
  <meta name="keywords" content="GPU memory, VRAM, video random access memory, pageable
  memory, pinned memory, managed memory, AMD, ROCm">
</head>

# GPU memory

For the HIP reference documentation, see:

* {doc}`hip:doxygen/html/group___memory`
* {doc}`hip:doxygen/html/group___memory_m`

Host memory exists on the host (e.g. CPU) of the machine in random access memory (RAM).

Device memory exists on the device (e.g. GPU) of the machine in video random access memory (VRAM).
Recent architectures use graphics double data rate (GDDR) synchronous dynamic random-access memory (SDRAM)such as GDDR6, or high-bandwidth memory (HBM) such as HBM2e.

## Memory allocation

Memory can be allocated in two ways: pageable memory, and pinned memory.
The following API calls with result in these allocations:

| API                | Data location | Allocation |
|--------------------|---------------|------------|
| System allocated   | Host          | Pageable   |
| `hipMallocManaged` | Host          | Managed    |
| `hipHostMalloc`    | Host          | Pinned     |
| `hipMalloc`        | Device        | Pinned     |

:::{tip}
`hipMalloc` and `hipFree` are blocking calls, however, HIP recently added non-blocking versions `hipMallocAsync` and `hipFreeAsync` which take in a stream as an additional argument.
:::

### Pageable memory

Pageable memory is usually gotten when calling `malloc` or `new` in a C++ application.
It is unique in that it exists on "pages" (blocks of memory), which can be migrated to other memory storage.
For example, migrating memory between CPU sockets on a motherboard, or a system that runs out of space in RAM and starts dumping pages of RAM into the swap partition of your hard drive.

### Pinned memory

Pinned memory (or page-locked memory, or non-pageable memory) is host memory that is mapped into the address space of all GPUs, meaning that the pointer can be used on both host and device.
Accessing host-resident pinned memory in device kernels is generally not recommended for performance, as it can force the data to traverse the host-device interconnect (e.g. PCIe), which is much slower than the on-device bandwidth (>40x on MI200).

Pinned host memory can be allocated with one of two types of coherence support:

:::{note}
In HIP, pinned memory allocations are coherent by default (`hipHostMallocDefault`).
There are additional pinned memory flags (e.g. `hipHostMallocMapped` and `hipHostMallocPortable`).
On MI200 these options do not impact performance.
<!-- TODO: link to programming_manual#memory-allocation-flags -->
For more information, see the section *memory allocation flags* in the HIP Programming Guide: {doc}`hip:how-to/programming_manual`.
:::

Much like how a process can be locked to a CPU core by setting affinity, a pinned memory allocator does this with the memory storage system.
On multi-socket systems it is important to ensure that pinned memory is located on the same socket as the owning process, or else each cache line will be moved through the CPU-CPU interconnect, thereby increasing latency and potentially decreasing bandwidth.

In practice, pinned memory is used to improve transfer times between host and device.
For transfer operations, such as `hipMemcpy` or `hipMemcpyAsync`, using pinned memory instead of pageable memory on host can lead to a ~3x improvement in bandwidth.

:::{tip}
If the application needs to move data back and forth between device and host (separate allocations), use pinned memory on the host side.
:::

### Managed memory

Managed memory refers to universally addressable, or unified memory available on the MI200 series of GPUs.
Much like pinned memory, managed memory shares a pointer between host and device and (by default) supports fine-grained coherence, however, managed memory can also automatically migrate pages between host and device.
The allocation will be managed by AMD GPU driver using the Linux HMM (Heterogeneous Memory Management) mechanism.

If heterogenous memory management (HMM) is not available, then `hipMallocManaged` will default back to using system memory and will act like pinned host memory.
Other managed memory API calls will have undefined behavior.
It is therefore recommended to check for managed memory capability with: `hipDeviceGetAttribute` and `hipDeviceAttributeManagedMemory`.

HIP supports additional calls that work with page migration:

* `hipMemAdvise`
* `hipMemPrefetchAsync`

:::{tip}
If the application needs to use data on both host and device regularly, does not want to deal with separate allocations, and is not worried about maxing out the VRAM on MI200 GPUs (64 GB per GCD), use managed memory.
:::

:::{tip}
If managed memory performance is poor, check to see if managed memory is supported on your system and if page migration (XNACK) is enabled.
:::

## Access behavior

Memory allocations for GPUs behave as follow:

| API                | Data location | Host access  | Device access        |
|--------------------|---------------|--------------|----------------------|
| System allocated   | Host          | Local access | Unhandled page fault |
| `hipMallocManaged` | Host          | Local access | Zero-copy            |
| `hipHostMalloc`    | Host          | Local access | Zero-copy*           |
| `hipMalloc`        | Device        | Zero-copy    | Local access         |

Zero-copy accesses happen over the Infinity Fabric interconnect or PCI-E lanes on discrete GPUs.

:::{note}
While `hipHostMalloc` allocated memory is accessible by a device, the host pointer must be converted to a device pointer with `hipHostGetDevicePointer`.

Memory allocated through standard system allocators such as `malloc`, can be accessed a device by registering the memory via `hipHostRegister`.
The device pointer to be used in kernels can be retrieved with `hipHostGetDevicePointer`.
Registered memory is treated like `hipHostMalloc` and will have similar performance.

On devices that support and have [](#xnack) enabled, such as the MI250X, `hipHostRegister` is not required as memory accesses are handled via automatic page migration.
:::

### XNACK

Normally, host and device memory are separate and data has to be transferred manually via `hipMemcpy`.

On a subset of GPUs, such as the MI200, there is an option to automatically migrate pages of memory between host and device.
This is important for managed memory, where the locality of the data is important for performance.
Depending on the system, page migration may be disabled by default in which case managed memory will act like pinned host memory and suffer degraded performance.

*XNACK* describes the GPUs ability to retry memory accesses that failed due a page fault (which normally would lead to a memory access error), and instead retrieve the missing page.

This also affects memory allocated by the system as indicated by the following table:

| API                | Data location | Host after device access | Device after host access |
|--------------------|---------------|--------------------------|--------------------------|
| System allocated   | Host          | Migrate page to host     | Migrate page to device   |
| `hipMallocManaged` | Host          | Migrate page to host     | Migrate page to device   |
| `hipHostMalloc`    | Host          | Local access             | Zero-copy                |
| `hipMalloc`        | Device        | Zero-copy                | Local access             |

To check if page migration is available on a platform, use `rocminfo`:

```sh
$ rocminfo | grep xnack
      Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack-
```

Here, `xnack-` means that XNACK is available but is disabled by default.
Turning on XNACK by setting the environment variable `HSA_XNACK=1` and gives the expected result, `xnack+`:

```sh
$ HSA_XNACK=1 rocminfo | grep xnack
Name:                    amdgcn-amd-amdhsa--gfx90a:sramecc+:xnack+
```

`hipcc`by default will generate code that runs correctly with both XNACK enabled or disabled.
Setting the `--offload-arch=`-option with `xnack+` or `xnack-` forces code to be only run with XNACK enabled or disabled respectively.

```sh
# Compiled kernels will run regardless if XNACK is enabled or is disabled. 
hipcc --offload-arch=gfx90a

# Compiled kernels will only be run if XNACK is enabled with XNACK=1.
hipcc --offload-arch=gfx90a:xnack+

# Compiled kernels will only be run if XNACK is disabled with XNACK=0.
hipcc --offload-arch=gfx90a:xnack-
```

:::{tip}
If you want to make use of page migration, use managed memory. While pageable memory will migrate correctly, it is not a portable solution and can have performance issues if the accessed data isn't page aligned.
:::

### Coherence

* *Coarse-grained coherence* means that memory is only considered up to date at kernel boundaries, which can be enforced through `hipDeviceSynchronize`, `hipStreamSynchronize`, or any blocking operation that acts on the null stream (e.g. `hipMemcpy`).
For example, cacheable memory is a type of coarse-grained memory where an up-to-date copy of the data can be stored elsewhere (e.g. in an L2 cache).
* *Fine-grained coherence* means the coherence is supported while a CPU/GPU kernel is running.
This can be useful if both host and device are operating on the same dataspace using system-scope atomic operations (e.g. updating an error code or flag to a buffer).
Fine-grained memory implies that up-to-date data may be made visible to others regardless of kernel boundaries as discussed above.

| API                     | Flag                         | Coherence      |
|-------------------------|------------------------------|----------------|
| `hipHostMalloc`         | `hipHostMallocDefault`       | Fine-grained   |
| `hipHostMalloc`         | `hipHostMallocNonCoherent`   | Coarse-grained |

| API                     | Flag                         | Coherence      |
|-------------------------|------------------------------|----------------|
| `hipExtMallocWithFlags` | `hipDeviceMallocDefault`     | Coarse-grained |
| `hipExtMallocWithFlags` | `hipDeviceMallocFinegrained` | Fine-grained   |

| API                     | `hipMemAdvise` argument      | Coherence      |
|-------------------------|------------------------------|----------------|
| `hipMallocManaged`      |                              | Fine-grained   |
| `hipMallocManaged`      | `hipMemAdviseSetCoarseGrain` | Coarse-grained |
| `malloc`                |                              | Fine-grained   |
| `malloc`                | `hipMemAdviseSetCoarseGrain` | Coarse-grained |

:::{tip}
Try to design your algorithms to avoid host-device memory coherence (e.g. system scope atomics). While it can be a useful feature in very specific cases, it is not supported on all systems, and can negatively impact performance by introducing the host-device interconnect bottleneck.
:::

The availability of fine- and coarse-grained memory pools can be checked with `rocminfo`:

```sh
$ rocminfo
...
*******
Agent 1
*******
Name:                    AMD EPYC 7742 64-Core Processor
...
Pool Info:
Pool 1
Segment:                 GLOBAL; FLAGS: FINE GRAINED
...
Pool 3
Segment:                 GLOBAL; FLAGS: COARSE GRAINED
...
*******
Agent 9
*******
Name:                    gfx90a
...
Pool Info:
Pool 1
Segment:                 GLOBAL; FLAGS: COARSE GRAINED
...
```

## System direct memory access

In most cases, the default behavior for HIP in transferring data from a pinned host allocation to device will run at the limit of the interconnect.
However, there are certain cases where the interconnect is not the bottleneck.

The primary way to transfer data onto and off of a GPU, such as the MI200, is to use the onboard System Direct Memory Access engine, which is used to feed blocks of memory to the off-device interconnect (either GPU-CPU or GPU-GPU).
Each GCD has a separate SDMA engine for host-to-device and device-to-host memory transfers.
Importantly, SDMA engines are separate from the computing infrastructure, meaning that memory transfers to and from a device will not impact kernel compute performance, though they do impact memory bandwidth to a limited extent.
The SDMA engines are mainly tuned for PCIe-4.0 x16, which means they are designed to operate at bandwidths up to 32 GB/s.

:::{note}
An important feature of the MI250X platform is the Infinity Fabric™ interconnect between host and device.
The Infinity Fabric interconnect supports improved performance over standard PCIe-4.0 (usually ~50% more bandwidth); however, since the SDMA engine does not run at this speed, it will not max out the bandwidth of the faster interconnect.
:::

The bandwidth limitation can be countered by bypassing the SDMA engine and replacing it with a type of copy kernel known as a "blit" kernel.
Blit kernels will use the compute units on the GPU, thereby consuming compute resources, which may not always be beneficial.
The easiest way to enable blit kernels is to set an environment variable `HSA_ENABLE_SDMA=0`, which will disable the SDMA engine.
On systems where the GPU uses a PCIe interconnect instead of an Infinity Fabric interconnect, blit kernels will not impact bandwidth, but will still consume compute resources.
The use of SDMA vs blit kernels also applies to MPI data transfers and GPU-GPU transfers.
