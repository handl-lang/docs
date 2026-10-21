# How-to guides

How-to guides are practical recipes. They assume you already know the
basics and want to accomplish a specific goal.

## Setup

- [Set up the platform](./setup) — clone the public repos and build the
  workspace.

## Building with the platform

- [Build a host](./build-a-host) — create an executable that composes
  plugins and runs capabilities.
- [Write a plugin](./write-a-plugin) — implement a plugin and contribute
  a rule.
- [Configure options](./configure-options) — declare and override
  options from kits and `.handl.toml`.

## The research stack (graphopt)

- [Optimize a model](./research/optimize-a-model) — `torch.nn.Module` →
  a verified, delivered optimized module.
- [Add a board](./research/add-a-board) — a new optimization game as an
  RL environment.
- [Register a player](./research/register-a-player) — a measured arm in
  the `gamekit` players registry.
- [Admit a law](./research/admit-a-law) — a candidate equality through
  the gauntlet into `DEFAULT`.

## When to use another section

- If you are new to the platform, start with
  [Tutorials](../tutorials/setup).
- If you want the theory behind a feature, read
  [Explanations](../explanation/).
- If you need function signatures and examples, use the
  [Reference](../reference/).
