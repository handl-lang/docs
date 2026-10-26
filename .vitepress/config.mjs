import { defineConfig } from "vitepress";
import referenceSidebar from "./sidebar-reference.mjs";
import * as adrsSidebar from "./sidebar-adrs.mjs";
import { productSidebars } from "./sidebar-products.mjs";
import { handlDark } from "./theme/shiki-themes.mjs";

const { handlAdrs = [], graphoptAdrs = [] } = adrsSidebar;

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "handl-lang",
  description:
    "handl-lang — products and services built on a categorical language foundation.",
  ignoreDeadLinks: true,
  appearance: "dark",
  // The site lives at the repo root (this repo is the docs hub); the ADR
  // worktree and the generator scripts are not site content.
  srcDir: ".",
  // Product repos ship their published docs under `docs/site/`; the
  // vendor script copies them to `vendored/<product>/`, and these
  // rewrites serve them at the site root.
  rewrites: {
    "vendored/:rest(.*)": ":rest",
  },
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
      {
        text: "Products",
        items: [
          { text: "Handl Language", link: "/handl/" },
        ],
      },
      {
        text: "Engines",
        link: "/engines/",
      },
      {
        text: "Research",
        items: [
          { text: "graphopt", link: "/graphopt/" },
        ],
      },
      {
        text: "Libraries",
        items: [
          { text: "eqsat", link: "/eqsat/" },
          { text: "gamekit", link: "/gamekit/" },
        ],
      },
    ],

    sidebar: {
      "/handl/": [
        {
          text: "Handl Language",
          items: [
            { text: "Overview", link: "/handl/" },
            { text: "Platform overview", link: "/handl/overview" },
            { text: "Arrow-native comparison", link: "/handl/comparison" },
            { text: "Kernel paper (PDF)", link: "https://github.com/handl-lang/kernel/blob/main/paper/paper.pdf" },
            { text: "Platform paper (PDF)", link: "https://github.com/handl-lang/host/blob/main/paper/paper.pdf" },
          ],
        },
        {
          text: "Tutorials",
          collapsed: false,
          items: [
            { text: "Overview", link: "/handl/tutorials/" },
            { text: "Set up the platform", link: "/handl/tutorials/setup" },
            { text: "Build a host", link: "/handl/tutorials/build-a-host" },
            { text: "Write a plugin", link: "/handl/tutorials/write-a-plugin" },
          ],
        },
        {
          text: "How-to guides",
          collapsed: false,
          items: [
            { text: "Overview", link: "/handl/how-to/" },
            { text: "Set up the platform", link: "/handl/how-to/setup" },
            { text: "Build a host", link: "/handl/how-to/build-a-host" },
            { text: "Write a plugin", link: "/handl/how-to/write-a-plugin" },
            { text: "Configure options", link: "/handl/how-to/configure-options" },
          ],
        },
        {
          text: "Explanations",
          collapsed: false,
          items: [
            { text: "Overview", link: "/handl/explanation/" },
            { text: "What is handl?", link: "/handl/explanation/what-is-handl" },
            { text: "The arrow calculus kernel", link: "/handl/explanation/arrow-calculus-kernel" },
            { text: "The type system", link: "/handl/explanation/type-system" },
            { text: "Language as data", link: "/handl/explanation/language-as-data" },
            { text: "The composable host", link: "/handl/explanation/composable-host" },
            { text: "Platform architecture", link: "/handl/explanation/platform-architecture" },
            { text: "Runtime", link: "/handl/explanation/runtime" },
            {
              text: "Plugins, rules, and operations",
              link: "/handl/explanation/plugins-rules-operations",
            },
            { text: "Kits and manifests", link: "/handl/explanation/kits-and-manifests" },
            { text: "Options and configuration", link: "/handl/explanation/options-and-configuration" },
            { text: "Security and trust", link: "/handl/explanation/security-and-trust" },
            { text: "Graded algebraic theory", link: "/handl/explanation/graded-algebraic-theory" },
            {
              text: "Graded Modal Sanada Arrow Calculus",
              link: "/handl/explanation/graded-modal-sanada-arrow-calculus",
            },
          ],
        },
        {
          text: "Design notes",
          collapsed: true,
          items: [
            {
              text: "Library API design principles",
              link: "/handl/explanation/ac-lib-api-design-principles",
            },
            { text: "Design principles", link: "/handl/explanation/design-principles" },
            { text: "Name explanation", link: "/handl/explanation/lang-name" },
            { text: "Polyglot runtimes", link: "/handl/explanation/polyglot-runtimes" },
          ],
        },
        {
          text: "Reference",
          collapsed: false,
          items: [
            { text: "Overview", link: "/handl/reference/" },
            { text: "Host concepts", link: "/handl/reference/host-concepts" },
            ...referenceSidebar,
          ],
        },
        {
          text: "Project",
          collapsed: false,
          items: [
            { text: "TODO", link: "/handl/project/TODO" },
            { text: "Backlog", link: "/handl/project/BACKLOG" },
            { text: "ADRs", link: "/adrs/handl" },
            { text: "ADRs", collapsed: true, items: handlAdrs },
          ],
        },
      ],
      "/graphopt/": [
        {
          text: "graphopt",
          items: [
            { text: "Overview", link: "/graphopt/" },
            { text: "How graphopt works", link: "/graphopt/explanation/mechanism" },
            { text: "Evaluation", link: "/graphopt/explanation/evaluation" },
            { text: "The three costs", link: "/graphopt/explanation/three-costs" },
            { text: "The game", link: "/graphopt/explanation/the-game" },
            { text: "The gauntlet", link: "/graphopt/explanation/the-gauntlet" },
          ],
        },
        {
          text: "Tutorials",
          collapsed: false,
          items: [
            { text: "Overview", link: "/graphopt/tutorials/" },
            { text: "Set up graphopt", link: "/graphopt/tutorials/setup" },
            { text: "Your first search()", link: "/graphopt/tutorials/first-search" },
            { text: "Watch a law get minted", link: "/graphopt/tutorials/mint-a-law" },
            { text: "Run the scorecard", link: "/graphopt/tutorials/run-the-scorecard" },
          ],
        },
        {
          text: "How-to guides",
          collapsed: false,
          items: [
            { text: "Optimize a model", link: "/graphopt/how-to/optimize-a-model" },
            { text: "Add a board", link: "/graphopt/how-to/add-a-board" },
            { text: "Register a player", link: "/graphopt/how-to/register-a-player" },
            { text: "Admit a law", link: "/graphopt/how-to/admit-a-law" },
          ],
        },
        {
          text: "Reference",
          collapsed: false,
          items: [
            { text: "The frozen API", link: "/graphopt/reference/frozen-api" },
            { text: "Discovery scorecard", link: "/graphopt/reference/scorecard" },
            { text: "Player leaderboard", link: "/graphopt/reference/leaderboard" },
            { text: "Limits table", link: "/graphopt/reference/limits" },
          ],
        },
        {
          text: "Project",
          collapsed: false,
          items: [
            { text: "TODO", link: "/graphopt/project/TODO" },
            { text: "Goals", link: "/graphopt/project/GOALS" },
            { text: "ADRs", link: "/adrs/graphopt" },
            { text: "ADRs", collapsed: true, items: graphoptAdrs },
          ],
        },
      ],
      "/eqsat/": [
        {
          text: "eqsat",
          items: [
            { text: "Overview", link: "/eqsat/" },
            { text: "The e-graph and dag_cost", link: "/eqsat/explanation/egraph" },
            { text: "Certificates", link: "/eqsat/explanation/certificates" },
            { text: "The ports", link: "/eqsat/explanation/ports" },
          ],
        },
        {
          text: "Reference",
          collapsed: false,
          items: [
            { text: "Overview", link: "/eqsat/reference/" },
            { text: "The e-graph", link: "/eqsat/reference/egraph" },
            { text: "The cost algebra", link: "/eqsat/reference/cost" },
            { text: "The ports", link: "/eqsat/reference/ports" },
            { text: "The frozen API (substrate slice)", link: "/eqsat/reference/frozen-api" },
          ],
        },
      ],
      "/gamekit/": [
        {
          text: "gamekit",
          items: [
            { text: "Overview", link: "/gamekit/" },
            { text: "The substrate-free kernel", link: "/gamekit/explanation/the-kernel" },
          ],
        },
        {
          text: "Reference",
          collapsed: false,
          items: [
            { text: "Overview", link: "/gamekit/reference/" },
            { text: "The Board protocol", link: "/gamekit/reference/board" },
            { text: "Players & the registry", link: "/gamekit/reference/players" },
            { text: "The frozen API (game slice)", link: "/gamekit/reference/frozen-api" },
          ],
        },
      ],
      "/engines/": [
        {
          text: "Engines",
          items: [{ text: "Overview", link: "/engines/" }],
        },
      ],
      ...productSidebars,
      "/adrs/": [
        {
          text: "ADRs",
          items: [
            { text: "handl-lang (org)", link: "/adrs/" },
            { text: "Handl Language", link: "/adrs/handl" },
            { text: "graphopt", link: "/adrs/graphopt" },
          ],
        },
      ],
    },

    search: {
      provider: "local",
    },

    socialLinks: [{ icon: "github", link: "https://github.com/handl-lang" }],
  },
});
