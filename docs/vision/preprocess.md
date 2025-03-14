# Image Preprocessing

Eliminate the bottleneck caused by slow CPU image processing to further accelerate your computer vision workloads on AMD Instinct GPUs with [rocAL](https://github.com/ROCm/rocAL) and [RPP](https://github.com/ROCm/rpp). These libraries allow you to perform a wide variety of well known computer vision operations with GPU acceleration to augment and transform your images, preparing them for your deep learning workloads.

## ROCm Augmentation Library

The [ROCm Augmentation Library (rocAL)](https://github.com/ROCm/rocAL) enables efficient loading and data preprocessing for deep learning applications. This allows for the creation of efficient computer vision pipelines that fully utilize the power of AMD Instinct GPUs. rocAL is designed to efficiently decode and process image and video from a variety of storage formats, saving you time that could be better spent training or running your models.

## ROCm Performance Primitives

The [ROCm Performance Primitives (RPP)](https://github.com/ROCm/rpp) library contains a collection of high-performance computer vision operations with HIP, OpenCL, or CPU backends. This library enables you to efficiently apply augmentations, statistical functions, geometric and morphological transformations, popular filters, color model conversions, or other popular computer vision operations to preprocess your images for all of your computer vision workloads.

## Documentation

For full documentation, please refer to the ROCm docs site:
- [rocAL](https://rocm.docs.amd.com/projects/rocAL/en/latest/)
- [RPP](https://rocm.docs.amd.com/projects/rpp/en/latest/)
