# ROCm 6.2.2 release notes

These release notes provide a summary of notable changes since the previous ROCm release.

```{note}
As ROCm 6.2.2 was released shortly after 6.2.1, the changes between these versions
are minimal. For a comprehensive overview of recent updates, the ROCm 6.2.1 release
notes are appended to the end of this document.

For detailed information about the changes in ROCm 6.2.1, refer to the appended
section: [ROCm 6.2.1 release notes](rocm-6-2-1-release-notes).
```

The [Compatibility matrix](https://rocm.docs.amd.com/en/docs-6.2.2/compatibility/compatibility-matrix.html)
provides the full list of supported hardware, operating systems, ecosystems, third-party components, and ROCm components
for each ROCm release.

Release notes for previous ROCm releases are available in earlier versions of the documentation.
See the [ROCm documentation release history](https://rocm.docs.amd.com/en/latest/release/versions.html).

## Release highlights

The following is a significant fix introduced in ROCm 6.2.2.

### Fixed Instinct MI300X error recovery failure

Improved the reliability of AMD Instinct MI300X accelerators in scenarios involving
uncorrectable errors. Previously, error recovery did not occur as expected,
potentially leaving the system in an undefined state. This fix ensures that error
recovery functions as expected, maintaining system stability.

See the [original issue](#instinct-mi300x-gpu-recovery-failure-on-uncorrectable-errors)
noted in the ROCm 6.2.1 release notes.

---

## ROCm 6.2.1 release notes

The ROCm 6.2.1 release notes document newly added ecosystem support, ROCm Offline Installer Creator updates,
and improvements to several ROCm libraries and tools.

- [Release highlights](release-highlights)

- [Operating system and hardware support changes](operating-system-and-hardware-support-changes)

- [ROCm components versioning](rocm-components)

- [Detailed component changes](detailed-component-changes)

- [ROCm known issues](rocm-known-issues)

- [ROCm upcoming changes](rocm-upcoming-changes)

### Release highlights

The following are notable new features and improvements in ROCm 6.2.1. For changes to individual components, see [Detailed component changes](#detailed-component-changes).

#### rocAL major version change

The new version of rocAL introduces many new features, but does not modify any of the existing public API functions. However, the version number was incremented from 1.3 to 2.0.
Applications linked to version 1.3 must be recompiled to link against version 2.0.

See [the rocAL detailed changes](#rocal-2-0-0) for more information.

#### New support for FBGEMM (Facebook General Matrix Multiplication)

As of ROCm 6.2.1, ROCm supports Facebook General Matrix Multiplication (FBGEMM) and the related FBGEMM_GPU library. 

FBGEMM is a low-precision, high-performance CPU kernel library for convolution and matrix multiplication. It is used for server-side inference and as a back end for PyTorch quantized operators. FBGEMM_GPU includes a collection of PyTorch GPU operator libraries for training and inference. For more information, see the ROCm [Model acceleration libraries guide](https://rocm.docs.amd.com/en/docs-6.2.1/how-to/llm-fine-tuning-optimization/model-acceleration-libraries.html)
and [PyTorch's FBGEMM GitHub repository](https://github.com/pytorch/FBGEMM).

#### ROCm Offline Installer Creator changes

The [ROCm Offline Installer Creator 6.2.1](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.2.1/install/rocm-offline-installer.html) introduces several new features and improvements including:

* Logging support for create and install logs
* More stringent checks for Linux versions and distributions
* Updated prerequisite repositories
* Fixed CTest issues

#### ROCm documentation changes 

There have been no changes to supported hardware or operating systems from ROCm 6.2.0 to ROCm 6.2.1.

* The Programming Model Reference and Understanding the Programming Model topics in HIP have been consolidated into one topic,
[HIP programming model (conceptual)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.1/understand/programming_model.html). 
* The [HIP virtual memory management](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.1/how-to/virtual_memory.html) and [HIP virtual memory management API](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.1/reference/virtual_memory_reference.html) topics have been added.

```{note}
The ROCm documentation, like all ROCm projects, is open source and available on GitHub. To contribute to ROCm documentation, see the [ROCm documentation contribution guidelines](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).
```

### Operating system and hardware support changes

ROCm 6.2.1 adds support for Ubuntu 24.04.1 (kernel: 6.8 [GA]).

See the [Compatibility matrix](https://rocm.docs.amd.com/en/docs-6.2.1/compatibility/compatibility-matrix.html) for the full list of supported operating systems and hardware architectures.

### ROCm components

The following table lists the versions of ROCm components for ROCm 6.2.1, including any version changes from 6.2.0 to 6.2.1. 

Click the component's updated version to go to a detailed list of its changes. Click <i class="fab fa-github fa-lg"></i> to go to the component's source code on GitHub.

<div class="pst-scrollable-table-container">
    <table id="rocm-rn-components" class="table">
        <thead>
            <tr>
                <th>Category</th>
                <th>Group</th>
                <th>Name</th>
                <th>Version</th>
                <th></th>
            </tr>
        </thead>
        <colgroup>
            <col span="1">
            <col span="1">
        </colgroup>
        <tbody class="rocm-components-libs rocm-components-ml">
            <tr>
                <th rowspan="8">Libraries</th>
                <th rowspan="8">Machine learning and computer vision</th>
                <td><a href="https://rocm.docs.amd.com/projects/composable_kernel/en/docs-6.2.1">Composable Kernel</a>
                </td>
                <td>1.1.0</td>
                <td><a href="https://github.com/ROCm/composable_kernel/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/AMDMIGraphX/en/docs-6.2.1">MIGraphX</a></td>
                <td>2.10</td>
                <td><a href="https://github.com/ROCm/AMDMIGraphX/releases/tag/rocm-6.2.1"><i class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/MIOpen/en/docs-6.2.1">MIOpen</a></td>
                <td>3.2.0</td>
                <td><a href="https://github.com/ROCm/MIOpen/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/MIVisionX/en/docs-6.2.1">MIVisionX</a></td>
                <td>3.0.0</td>
                <td><a href="https://github.com/ROCm/MIVisionX/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocAL/en/docs-6.2.1">rocAL</a></td>
                <td>1.0.0&nbsp;&Rightarrow;&nbsp;<a href="#rocal-2-0-0">2.0.0</a></td>
                <td><a href="https://github.com/ROCm/rocAL/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocDecode/en/docs-6.2.1">rocDecode</a></td>
                <td>0.6.0</td>
                <td><a href="https://github.com/ROCm/rocDecode/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocPyDecode/en/docs-6.2.1">rocPyDecode</a></td>
                <td>0.1.0</td>
                <td><a href="https://github.com/ROCm/rocPyDecode/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rpp/en/docs-6.2.1">RPP</a></td>
                <td>1.8.0</td>
                <td><a href="https://github.com/ROCm/rpp/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-libs rocm-components-communication">
            <tr>
                <th rowspan="1"></th>
                <th rowspan="1">Communication</th>
                <td><a href="https://rocm.docs.amd.com/projects/rccl/en/docs-6.2.1">RCCL</a></td>
                <td>2.20.5&nbsp;&Rightarrow;&nbsp;<a href="#rccl-2-20-5">2.20.5</a></td>
                <td><a href="https://github.com/ROCm/rccl/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-libs rocm-components-math tbody-reverse-zebra">
            <tr>
                <th rowspan="16"></th>
                <th rowspan="16">Math</th>
                <td><a href="https://rocm.docs.amd.com/projects/hipBLAS/en/docs-6.2.1">hipBLAS</a></td>
                <td>2.2.0</td>
                <td><a href="https://github.com/ROCm/hipBLAS/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipBLASLt/en/docs-6.2.1">hipBLASLt</a></td>
                <td>0.8.0</td>
                <td><a href="https://github.com/ROCm/hipBLASLt/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipFFT/en/docs-6.2.1">hipFFT</a></td>
                <td>1.0.15</td>
                <td><a href="https://github.com/ROCm/hipFFT/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipfort/en/docs-6.2.1">hipfort</a></td>
                <td>0.4.0</td>
                <td><a href="https://github.com/ROCm/hipfort/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipRAND/en/docs-6.2.1">hipRAND</a></td>
                <td>2.11.0</td>
                <td><a href="https://github.com/ROCm/hipRAND/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipSOLVER/en/docs-6.2.1">hipSOLVER</a></td>
                <td>2.2.0</td>
                <td><a href="https://github.com/ROCm/hipSOLVER/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipSPARSE/en/docs-6.2.1">hipSPARSE</a></td>
                <td>3.1.1</td>
                <td><a href="https://github.com/ROCm/hipSPARSE/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipSPARSELt/en/docs-6.2.1">hipSPARSELt</a></td>
                <td>0.2.1</td>
                <td><a href="https://github.com/ROCm/hipSPARSELt/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocALUTION/en/docs-6.2.1">rocALUTION</a></td>
                <td>3.2.0</td>
                <td><a href="https://github.com/ROCm/rocALUTION/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocBLAS/en/docs-6.2.1">rocBLAS</a></td>
                <td>4.1.2&nbsp;&Rightarrow;&nbsp;<a href="#rocblas-4-2-1">4.2.1</a></td>
                <td><a href="https://github.com/ROCm/rocBLAS/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocFFT/en/docs-6.2.1">rocFFT</a></td>
                <td>1.0.28&nbsp;&Rightarrow;&nbsp;<a href="#rocfft-1-0-29">1.0.29</a></td>
                <td><a href="https://github.com/ROCm/rocFFT/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocRAND/en/docs-6.2.1">rocRAND</a></td>
                <td>3.1.0</td>
                <td><a href="https://github.com/ROCm/rocRAND/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocSOLVER/en/docs-6.2.1">rocSOLVER</a></td>
                <td>3.26.0</td>
                <td><a href="https://github.com/ROCm/rocSOLVER/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocSPARSE/en/docs-6.2.1">rocSPARSE</a></td>
                <td>3.2.0</td>
                <td><a href="https://github.com/ROCm/rocSPARSE/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocWMMA/en/docs-6.2.1">rocWMMA</a></td>
                <td>1.5.0</td>
                <td><a href="https://github.com/ROCm/rocWMMA/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://github.com/ROCm/Tensile">Tensile</a></td>
                <td>4.41.0</td>
                <td><a href="https://github.com/ROCm/tensile/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-libs rocm-components-primitives tbody-reverse-zebra">
            <tr>
                <th rowspan="4"></th>
                <th rowspan="4">Primitives</th>
                <td><a href="https://rocm.docs.amd.com/projects/hipCUB/en/docs-6.2.1">hipCUB</a></td>
                <td>3.2.0</td>
                <td><a href="https://github.com/ROCm/hipCUB/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/hipTensor/en/docs-6.2.1">hipTensor</a></td>
                <td>1.3.0</td>
                <td><a href="https://github.com/ROCm/hipTensor/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocPRIM/en/docs-6.2.1">rocPRIM</a></td>
                <td>3.2.0&nbsp;&Rightarrow;&nbsp;<a href="#rocprim-3-2-1">3.2.1</a></td>
                <td><a href="https://github.com/ROCm/rocPRIM/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocThrust/en/docs-6.2.1">rocThrust</a></td>
                <td>3.1.0</td>
                <td><a href="https://github.com/ROCm/rocThrust/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-tools rocm-components-system tbody-reverse-zebra">
            <tr>
                <th rowspan="6">Tools</th>
                <th rowspan="6">System management</th>
                <td><a href="https://rocm.docs.amd.com/projects/amdsmi/en/docs-6.2.1">AMD SMI</a></td>
                <td>24.6.2&nbsp;&Rightarrow;&nbsp;<a href="#amd-smi-24-6-3">24.6.3</a></td>
                <td><a href="https://github.com/ROCm/amdsmi/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocminfo/en/docs-6.2.1">rocminfo</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/ROCm/rocminfo/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rdc/en/docs-6.2.1">ROCm Data Center Tool</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/ROCm/rdc/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocm_smi_lib/en/docs-6.2.1">ROCm SMI</a></td>
                <td>7.3.0&nbsp;&Rightarrow;&nbsp;<a href="#rocm-smi-7-3-0">7.3.0</a></td>
                <td><a href="https://github.com/ROCm/rocm_smi_lib/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/docs-6.2.1">ROCm Validation Suite</a></td>
                <td>1.0.0</td>
                <td><a href="https://github.com/ROCm/ROCmValidationSuite/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-tools rocm-components-perf">
            <tr>
                <th rowspan="6"></th>
                <th rowspan="6">Performance</th>
                <td><a href="https://rocm.docs.amd.com/projects/omniperf/en/docs-6.2.1">Omniperf</a></td>
                <td>2.0.1</td>
                <td><a href="https://github.com/ROCm/omniperf/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/omnitrace/en/docs-6.2.1">Omnitrace</a></td>
                <td>1.11.2&nbsp;&Rightarrow;&nbsp;<a href="#omnitrace-1-11-2">1.11.2</a></td>
                <td><a href="https://github.com/ROCm/omnitrace/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocm_bandwidth_test/en/docs-6.2.1">ROCm Bandwidth
                        Test</a></td>
                <td>1.4.0</td>
                <td><a href="https://github.com/ROCm/rocm_bandwidth_test/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocprofiler/en/docs-6.2.1/">ROCProfiler</a></td>
                <td>2.0.0</td>
                <td><a href="https://github.com/ROCm/ROCProfiler/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/docs-6.2.1">ROCprofiler-SDK</a></td>
                <td>0.4.0</td>
                <td><a href="https://github.com/ROCm/rocprofiler-sdk/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr >
                <td><a href="https://rocm.docs.amd.com/projects/roctracer/en/docs-6.2.1/">ROCTracer</a></td>
                <td>4.1.0</td>
                <td><a href="https://github.com/ROCm/ROCTracer/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-tools rocm-components-dev">
            <tr>
                <th rowspan="5"></th>
                <th rowspan="5">Development</th>
                <td><a href="https://rocm.docs.amd.com/projects/HIPIFY/en/docs-6.2.1/">HIPIFY</a></td>
                <td>18.0.0&nbsp;&Rightarrow;&nbsp;<a href="#hipify-18-0-0">18.0.0</a></td>
                <td><a href="https://github.com/ROCm/HIPIFY/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/ROCdbgapi/en/docs-6.2.1">ROCdbgapi</a></td>
                <td>0.76.0</td>
                <td><a href="https://github.com/ROCm/ROCdbgapi/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/ROCmCMakeBuildTools/en/docs-6.2.1/">ROCm CMake</a></td>
                <td>0.13.0</td>
                <td><a href="https://github.com/ROCm/rocm-cmake/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/ROCgdb/en/docs-6.2.1">ROCm Debugger (ROCgdb)</a>
                </td>
                <td>14.2</td>
                <td><a href="https://github.com/ROCm/ROCgdb/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/rocr_debug_agent/en/docs-6.2.1">ROCr Debug Agent</a>
                </td>
                <td>2.0.3</td>
                <td><a href="https://github.com/ROCm/rocr_debug_agent/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-compilers tbody-reverse-zebra">
            <tr>
                <th rowspan="2" colspan="2">Compilers</th>
                <td><a href="https://rocm.docs.amd.com/projects/HIPCC/en/docs-6.2.1">HIPCC</a></td>
                <td>1.1.1</td>
                <td><a href="https://github.com/ROCm/llvm-project/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/llvm-project/en/docs-6.2.1">llvm-project</a></td>
                <td>18.0.0</td>
                <td><a href="https://github.com/ROCm/llvm-project/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
        <tbody class="rocm-components-runtimes tbody-reverse-zebra">
            <tr>
                <th rowspan="2" colspan="2">Runtimes</th>
                <td><a href="https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.1">HIP</a></td>
                <td>6.2&nbsp;&Rightarrow;&nbsp;<a href="#hip-6-2-1">6.2.1</a></td>
                <td><a href="https://github.com/ROCm/HIP/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
            <tr>
                <td><a href="https://rocm.docs.amd.com/projects/ROCR-Runtime/en/docs-6.2.1">ROCr Runtime</a></td>
                <td>1.14.0</td>
                <td><a href="https://github.com/ROCm/ROCR-Runtime/releases/tag/rocm-6.2.1"><i
                            class="fab fa-github fa-lg"></i></a></td>
            </tr>
        </tbody>
    </table>
</div>

### Detailed component changes

The following sections describe key changes to ROCm components.

#### **AMD SMI** (24.6.3)

##### Changes

* Added `amd-smi static --ras` on Guest VMs. Guest VMs can view enabled/disabled RAS features on Host cards.

##### Removals

* Removed `amd-smi metric --ecc` & `amd-smi metric --ecc-blocks` on Guest VMs. Guest VMs do not support getting current ECC counts from the Host cards.

##### Resolved issues

* Fixed TypeError in `amd-smi process -G`.
* Updated CLI error strings to handle empty and invalid GPU/CPU inputs.
* Fixed Guest VM showing passthrough options.
* Fixed firmware formatting where leading 0s were missing.

#### **HIP** (6.2.1)

##### Resolved issues

* Soft hang when using `AMD_SERIALIZE_KERNEL`
* Memory leak in `hipIpcCloseMemHandle`

#### **HIPIFY** (18.0.0)

##### Changes

* Added CUDA 12.5.1 support
* Added cuDNN 9.2.1 support
* Added LLVM 18.1.8 support
* Added `hipBLAS` 64-bit APIs support
* Added Support for math constants `math_constants.h`

#### **Omnitrace** (1.11.2)

##### Known issues

Perfetto can no longer open Omnitrace proto files. Loading Perfetto trace output `.proto` files in the latest version of `ui.perfetto.dev` can result in a dialog with the message, "Oops, something went wrong! Please file a bug." The information in the dialog will refer to an "Unknown field type." The workaround is to open the files with the previous version of the Perfetto UI found at [https://ui.perfetto.dev/v46.0-35b3d9845/#!/](https://ui.perfetto.dev/v46.0-35b3d9845/#!/).

See [issue #3767](https://github.com/ROCm/ROCm/issues/3767) on GitHub.

#### **RCCL** (2.20.5)

##### Known issues

On systems running Linux kernel 6.8.0, such as Ubuntu 24.04, Direct Memory Access (DMA) transfers between the GPU and NIC are disabled and impacts multi-node RCCL performance.
This issue was reproduced with RCCL 2.20.5 (ROCm 6.2.0 and 6.2.1) on systems with Broadcom Thor-2 NICs and affects other systems with RoCE networks using Linux 6.8.0 or newer.
Older RCCL versions are also impacted.

This issue will be addressed in a future ROCm release.

See [issue #3772](https://github.com/ROCm/ROCm/issues/3772) on GitHub.

#### **rocAL** (2.0.0)

##### Changes
 
* The new version of rocAL introduces many new features, but does not modify any of the existing public API functions.However, the version number was incremented from 1.3 to 2.0.
  Applications linked to version 1.3 must be recompiled to link against version 2.0.
* Added development and test packages.
* Added C++ rocAL audio unit test and Python script to run and compare the outputs.
* Added Python support for audio decoders.
* Added Pytorch iterator for audio.
* Added Python audio unit test and support to verify outputs.
* Added rocDecode for HW decode.
* Added support for: 
    * Audio loader and decoder, which uses libsndfile library to decode wav files
    * Audio augmentation - PreEmphasis filter, Spectrogram, ToDecibels, Resample, NonSilentRegionDetection, MelFilterBank 
    * Generic augmentation - Slice, Normalize
    * Reading from file lists in file reader
    * Downmixing audio channels during decoding
    * TensorTensorAdd and TensorScalarMultiply operations
    * Uniform and Normal distribution nodes
* Image to tensor updates
* ROCm install - use case graphics removed

##### Known issues
 
* Dependencies are not installed with the rocAL package installer. Dependencies must be installed with the prerequisite setup script provided. See the [rocAL README on GitHub](https://github.com/ROCm/rocAL/blob/docs/6.2.1/README.md#prerequisites-setup-script) for details.

#### **rocBLAS** (4.2.1)

##### Removals

* Removed Device_Memory_Allocation.pdf link in documentation.

##### Resolved issues

* Fixed error/warning message during `rocblas_set_stream()` call.

#### **rocFFT** (1.0.29)

##### Optimizations

* Implemented 1D kernels for factorizable sizes less than 1024.

#### **ROCm SMI** (7.3.0)

##### Optimizations

* Improved handling of UnicodeEncodeErrors with non UTF-8 locales. Non UTF-8 locales were causing crashes on UTF-8 special characters.

##### Resolved issues

* Fixed an issue where the Compute Partition tests segfaulted when AMDGPU was loaded with optional parameters.

##### Known issues

* When setting CPX as a partition mode, there is a DRM node limit of 64. This is a known limitation when multiple drivers are using the DRM nodes. The `ls /sys/class/drm` command can be used to see the number of DRM nodes, and the following steps can be used to remove unnecessary drivers:
        
    1. Unload AMDGPU: `sudo rmmod amdgpu`.
    2. Remove any unnecessary drivers using `rmmod`. For example, to remove an AST driver, run `sudo rmmod ast`.
    3. Reload AMDGPU using `modprobe`: `sudo modprobe amdgpu`.

#### **rocPRIM** (3.2.1)

##### Optimizations

* Improved performance of `block_reduce_warp_reduce` when warp size equals block size.

### ROCm known issues

ROCm known issues are tracked on [GitHub](https://github.com/ROCm/ROCm/labels/Verified%20Issue). Known issues related to
individual components are listed in the [Detailed component changes](detailed-component-changes) section.

#### Instinct MI300X GPU recovery failure on uncorrectable errors

For the AMD Instinct MI300X accelerator, GPU recovery resets triggered by uncorrectable errors (UE) might not complete
successfully, which can result in the system being left in an undefined state. A system reboot is needed to recover from
this state. Additionally, error logging might fail in these situations, hindering diagnostics.

This issue is under investigation and will be resolved in a future ROCm release.

See [issue #3766](https://github.com/ROCm/ROCm/issues/3766) on GitHub.

### ROCm upcoming changes

The following changes to the ROCm software stack are anticipated for future releases.

#### rocm-llvm-alt

The `rocm-llvm-alt` package will be removed in an upcoming release. Users relying on the functionality provided by the closed-source compiler should transition to the open-source compiler. Once the `rocm-llvm-alt` package is removed, any compilation requesting functionality provided by the closed-source compiler will result in a Clang warning: "*[AMD] proprietary optimization compiler has been removed*".

#### rccl-rdma-sharp-plugins

The RCCL plugin package, `rccl-rdma-sharp-plugins`, will be removed in an upcoming ROCm release. 
