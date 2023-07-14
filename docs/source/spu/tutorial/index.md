# Your first MPC application with SPU

:::{admonition} 编者备注
:class: notes dropdown

[The MNIST example](https://github.com/secretflow/spu/tree/atc23_ae) from the ATC '23 paper was attractive and we should make it a full-fledged tutorial.
:::

We will be training a neural network on the [MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database) using SPU.

This tutorial assumes basic knowledge of machine learning. We will be

:::{admonition} 编者备注：目标读者
:class: notes dropdown

我们假设读者熟悉机器学习但不熟悉 MPC 或是编译器相关知识。
:::

The goal of this tutorial is to demonstrate how to adapt a typical ML workflow to run in a MPC topology. Through this tutorial, you will:

- Have your (very simple) SPU program, ready to go.
- Gain a basic understanding of secure multi-party computation (MPC).
- Learn about key components in the SPU compiler and runtime.
- ...
