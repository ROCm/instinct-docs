|A black background with a black square Description automatically
generated with medium confidence|

| AMD Instinct MI300X Customer
| Acceptance Test Guide

Publication Number: 58708 v0.9
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

October 2024
^^^^^^^^^^^^

Contents
========

`Chapter 1: Introduction <#chapter-1-introduction>`__
`5 <#chapter-1-introduction>`__

`Chapter 2: Prerequisites <#chapter-2-prerequisites>`__
`5 <#chapter-2-prerequisites>`__

`2.1 System BIOS Settings <#system-bios-settings>`__
`6 <#system-bios-settings>`__

`2.2 Supported Operating Systems <#supported-operating-systems>`__
`6 <#supported-operating-systems>`__

`2.3 GRUB Settings <#grub-settings>`__ `6 <#grub-settings>`__

`2.4 Operating System Settings <#operating-system-settings>`__
`6 <#operating-system-settings>`__

`2.5 Updating System Firmware <#updating-system-firmware>`__
`6 <#updating-system-firmware>`__

`2.6 ROCm Installation <#rocm-installation>`__
`7 <#rocm-installation>`__

`Chapter 3: Basic System Health
Checks <#chapter-3-basic-system-health-checks>`__
`7 <#chapter-3-basic-system-health-checks>`__

`3.1 Check OS and host system
checks <#check-os-and-host-system-checks>`__
`8 <#check-os-and-host-system-checks>`__

`3.1.1 Check OS distribution
(os-release) <#check-os-distribution-os-release>`__
`8 <#check-os-distribution-os-release>`__

`3.1.2 Check kernel boot arguments
(cmdline) <#check-kernel-boot-arguments-cmdline>`__
`8 <#check-kernel-boot-arguments-cmdline>`__

`3.1.3 Check for driver errors
(dmesg) <#check-for-driver-errors-dmesg>`__
`9 <#check-for-driver-errors-dmesg>`__

`3.1.4 Check for available memory
(lsmem) <#check-for-available-memory-lsmem>`__
`9 <#check-for-available-memory-lsmem>`__

`3.2 Check GPU Presence (lspci) <#check-gpu-presence-lspci>`__
`9 <#check-gpu-presence-lspci>`__

`3.3 Check GPU link speed and width on PCIe bus (sudo lspci
-vvv) <#check-gpu-link-speed-and-width-on-pcie-bus-sudo-lspci--vvv>`__
`10 <#check-gpu-link-speed-and-width-on-pcie-bus-sudo-lspci--vvv>`__

`3.4 Monitoring Utilization Metrics
(amd-smi) <#monitoring-utilization-metrics-amd-smi>`__
`11 <#monitoring-utilization-metrics-amd-smi>`__

`3.5 Check the System Kernel Logs for Other Errors
(dmesg) <#check-the-system-kernel-logs-for-other-errors-dmesg>`__
`11 <#check-the-system-kernel-logs-for-other-errors-dmesg>`__

`Chapter 4: System Validation
Tests <#chapter-4-system-validation-tests>`__
`13 <#chapter-4-system-validation-tests>`__

`4.1 Compute / GPU <#compute-gpu>`__ `13 <#compute-gpu>`__

`4.1.1 Properties <#properties>`__ `14 <#properties>`__

`4.1.2 Benchmark / Stress /
Qualification <#benchmark-stress-qualification>`__
`15 <#benchmark-stress-qualification>`__

`4.2 Memory <#memory>`__ `18 <#memory>`__

`4.2.1 MEM <#mem>`__ `18 <#mem>`__

`4.2.2 BABEL <#babel>`__ `19 <#babel>`__

`4.3 IO <#io>`__ `19 <#io>`__

`4.3.1 PEBB (PCIe Bandwidth
Benchmark) <#pebb-pcie-bandwidth-benchmark>`__
`20 <#pebb-pcie-bandwidth-benchmark>`__

`4.3.2 PEQT (PCIe Qualification Tool) <#peqt-pcie-qualification-tool>`__
`21 <#peqt-pcie-qualification-tool>`__

`4.3.3 PBQT (P2P Benchmark and Qualification
Tool) <#pbqt-p2p-benchmark-and-qualification-tool>`__
`22 <#pbqt-p2p-benchmark-and-qualification-tool>`__

`Chapter 5: Performance
Benchmarking <#chapter-5-performance-benchmarking>`__
`24 <#chapter-5-performance-benchmarking>`__

`5.1 TransferBench Benchmarking
Results <#transferbench-benchmarking-results>`__
`24 <#transferbench-benchmarking-results>`__

`5.1.1 TransferBench Qualification <#transferbench-qualification>`__
`24 <#transferbench-qualification>`__

`5.2 RCCL Benchmarking Results <#rccl-benchmarking-results>`__
`29 <#rccl-benchmarking-results>`__

`5.2.1 RCCL Qualification <#rccl-qualification>`__
`30 <#rccl-qualification>`__

`5.3 rocBLAS Benchmarking Results <#rocblas-benchmarking-results>`__
`32 <#rocblas-benchmarking-results>`__

`5.3.1 rocBLAS Qualification <#rocblas-qualification>`__
`33 <#rocblas-qualification>`__

`5.4 BabelStream Benchmarking
Results <#babelstream-benchmarking-results>`__
`34 <#babelstream-benchmarking-results>`__

`5.4.1 BabelStream Qualification <#babelstream-qualification>`__
`35 <#babelstream-qualification>`__

`Chapter 6: Acceptance Criteria <#chapter-6-acceptance-criteria>`__
`38 <#chapter-6-acceptance-criteria>`__

`Chapter 7: Next Steps <#chapter-7-next-steps>`__
`40 <#chapter-7-next-steps>`__

`7.1 MI300X AI Model Performance Validation
Guide <#mi300x-ai-model-performance-validation-guide>`__
`40 <#mi300x-ai-model-performance-validation-guide>`__

`7.2 MI300X Cluster Network Performance Validation
Guide <#mi300x-cluster-network-performance-validation-guide>`__
`40 <#mi300x-cluster-network-performance-validation-guide>`__

`7.3 MI300X Workload Optimization
Guide <#mi300x-workload-optimization-guide>`__
`40 <#mi300x-workload-optimization-guide>`__

`Appendix A: Acronyms <#appendix-a-acronyms>`__
`41 <#appendix-a-acronyms>`__

`Appendix B: Reference Documents <#appendix-b-reference-documents>`__
`42 <#appendix-b-reference-documents>`__

`Appendix C: Collecting Logs
(rocm_techsupport.sh) <#pappendix-c-collecting-logs-rocm_techsupport.sh>`__
`43 <#pappendix-c-collecting-logs-rocm_techsupport.sh>`__

`Appendix D: Revision History <#appendix-d-revision-history>`__
`43 <#appendix-d-revision-history>`__

`Appendix E: Notices <#appendix-e-notices>`__
`44 <#appendix-e-notices>`__

`Trademarks <#trademarks>`__ `44 <#trademarks>`__

**
**

**List of Tables**

`Table 1: Average, Pass/Fail Bandwidth in GB/s for TransferBench
All-to-All Benchmarking <#_Toc180918271>`__ `25 <#_Toc180918271>`__

`Table 2: Average, Pass/Fail Bandwidth in GB/s for TransferBench
Peer-to-Peer Benchmarking <#_Toc180918272>`__ `27 <#_Toc180918272>`__

`Table 3: Average, Pass/Fail Bandwidth in GB/s for TransferBench
Benchmarking <#_Toc180918273>`__ `29 <#_Toc180918273>`__

`Table 4: Average, Pass/Fail Bandwidth in GB/s for RCCL
Benchmarking <#_Toc180918274>`__ `32 <#_Toc180918274>`__

`Table 5: Average, Pass/Fail Bandwidth in TFLOPS for GEMM
Benchmarking <#_Toc180918275>`__ `34 <#_Toc180918275>`__

`Table 6: Average, Pass/Fail Memory Bandwidth in MB/s for BabelStream
Benchmarking <#_Toc180918276>`__ `36 <#_Toc180918276>`__

`Table 7: Summary of the Basic System Health Checks <#_Toc180918277>`__
`38 <#_Toc180918277>`__

`Table 8: Summary of System Validation Tests <#_Toc180918278>`__
`38 <#_Toc180918278>`__

`Table 9: Summary of Performance Benchmarking Tests <#_Toc180918279>`__
`39 <#_Toc180918279>`__

`Table 10: Acronyms <#_Toc180918280>`__ `41 <#_Toc180918280>`__

`Table 11: Reference Documents <#_Toc180918281>`__
`42 <#_Toc180918281>`__

`Table 12: Revision History <#_Toc180918282>`__ `43 <#_Toc180918282>`__

Chapter 1: Introduction
=======================

This guide provides detailed instructions for qualified data center
system operators to test the proper functioning and optimal performance
of server systems equipped with AMD Instinct MI300X GPU accelerators.

This document is organized into chapters to follow in sequence to
configure the system, run tests, and interpret results to quickly
determine system health. Links to supporting documentation are also
included for reference.

Prior to system validation, the system operator should refer to
**Chapter 2: Prerequisites** to ensure the server has a supported OS
installed and is configured with recommended BIOS, GRUB, and OS settings
to ensure proper operation and peak performance operation.

**Chapter 3: Basic System Health Checks** provides the recommended tests
to validate the system health and configuration of the system across the
OS, boot configuration, host memory, and GPU connectivity.

**Chapter 4: System Validation Tests** provides the recommended tests to
validate the system’s Compute (GPUs), Memory, IO and Power using the
ROCm Validation Suite (RVS).

**Chapter 5: Performance Benchmarking** provides a list of
microbenchmarks to validate the performance of the GPUs in the system.
Tests include TransferBench, RCCL, rocBLAS, and BabelStream.

**Chapter 6: Acceptance Criteria** provides a summary of the commands
and PASS/FAIL criteria to compare against recently gathered test
results. This comparison is the basis for customer acceptance of a
tested server. By changing one parameter at a time and repeating
specific tests in earlier chapters, new results can be compared to the
baseline data gathered to ensure the best performance for your targeted
application(s).

After completing the tests outlined in this guide to determine if the
server/system under test (SUT) meets expected functionality and
performance, you should proceed to review the recommended referenced
documents in `Appendix B <#appendix-b-reference-documents>`__ and move
to the next stage of performance validation testing and optimization
outlined in `Chapter 7: Next Steps <#chapter-7-next-steps>`__.

Chapter 2: Prerequisites
========================

Prior to proceeding to the prerequisites in this section, the operator
should ensure the system does not have visible damage and is installed
correctly. Refer to the installation guide from the system manufacturer
to ensure the system has been correctly installed in a rack with
sufficient cooling, has been connected to required power, and is
accessible from the network.

If errors or warnings are discovered during setup, troubleshooting the
issue may be required, e.g. reseating auxiliary PCBs, checking internal
cable connections, or monitoring the situation. For debugging support,
reach out to your system manufacturer.

This section describes which server settings to configure prior to
testing including:

- System BIOS Settings

- Supported Operating Systems

- GRUB Settings

- Operating System Settings

- Updating System Firmware

- ROCm Installation

**NOTE:** Before changing any system settings and doing testing, it is
recommended to record existing production system settings to allow the
system to be returned to the original settings.

2.1 System BIOS Settings
------------------------

Some server manufacturers offer tools that allow the current BIOS
configuration settings to be exported to a file, modified with needed
changes, and loaded back to the system. In the case that the server
manufacturer does not offer such a tool, the BIOS settings will need to
be reviewed and updated manually from the BIOS setup interface prior to
booting the OS.

Refer to the recommended `System BIOS
Settings <https://rocm.docs.amd.com/en/latest/how-to/system-optimization/mi300x.html#mi300x-bios-settings>`__
for MI300X to ensure the system BIOS is setup correctly for maximum
performance prior to validating the system with AMD EPYC™ 9004-series
processors and AMI System BIOS. These settings should be set as default
values in the system BIOS. Analogous settings for other non-AMI System
BIOS providers could be set similarly. For systems with Intel
processors, some settings may not apply or be available.

2.2 Supported Operating Systems
-------------------------------

AMD ROCm software supports certain Linux distributions. Refer to the
list of `Support Operating
Systems <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html#supported-distributions>`__
and ensure the system is installed with one of the supported Linux
distributions. Other distributions may not be able to run ROCm or
complete the validation tests listed in this document.

To obtain and validate the Linux distribution information for systems
with the OS already installed, refer to the `Installation
Prerequisites <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html>`__
for ROCm.

2.3 GRUB Settings
-----------------

GRUB, or GNU Grand Unified Bootloader, is a boot loader and boot manager
for Linux that allows the operator to select which operating system and
kernel configuration to use when booting the system. MI300X based
servers require appending strings to the Linux command line and this is
done in the GRUB configuration file as described in the recommended
`GRUB
settings <https://rocm.docs.amd.com/en/latest/how-to/system-optimization/mi300x.html#mi300x-grub-settings>`__
for MI300X. After updating GRUB and rebooting the system, it is
recommended to check the GRUB configuration file before proceeding.

2.4 Operating System Settings
-----------------------------

To ensure the system is operating at maximum performance prior to
running the validations and performance tests in this document, the
operator should ensure that power gating is disabled, NUMA configuration
is set appropriately, and specific environment variables are exported as
outlined in the `Operating System
Settings <https://rocm.docs.amd.com/en/latest/how-to/system-optimization/mi300x.html#mi300x-os-settings>`__
for MI300X. For the purposes of illustration, in all the sections to
follow the commands and their output shown, are for Ubuntu 22.04 Linux
unless otherwise specified.

2.5 Updating System Firmware
----------------------------

Ensure that the system under test is running the latest firmware
versions by contacting your system manufacturer. Systems with older
firmware versions may not fully be validated, and performance or
functionality could be sub-optimal.

2.6 ROCm Installation
---------------------

Once the system is properly configured, ROCm software can be installed.
Prior to validating the system, ensure that ROCm 6.2 or greater is
installed. For maximum performance and functionality, it is recommended
to always install the latest version of ROCm on the system.

Refer to `ROCm Installation for
Linux <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/index.html>`__
for the available options to install ROCm on your system. For operators
new to ROCm, please refer to the `Quick Start Installation
Guide <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html>`__
for your supported distribution. Once ROCm is installed, it is
recommended to follow the `Post-Installation
Instructions <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html>`__.
To troubleshoot issues encountered when installing ROCm tools or
libraries, please refer to the `Installation
Troubleshooting <https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/install-faq.html>`__
guide.

To check the ROCm version running on the system after installation, run
the following command.

:mark:`cat /opt/rocm/.info/version`

An example output log is given below. In this case, the system has ROCm
version 6.2.0-66

:mark:`6.2.0-66`

**NOTE:** Contact your system manufacturer support representative to
ensure this version of ROCm installed is compatible with the system
firmware.

Chapter 3: Basic System Health Checks
=====================================

Prior to proceeding to more extensive system validation, it is important
to ensure all components in the system are operating at peak performance
and bandwidth.

A typical MI300X based GPU server architecture consists of:

- Host CPUs: Usually dual socket, handling general processing and
  orchestrating tasks.

- Memory: DRAM attached to each CPU socket for fast data access.

- GPUs: Multiple GPUs connected over AMD Infinity Fabric Link for
  parallel processing and acceleration.

- HBM3 Memory: attached to GPUs through I/O Die (IOD)

- Storage: High-speed NVMe SSDs or traditional HDDs for data storage.

- Networking: High-bandwidth network interfaces like 100-400GbE or
  InfiniBand for fast data transfer between systems.

The CPUs, memory, GPUs, storage, and networking components are
interconnected via high-speed communication paths, with PCIe lanes
facilitating data flow between CPUs and GPUs. This architecture allows
for efficient parallel processing and accelerated computation for AI,
HPC, and other demanding workloads.

This section covers the basic system checks for the MI300X GPU
Accelerators connected in the system using:

- Basic Linux system commands: cat, dmesg, lsmem, and lspci

- ROCm Monitoring Tool: amd-smi

**NOTE: Checking the health of other components in the system is outside
the scope of this document.**

After the system boots, run the following commands listed in the
sections below. For each command, an example output is provided. Expect
to observe similar output when these commands are executed on the System
Under Test (SUT). For illustration purposes, commands and the output
shown below were obtained from a system running Ubuntu 22.04, which is
one of the supported distributions for ROCm 6.2 at the time of release
of this guide. Running other supported distributions on the SUT may
result in slightly different output.

3.1 Check OS and host system checks
-----------------------------------

The following sub-sections lists items to check for the operating system
and host CPU and memory checks. For each, a sample command along with
corresponding log output is shown. The sample output provides typical
results and serves as a guideline.

**NOTE:** If results vary from the sample expected output, contact your
system manufacturer support representative for further assistance.

3.1.1 Check OS distribution (os-release)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the OS distribution installed on the SUT using the following
command.

:mark:`cat /etc/os-release`

An example of the output is given below. The output may vary based on
the OS distribution running.

:mark:`VERSION="22.04.4 LTS (Jammy Jellyfish)"`

Ensure that the OS distribution used is listed in the AMD’s ROCm
`Compatibility
matrix <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html>`__
page or in `Past versions of ROCm compatibility
matrix <https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html#past-rocm-compatibility-matrix>`__
page.

Result:

- PASSED: VERSION is listed in the compatibility matrix page.

- FAILED: Not listed in the compatibility matrix page.

  - Action: If the operating system distribution is not listed in the
    compatibility matrix pages, do not continue with the following
    steps. Instead, install a supported distribution and then proceed
    with the installation of ROCm 6.2 or a newer version.

3.1.2 Check kernel boot arguments (cmdline)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Correct boot arguments must be utilized by the Linux kernel during the
startup of the System Under Test (SUT). Once the system has booted, run
the following command in the terminal to display the boot arguments:

Command:

:mark:`cat /proc/cmdline`

An example of the output from an AMD CPU based system is given below
with the required boot parameters highlighted in yellow. Output may vary
based on OS distribution and GRUB settings. When using Intel host
processors, replace *amd_iommu* with *intel_iommu*

:mark:`BOOT_IMAGE=/boot/vmlinuz-6.8.0-40-generic
root=UUID=372435f6-bb80-4d82-83ed-c4d077dc5e23 ro pci=realloc=off
amd_iommu=on iommu=pt`

Result:

- PASSED: If output displays the following settings:

  - *pci=realloc=off*

  - *amd_iommu=on OR intel_iommu=on*

    - Be sure to use the parameter appropriate for the host CPU used

  - *iommu=pt*

- FAILED: otherwise

  - Action: Don’t proceed further. Updated the GRUB settings of the SUT
    and reboot, and then start the acceptance testing from this section.
    Note that if pci=realloc=off is not in GRUB configuration in Ubuntu
    distribution, not all GPUs may be recognized.

3.1.3 Check for driver errors (dmesg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following command to check for driver errors in the Linux OS
diagnostic messages (dmesg).

:mark:`sudo dmesg –T \| grep amdgpu \| grep -i error`

The expected output should be return no results (null).

Result:

- PASSED: Null

- FAILED: Errors reported

  - Action: Don’t proceed further. Reinstall amdgpu driver and then
    start the acceptance testing from this section.

3.1.4 Check for available memory (lsmem)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confirm there is at least 1.5T of memory in the system.

Command:

:mark:`lsmem \| grep "Total online memory"`

Expected output:

:mark:`Total online memory: 1.5T`

Warning:

If the available memory is less than 1.5T, the system may not function
properly when a large workload is run. But you can continue to next
check.

3.2 Check GPU Presence (lspci)
------------------------------

Confirm all GPU accelerators are present and available on the PCIe bus
by running the following command.

:mark:`lspci \| grep MI300X`

The following is an example of the output.

:mark:`05:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`26:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`46:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`65:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`85:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`a6:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`c6:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

:mark:`e5:00.0 Processing accelerators: Advanced Micro Devices, Inc.
[AMD/ATI] Aqua Vanjaram [Instinct MI300X]`

Result:

- PASSED: If all 8 GPUs are found shown above

- FAILED: otherwise

  - Action:

    - Don’t proceed further. Adjust GRUB configuration to ensure
      *pci=realloc=off* is present.

    - Reboot and rerun the above command to confirm all eight GPUs are
      shown.

    - If the issue persists despite previous attempts, verify that the
      torque applied to OAMs meets required specification.

    - If adjusting the torque does not resolve the problem, contact your
      system manufacturer for further assistance.

3.3 Check GPU link speed and width on PCIe bus (sudo lspci -vvv)
----------------------------------------------------------------

Confirm PCIe links to each of the GPUs are running at full speed and
width. Use the following lspci command with the highest verbosity mode
(-vvv) available and designating the vendor ID=1002 with device
ID=0x74a1 and grep for device status (DevSta) and link status (LnkSta):

Command:

:mark:`sudo lspci -d 1002:74a1 -vvv \| grep -e DevSta -e LnkSta`

Expected output:

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

:mark:`**DevSta**: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr-
TransPend-`

:mark:`**LnkSta**: Speed 32GT/s, Width x16`

Result:

- PASSED: Each output line must have:

  - LinkSta displays link speed is 32GT/s and width is x16, and

  - FatalErr+ is not displayed

- FAILED: If FatalErr+ is present

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

3.4 Monitoring Utilization Metrics (amd-smi)
--------------------------------------------

The amd-smi monitor command-line tool, typically installed with ROCm,
can be used to monitor AMD GPU hardware, including thermal, power,
hardware performance along with error reporting. The amd-smi can be run
in parallel with the validation tests outlined in this guide to provide
additional information on the operation of the system. See `Getting to
Know Your GPU: A Deep Dive into AMD
SMI <https://rocm.blogs.amd.com/software-tools-optimization/amd-smi-overview/README.html>`__
for details on this tool.

**NOTE:** This check requires that ROCm be installed on the SUT. The
monitoring tool rocm-smi may alternatively be used.

Run the following command to display GPU metrics when the system is idle
i.e. not running any workload.

:mark:`amd-smi monitor -putm`

An output similar to the following will be displayed. Please note that
the results will vary when the system is running a workload.

:mark:`GPU POWER GPU_TEMP MEM_TEMP **GFX_UTIL** **GFX_CLOCK**
**MEM_UTIL** **MEM_CLOCK**`

:mark:`0 125 W 37 °C 32 °C 0 % 158 MHz 0 % 900 MHz`

:mark:`1 121 W 36 °C 28 °C 0 % 139 MHz 0 % 900 MHz`

:mark:`2 124 W 39 °C 29 °C 0 % 141 MHz 0 % 900 MHz`

:mark:`3 122 W 36 °C 28 °C 0 % 158 MHz 0 % 900 MHz`

:mark:`4 125 W 40 °C 32 °C 0 % 140 MHz 0 % 900 MHz`

:mark:`5 124 W 36 °C 29 °C 0 % 139 MHz 0 % 900 MHz`

:mark:`6 124 W 38 °C 31 °C 0 % 139 MHz 0 % 900 MHz`

:mark:`7 122 W 37 °C 29 °C 0 % 142 MHz 0 % 900 MHz`

When the system is idle, the GPU’s utilization (GFX_UTIL) and memory
utilization (MEM_UTIL) will be 0%. The frequency of the GPU clock
(GFX_CLOCK) will be throttled back to under 200MHz and memory
(MEM_CLOCK) throttled down to 900 MHz. The GPU temperature (GPU_TEMP)
should also be well under 85°C when idle.

Result for an idle system:

- PASSED: When the system is idle, the GPU’s utilization (GFX_UTIL) and
  memory utilization (MEM_UTIL) should be 0%, the frequency of the GPU
  clock (GFX_CLOCK) throttled back to under 200 MHz, memory (MEM_CLOCK)
  throttled down to 900 MHz, and GPU Temperature (GPU_TEMP) should also
  be well under 85°C.

- FAILED: Otherwise

  - Action: Check the data center ambient temp and system fan speed.
    Power cycle the system. If the issue persists, report this issue to
    your system manufacturer.

3.5 Check the System Kernel Logs for Other Errors (dmesg)
---------------------------------------------------------

The command line utility *dmesg* prints boot-time message and on-going
kernel event messages about the state of the system hardware and
drivers. The utility is useful for capturing diagnostic information for
troubleshooting hardware and driver issues.

To check for errors in the kernel messages, use the following command:

:mark:`sudo dmesg -T \| grep -i 'error\\|warn\\|fail\\|exception'`

Expected output:

When system is operating without errors, warnings, or failures, the
output of the command will be null.

Result:

- PASSED: The output will be null, when the system is running properly

- FAILED: Otherwise

  - Action: Don’t proceed further. Analyze each *dmesg*
    error/fail/exception

Refer to `Appendix C Collecting
Logs <#pappendix-c-collecting-logs-rocm_techsupport.sh>`__ for
information on the rocm_techsupport.sh script utility from AMD which
collect system logs for purpose of support and troubleshooting.

Chapter 4: System Validation Tests
==================================

The validation tests in this section are intended to ensure that a
system is operating correctly as expected. In this section, ROCm
Validation Suite (rvs) is used which is a collection of tests,
benchmarks, and qualification tools, each targeting a specific subsystem
of the SUT.

| If not already installed on the SUT, run the following install command
  (Ubuntu):
| :mark:`sudo apt install rocm-validation-suite`

Then ensure that the path to the rvs executable, located at
:mark:`/opt/rocm/bin`\ **,** is added to the path. Use the following
command:

:mark:`export PATH=$PATH:/opt/rocm/bin`

The rvs tool consists of modules (each module implements a particular
test functionality). The collection of the modules can be broadly
categorized as targeting the following aspects of the hardware platform:

- Compute / GPU

- Memory

- IO / PCIe

Each *category* listed above runs a subset of rvs modules to validate
that the category is working as expected. The standard way to run an rvs
module is by providing a configuration file prefixed with the -c option.
When rvs is installed properly on the SUT, the **conf** files are found
in the following folder:

:mark:`/opt/rocm/share/rocm-validation-suite/conf/`

Since this path is a part of every rvs command in this document, an
environment variable is defined which will be used in place of the long
path for commands and their output. To set this variable in the
environment, run the following command:

:mark:`export RVS_CONF=/opt/rocm/share/rocm-validation-suite/conf`

The configuration files section of the `ROCm Validation Suite User
Guide <https://github.com/ROCm/ROCmValidationSuite/blob/master/docs/ug1main.md#configuration-files>`__
provides detailed description about the conf file, it’s formation, and
keys. It is advisable to become familiar with the conf file format
before running the rvs tests described below. Be aware, some conf files
are included in product specific sub-folders (i.e.
:mark:`=/opt/rocm/share/rocm-validation-suite/conf/MI300X`). If present,
always use GPU specific configurations instead of default test
configurations.

In the following subsections, under each of the categories, the relevant
rvs test modules are listed along with descriptions how the category is
validated. Example rvs commands with the expected output are also
provided. Most of the rvs tests do not have strict PASS / FAIL
conditions reported, rather it is expected that when they are run on the
SUT, the output observed are within a reasonable range provided.

4.1 Compute / GPU
-----------------

The rvs has three different *types* of modules to validate the Compute
subsystem. These are:

- Properties

- Benchmark / Stress / Qualification

- Monitor

MI300X GPU accelerators have many architectural features. Similar to
section `3.2 Check GPU Presence (lspci) <#_3.2_Check_GPU>`__, rvs has an
option to display all MI300X GPU accelerators present in the SUT. Before
proceeding with the modules below, run the following command to make
sure all the GPUs are seen with their correct PCIe properties.

Command:

:mark:`rvs -g`

Expected output:

:mark:`ROCm Validation Suite (version 0.0.60202)`

:mark:`Supported GPUs available:`

:mark:`0000:05:00.0 - GPU[ 2 - 28851] AMD Instinct MI300X (Device
29857)`

:mark:`0000:26:00.0 - GPU[ 3 - 23018] AMD Instinct MI300X (Device
29857)`

:mark:`0000:46:00.0 - GPU[ 4 - 29122] AMD Instinct MI300X (Device
29857)`

:mark:`0000:65:00.0 - GPU[ 5 - 22683] AMD Instinct MI300X (Device
29857)`

:mark:`0000:85:00.0 - GPU[ 6 - 53458] AMD Instinct MI300X (Device
29857)`

:mark:`0000:a6:00.0 - GPU[ 7 - 63883] AMD Instinct MI300X (Device
29857)`

:mark:`0000:c6:00.0 - GPU[ 8 - 53667] AMD Instinct MI300X (Device
29857)`

:mark:`0000:e5:00.0 - GPU[ 9 - 63738] AMD Instinct MI300X (Device
29857)`

Result:

- PASSED: All 8 GPUs are seen in the output

- FAILED: Otherwise

  - Action: Don’t proceed further. Debug the issue of not being able to
    see all GPUs.

4.1.1 Properties 
~~~~~~~~~~~~~~~~~

The GPU Properties module queries the configuration of a targeted GPU
and returns the device’s static characteristics. These static values can
be used to debug issues such as device support, performance and firmware
problems.

To confirm the architectural properties of the GPU, use the GPUP module
which makes use of the GPUP configuration file.

The configuration file for GPUP module is located at:

:mark:`{RVS_CONF}/gpup_single.conf`

The GPUP module section of the `ROCm Validation Suite User
Guide <https://github.com/ROCm/ROCmValidationSuite/blob/master/docs/ug1main.md#gpup-module>`__
provides detailed description about the GPUP conf file, it’s formation,
and keys.

Command:

:mark:`rvs -c ${RVS_CONF}/gpup_single.conf`

Expected output (truncated):

The conf file has six test cases RVS-GPUP-TC1,
RVS-GPUP-TC2,..,RV-GPUP-TC6. Only truncated version of output of
RVS-GPUP-TC1 is shown here. The other tests are modified versions of
RVS-GPUP-TC1 which display a subset of properties and/or a subset of
io_links-properites.

The first block of output displays the properties (all):

:mark:`[RESULT] [ 54433.732433] Action name :RVS-GPUP-TC1`

:mark:`[RESULT] [ 54433.733858] Module name :gpup`

:mark:`[RESULT] [ 54433.733992] [RVS-GPUP-TC1] gpup 28851
cpu_cores_count 0`

:mark:`[RESULT] [ 54433.733994] [RVS-GPUP-TC1] gpup 28851 simd_count
1216`

:mark:`...`

:mark:`[RESULT] [ 54433.734018] [RVS-GPUP-TC1] gpup 28851 num_xcc 8`

:mark:`[RESULT] [ 54433.734018] [RVS-GPUP-TC1] gpup 28851
max_engine_clk_ccompute 3250`

The block below shows only one of the io_link-properties of the eight
GPUs (0 to 7):

:mark:`[RESULT] [ 96878.647964] [RVS-GPUP-TC1] gpup 28851 0 type 2`

:mark:`[RESULT] [ 96878.647973] [RVS-GPUP-TC1] gpup 28851 0
version_major 0`

:mark:`[RESULT] [ 96878.647982] [RVS-GPUP-TC1] gpup 28851 0
version_minor 0`

:mark:`[RESULT] [ 96878.647990] [RVS-GPUP-TC1] gpup 28851 0 node_from 2`

:mark:`[RESULT] [ 96878.647997] [RVS-GPUP-TC1] gpup 28851 0 node_to 0`

:mark:`[RESULT] [ 96878.648013] [RVS-GPUP-TC1] gpup 28851 0 weight 20`

:mark:`[RESULT] [ 96878.648020] [RVS-GPUP-TC1] gpup 28851 0 min_latency
0`

:mark:`[RESULT] [ 96878.648029] [RVS-GPUP-TC1] gpup 28851 0 max_latency
0`

:mark:`[RESULT] [ 96878.648037] [RVS-GPUP-TC1] gpup 28851 0
min_bandwidth 312`

:mark:`[RESULT] [ 96878.648045] [RVS-GPUP-TC1] gpup 28851 0
max_bandwidth 64000`

:mark:`[RESULT] [ 96878.648053] [RVS-GPUP-TC1] gpup 28851 0
recommended_transfer_size 0`

:mark:`[RESULT] [ 96878.648060] [RVS-GPUP-TC1] gpup 28851 0 flags 1`

Result:

- PASSED: If generated output looks similar

- FAILED: If any GPU is not listed in output or we see ERROR tagged logs

  - Typically, it is not expected that this module will fail

4.1.2 Benchmark / Stress / Qualification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These categories of modules perform qualification of the GPU subsystem,
execute stress test, and compute and display bandwidth. The modules do
not produce a PASS / FAIL result. When bandwidth is measured it only
reports the bandwidth and doesn’t make any comparisons with existing set
of numbers. Only exceptions are GST and IET modules.

4.1.2.1 Benchmark
^^^^^^^^^^^^^^^^^

The GPU Stress Test (GST) module stresses the GPU FLOPS performance for
SGEMM, DGEMM and HGEMM operations and computes and displays peak
GFLOPs/s. Two configuration files are used by the GST module – one is
general purpose (gst_single.conf), and the other is MI300X specific
(gst_ext.conf). Each is detailed below.

The MI300X specific gst_single.conf configuration file for the GST
module is located at:

:mark:`${RVS_CONF}/MI300X/gst_single.conf`

Run the following command to perform the general GPU stress test using
the gst_single.conf config file.

Command:

:mark:`rvs -c ${RVS_CONF}/MI300X/gst_single.conf`

Expected output (truncated):

:mark:`[RESULT] [1101980.682169] Action name
:gst-1215Tflops-4K4K8K-rand-fp8`

:mark:`[RESULT] [1101980.683973] Module name :gst`

:mark:`[RESULT] [1101980.836841] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] Start of GPU ramp up`

:mark:`[RESULT] [1101987.830800] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1539705`

:mark:`[RESULT] [1101988.831928] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] End of GPU ramp up`

:mark:`[RESULT] [1101992.16545 ] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1640057`

:mark:`[RESULT] [1101995.85574 ] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1595462`

:mark:`[RESULT] [1101998.181333] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1687129`

:mark:`[RESULT] [1102001.278962] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1686102`

:mark:`[RESULT] [1102003.864611] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1687129`

:mark:`[RESULT] [1102003.864648] [gst-1215Tflops-4K4K8K-rand-fp8] [GPU::
28851] GFLOPS 1687129 Target GFLOPS: 1215000 met: TRUE`

:mark:`...`

Result:

- PASSED: If “met: TRUE” is displayed in test log for all eight GPUs and
  actions, it indicates the test was able to hit peak GFLOP/s which
  matches or exceeds the target values listed in the config file.

- FAILED: Test results fail to meet the target GFLOP/s

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

The MI300X specific gst_ext.conf configuration file for the GST module
is located at:

:mark:`${RVS_CONF}/MI300X/gst_ext.conf`

Run the following command to perform the MI300X GPU specific stress test
using the gst_ext.conf config file.

Command:

:mark:`ROCBLAS_TENSILE_LIBPATH=/opt/rocm/lib/rocblas/library/ rvs -c
${RVS_CONF}/MI300X/gst_ext.conf`

Expected output (truncated):

:mark:`[RESULT] [603545.521766] Action name
:gst-1000Tflops-8KB-fp8_r-false`

:mark:`[RESULT] [603545.523245] Module name :gst`

:mark:`[RESULT] [603545.685745] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] Start of GPU ramp up`

:mark:`[RESULT] [603552.11787 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235406`

:mark:`[RESULT] [603553.12495 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1250866`

:mark:`[RESULT] [603554.12557 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235406`

:mark:`[RESULT] [603555.12386 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] End of GPU ramp up`

:mark:`[RESULT] [603556.12907 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1220772`

:mark:`[RESULT] [603557.13180 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1221056`

:mark:`[RESULT] [603558.13786 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1238206`

:mark:`[RESULT] [603559.13885 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1231140`

:mark:`[RESULT] [603560.14584 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1232638`

:mark:`[RESULT] [603561.14988 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1237375`

:mark:`[RESULT] [603562.15658 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1237069`

:mark:`[RESULT] [603563.16277 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1237102`

:mark:`[RESULT] [603564.16494 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1236422`

:mark:`[RESULT] [603565.17256 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1236946`

:mark:`[RESULT] [603566.17565 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1236323`

:mark:`[RESULT] [603567.17654 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235515`

:mark:`[RESULT] [603568.17924 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235281`

:mark:`[RESULT] [603569.18070 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235452`

:mark:`[RESULT] [603570.18519 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1235085`

:mark:`[RESULT] [603571.18960 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1234038`

:mark:`[RESULT] [603572.19046 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1234418`

:mark:`[RESULT] [603573.19153 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1234417`

:mark:`[RESULT] [603574.19692 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1233895`

:mark:`[RESULT] [603575.20205 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1233942`

:mark:`[RESULT] [603576.20336 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1233328`

:mark:`[RESULT] [603577.20441 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1233327`

:mark:`[RESULT] [603578.21167 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1233693`

:mark:`[RESULT] [603579.21800 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1231561`

:mark:`[RESULT] [603580.22072 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1232009`

:mark:`[RESULT] [603581.22249 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1232113`

:mark:`[RESULT] [603582.22852 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1232700`

:mark:`[RESULT] [603583.23573 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1232620`

:mark:`[RESULT] [603584.23655 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1231152`

:mark:`[RESULT] [603585.12439 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1238206`

:mark:`[RESULT] [603585.12457 ] [gst-1000Tflops-8KB-fp8_r-false] [GPU::
28851] GFLOPS 1238206 Target GFLOPS: 1000000 met: TRUE`

:mark:`…`

Result:

- PASSED: If “met: TRUE” is displayed in the test log for all eight
  GPUs, it indicates the test was able to hit peak GFLOP/s which matches
  or exceeds the target values listed in the config file.

- FAILED: Test results fail to meet the target GFLOP/s

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

- 

4.1.2.2 Stress
^^^^^^^^^^^^^^

The Input Energy Delay Product (EDPp) test (IET) module runs GEMM
workloads to stress the GPU power, i.e. Total Graphics Power (TGP).

This test is used to:

- Verify the GPU is capable of handling maximum power stress for a
  sustained period.

- Check that the GPU power reaches a set target power.

The configuration file for IET module is located at:

:mark:`{RVS_CONF}/MI300X/iet_single.conf`

Command:

:mark:`rvs -c ${RVS_CONF}/MI300X/iet_single.conf`

IET module run six different actions. Each action will be performed on
all eight GPUs. Each GPU power test will display TRUE or FALSE status as
shown in the following output example.

Expected output (truncated):

:mark:`[RESULT] [1102597.157090] Action name :iet-620W-1K-rand-dgemm`

:mark:`[RESULT] [1102597.159274] Module name :iet`

:mark:`[RESULT] [1102597.333747] [iet-620W-1K-rand-dgemm] [GPU:: 28851]
Power(W) 127.000000`

:mark:`[RESULT] [1102597.334457] [iet-620W-1K-rand-dgemm] [GPU:: 23018]
Power(W) 123.000000`

:mark:`[RESULT] [1102597.334500] [iet-620W-1K-rand-dgemm] [GPU:: 22683]
Power(W) 123.000000`

:mark:`...`

:mark:`[RESULT] [1102657.372824] [iet-620W-1K-rand-dgemm] [GPU:: 29122]
pass: TRUE`

:mark:`[RESULT] [1102657.372859] [iet-620W-1K-rand-dgemm] [GPU:: 23018]
pass: TRUE`

:mark:`[RESULT] [1102657.372936] [iet-620W-1K-rand-dgemm] [GPU:: 28851]
pass: TRUE`

:mark:`[RESULT] [1102657.373301] [iet-620W-1K-rand-dgemm] [GPU:: 53458]
pass: TRUE`

:mark:`[RESULT] [1102657.373508] [iet-620W-1K-rand-dgemm] [GPU:: 63738]
pass: TRUE`

:mark:`[RESULT] [1102657.373620] [iet-620W-1K-rand-dgemm] [GPU:: 63883]
pass: TRUE`

:mark:`[RESULT] [1102657.374090] [iet-620W-1K-rand-dgemm] [GPU:: 22683]
pass: TRUE`

:mark:`[RESULT] [1102657.374158] [iet-620W-1K-rand-dgemm] [GPU:: 53667]
pass: TRUE`

:mark:`[RESULT] [1102658.379728] Action name
:iet-wait-750W-28K-rand-dgemm`

:mark:`[RESULT] [1102658.379781] Module name :iet`

Result:

- PASSED: The phrase “pass: TRUE” must be displayed for each GPU.

- FAILED: Test results FAIL

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

4.1.2.3 Qualification
^^^^^^^^^^^^^^^^^^^^^

The GPU monitor (GM) module is used to report and validate the following
system attributes.

- Temperature

- Fan speed

- Memory clock

- System clock

- Power

The configuration file for GST module is located at:

:mark:`{RVS_CONF}/gm_single.conf`

Command:

:mark:`rvs -c ${RVS_CONF}/gm_single.conf`

Expected output (truncated):

:mark:`[RESULT] [209228.305186] [metrics_monitor] gm 28851 temp
violations 0`

:mark:`[RESULT] [209228.305186] [metrics_monitor] gm 28851 clock
violations 0`

:mark:`[RESULT] [209228.305186] [metrics_monitor] gm 28851 mem_clock
violations 0`

:mark:`[RESULT] [209228.305186] [metrics_monitor] gm 28851 fan
violations 0`

:mark:`[RESULT] [209228.305186] [metrics_monitor] gm 28851 power
violations 0`

:mark:`...`

Result:

- PASSED: If the output displays “violations 0” for all give attributes
  for each GPU. Pipe output to grep to create a quick summary of
  violations.

- FAILED: If any violations have a non-zero value

  - Action: Continue with the next step but periodically monitor by
    running this module.

4.2 Memory
----------

To validate the GPU memory subsystem, rvs has the following two *types*
of modules:

- MEM

- BABEL

4.2.1 MEM
~~~~~~~~~

The Memory module, MEM, tests the GPU memory for hardware errors and
soft errors using HIP. It consists of various tests that use algorithms
like Walking 1 bit, Moving inversion and Modulo 20. The module executes
the following memory tests [Algorithm, data pattern]:

- Walking 1 bit

- Own address test

- Moving inversions, ones & zeros

- Moving inversions, 8 bit pattern

- Moving inversions, random pattern

- Block move, 64 moves

- Moving inversions, 32 bit pattern

- Random number sequence

- Modulo 20, random pattern

- Memory stress test

The configuration file for GST module is located at:

:mark:`{RVS_CONF}/mem.conf`

Command:

:mark:`rvs -c ${RVS_CONF}/mem.conf -l mem.txt`

The entire output file is not shown here for brevity. Performing grep
for certain string(s) in the file where the log is saved makes it easier
to understand the log. The “-l mem.txt” option in the command line dumps
the entire output into the file.

Performing grep for the string “mem Test 1:” shows, Test 1 (Change one
bit memory address) is launched for each GPU.

:mark:`grep "mem Test 1:" mem.txt`

:mark:`[RESULT] [214775.925788] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214776.112738] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214776.299030] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214776.486354] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214776.674529] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214776.865057] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214777.52685 ] [action_1] mem Test 1: Change one bit
memory addresss`

:mark:`[RESULT] [214777.155703] [action_1] mem Test 1: Change one bit
memory addresss`

Performing grep for the string “mem Test 1 :” shows, Test 1 passed for
all GPUs.

:mark:`[RESULT] [214775.947349] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214776.134798] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214776.320838] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214776.509205] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214776.697979] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214776.888054] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214777.75572 ] [action_1] mem Test 1 : PASS`

:mark:`[RESULT] [214777.178653] [action_1] mem Test 1 : PASS`

Similarly, other string(s) can be used to parse the log file easily.

Performing grep for the string “bandwidth” shows the memory bandwidth
perceived by each of the eight GPUs.

:mark:`grep "bandwidth" mem.txt`

:mark:`[RESULT] [214808.291036] [action_1] mem Test 11: elapsedtime =
6390.423828 bandwidth = 2003.017090GB/s`

:mark:`[RESULT] [214812.175895] [action_1] mem Test 11: elapsedtime =
6387.198242 bandwidth = 2004.028564GB/s`

:mark:`[RESULT] [214813.999085] [action_1] mem Test 11: elapsedtime =
6400.554199 bandwidth = 1999.846802GB/s`

:mark:`[RESULT] [214814.406234] [action_1] mem Test 11: elapsedtime =
6397.101074 bandwidth = 2000.926392GB/s`

:mark:`[RESULT] [214814.583630] [action_1] mem Test 11: elapsedtime =
6388.572266 bandwidth = 2003.597534GB/s`

:mark:`[RESULT] [214815.176800] [action_1] mem Test 11: elapsedtime =
6378.345703 bandwidth = 2006.810059GB/s`

:mark:`[RESULT] [214815.384878] [action_1] mem Test 11: elapsedtime =
6404.943848 bandwidth = 1998.476196GB/s`

:mark:`[RESULT] [214815.419048] [action_1] mem Test 11: elapsedtime =
6416.849121 bandwidth = 1994.768433GB/s`

Result:

- PASSED: If all memory tests passed without memory errors and the
  bandwidth obtained in Test 11 is about ~2TB/s

- FAILED: If any memory errors report and/or the obtained bandwidth is
  not even close to 2TB/s

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

4.2.2 BABEL
~~~~~~~~~~~

Refer to section `5.4 BabelStream <#babelstream-benchmarking-results>`__
for instructions on how to run this module to test memory.

4.3 IO
------

To validate the GPU interfaces, rvs has the following three *types* of
modules:

- PEBB – PCIe Bandwidth Benchmark

- PEQT – PCIe Qualification Tool

- PBQT – P2P Benchmark and Qualification Tool

4.3.1 PEBB (PCIe Bandwidth Benchmark)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PCIe Bandwidth Benchmark attempts to saturate the PCIe bus with DMA
transfers between system memory and a target GPU card’s memory. The
maximum bandwidth obtained is reported.

The configuration file for GST module is located at:

:mark:`{RVS_CONF}/MI300X/pebb_single.conf`

Command:

:mark:`rvs -c ${RVS_CONF}/MI300X/pebb_single.conf -l pebb.txt`

Expected output (truncated):

The PEBB modules has the following tests (h2d=host to device, d2h=device
to host, xMB=random block size, b2b=back to back) defined in the conf
file:

- h2d-sequential-51MB

- d2h-sequential-51MB

- h2d-d2h-sequential-51MB

- h2d-parallel-xMB

- d2h-parallel-xMB

- h2d-d2h-xMB

- h2d-b2b-51MB

- d2h-b2b-51MB

- h2d-d2h-b2b-51MB

Each of these tests will produce the following header as part of the
output log. It shows the distances between CPUs and GPUs.

:mark:`[RESULT] [1103843.610745] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 2 - 28851 - 0000:05:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610763] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 2 - 28851 - 0000:05:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610771] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 3 - 23018 - 0000:26:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610778] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 3 - 23018 - 0000:26:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610787] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 4 - 29122 - 0000:46:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610795] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 4 - 29122 - 0000:46:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610802] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 5 - 22683 - 0000:65:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610810] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 5 - 22683 - 0000:65:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610817] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 6 - 53458 - 0000:85:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610825] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 6 - 53458 - 0000:85:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610833] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 7 - 63883 - 0000:a6:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610841] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 7 - 63883 - 0000:a6:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610848] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 8 - 53667 - 0000:c6:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610856] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 8 - 53667 - 0000:c6:00.0] distance:20 PCIe:20`

:mark:`[RESULT] [1103843.610863] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 0] [GPU:: 9 - 63738 - 0000:e5:00.0] distance:52 PCIe:52`

:mark:`[RESULT] [1103843.610871] [d2h-sequential-64MB] pcie-bandwidth
[CPU:: 1] [GPU:: 9 - 63738 - 0000:e5:00.0] distance:20 PCIe:20`

The other half of the output for each of the tests, shows the transfer
bandwidth and indicates whether its bidirectional or unidirectional
transfer.

:mark:`[RESULT] [1103903.617888] [d2h-sequential-64MB] pcie-bandwidth [
1/16] [CPU:: 0] [GPU:: 2 - 28851 - 0000:05:00.0] h2d::false d2h::true
56.298 GBps ...`

:mark:`[RESULT] [1103903.617971] [d2h-sequential-64MB] pcie-bandwidth [
2/16] [CPU:: 1] [GPU:: 2 - 28851 - 0000:05:00.0] h2d::false d2h::true
55.664 GBps ...`

:mark:`[RESULT] [1103903.617982] [d2h-sequential-64MB] pcie-bandwidth [
3/16] [CPU:: 0] [GPU:: 3 - 23018 - 0000:26:00.0] h2d::false d2h::true
56.304 GBps ...`

:mark:`[RESULT] [1103903.617993] [d2h-sequential-64MB] pcie-bandwidth [
4/16] [CPU:: 1] [GPU:: 3 - 23018 - 0000:26:00.0] h2d::false d2h::true
56.318 GBps ...`

:mark:`[RESULT] [1103903.618009] [d2h-sequential-64MB] pcie-bandwidth [
5/16] [CPU:: 0] [GPU:: 4 - 29122 - 0000:46:00.0] h2d::false d2h::true
56.318 GBps ...`

:mark:`[RESULT] [1103903.618019] [d2h-sequential-64MB] pcie-bandwidth [
6/16] [CPU:: 1] [GPU:: 4 - 29122 - 0000:46:00.0] h2d::false d2h::true
56.273 GBps ...`

:mark:`[RESULT] [1103903.618029] [d2h-sequential-64MB] pcie-bandwidth [
7/16] [CPU:: 0] [GPU:: 5 - 22683 - 0000:65:00.0] h2d::false d2h::true
56.297 GBps ...`

:mark:`[RESULT] [1103903.618039] [d2h-sequential-64MB] pcie-bandwidth [
8/16] [CPU:: 1] [GPU:: 5 - 22683 - 0000:65:00.0] h2d::false d2h::true
55.592 GBps ...`

:mark:`[RESULT] [1103903.618052] [d2h-sequential-64MB] pcie-bandwidth [
9/16] [CPU:: 0] [GPU:: 6 - 53458 - 0000:85:00.0] h2d::false d2h::true
56.293 GBps ...`

:mark:`[RESULT] [1103903.618063] [d2h-sequential-64MB] pcie-bandwidth
[10/16] [CPU:: 1] [GPU:: 6 - 53458 - 0000:85:00.0] h2d::false d2h::true
56.337 GBps ...`

:mark:`[RESULT] [1103903.618072] [d2h-sequential-64MB] pcie-bandwidth
[11/16] [CPU:: 0] [GPU:: 7 - 63883 - 0000:a6:00.0] h2d::false d2h::true
56.298 GBps ...`

:mark:`[RESULT] [1103903.618083] [d2h-sequential-64MB] pcie-bandwidth
[12/16] [CPU:: 1] [GPU:: 7 - 63883 - 0000:a6:00.0] h2d::false d2h::true
56.325 GBps ...`

:mark:`[RESULT] [1103903.618116] [d2h-sequential-64MB] pcie-bandwidth
[13/16] [CPU:: 0] [GPU:: 8 - 53667 - 0000:c6:00.0] h2d::false d2h::true
56.311 GBps ...`

:mark:`[RESULT] [1103903.618124] [d2h-sequential-64MB] pcie-bandwidth
[14/16] [CPU:: 1] [GPU:: 8 - 53667 - 0000:c6:00.0] h2d::false d2h::true
56.340 GBps ...`

:mark:`[RESULT] [1103903.618134] [d2h-sequential-64MB] pcie-bandwidth
[15/16] [CPU:: 0] [GPU:: 9 - 63738 - 0000:e5:00.0] h2d::false d2h::true
56.287 GBps ...`

:mark:`[RESULT] [1103903.618142] [d2h-sequential-64MB] pcie-bandwidth
[16/16] [CPU:: 1] [GPU:: 9 - 63738 - 0000:e5:00.0] h2d::false d2h::true
56.334 GBps ...`

Result:

- PASSED: If all CPUs-GPUs distances are displayed and CPUx (x=0/1) to
  GPUy (y=2/3/4/5/6/7/8/9) PCIe transfer bandwidths are displayed.

- FAILED: Otherwise

  - Action: Proceed to next step. Run this same test later again.

4.3.2 PEQT (PCIe Qualification Tool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PCIe Qualification Tool is used to qualify the PCIe bus on which the
GPU is connected to. The qualification tool can determine the following
characteristics of the PCIe bus interconnect to a GPU:

- Support for Gen 3 atomic completers

- DMA transfer statistics

- PCIe link speed

- PCIe link width

The configuration file for peqt module is located at:

:mark:`{RVS_CONF}/peqt_single.conf`

Command:

:mark:`sudo rvs -c ${RVS_CONF}/peqt_single.conf`

| This module has total 17 tests (pcie_act_1 – pcie_act_17). Each test
  checks for a subset of PCIe capabilities and shows the true or false
  status.
| **Test needs sudo permission to run properly**

Expected output:

:mark:`[RESULT] [1105558.986882] Action name :pcie_act_1`

:mark:`[RESULT] [1105558.988288] Module name :peqt`

:mark:`[RESULT] [1105559.33461 ] [pcie_act_1] peqt true`

:mark:`[RESULT] [1105559.33492 ] Action name :pcie_act_2`

:mark:`[RESULT] [1105559.33497 ] Module name :peqt`

:mark:`[RESULT] [1105559.72308 ] [pcie_act_2] peqt true`

:mark:`[RESULT] [1105559.72325 ] Action name :pcie_act_3`

:mark:`[RESULT] [1105559.72330 ] Module name :peqt`

:mark:`[RESULT] [1105559.114937] [pcie_act_3] peqt true`

:mark:`[RESULT] [1105559.114957] Action name :pcie_act_4`

:mark:`[RESULT] [1105559.114962] Module name :peqt`

:mark:`[RESULT] [1105559.155511] [pcie_act_4] peqt true`

:mark:`[RESULT] [1105559.155526] Action name :pcie_act_5`

:mark:`[RESULT] [1105559.155531] Module name :peqt`

:mark:`[RESULT] [1105559.190472] [pcie_act_5] peqt true`

:mark:`[RESULT] [1105559.190491] Action name :pcie_act_6`

:mark:`[RESULT] [1105559.190495] Module name :peqt`

:mark:`[RESULT] [1105559.230632] [pcie_act_6] peqt true`

:mark:`[RESULT] [1105559.230646] Action name :pcie_act_7`

:mark:`[RESULT] [1105559.230651] Module name :peqt`

:mark:`[RESULT] [1105559.273512] [pcie_act_7] peqt true`

:mark:`[RESULT] [1105559.273534] Action name :pcie_act_8`

:mark:`[RESULT] [1105559.273538] Module name :peqt`

:mark:`[RESULT] [1105559.316290] [pcie_act_8] peqt true`

:mark:`[RESULT] [1105559.316305] Action name :pcie_act_9`

:mark:`[RESULT] [1105559.316310] Module name :peqt`

:mark:`[RESULT] [1105559.357042] [pcie_act_9] peqt true`

:mark:`[RESULT] [1105559.357064] Action name :pcie_act_10`

:mark:`[RESULT] [1105559.357069] Module name :peqt`

:mark:`[RESULT] [1105559.391754] [pcie_act_10] peqt true`

:mark:`[RESULT] [1105559.391767] Action name :pcie_act_11`

:mark:`[RESULT] [1105559.391771] Module name :peqt`

:mark:`[RESULT] [1105559.434373] [pcie_act_11] peqt true`

:mark:`[RESULT] [1105559.434391] Action name :pcie_act_12`

:mark:`[RESULT] [1105559.434395] Module name :peqt`

:mark:`[RESULT] [1105559.470072] [pcie_act_12] peqt true`

:mark:`[RESULT] [1105559.470087] Action name :pcie_act_13`

:mark:`[RESULT] [1105559.470091] Module name :peqt`

:mark:`[RESULT] [1105559.512754] [pcie_act_13] peqt true`

:mark:`[RESULT] [1105559.512774] Action name :pcie_act_14`

:mark:`[RESULT] [1105559.512778] Module name :peqt`

:mark:`[RESULT] [1105559.552761] [pcie_act_14] peqt true`

:mark:`[RESULT] [1105559.552779] Action name :pcie_act_15`

:mark:`[RESULT] [1105559.552783] Module name :peqt`

:mark:`[RESULT] [1105559.586778] [pcie_act_15] peqt true`

:mark:`[RESULT] [1105559.586794] Action name :pcie_act_16`

:mark:`[RESULT] [1105559.586798] Module name :peqt`

:mark:`[RESULT] [1105559.620305] [pcie_act_16] peqt true`

:mark:`[RESULT] [1105559.620322] Action name :pcie_act_17`

:mark:`[RESULT] [1105559.620326] Module name :peqt`

:mark:`[RESULT] [1105559.651564] [pcie_act_17] peqt true`

Result:

- PASSED: “[pcie_act_x] peqt true” can be seen for all 17 actions.

- FAILED: If any tests show true.

  - Action: Check that you are running this test as root or with sudo
    privileges. If not, actions 6 through 16 will fail. Run this same
    test later again.

4.3.3 PBQT (P2P Benchmark and Qualification Tool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PBQT module executes the following tests:

- List all GPUs that support P2P

- Characterizes the P2P links between peers

- Performs a peer-to-peer throughput test between all P2P pairs

The configuration file for the pbqt module for MI300X is located here:

:mark:`{RVS_CONF}/MI300X/pbqt_single.conf`

The conf file has 12 “actions_xy” test segments. Each of these, checks
for peer-to-peer connectivity among GPUs and provides a true/false
status. In addition, it also performs bidirectional throughput test and
reports the throughput obtained based on config parameters. Since
comparison is not performed for some target throughput numbers, there is
no PASS/FAIL condition for the overall test.

It is recommended to carefully review the pbqt_single.conf file before
running the following command.

Command:

:mark:`rvs -c ${RVS_CONF}/MI300X/pbqt_single.conf`

Only two example lines from the very long log file is shown because
other lines look similar as all combinations of GPU pairs are considered
and numbers for those pairs are reported.

Expected output below (truncated) shows uni-directional connectivity is
true for the GPU and its connection to the other seven GPU peers:

:mark:`[RESULT] [1104553.34268 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 3 - 23018 - 0000:26:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34276 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 4 - 29122 - 0000:46:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34280 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 5 - 22683 - 0000:65:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34283 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 6 - 53458 - 0000:85:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34289 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 7 - 63883 - 0000:a6:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34294 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 8 - 53667 - 0000:c6:00.0] peers:true
distance:15 xGMI:15`

:mark:`[RESULT] [1104553.34298 ] [p2p-unidir-sequential-64MB] p2p [GPU::
2 - 28851 - 0000:05:00.0] [GPU:: 9 - 63738 - 0000:e5:00.0] peers:true
distance:15 xGMI:15`

The following lines show unidirectional throughput between the 56 GPU
pairs (not all are shown):

:mark:`[RESULT] [1104673.143726] [p2p-unidir-parallel-64MB]
p2p-bandwidth[ 1/56] [GPU:: 2 - 28851 - 0000:05:00.0] [GPU:: 3 - 23018 -
0000:26:00.0] bidirectional: false 48.962 GBps duration: 1.462462 secs`

:mark:`[RESULT] [1104673.144823] [p2p-unidir-parallel-64MB]
p2p-bandwidth[ 2/56] [GPU:: 2 - 28851 - 0000:05:00.0] [GPU:: 4 - 29122 -
0000:46:00.0] bidirectional: false 48.914 GBps duration: 1.470746 secs`

:mark:`[RESULT] [1104673.145898] [p2p-unidir-parallel-64MB]
p2p-bandwidth[ 3/56] [GPU:: 2 - 28851 - 0000:05:00.0] [GPU:: 5 - 22683 -
0000:65:00.0] bidirectional: false 48.577 GBps duration: 1.480956 secs`

Result:

- PASSED: If “peers:true” lines are observed for GPUs peer-to-peer
  connectivity and if throughput values are non-zeros.

- FAILED: Otherwise

  - Action: Do not proceed further. Report this issue to your system
    manufacturer immediately.

Chapter 5: Performance Benchmarking
===================================

The benchmarking tests outlined in this chapter validate compute, IO,
and memory performance for all eight GPUs in a server system. The
benchmarking tests require ROCm installation - see section 2.6 ROCm
Installation for details. During the test, it is recommended to monitor
system utilization, power, and temperature using amd-smi, and check for
errors using lspci and dmesg as detailed in Chapter 2.

Benchmark tests in this section leverage and include instructions for
the following

- TransferBench

- ROCm Collective Communications Library
  (`RCCL <https://github.com/ROCm/rccl>`__)

- rocBLAS

- BabelStream

5.1 TransferBench Benchmarking Results 
---------------------------------------

TransferBench is a tool and utility for benchmarking copies between
user-specified CPU and GPU devices. For more information, see the
TransferBench
`documentation <https://rocm.docs.amd.com/projects/TransferBench/en/latest/index.html>`__
and `source code <https://github.com/ROCm/TransferBench>`__.

The system health benchmarks run 6 TransferBench tests from the `example
file <https://github.com/ROCm/TransferBench/blob/develop/examples/example.cfg>`__.
For reference, the six transfers are:

1. Single GPU-executed Transfer between GPUs 0 and 1 using 4 Compute
   Units (CUs)

2. Single DMA executed Transfer between GPUs 0 and 1

3. Copy 1 MB from GPU 0 to GPU 1 with 4 CUs, and 2 MB from GPU 1 to GPU
   0 with 8 CUs – This test reports results for both Transfers

4. "Memset" by GPU 0 to GPU 0 memory

5. "Read-only" by CPU 0

6. Broadcast from GPU 0 to GPU 0 and GPU 1

5.1.1 TransferBench Qualification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure that ROCm and libnuma are first installed on the SUT. To download
and install TransferBench, run the following commands:

:mark:`git clone https://github.com/ROCm/TransferBench.git`

:mark:`cd TransferBench`

:mark:`CC=hipcc make`

TransferBench can be run in a variety of configurations, however for SUT
validation use the built-in tests below. Once TransferBench is installed
on your SUT, follow the instructions below to run the All-to-All and
Peer-to-Peer benchmarks. We also include a section on the TransferBench
ConfigFile format, which allows for a set of Transfers (a Test) to run
in parallel.

5.1.1.1 All-to-All
^^^^^^^^^^^^^^^^^^

In GPU All-To-All benchmark, each GPU sends data to every other GPU and
receives data from every other GPU. TransferBench a2a test, measures and
reports all those data transfer rates. Run the following command:

:mark:`TransferBench a2a`

Expected output (truncated) - Note that these values do not map to the
run that produced the results on **Table 1** but are within our
reproducibility acceptance criteria:

:mark:`Summary:`

:mark:`==========================================================`

:mark:`SRC\\DST GPU 00 GPU 01 GPU 02 GPU 03 GPU 04 GPU 05 GPU 06 GPU 07
STotal Actual`

:mark:`GPU 00 N/A 43.666 36.624 43.480 36.677 43.729 36.871 43.607
284.653 255.598`

:mark:`GPU 01 37.858 N/A 39.964 37.983 40.440 38.410 40.209 38.156
273.019 264.392`

:mark:`GPU 02 31.420 34.604 N/A 31.624 34.795 31.512 34.678 31.556
230.188 219.577`

:mark:`GPU 03 30.883 28.583 30.972 N/A 28.649 30.883 28.658 30.918
209.546 199.797`

:mark:`GPU 04 34.388 35.432 34.283 35.309 N/A 34.198 35.236 34.260
243.106 238.708`

:mark:`GPU 05 29.553 30.244 29.432 30.169 29.448 N/A 30.152 29.392
208.391 204.972`

:mark:`GPU 06 38.320 40.466 38.538 40.823 38.526 40.436 N/A 38.188
275.297 266.935`

:mark:`GPU 07 42.405 36.295 42.521 36.361 42.635 36.472 42.553 N/A
279.240 253.728`

:mark:`RTotal 244.827 249.288 252.334 255.749 251.169 255.639 248.357
246.077 2003.440 199.797 266.935`

:mark:`Average bandwidth (GPU Timed): 35.776 GB/s`

:mark:`Aggregate bandwidth (GPU Timed): 2003.440 GB/s`

:mark:`Aggregate bandwidth (CPU Timed): 1411.163 GB/s`

.. table:: **Table 1**: Average, Pass/Fail Bandwidth in GB/s for
TransferBench All-to-All Benchmarking

   +--------------------------------+-------------------------------------+
   |    **TransferBench Test**      |    **Minimum Passing Score (GB/s)** |
   +================================+=====================================+
   |    a2a Avg Bandwidth           |    32.9                             |
   +--------------------------------+-------------------------------------+

.. _section-1:

5.1.1.2 Peer-to-Peer
^^^^^^^^^^^^^^^^^^^^

Shows peak bandwidth of unidirectional and bidirectional copy between
CPU and GPUs. Run the following command:

:mark:`TransferBench p2p`

Expected output (truncated) - Note that these values do not map to the
run that produced the results on **Table 2** but are within our
reproducibility acceptance criteria:

:mark:`Bytes Per Direction 67108864`

:mark:`Unidirectional copy peak bandwidth GB/s [Local read / Remote
write] (GPU-Executor: GFX)`

:mark:`SRC+EXE\\DST CPU 00 CPU 01 GPU 00 GPU 01 GPU 02 GPU 03 GPU 04 GPU
05 GPU 06 GPU 07`

:mark:`CPU 00 -> 42.75 38.85 41.97 42.33 42.50 42.19 41.56 41.45 41.31
41.05`

:mark:`CPU 01 -> 32.85 43.39 41.53 41.65 41.76 42.38 42.67 42.36 42.31
42.60`

:mark:`GPU 00 -> 55.23 55.26 1689.85 48.46 48.73 48.96 48.29 47.89 47.47
47.80`

:mark:`GPU 01 -> 55.23 55.24 48.51 1672.91 48.40 48.72 48.47 48.12 47.79
47.73`

:mark:`GPU 02 -> 55.25 55.24 48.83 48.53 1690.87 48.80 48.59 48.87 48.08
48.07`

:mark:`GPU 03 -> 55.22 55.25 48.81 48.79 48.78 1675.13 48.72 48.66 48.32
47.93`

:mark:`GPU 04 -> 55.23 55.26 48.39 48.46 48.76 48.72 1703.05 48.83 48.85
48.95`

:mark:`GPU 05 -> 55.26 55.26 47.92 48.48 48.59 48.83 48.95 1650.41 48.63
48.88`

:mark:`GPU 06 -> 55.22 55.24 47.71 47.74 48.12 48.35 48.78 48.87 1717.22
48.64`

:mark:`GPU 07 -> 55.26 55.25 47.71 47.69 47.54 48.38 48.78 48.97 48.74
1699.95`

:mark:`CPU->CPU CPU->GPU GPU->CPU GPU->GPU`

:mark:`Averages (During UniDir): 35.85 41.98 55.24 48.44`

:mark:`Bidirectional copy peak bandwidth GB/s [Local read / Remote
write] (GPU-Executor: GFX)`

:mark:`SRC\\DST CPU 00 CPU 01 GPU 00 GPU 01 GPU 02 GPU 03 GPU 04 GPU 05
GPU 06 GPU 07`

:mark:`CPU 00 -> N/A 31.06 41.37 42.07 41.56 41.42 39.96 40.94 40.51
39.60`

:mark:`CPU 00 <- N/A 37.56 54.66 54.63 54.49 54.64 39.40 37.32 37.70
39.52`

:mark:`CPU 00 <-> N/A 68.62 96.03 96.70 96.05 96.06 79.35 78.26 78.20
79.12`

:mark:`CPU 01 -> 32.89 N/A 40.64 41.25 41.25 40.14 41.99 42.04 42.23
42.03`

:mark:`CPU 01 <- 21.38 N/A 39.22 37.17 37.57 39.67 54.51 54.50 54.49
54.49`

:mark:`CPU 01 <-> 54.27 N/A 79.86 78.41 78.82 79.82 96.50 96.54 96.72
96.52`

:mark:`GPU 00 -> 54.51 39.20 N/A 46.11 46.21 46.18 46.23 46.19 46.22
46.00`

:mark:`GPU 00 <- 41.46 40.33 N/A 46.09 46.45 46.22 46.17 46.09 46.25
46.09`

:mark:`GPU 00 <-> 95.97 79.53 N/A 92.20 92.65 92.40 92.40 92.28 92.48
92.09`

:mark:`GPU 01 -> 54.53 37.43 46.22 N/A 46.37 46.44 46.25 46.09 46.03
46.25`

:mark:`GPU 01 <- 41.00 41.07 46.16 N/A 46.20 46.44 46.27 46.22 46.05
46.09`

:mark:`GPU 01 <-> 95.53 78.50 92.37 N/A 92.57 92.88 92.51 92.31 92.07
92.34`

:mark:`GPU 02 -> 54.52 37.48 46.19 46.18 N/A 46.29 46.54 46.26 46.04
46.08`

:mark:`GPU 02 <- 41.49 41.39 46.19 46.40 N/A 46.29 46.46 46.07 46.20
46.09`

:mark:`GPU 02 <-> 96.00 78.87 92.38 92.58 N/A 92.58 93.00 92.33 92.24
92.17`

:mark:`GPU 03 -> 54.63 39.36 46.28 46.50 46.32 N/A 46.41 46.23 46.23
46.13`

:mark:`GPU 03 <- 41.79 40.15 46.27 46.15 46.27 N/A 46.37 46.62 46.24
46.29`

:mark:`GPU 03 <-> 96.42 79.50 92.55 92.64 92.60 N/A 92.79 92.85 92.47
92.42`

:mark:`GPU 04 -> 39.65 54.62 46.25 46.32 46.51 46.31 N/A 46.23 46.48
46.24`

:mark:`GPU 04 <- 39.40 41.96 46.22 46.19 46.47 46.38 N/A 46.28 46.45
46.31`

:mark:`GPU 04 <-> 79.05 96.58 92.47 92.52 92.98 92.69 N/A 92.51 92.94
92.56`

:mark:`GPU 05 -> 37.54 54.65 46.01 46.23 46.21 46.33 46.31 N/A 46.10
46.51`

:mark:`GPU 05 <- 39.82 42.12 46.00 46.24 46.23 46.28 46.08 N/A 46.18
46.26`

:mark:`GPU 05 <-> 77.35 96.77 92.01 92.47 92.44 92.61 92.39 N/A 92.29
92.77`

:mark:`GPU 06 -> 37.23 54.48 45.94 46.07 46.10 46.27 46.37 46.20 N/A
46.06`

:mark:`GPU 06 <- 40.62 41.99 45.99 46.19 46.00 46.28 46.11 46.17 N/A
46.41`

:mark:`GPU 06 <-> 77.85 96.47 91.93 92.26 92.10 92.55 92.48 92.37 N/A
92.47`

:mark:`GPU 07 -> 39.38 54.61 46.20 46.26 46.13 46.27 46.25 46.25 46.30
N/A`

:mark:`GPU 07 <- 39.37 42.31 46.21 46.21 46.08 46.20 46.50 46.45 46.21
N/A`

:mark:`GPU 07 <-> 78.76 96.91 92.41 92.47 92.20 92.47 92.74 92.70 92.50
N/A`

:mark:`CPU->CPU CPU->GPU GPU->CPU GPU->GPU`

:mark:`Averages (During BiDir): 30.72 43.84 43.75 46.24`

.. table:: **Table 2**: Average, Pass/Fail Bandwidth in GB/s for
TransferBench Peer-to-Peer Benchmarking

   +-----------------------------------+----------------------------------+
   |    **TransferBench Test**         |    **Minimum Passing Score       |
   |                                   |    (GB/s)**                      |
   +===================================+==================================+
   |    p2p Avg Unidirectional Copy    |    33.9                          |
   |    (GPU->GPU)                     |                                  |
   +-----------------------------------+----------------------------------+
   |    P2p Avg Bidirectional Copy     |    43.9                          |
   |    (GPU<->GPU)                    |                                  |
   +-----------------------------------+----------------------------------+

5.1.1.3 TransferBench Default ConfigFile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The TransferBench default ConfigFile test allows a set of Transfers (a
Test) to run in parallel. To learn more about the ConfigFile format,
please review the `official
documentation <https://rocm.docs.amd.com/projects/TransferBench/en/latest/how%20to/use-transferbench.html>`__.
Run the following command:

:mark:`TransferBench examples/example.cfg`

Expected output (truncated) - Note that these values do not map to the
run that produced the results on **Table 3** but are within our
reproducibility acceptance criteria:

:mark:`## Single GPU-executed Transfer between GPUs 0 and 1 using 4 CUs`

:mark:`Test 1:`

:mark:`Executor: GPU 00 \| 47.772 GB/s \| 1.405 ms \| 67108864 bytes \|
47.774 GB/s (sum)`

:mark:`Transfer 00 \| 47.774 GB/s \| 1.405 ms \| 67108864 bytes \| G0 ->
GPU00:004 -> G1`

:mark:`Aggregate (CPU) \| 42.490 GB/s \| 1.579 ms \| 67108864 bytes \|
Overhead: 0.175 ms`

:mark:`## Single DMA executed Transfer between GPUs 0 and 1`

:mark:`Test 2:`

:mark:`Executor: DMA 00 \| 48.349 GB/s \| 1.388 ms \| 67108864 bytes \|
48.349 GB/s (sum)`

:mark:`Transfer 00 \| 48.349 GB/s \| 1.388 ms \| 67108864 bytes \| G0 ->
DMA00.\*:001 -> G1`

:mark:`Aggregate (CPU) \| 44.653 GB/s \| 1.503 ms \| 67108864 bytes \|
Overhead: 0.115 ms`

:mark:`## Copy 1Mb from GPU0 to GPU1 with 4 CUs, and 2Mb from GPU1 to
GPU0 with 8 CUs`

:mark:`Test 3:`

:mark:`Executor: GPU 00 \| 35.921 GB/s \| 0.029 ms \| 1048576 bytes \|
32.809 GB/s (sum)`

:mark:`Transfer 00 \| 32.809 GB/s \| 0.032 ms \| 1048576 bytes \| G0 ->
GPU00:004 -> G1`

:mark:`Executor: GPU 01 \| 41.228 GB/s \| 0.051 ms \| 2097152 bytes \|
39.603 GB/s (sum)`

:mark:`Transfer 01 \| 39.603 GB/s \| 0.053 ms \| 2097152 bytes \| G1 ->
GPU01:008 -> G0`

:mark:`Aggregate (CPU) \| 16.036 GB/s \| 0.196 ms \| 3145728 bytes \|
Overhead: 0.145 ms`

:mark:`## "Memset" by GPU 0 to GPU 0 memory`

:mark:`Test 4:`

:mark:`Executor: GPU 00 \| 1351.543 GB/s \| 0.050 ms \| 67108864 bytes
\| 1274.598 GB/s (sum)`

:mark:`Transfer 00 \| 1274.598 GB/s \| 0.053 ms \| 67108864 bytes \| N
-> GPU00:032 -> G0`

:mark:`Aggregate (CPU) \| 305.581 GB/s \| 0.220 ms \| 67108864 bytes \|
Overhead: 0.170 ms`

:mark:`## "Read-only" by CPU 0`

:mark:`Test 5:`

:mark:`Executor: CPU 00 \| 20.344 GB/s \| 3.299 ms \| 67108864 bytes \|
20.344 GB/s (sum)`

:mark:`Transfer 00 \| 20.344 GB/s \| 3.299 ms \| 67108864 bytes \| C0 ->
CPU00:004 -> N`

:mark:`Aggregate (CPU) \| 19.338 GB/s \| 3.470 ms \| 67108864 bytes \|
Overhead: 0.171 ms`

:mark:`## Broadcast from GPU 0 to GPU 0 and GPU 1`

:mark:`Test 6:`

:mark:`Executor: GPU 00 \| 48.964 GB/s \| 1.371 ms \| 67108864 bytes \|
48.933 GB/s (sum)`

:mark:`Transfer 00 \| 48.933 GB/s \| 1.371 ms \| 67108864 bytes \| G0 ->
GPU00:016 -> G0G1`

:mark:`Aggregate (CPU) \| 44.433 GB/s \| 1.510 ms \| 67108864 bytes \|
Overhead: 0.140 ms`

The table below shows the reference performance results for
TransferBench on an MI300X system. For TransferBench, higher scores are
better.

.. table:: **Table 3:** Average, Pass/Fail Bandwidth in GB/s for
TransferBench Benchmarking

   +----------------------------+-----------------------------------------+
   |    **TransferBench Test**  |    **Minimum Passing Score (GB/s)**     |
   +============================+=========================================+
   |    Test 1                  |    47.1                                 |
   +----------------------------+-----------------------------------------+
   |    Test 2                  |    48.4                                 |
   +----------------------------+-----------------------------------------+
   |    Test 3 – 0 to 1         |    31.9                                 |
   +----------------------------+-----------------------------------------+
   |    Test 3 – 1 to 0         |    38.9                                 |
   +----------------------------+-----------------------------------------+
   |    Test 4                  |    1264                                 |
   +----------------------------+-----------------------------------------+
   |    Test 5\*                |    N/A                                  |
   +----------------------------+-----------------------------------------+
   |    Test 6                  |    48.6                                 |
   +----------------------------+-----------------------------------------+

**\* Note:** TransferBench Test 5 is a CPU-only benchmark. Results are
highly platform dependent and should not be used to validate GPU
performance.

5.2 RCCL Benchmarking Results
-----------------------------

The ROCm Collective Communications Library
(`RCCL <https://github.com/ROCm/rccl>`__) is available as open-source
software. Though RCCL is designed to be used as a performant backend for
downstream applications, particularly AI training and inference
workloads, it also has a test suite to benchmark and validate
performance.

GPU collectives can measure performance in several ways, and RCCL
benchmarks include both “algorithm” bandwidth and “bus” bandwidth
metrics. For point-to-point operations, algorithm bandwidth is a
reliable indication of hardware utilization, while for large collective
operations bus bandwidth is a better measurement of hardware
utilization. For more on the bus band metrics, please refer to the
`performance
documentation <https://github.com/ROCm/rccl-tests/blob/develop/doc/PERFORMANCE.md>`__
in the RCCL tests repository.

In this document, we report the expected bus bandwidth of the all_reduce
operators. Additional tests are available in the `RCCL tests
directory <https://github.com/ROCm/rccl-tests/tree/develop/test>`__.

The **Table 4** contains RCCL benchmark pass/fail criteria. Measurements
are reported for bus bandwidth and in-place operations, for message
sizes of 8 GB. Higher scores are better.

5.2.1 RCCL Qualification
~~~~~~~~~~~~~~~~~~~~~~~~

Build RCCL tests from source using the official documentation or by
running the commands below in your terminal:

+-----------------------------------------------------------------------+
| :mark:`git clone https://github.com/ROCm/rccl-tests.git`              |
|                                                                       |
| :mark:`cd rccl_tests/`                                                |
|                                                                       |
| :mark:`make NCCL_HOME=/opt/rocm/`                                     |
+=======================================================================+
+-----------------------------------------------------------------------+

Once RCCL tests is installed on your SUT, follow these instructions to
run the All-Reduce benchmark.

5.2.1.2 All-Reduce
^^^^^^^^^^^^^^^^^^

To evaluate the All -Reduce operator using the RCCL tests benchmark, run
the following command in your terminal:

:mark:`build/all_reduce_perf -b 8 -e 8G -f 2 -g 8`

The RCCL all-reduce test criteria is to exceed an in-place busbw metric
of 304 GB/s at a message size of 8589934592B, approximately 8GB – the
reported value is shown in the example output below:

:mark:`# nThread 1 nGpus 8 minBytes 8 maxBytes 8589934592 step:
2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0`

:mark:`#`

:mark:`rccl-tests: Version develop:ae3e635`

:mark:`# Using devices`

:mark:`# Rank 0 Pid 806883 on SMC-SC-DC19-06 device 0 [0000:05:00.0] AMD
Instinct MI300X`

:mark:`# Rank 1 Pid 806883 on SMC-SC-DC19-06 device 1 [0000:26:00.0] AMD
Instinct MI300X`

:mark:`# Rank 2 Pid 806883 on SMC-SC-DC19-06 device 2 [0000:46:00.0] AMD
Instinct MI300X`

:mark:`# Rank 3 Pid 806883 on SMC-SC-DC19-06 device 3 [0000:65:00.0] AMD
Instinct MI300X`

:mark:`# Rank 4 Pid 806883 on SMC-SC-DC19-06 device 4 [0000:85:00.0] AMD
Instinct MI300X`

:mark:`# Rank 5 Pid 806883 on SMC-SC-DC19-06 device 5 [0000:a6:00.0] AMD
Instinct MI300X`

:mark:`# Rank 6 Pid 806883 on SMC-SC-DC19-06 device 6 [0000:c6:00.0] AMD
Instinct MI300X`

:mark:`# Rank 7 Pid 806883 on SMC-SC-DC19-06 device 7 [0000:e5:00.0] AMD
Instinct MI300X`

:mark:`#`

:mark:`# size count type redop root time algbw busbw #wrong time algbw
busbw #wrong`

:mark:`# (B) (elements) (us) (GB/s) (GB/s) (us) (GB/s) (GB/s)`

:mark:`8 2 float sum -1 34.13 0.00 0.00 0 39.55 0.00 0.00 0`

:mark:`16 4 float sum -1 38.73 0.00 0.00 0 38.92 0.00 0.00 0`

:mark:`32 8 float sum -1 39.48 0.00 0.00 0 39.23 0.00 0.00 0`

:mark:`64 16 float sum -1 39.18 0.00 0.00 0 54.09 0.00 0.00 0`

:mark:`128 32 float sum -1 39.36 0.00 0.01 0 182.4 0.00 0.00 0`

:mark:`256 64 float sum -1 41.24 0.01 0.01 0 44.39 0.01 0.01 0`

:mark:`512 128 float sum -1 44.23 0.01 0.02 0 44.43 0.01 0.02 0`

:mark:`1024 256 float sum -1 45.84 0.02 0.04 0 58.30 0.02 0.03 0`

:mark:`2048 512 float sum -1 44.60 0.05 0.08 0 44.59 0.05 0.08 0`

:mark:`4096 1024 float sum -1 45.01 0.09 0.16 0 45.16 0.09 0.16 0`

:mark:`8192 2048 float sum -1 43.72 0.19 0.33 0 43.06 0.19 0.33 0`

:mark:`16384 4096 float sum -1 55.70 0.29 0.51 0 43.96 0.37 0.65 0`

:mark:`32768 8192 float sum -1 44.39 0.74 1.29 0 43.22 0.76 1.33 0`

:mark:`65536 16384 float sum -1 44.35 1.48 2.59 0 57.02 1.15 2.01 0`

:mark:`131072 32768 float sum -1 47.47 2.76 4.83 0 41.03 3.19 5.59 0`

:mark:`262144 65536 float sum -1 59.18 4.43 7.75 0 41.75 6.28 10.99 0`

:mark:`524288 131072 float sum -1 57.96 9.05 15.83 0 51.85 10.11 17.70
0`

:mark:`1048576 262144 float sum -1 58.47 17.93 31.38 0 58.94 17.79 31.13
0`

:mark:`2097152 524288 float sum -1 59.86 35.03 61.31 0 61.09 34.33 60.08
0`

:mark:`4194304 1048576 float sum -1 90.74 46.22 80.89 0 90.50 46.34
81.10 0`

:mark:`8388608 2097152 float sum -1 110.8 75.71 132.49 0 116.3 72.13
126.23 0`

:mark:`16777216 4194304 float sum -1 169.7 98.87 173.02 0 171.7 97.71
170.99 0`

:mark:`33554432 8388608 float sum -1 257.6 130.28 227.99 0 271.7 123.51
216.14 0`

:mark:`67108864 16777216 float sum -1 428.1 156.76 274.33 0 437.3 153.44
268.53 0`

:mark:`134217728 33554432 float sum -1 801.8 167.41 292.96 0 807.4
166.23 290.90 0`

:mark:`268435456 67108864 float sum -1 1546.5 173.58 303.76 0 1554.9
172.64 302.12 0`

:mark:`536870912 134217728 float sum -1 3038.1 176.71 309.25 0 3046.8
176.21 308.36 0`

:mark:`1073741824 268435456 float sum -1 6003.9 178.84 312.97 0 6003.6
178.85 312.99 0`

:mark:`2147483648 536870912 float sum -1 11938 179.88 314.80 0 11960
179.55 314.22 0`

:mark:`4294967296 1073741824 float sum -1 23849 180.09 315.15 0 23881
179.85 314.74 0`

:mark:`8589934592 2147483648 float sum -1 47488 180.88 316.55 0 47594
180.48` :mark:`315.84` :mark:`0`

:mark:`# Errors with asterisks indicate errors that have exceeded the
maximum threshold.`

:mark:`# Out of bounds values : 0 OK`

:mark:`# Avg bus bandwidth : 102.138`

.. table:: **Table 4:** Average, Pass/Fail Bandwidth in GB/s for RCCL
Benchmarking

   +-----------------------------------+-----------------------------------+
   |    **Operation**                  |    **Minimum Passing Score        |
   |                                   |    (GB/s)**                       |
   +===================================+===================================+
   |    all_reduce                     |    304                            |
   +-----------------------------------+-----------------------------------+

5.3 rocBLAS Benchmarking Results
--------------------------------

AI models rely on highly optimized GEMM kernels (General Matrix
Multiply) for optimal performance in both training and inference. AMD
provides the rocBLAS and other libraries to enable applications and
libraries to leverage AMD-optimized GEMM kernels.

The rocBLAS test application allows users to benchmark the GEMM
performance of rocBLAS in a standalone application. The numbers below
indicate for the included benchmark (fp32) and two half precision GEMMs
the expected performance of rocBLAS on a validated system.

|Shape|

**Note:** rocBLAS provides generic, performant BLAS and GEMM operations,
but for some situations and kernels, other AMD ROCm supported tools,
such as hipBLASLt, Triton and Composable Kernel, can provide superior
performance.

*For more information, see*
`rocblas-bench <https://rocm.docs.amd.com/projects/rocBLAS/en/develop/how-to/Programmers_Guide.html#rocblas-bench>`__.
Future updates of ROCm in particular can boost performance of GEMM
benchmarks, so these numbers are expected to vary in the future.

.. _section-2:

5.3.1 rocBLAS Qualification 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

rocBLAS can be built from source to target tests and benchmarks only,
which have a dependency on gtest. On Ubuntu, install gtest by running
the following command:

+-----------------------------------------------------------------------+
| :mark:`sudo apt install libgtest-dev`                                 |
+=======================================================================+
+-----------------------------------------------------------------------+

Build rocBLAS from source by running the following commands in your
terminal:

:mark:`git clone https://github.com/ROCm/rocBLAS.git`

:mark:`cd rocBLAS`

:mark:`git checkout rocm-6.2.0`

:mark:`./install --clients-only --library-path /opt/rocm`

**Note:** The instructions above target a release of rocBLAS at 6.2.0 –
it is not recommended to use the latest development branchs of rocBLAS
for system hardware validation. This build can take several minutes to
complete.

We include 3 rocBLAS benchmarks here targeting single, bf16, and int8
precisions. Half precision and fp8 precision are not in the scope of
rocBLAS, and are not included in system validation. Compare test results
to **Table 5**, below.

5.3.1.1 FP32 – Full Precision Benchmark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the FP32 full-precision benchmark, run the following command in
your terminal:

:mark:`*rocblas-bench -f gemm -r s -m 4000 -n 4000 -k 4000 --lda 4000
--ldb 4000 --ldc 4000 --transposeA N --transposeB T*`

In the output, expect to find a performance benchmark line near the end
of the output. Truncated example output is shown here:

:mark:`rocBLAS info: maximum library size per device is 0.61866 GB.`

:mark:`transA,transB,M,N,K,alpha,lda,beta,ldb,ldc,rocblas-Gflops,us`

:mark:`N,T,4000,4000,4000,1,4000,0,4000,4000, 97190.6, 1317`

5.3.1.2 BF16 Half Precision Benchmark 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the BF16 half-precision benchmark, run the following command in
your terminal:

:mark:`rocblas-bench -f gemm_strided_batched_ex --transposeA N
--transposeB T -m 1024 -n 2048 -k 512 --a_type h --lda 1024 --stride_a
4096 --b_type h --ldb 2048 --stride_b 4096 --c_type s --ldc 1024
--stride_c 2097152 --d_type s --ldd 1024 --stride_d 2097152
--compute_type s --alpha 1.1 --beta 1 --batch_count 5`

In the output, expect to find a performance benchmark line near the end
of the output. Truncated example output is shown here::

:mark:`rocBLAS info: maximum library size per device is 0.61866 GB.`

:mark:`transA,transB,M,N,K,alpha,lda,stride_a,beta,ldb,stride_b,ldc,stride_c,ldd,stride_d,batch_count,rocblas-Gflops,us`

:mark:`N,T,1024,2048,512,1.1,1024,4096,1,2048,4096,1024,2097152,1024,2097152,5,
159783, 67.2`

5.3.1.3 INT8 Integer Precision Benchmark
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the int8 integer-precision benchmark, run the following command
in your terminal:

:mark:`rocblas-bench -f gemm_strided_batched_ex --transposeA N
--transposeB T -m 1024 -n 2048 -k 512 --a_type i8_r --lda 1024
--stride_a 4096 --b_type i8_r --ldb 2048 --stride_b 4096 --c_type i32_r
--ldc 1024 --stride_c 2097152 --d_type i32_r --ldd 1024 --stride_d
2097152 --compute_type i32_r --alpha 1.1 --beta 1 --batch_count 5`

In the output, expect to find a performance benchmark line near the end
of the output. Truncated example output is shown here:

:mark:`rocBLAS info: maximum library size per device is 0.61866 GB.`

:mark:`transA,transB,M,N,K,alpha,lda,stride_a,beta,ldb,stride_b,ldc,stride_c,ldd,stride_d,batch_count,rocblas-Gflops,us`

:mark:`N,T,1024,2048,512,1,1024,4096,1,2048,4096,1024,2097152,1024,2097152,5,
177478, 60.5`

The following table contains GEMM benchmark pass/fail criteria. For GEMM
Benchmarks, larger scores are better.

.. table:: **Table 5:** Average, Pass/Fail Bandwidth in TFLOPS for GEMM
Benchmarking

   +-----------------------------------+-----------------------------------+
   |    **GEMM**                       |    **Minimum Passing Score        |
   |                                   |    (TFLOPS)**                     |
   +===================================+===================================+
   |    FP32 4kx4kx4k                  |    94100                          |
   +-----------------------------------+-----------------------------------+
   |    Strided BF16, BS 5, 1kx2kx512  |    130600                         |
   +-----------------------------------+-----------------------------------+
   |    Strided Int8, BS5, 1kx2kx512   |    162700                         |
   +-----------------------------------+-----------------------------------+

NOTE: Typically, rocBLAS benchmarking requires multiple test runs to
obtain peak performance. It is recommended to use the highest TFLOPS
score obtained for each GEMM test to validate the compute performance.

5.4 BabelStream Benchmarking Results
------------------------------------

BabelStream is an open-source benchmark to measure transfer rates
to/from global device memory on GPUs. For more information, see
`BabelStream <https://github.com/UoB-HPC/BabelStream>`__.

The qualification section will explain how to configure BabelStream.
Running the test will perform the benchmark on each GPU concurrently.
**Table 6** contains BabelStream v5.0 benchmark pass/fail criteria. For
BabelStream, higher scores are better.

5.4.1 BabelStream Qualification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build BabelStream tests from source using the official documentation or
by running the commands below in your terminal:

:mark:`git clone https://github.com/UoB-HPC/BabelStream.git`

:mark:`cd BabelStream`

:mark:`cmake -Bbuild -H. -DMODEL=hip -DCMAKE_CXX_COMPILER=hipcc`

:mark:`cmake --build build`

:mark:`export PATH=$PWD/build:$PATH`

Running babelstream on all eight 300X GPUs concurrently requires
coordinated job launching and device identification as an argument to
the hip-stream executable. AMD recommends mpi to orchestrate this, and
the easiest way to run on the SUT is to create a script called
*wrapper.sh* and populate it with the following lines:

+-----------------------------------------------------------------------+
| #!/bin/bash                                                           |
|                                                                       |
| # Use the mpirank to manage the device:                               |
|                                                                       |
| hip-stream --device $OMPI_COMM_WORLD_RANK -n 50 -s 268435456          |
+=======================================================================+
+-----------------------------------------------------------------------+

**Note:** The MPI rank needs to be specified properly based on the MPI
implementation. We assume Open MPI.

Open MPI can be installed on Ubuntu platforms with the following syntax:

sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev

After completing the babelstream tests, openmpi can be uninstalled.

For your first benchmark run, execute the following command to assign
proper permissions to the wrapper script:

:mark:`chmod u+x wrapper.sh`.

To run the benchmark, execute the following command in the terminal:

:mark:`mpiexec -n 8 wrapper.sh`

Expected output (truncated) -

:mark:`BabelStream`

:mark:`Version: 5.0`

:mark:`Implementation: HIP`

:mark:`Running kernels 50 times`

:mark:`Precision: **double**`

:mark:`Array size: 2147.5 MB (=2.1 GB)`

:mark:`Total size: 6442.5 MB (=6.4 GB)`

:mark:`BabelStream`

:mark:`Version: 5.0`

:mark:`Implementation: HIP`

:mark:`Running kernels 50 times`

:mark:`. . .`

:mark:`Using HIP device AMD Instinct MI300X`

:mark:`Driver: 60241133`

:mark:`Memory: DEFAULT`

:mark:`Using HIP device AMD Instinct MI300X`

:mark:`Driver: 60241133`

:mark:`Memory: DEFAULT`

:mark:`Using HIP device AMD Instinct MI300X`

:mark:`Driver: 60241133`

:mark:`. . .`

:mark:`Init: 0.400851 s (=16071.943100 MBytes/sec)`

:mark:`Read: 0.189949 s (=33916.687305 MBytes/sec)`

:mark:`Init: 0.401357 s (=16051.675182 MBytes/sec)`

:mark:`. . .`

:mark:`Function MBytes/sec Min (sec) Max Average`

:mark:`Copy 4255995.148 0.00101 0.00117 0.00106`

:mark:`Mul 4115971.910 0.00104 0.00111 0.00106`

:mark:`Add 3956389.991 0.00163 0.00170 0.00165`

:mark:`Triad 3948061.647 0.00163 0.00180 0.00166`

:mark:`Dot 3878410.495 0.00111 0.00120 0.00116`

:mark:`Function MBytes/sec Min (sec) Max Average`

:mark:`Copy 4269126.275 0.00101 0.00109 0.00105`

:mark:`Mul 4113642.067 0.00104 0.00111 0.00107`

:mark:`Add 3948620.619 0.00163 0.00177 0.00166`

:mark:`Triad 3947212.603 0.00163 0.00167 0.00165`

:mark:`Dot 3927179.117 0.00109 0.00117 0.00113`

:mark:`. . .`

.. table:: **Table 6:** Average, Pass/Fail Memory Bandwidth in MB/s for
BabelStream Benchmarking

   +---------------+------------------------------------------------------+
   |               |    **Minimum Passing Score                           |
   |  **Function** |    (MB/s)**                                          |
   +===============+======================================================+
   |    Copy       |    4,177,285                                         |
   +---------------+------------------------------------------------------+
   |    Mul        |    4,067,069                                         |
   +---------------+------------------------------------------------------+
   |    Add        |    3,920,853                                         |
   +---------------+------------------------------------------------------+
   |    Triad      |    3,885,301                                         |
   +---------------+------------------------------------------------------+
   |    Dot        |    3,660,781                                         |
   +---------------+------------------------------------------------------+

Chapter 6: Acceptance Criteria
==============================

If all the Results section PASSED, the SUT is ready and should be
accepted.

.. table:: **Table 7:** Summary of the Basic System Health Checks

   +------------+----------------+---------------------------------------+
   | Test       | Command        | Pass/Fail Criteria                    |
   +============+================+=======================================+
   | Check OS   | cat            | **Pass:** OS version listed in        |
   | Di         | /              | compatibility matrix                  |
   | stribution | etc/os-release | **Fail:** Otherwise                   |
   +------------+----------------+---------------------------------------+
   | Check      | cat            | **                                    |
   | Kernel     | /proc/cmdline  | Pass:** Contains pci=realloc=off, amd |
   | Boot       |                | _iommu=on or intel_iommu=on, iommu=pt |
   | Arguments  |                | **Fail:** Otherwise                   |
   +------------+----------------+---------------------------------------+
   | Check for  | sudo dmesg –T  | **Pass:** Null                        |
   | Driver     | \| grep amdgpu | **Fail:** Errors reported             |
   | Errors     | \| grep -i     |                                       |
   |            | error          |                                       |
   +------------+----------------+---------------------------------------+
   | Check      | lsmem \| grep  | **Pass:** 1.5T or more                |
   | Available  | "Total online  | **Fail:** Less than 1.5T              |
   | Memory     | memory"        |                                       |
   +------------+----------------+---------------------------------------+
   | Check GPU  | lspci \| grep  | **Pass:** All 8 GPUs found            |
   | Presence   | MI300X         | **Fail:** Otherwise                   |
   +------------+----------------+---------------------------------------+
   | Check GPU  | sudo lspci -d  | **Pass:** Speed 32GT/s, Width x16, no |
   | Link Speed | 1002:74a1 -vvv | FatalErr+                             |
   | and Width  | \| grep -e     | **Fail:** Otherwise                   |
   |            | DevSta -e      |                                       |
   |            | LnkSta         |                                       |
   +------------+----------------+---------------------------------------+
   | Monitor    | amd-smi        | **Pass:** Idle metrics as specified   |
   | U          | monitor -putm  | **Fail:** Otherwise                   |
   | tilization |                |                                       |
   | Metrics    |                |                                       |
   +------------+----------------+---------------------------------------+
   | Check      | sudo dmesg -T  | **Pass:** Null                        |
   | System     | \| grep -i     | **Fail:** Otherwise                   |
   | Kernel     | 'error|warn|f  |                                       |
   | Logs for   | ail|exception' |                                       |
   | Errors     |                |                                       |
   +------------+----------------+---------------------------------------+

.. table:: **Table 8:** Summary of System Validation Tests

   +------------------+--------------------------+-----------------------+
   | Test             | Command                  | Pass/Fail Criteria    |
   +==================+==========================+=======================+
   | Compute/GPU      | rvs -c                   | **Pass:** All GPUs    |
   | Properties       | ${RV                     | listed, no errors     |
   |                  | S_CONF}/gpup_single.conf | **Fail:** Missing     |
   |                  |                          | GPUs or errors        |
   +------------------+--------------------------+-----------------------+
   | GPU Stress Test  | rvs -c                   | **Pass:** "met: TRUE" |
   | (GST)            | ${RVS_CONF               | in logs               |
   |                  | }/MI300X/gst_single.conf | **Fail:** Target      |
   |                  |                          | GFLOP/s not met       |
   +------------------+--------------------------+-----------------------+
   | Input Energy     | rvs -c ${RVS_CONF}/      | **Pass:** "pass:      |
   | Delay Product    | MI300X/iet_single.conf   | TRUE" for all actions |
   | (IET)            |                          | **Fail:** Otherwise   |
   +------------------+--------------------------+-----------------------+
   | Memory Test      | rvs -c                   | **Pass:** All tests   |
   | (MEM)            | ${RVS_CONF}/mem.conf -l  | passed, bandwidth     |
   |                  | mem.txt                  | ~2TB/s                |
   |                  |                          | **Fail:** Any test    |
   |                  |                          | failed or low         |
   |                  |                          | bandwidth             |
   +------------------+--------------------------+-----------------------+
   | PCIe Bandwidth   | rvs -c ${RVS_CONF}/      | **Pass:** All         |
   | Benchmark (PEBB) | MI300X/pebb_single.conf  | distances and         |
   |                  |                          | bandwidths displayed  |
   |                  |                          | **Fail:** Missing     |
   |                  |                          | data                  |
   +------------------+--------------------------+-----------------------+
   | PCIe             | sudo rvs -c              | **Pass:** All actions |
   | Qualification    | ${RV                     | true                  |
   | Tool (PEQT)      | S_CONF}/peqt_single.conf | **Fail:** Otherwise   |
   +------------------+--------------------------+-----------------------+
   | P2P Benchmark    | rvs -c ${RVS_CONF}/      | *                     |
   | and              | MI300X/pbqt_single.conf  | *Pass:** "peers:true" |
   | Qualification    |                          | lines and non-zero    |
   | Tool (PBQT)      |                          | throughput            |
   |                  |                          | **Fail:** Otherwise   |
   +------------------+--------------------------+-----------------------+

.. table:: **Table 9:** Summary of Performance Benchmarking Tests

   +-----------+----------------------------+-----------------------------+
   | Test      | Command                    | Pass/Fail Criteria          |
   +===========+============================+=============================+
   | Tran      | TransferBench a2a          | **Pass:** ≥ 32.9            |
   | sferBench |                            |                             |
   | A         |                            | **Fail:** Otherwise         |
   | ll-to-All |                            |                             |
   +-----------+----------------------------+-----------------------------+
   | Tran      | TransferBench p2p          | **UniDir Pass:** ≥ 33.9     |
   | sferBench |                            |                             |
   | Pee       |                            | **BiDir Pass:** ≥ 43.9      |
   | r-to-Peer |                            |                             |
   |           |                            | **Fail:** Otherwise         |
   +-----------+----------------------------+-----------------------------+
   | Tran      | TransferBench example.cfg  | | **Test 1 Pass:** ≥ 47.1   |
   | sferBench |                            |   GB/s                      |
   | Tests 1-6 |                            | | **Test 2 Pass:** ≥ 48.4   |
   |           |                            |   GB/s                      |
   |           |                            |                             |
   |           |                            | **Test 3 Pass:** ≥ 31.9     |
   |           |                            | GB/s (0 to 1)               |
   |           |                            |                             |
   |           |                            | ≥ 38.9 GB/s (1 to 0)        |
   |           |                            |                             |
   |           |                            | **Test 4 Pass:** ≥ 1264     |
   |           |                            | GB/s                        |
   |           |                            |                             |
   |           |                            | **Test 5 Pass:** N/A for    |
   |           |                            | GPU validation              |
   |           |                            |                             |
   |           |                            | **Test 6 Pass:** ≥ 48.6     |
   |           |                            | GB/s                        |
   |           |                            |                             |
   |           |                            | **Fail:** Otherwise         |
   +-----------+----------------------------+-----------------------------+
   | RCCL      | build/all_reduce_perf -b 8 | **Pass:** ≥ 304 GB/s        |
   | Allreduce | -e 8G -f 2 -g 8            | **Fail:** Otherwise         |
   +-----------+----------------------------+-----------------------------+
   | rocBLAS   | rocblas-bench -f gemm -r s | **Pass:** ≥ 94100 TFLOPS    |
   | FP32      | -m 4000 -n 4000 -k 4000    | **Fail:** Otherwise         |
   | Benchmark | --lda 4000 --ldb 4000      |                             |
   |           | --ldc 4000 --transposeA N  |                             |
   |           | --transposeB T             |                             |
   +-----------+----------------------------+-----------------------------+
   | rocBLAS   | rocblas-bench -f           | **Pass:** ≥ 130600 TFLOPS   |
   | BF16      | gemm_strided_batched_ex    | **Fail:** Otherwise         |
   | Benchmark | --transposeA N             |                             |
   |           | --transposeB T -m 1024 -n  |                             |
   |           | 2048 -k 512 --a_type h     |                             |
   |           | --lda 1024 --stride_a 4096 |                             |
   |           | --b_type h --ldb 2048      |                             |
   |           | --stride_b 4096 --c_type s |                             |
   |           | --ldc 1024 --stride_c      |                             |
   |           | 2097152 --d_type s --ldd   |                             |
   |           | 1024 --stride_d 2097152    |                             |
   |           | --compute_type s --alpha   |                             |
   |           | 1.1 --beta 1 --batch_count |                             |
   |           | 5                          |                             |
   +-----------+----------------------------+-----------------------------+
   | rocBLAS   | rocblas-bench -f           | **Pass:** ≥ 162700 TFLOPS   |
   | INT8      | gemm_strided_batched_ex    | **Fail:** Otherwise         |
   | Benchmark | --transposeA N             |                             |
   |           | --transposeB T -m 1024 -n  |                             |
   |           | 2048 -k 512 --a_type i8_r  |                             |
   |           | --lda 1024 --stride_a 4096 |                             |
   |           | --b_type i8_r --ldb 2048   |                             |
   |           | --stride_b 4096 --c_type   |                             |
   |           | i32_r --ldc 1024           |                             |
   |           | --stride_c 2097152         |                             |
   |           | --d_type i32_r --ldd 1024  |                             |
   |           | --stride_d 2097152         |                             |
   |           | --compute_type i32_r       |                             |
   |           | --alpha 1.1 --beta 1       |                             |
   |           | --batch_count 5            |                             |
   +-----------+----------------------------+-----------------------------+
   | Ba        | mpiexec -n 8 wrapper.sh    | **Copy Pass:** ≥ 4,177,285  |
   | belStream |                            | MB/s                        |
   |           |                            |                             |
   |           |                            | **Mul Pass:** ≥ 4,067,069   |
   |           |                            | MB/s                        |
   |           |                            |                             |
   |           |                            | **Add Pass:** ≥ 3,920,853   |
   |           |                            | MB/s                        |
   |           |                            |                             |
   |           |                            | **Triad Pass:** ≥ 3,885,301 |
   |           |                            | MB/s                        |
   |           |                            |                             |
   |           |                            | **Dot Pass:** ≥ 3,660,781   |
   |           |                            | MB/s                        |
   |           |                            |                             |
   |           |                            | **Fail:** Otherwise         |
   +-----------+----------------------------+-----------------------------+

Chapter 7: Next Steps
=====================

After successfully completing the tests mentioned in this guide, the
System Under Test (SUT) meets the customer acceptance criteria. The test
results related to performance serve as a baseline for further
enhancements. To further optimize the system, it is recommended to make
incremental changes to individual parameters noted in the pre-requisites
and repeat the tests. Once complete, AMD recommends proceeding with AI
model validation and cluster network validation using the guides
mentioned below. Refer to the `Appendix
B <#appendix-b-reference-documents>`__ for a list of links to all
referenced documentation in this guide.

7.1 MI300X AI Model Performance Validation Guide
------------------------------------------------

Larger AI applications, such as Large Language Models, are beyond the
scope of this document for system acceptance guidance. However, the SUT
should be ready to run these large models. For reference, please see the
AMD Instinct MI300X Performance Validation Guide (PVG) which has
detailed platform configuration information, application instructions,
and guidance for AI application performance validation. Models are
available on `AMD Infinity
Hub <https://www.amd.com/en/developer/resources/infinity-hub.html>`__
and the `Performance Validation
Guide <https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi300x-performance-validation-guide.pdf>`__
is available on the AMD Documentation Hub.

7.2 MI300X Cluster Network Performance Validation Guide
-------------------------------------------------------

After validating single node performance, it is now time to configure
each server for maximum data transfer and bandwidth. It's essential to
test both host and device performance in single-node and multi-node
setups using targeted benchmarks. The `Cluster Network Performance
Validate
Guide <https://rocm.docs.amd.com/projects/gpu-cluster-networking/en/latest/>`__
for single-node networking and multi-node networking provides
step-by-step instructions on configuring network settings, devices, and
running performance tests to ensure AMD Instinct MI300X based GPU
clusters operate at peak speed and bandwidth.

7.3 MI300X Workload Optimization Guide
--------------------------------------

Once the system and networking have been fully validated, it is
recommended to review the `Workload Optimization
Guide <https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html>`__
to learn more about how to take advantage of workload tuning strategies
to further improve performance and efficiency of the workloads operating
on the MI300X based system(s).

Appendix A: Acronyms
====================

The following table contains acronyms and definitions used throughout
this document.

.. table:: **Table 10:** Acronyms

   +---------------+------------------------------------------------------+
   | Acronym       | Description                                          |
   +===============+======================================================+
   | AMI           | American Megatrends Inc. (BIOS provider)             |
   +---------------+------------------------------------------------------+
   | BIOS          | Basic Input/Output System                            |
   +---------------+------------------------------------------------------+
   | CUs           | Compute Units                                        |
   +---------------+------------------------------------------------------+
   | DGEMM         | Double-precision General Matrix Multiply             |
   +---------------+------------------------------------------------------+
   | DMA           | Direct Memory Access                                 |
   +---------------+------------------------------------------------------+
   | GB/s          | Gigabytes per second                                 |
   +---------------+------------------------------------------------------+
   | GPU           | Graphics Processing Unit                             |
   +---------------+------------------------------------------------------+
   | GRUB          | GNU Grand Unified Bootloader                         |
   +---------------+------------------------------------------------------+
   | GST           | GPU Stress Test                                      |
   +---------------+------------------------------------------------------+
   | HBM3          | High Bandwidth Memory 3                              |
   +---------------+------------------------------------------------------+
   | HIP           | Heterogeneous-computing Interface for Portability    |
   +---------------+------------------------------------------------------+
   | IET           | Input Energy Delay Product                           |
   +---------------+------------------------------------------------------+
   | MB/s          | Megabytes per second                                 |
   +---------------+------------------------------------------------------+
   | MEM           | Memory                                               |
   +---------------+------------------------------------------------------+
   | MPI           | Message Passing Interface                            |
   +---------------+------------------------------------------------------+
   | NVMe          | Non-Volatile Memory Express                          |
   +---------------+------------------------------------------------------+
   | OAM           | Open Accelerator Module                              |
   +---------------+------------------------------------------------------+
   | ORC           | Online Resource Center for AMD partners              |
   +---------------+------------------------------------------------------+
   | OS            | Operating System                                     |
   +---------------+------------------------------------------------------+
   | PBQT          | P2P Benchmark and Qualification Tool                 |
   +---------------+------------------------------------------------------+
   | PEBB          | PCIe Bandwidth Benchmark                             |
   +---------------+------------------------------------------------------+
   | PEQT          | PCIe Qualification Tool                              |
   +---------------+------------------------------------------------------+
   | PCIe          | Peripheral Component Interconnect Express            |
   +---------------+------------------------------------------------------+
   | PVG           | Performance Validation Guide                         |
   +---------------+------------------------------------------------------+
   | RCCL          | ROCm Collective Communications Library               |
   +---------------+------------------------------------------------------+
   | rocBLAS       | ROCm Basic Linear Algebra Subprograms                |
   +---------------+------------------------------------------------------+
   | RVS           | ROCm Validation Suite                                |
   +---------------+------------------------------------------------------+
   | SGEMM         | Single-precision General Matrix Multiply             |
   +---------------+------------------------------------------------------+
   | SUT           | System Under Test                                    |
   +---------------+------------------------------------------------------+
   | TFLOPS        | Tera Floating Point Operations Per Second            |
   +---------------+------------------------------------------------------+
   | xGMI          | Inter-chip (x) Global Memory Interconnect            |
   +---------------+------------------------------------------------------+

Appendix B: Reference Documents
===============================

The table below provides the relevant reference documents and links to
setup the system and run the tests in this guide.

.. table:: **Table 11:** Reference Documents

   +---------------+------------------------------------------------------+
   | Document Name | Link                                                 |
   +===============+======================================================+
   | System BIOS   | https://rocm.docs.amd.com/en/latest/how-to/s         |
   | Settings      | ystem-optimization/mi300x.html#mi300x-bios-settings  |
   +---------------+------------------------------------------------------+
   | Supported     | https://rocm.doc                                     |
   | Operating     | s.amd.com/projects/install-on-linux/en/latest/refere |
   | Systems       | nce/system-requirements.html#supported-distributions |
   +---------------+------------------------------------------------------+
   | ROCm          | https://rocm.docs.amd.com/projects/i                 |
   | Installation  | nstall-on-linux/en/latest/install/prerequisites.html |
   | Prerequisites |                                                      |
   +---------------+------------------------------------------------------+
   | GRUB Settings | https://rocm.docs.amd.com/en/latest/how-to/          |
   |               | system-optimization/mi300x.html#mi300x-grub-settings |
   +---------------+------------------------------------------------------+
   | Operating     | https://rocm.docs.amd.com/en/latest/how-t            |
   | System        | o/system-optimization/mi300x.html#mi300x-os-settings |
   | Settings      |                                                      |
   +---------------+------------------------------------------------------+
   | ROCm          | https://rocm.docs.amd.co                             |
   | Compatibility | m/en/latest/compatibility/compatibility-matrix.htmlP |
   | Matrix        |                                                      |
   +---------------+------------------------------------------------------+
   | ROCm Quick    | https://rocm.docs.amd.com/projects                   |
   | Start         | /install-on-linux/en/latest/install/quick-start.html |
   | Installation  |                                                      |
   | Guide         |                                                      |
   +---------------+------------------------------------------------------+
   | ROCm          | https://rocm.docs.am                                 |
   | Installation  | d.com/projects/install-on-linux/en/latest/index.html |
   | for Linux     |                                                      |
   +---------------+------------------------------------------------------+
   | ROCm Post     | https://rocm.docs.amd.com/projects/                  |
   | Installation  | install-on-linux/en/latest/install/post-install.html |
   | Instructions  |                                                      |
   +---------------+------------------------------------------------------+
   | ROCm          | https://rocm.docs.amd.com/projects/i                 |
   | Installation  | nstall-on-linux/en/latest/reference/install-faq.html |
   | Tr            |                                                      |
   | oubleshooting |                                                      |
   +---------------+------------------------------------------------------+
   | RVS           | https://github.com/                                  |
   | Configuration | ROCm/ROCmValidationSuite/blob/master/docs/ug1main.md |
   | File          |                                                      |
   +---------------+------------------------------------------------------+
   | RVS User      | https://github.com/                                  |
   | Guide         | ROCm/ROCmValidationSuite/blob/master/docs/ug1main.md |
   +---------------+------------------------------------------------------+
   | RVS Modules   | https://github.                                      |
   |               | com/ROCm/ROCmValidationSuite/blob/master/FEATURES.md |
   +---------------+------------------------------------------------------+
   | TransferBench | https://github.com/ROCm/TransferBench                |
   | Repository    |                                                      |
   +---------------+------------------------------------------------------+
   | TransferBench | `https://ro                                          |
   | How To Guide  | cm.docs.amd.com/projects/TransferBench/en/latest/how |
   |               | to/use-transferbe                                    |
   |               | nch.html <https://rocm.docs.amd.com/projects/Transfe |
   |               | rBench/en/latest/how%20to/use-transferbench.html>`__ |
   |               |                                                      |
   +---------------+------------------------------------------------------+
   | TransferBench | https://github.com/                                  |
   | Example       | ROCm/TransferBench/blob/develop/examples/example.cfg |
   | Configuration |                                                      |
   +---------------+------------------------------------------------------+
   | RCCL          | https://github.com/ROCm/rccl                         |
   | Repository    |                                                      |
   +---------------+------------------------------------------------------+
   | RCCL Test     | https://github.com/ROCm/rccl-tests/tree/develop      |
   | Repository    |                                                      |
   +---------------+------------------------------------------------------+
   | RCCL          | https://github                                       |
   | Performance   | .com/ROCm/rccl-tests/blob/develop/doc/PERFORMANCE.md |
   | Guide         |                                                      |
   +---------------+------------------------------------------------------+
   | RCCL Tests    | h                                                    |
   | (All)         | ttps://github.com/ROCm/rccl-tests/tree/develop/test  |
   +---------------+------------------------------------------------------+
   | rocBLAS       | https://rocm                                         |
   | Documentation | .docs.amd.com/projects/rocBLAS/en/develop/index.html |
   +---------------+------------------------------------------------------+
   | rocBLAS Bench | https://rocm.docs.amd.com/projects/rocBLAS/en        |
   | Guide         | /develop/how-to/Programmers_Guide.html#rocblas-bench |
   +---------------+------------------------------------------------------+
   | BabelStream   | https://github.com/UoB-HPC/BabelStream               |
   | Repository    |                                                      |
   +---------------+------------------------------------------------------+
   | Performance   | https://www.amd.com/content/dam                      |
   | Validation    | /amd/en/documents/instinct-tech-docs/product-briefs/ |
   | Guide         | amd-instinct-mi300x-performance-validation-guide.pdf |
   +---------------+------------------------------------------------------+
   | Infinity Hub  | https://                                             |
   | Portal        | www.amd.com/en/developer/resources/infinity-hub.html |
   +---------------+------------------------------------------------------+
   | Cluster       | https://rocm.doc                                     |
   | Network       | s.amd.com/projects/gpu-cluster-networking/en/latest/ |
   | Performance   |                                                      |
   | Validation    |                                                      |
   | Guide         |                                                      |
   +---------------+------------------------------------------------------+
   | Workload      | https://rocm.docs.amd.com                            |
   | Optimization  | /en/latest/how-to/tuning-guides/mi300x/workload.html |
   | Guide         |                                                      |
   +---------------+------------------------------------------------------+

PAppendix C: Collecting Logs (rocm_techsupport.sh)
==================================================

ROCm Tech Support is a shell utility script that collects logs for
troubleshooting purposes. Information such as ROCm packages installed,
rocm-smi, PCI bridges, system peripherals and more are logged into a
text file. When performing basic checks on the system, it is useful to
first collect the logs as a baseline before making any changes to the
system.

For more information on how to install and use this utility, refer to
the README located at https://github.com/amddcgpuce/rocmtechsupport.

Appendix D: Revision History
============================

The following table shows the revision history of this document.

.. table:: **Table 12:** Revision History

   +-----------------------------------------------------------------------+
   |    Revision Summary                                                   |
   +=======================================================================+
   |    October 2024, Version 0.9                                          |
   +-----------------------------------------------------------------------+
   | - Initial release.                                                    |
   +-----------------------------------------------------------------------+

Appendix E: Notices
===================

   © Copyright 2024 Advanced Micro Devices, Inc.

   The information presented in this document is for informational
   purposes only and may contain technical inaccuracies, omissions, and
   typographical errors. The information contained herein is subject to
   change and may be rendered inaccurate for many reasons, including but
   not limited to product and roadmap changes, component and motherboard
   version changes, new model and/or product releases, product
   differences between differing manufacturers, software changes, BIOS
   flashes, firmware upgrades, or

   the like. Any computer system has risks of security vulnerabilities
   that cannot be completely prevented or mitigated. AMD assumes no
   obligation to update or otherwise correct or revise this information.

   However, AMD reserves the right to revise this information and to
   make changes from time to time to the content hereof without
   obligation of AMD to notify any person of such revisions or changes.

   THIS INFORMATION IS PROVIDED "AS IS." AMD MAKES NO REPRESENTATIONS OR
   WARRANTIES WITH RESPECT TO THE CONTENTS HEREOF AND ASSUMES NO
   RESPONSIBILITY FOR

   ANY INACCURACIES, ERRORS, OR OMISSIONS THAT MAY APPEAR IN THIS
   INFORMATION. AMD SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTIES OF
   NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR
   PURPOSE. IN NO EVENT WILL AMD BE LIABLE TO ANY PERSON FOR ANY
   RELIANCE, DIRECT, INDIRECT, SPECIAL, OR OTHER CONSEQUENTIAL DAMAGES
   ARISING FROM THE USE OF ANY INFORMATION CONTAINED HEREIN, EVEN IF AMD
   IS EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

Trademarks
----------

   AMD, the AMD Arrow logo, and combinations thereof are trademarks of
   Advanced Micro Devices, Inc.

   Other product names used in this publication are for identification
   purposes only and may be trademarks of their respective companies.

PCIe® is a registered trademark of PCI-SIG Corporation.

.. |A black background with a black square Description automatically generated with medium confidence| image:: media/image1.png
   :width: 2.9077in
   :height: 0.69771in
.. |Shape| image:: media/image8.png
   :width: 7.02084in
