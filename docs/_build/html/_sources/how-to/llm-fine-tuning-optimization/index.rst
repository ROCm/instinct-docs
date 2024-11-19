.. meta::
   :description: How to fine-tune LLMs with ROCm
   :keywords: ROCm, LLM, fine-tuning, usage, tutorial

*******************************************
Fine-tuning LLMs and inference optimization
*******************************************

ROCm empowers the fine-tuning and optimization of large language models, making them accessible and efficient for
specialized tasks. ROCm supports the broader AI ecosystem to ensure seamless integration with open frameworks,
models, and tools.

For more information, see `What is ROCm? <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_

Throughout the following topics, this guide discusses the goals and :ref:`challenges of fine-tuning a large language
model <fine-tuning-llms-concept-challenge>` like Llama 2. Then, it introduces :ref:`common methods of optimizing your
fine-tuning <fine-tuning-llms-concept-optimizations>` using techniques like LoRA with libraries like PEFT. In the
sections that follow, you'll find practical guides on libraries and tools to accelerate your fine-tuning.

- :doc:`Conceptual overview of fine-tuning LLMs <overview>`

- :doc:`Fine-tuning and inference <fine-tuning-and-inference>` using a
  :doc:`single-accelerator <single-gpu-fine-tuning-and-inference>` or
  :doc:`multi-accelerator <multi-gpu-fine-tuning-and-inference>` system.

- :doc:`Model quantization <model-quantization>`

- :doc:`Model acceleration libraries <model-acceleration-libraries>`

- :doc:`LLM inference frameworks <llm-inference-frameworks>`

- :doc:`Optimizing with Composable Kernel <optimizing-with-composable-kernel>`

- :doc:`Optimizing Triton kernels <optimizing-triton-kernel>`

- :doc:`Profiling and debugging <profiling-and-debugging>`

