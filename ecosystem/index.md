# Handl ecosystem

Handl is a modular language infrastructure built around a categorical,
runtime-independent IR. Its foundation is a closed arrow calculus with
globular higher-categorical structure, allowing computation, laws, and
transformations to share a common representation.

The ecosystem separates this foundation from the engines that process it, the
abstractions built on top of it, and the environments in which it operates.

## 1. Kernel

The Kernel defines Handl's computational foundation: its arrow calculus, IR,
value representation, and language schema. It is a closed arrow calculus
(LWY + Sanada) extended with graded effects and globular
higher-categorical structure, where programs, laws, and transformations are
all data.

The Kernel provides a stable foundation without prescribing a particular
runtime or execution strategy. See [the paradigm](/paradigm/) for what the
calculus buys you.

<div class="eco-grid">
  <div class="eco-card">
    <strong>kernel</strong>
    <p>The arrow-calculus substrate: language schema, tagged values, and extension ABI.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/kernel">GitHub</a>
      <a href="/kernel/">Docs</a>
    </div>
  </div>
</div>

## 2. Engines

Independent components that process Handl representations. Engines can
analyze, transform, compile, or execute the IR.

<div class="eco-grid">
  <div class="eco-card">
    <strong>Compilation</strong>
    <p>LLVM (native), Triton, CUDA emitters.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/compile-llvm">tool-compile-llvm</a> (private)
      <a href="https://github.com/handl-lang/compile-triton">tool-compile-triton</a> (private)
      <a href="https://github.com/handl-lang/compile-cuda">tool-compile-cuda</a> (private)
    </div>
  </div>
  <div class="eco-card">
    <strong>Execution</strong>
    <p>Cranelift JIT, bytecode VM, and the tree-walk reference interpreter.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/exec-cranelift">exec-cranelift</a>
      <a href="https://github.com/handl-lang/exec-bytecode">exec-bytecode</a>
      <a href="https://github.com/handl-lang/exec-tree-walk">exec-tree-walk</a>
    </div>
  </div>
  <div class="eco-card">
    <strong>Transformation</strong>
    <p>IR-to-IR rewriting, desugaring, and optimization.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/tool-transform-rewrite">tool-transform-rewrite</a>
    </div>
  </div>
  <div class="eco-card">
    <strong>Language processing</strong>
    <p>Lexer, parser, typechecker, linter, and formatter engines.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/tool-lex-pattern">tool-lex-pattern</a>
      <a href="https://github.com/handl-lang/tool-parse-pratt">tool-parse-pratt</a>
      <a href="https://github.com/handl-lang/tool-typecheck">tool-typecheck</a>
      <a href="https://github.com/handl-lang/tool-lint">tool-lint</a>
      <a href="https://github.com/handl-lang/tool-fmt">tool-fmt</a>
    </div>
  </div>
</div>

Engines are interchangeable consumers and processors of the shared
representation, not intrinsic parts of the Kernel.

## 3. Libraries (`lib-*`)

Reusable Handl libraries (`.hnl`) providing foundational and domain-specific
functionality, such as mathematics, strings, logic, and other utilities.

Libraries provide runtime-agnostic abstractions: the same APIs can be used
across different execution environments, with runtime-specific implementations
preserving compatible interfaces and semantics. This allows application code
and higher-level libraries to remain independent of the underlying runtime.

## 4. Kits (`kit-*`)

Curated collections of libraries and components targeting particular
environments or use cases, such as testing, server-side development,
and web services. Kits provide ready-to-use environments by assembling
compatible libraries, engines, and supporting components.

## 5. Tools

Developer utilities and generators that facilitate development and
interoperability with external systems. SDK generators produce type-safe
Handl APIs from existing interfaces.

<div class="eco-grid">
  <div class="eco-card">
    <strong>tool-codegen-python</strong>
    <p>Python interoperability.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/sdkgen-python">GitHub</a> (private)
    </div>
  </div>
  <div class="eco-card">
    <strong>tool-codegen-c</strong>
    <p>C interoperability, including libc, libcurl, and zlib.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/sdkgen-c">GitHub</a> (private)
    </div>
  </div>
  <div class="eco-card">
    <strong>tool-codegen-webidl</strong>
    <p>Web APIs, including Fetch and Console.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/sdkgen-webidl">GitHub</a> (private)
    </div>
  </div>
  <div class="eco-card">
    <strong>tool-codegen-cli</strong>
    <p>Type-safe APIs for spawning and interacting with CLI processes.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/sdkgen-cli">GitHub</a> (private)
    </div>
  </div>
</div>

## 6. Hosts

The distribution layer exposing Handl to users: the CLI and LSP.

<div class="eco-grid">
  <div class="eco-card">
    <strong>host-cli</strong>
    <p>The Handl command-line interface.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/host-cli">GitHub</a>
    </div>
  </div>
  <div class="eco-card">
    <strong>host-lsp</strong>
    <p>The language server for editors.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/host-lsp">GitHub</a> (private)
    </div>
  </div>
</div>

## 7. Extensions

Editor integrations for development environments.

<div class="eco-grid">
  <div class="eco-card">
    <strong>extension-vscode</strong>
    <p>VS Code integration.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/extension-vscode">GitHub</a> (private)
    </div>
  </div>
  <div class="eco-card">
    <strong>extension-neovim</strong>
    <p>Neovim integration.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/extension-neovim">GitHub</a> (private)
    </div>
  </div>
</div>

The Hosts and Extensions together form the integration layer that exposes
Handl to users and development environments.

## 8. Documentation

Aggregated documentation across the ecosystem.

<div class="eco-grid">
  <div class="eco-card">
    <strong>docs</strong>
    <p>This site: the hub for handl-lang documentation.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/docs">GitHub</a>
    </div>
  </div>
</div>

## 9. Research

Research projects built on Handl.

<div class="eco-grid">
  <div class="eco-card">
    <strong>MLOpt</strong>
    <p>Optimization of existing machine learning models for embedded architectures.</p>
    <div class="eco-links">
      <a href="https://github.com/handl-lang/mlopt">GitHub</a>
    </div>
  </div>
</div>

## 10. Products

Applications built on Handl. None yet; this section is a placeholder for
what the ecosystem produces.
