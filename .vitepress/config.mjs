import { defineConfig } from "vitepress";
import referenceSidebar from "./sidebar-reference.mjs";
import { handlDark } from "./theme/shiki-themes.mjs";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "handl",
  description: "Documentation for the handl language",
  ignoreDeadLinks: true,
  appearance: "dark",
  // The site lives at the repo root (this repo is the docs hub); the ADR
  // worktree and the generator scripts are not site content.
  srcDir: ".",
  // Project Pages are served from https://handl-lang.github.io/docs/ ;
  // `DOCS_BASE` overrides this for local `vitepress dev` (use "/").
  base: process.env.DOCS_BASE ?? "/docs/",
  srcExclude: [
    "README.md",
    "ANALYSIS.md",
    "DESIGN.md",
    "project/**",
    "scripts/**",
    "node_modules/**",
  ],
  head: [
    ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
    ["link", { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" }],
    [
      "link",
      {
        href: "https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;1,400&display=swap",
        rel: "stylesheet",
      },
    ],
  ],
  markdown: {
    theme: {
      dark: handlDark,
      light: "github-light",
    },
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Tutorials", link: "/tutorials/" },
      { text: "How-to", link: "/how-to/" },
      { text: "Explanation", link: "/explanation/" },
      { text: "Reference", link: "/reference/" },
      { text: "ADRs", link: "/ADR-INDEX" },
    ],

    sidebar: {
      "/tutorials/": [
        {
          text: "Tutorials",
          items: [
            { text: "Overview", link: "/tutorials/" },
            { text: "Getting started", link: "/tutorials/getting-started" },
            { text: "Build a host", link: "/tutorials/build-a-host" },
            { text: "Write a plugin", link: "/tutorials/write-a-plugin" },
          ],
        },
      ],
      "/how-to/": [
        {
          text: "How-to guides",
          items: [
            { text: "Overview", link: "/how-to/" },
            { text: "Install hnl", link: "/how-to/install-handl" },
            { text: "Write a handl script", link: "/how-to/write-a-script" },
            { text: "Build a host", link: "/how-to/build-a-host" },
            { text: "Write a plugin", link: "/how-to/write-a-plugin" },
            { text: "Configure options", link: "/how-to/configure-options" },
          ],
        },
      ],
      "/explanation/": [
        {
          text: "Explanations",
          items: [
            { text: "Overview", link: "/explanation/" },
            { text: "What is handl?", link: "/explanation/what-is-handl" },
            { text: "Language overview", link: "/explanation/language-overview" },
            { text: "Runtime", link: "/explanation/runtime" },
            { text: "Platform architecture", link: "/explanation/platform-architecture" },
            { text: "The composable host", link: "/explanation/composable-host" },
            { text: "The arrow calculus kernel", link: "/explanation/arrow-calculus-kernel" },
            {
              text: "Plugins, rules, and operations",
              link: "/explanation/plugins-rules-operations",
            },
            { text: "Kits and manifests", link: "/explanation/kits-and-manifests" },
            { text: "Options and configuration", link: "/explanation/options-and-configuration" },
            { text: "Security and trust", link: "/explanation/security-and-trust" },
            { text: "Graded algebraic theory", link: "/explanation/graded-algebraic-theory" },
            {
              text: "Graded Modal Sanada Arrow Calculus",
              link: "/explanation/graded-modal-sanada-arrow-calculus",
            },
            {
              text: "Strings, chars, and Unicode",
              link: "/explanation/strings-chars-unicode-layers",
            },
          ],
        },
        {
          text: "Design notes",
          collapsed: true,
          items: [
            {
              text: "Library API design principles",
              link: "/explanation/ac-lib-api-design-principles",
            },
            { text: "Design principles", link: "/explanation/design-principles" },
            { text: "Fields, not keys", link: "/explanation/fields-not-keys" },
            { text: "Name explanation", link: "/explanation/lang-name" },
            {
              text: "Per-workspace language variants",
              link: "/explanation/per-workspace-language-variants",
            },
            { text: "Polyglot runtimes", link: "/explanation/polyglot-runtimes" },
            { text: "Why the kernel is small", link: "/explanation/small-kernel" },
            {
              text: "VS Code extension constraints",
              link: "/explanation/vscode-extension-constraints",
            },
          ],
        },
      ],
      "/reference/": [
        {
          text: "Reference",
          link: "/reference/",
          collapsed: false,
          items: referenceSidebar,
        },
      ],
    },

    search: {
      provider: "local",
    },

    socialLinks: [{ icon: "github", link: "https://github.com/handl-lang" }],
  },
});
