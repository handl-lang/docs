import { defineConfig } from "vitepress";
import { productSidebars } from "./sidebar-products.mjs";
import { handlDark } from "./theme/shiki-themes.mjs";

// Shared sidebar groups: the "why/what" pages (story, paradigm, strategy,
// bibliography), the ecosystem map (overview, kernel), and the "who"
// pages (members, contact).
const learnSidebar = [
  {
    text: "Learn",
    items: [
      { text: "Story", link: "/story/" },
      { text: "Paradigm", link: "/paradigm/" },
      { text: "Strategy", link: "/strategy/" },
      { text: "Bibliography", link: "/ecosystem/bibliography" },
    ],
  },
];

const ecosystemSidebar = [
  {
    text: "Ecosystem",
    items: [
      { text: "Overview", link: "/ecosystem/" },
      { text: "Kernel", link: "/kernel/" },
    ],
  },
];

const communitySidebar = [
  {
    text: "Community",
    items: [
      { text: "Members", link: "/members/" },
      { text: "Contact", link: "/contact/" },
    ],
  },
];

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
    "AGENTS.md",
    "ANALYSIS.md",
    "DESIGN.md",
    // Internal org/checkout map — names private repos; not site content.
    "structure.md",
    // Internal dep-pinning convention for the fleet — same audience.
    "pinning.md",
    // Generated / parked content — kept in the repo, not published.
    "api/**",
    "adrs/**",
    "engines/**",
    "handl/**",
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
        text: "Learn",
        items: [
          { text: "Story", link: "/story/" },
          { text: "Paradigm", link: "/paradigm/" },
          { text: "Strategy", link: "/strategy/" },
          { text: "Bibliography", link: "/ecosystem/bibliography" },
        ],
      },
      {
        text: "Ecosystem",
        items: [
          { text: "Overview", link: "/ecosystem/" },
          { text: "Kernel", link: "/kernel/" },
        ],
      },
      {
        text: "Community",
        items: [
          { text: "Members", link: "/members/" },
          { text: "Contact", link: "/contact/" },
        ],
      },
    ],

    sidebar: {
      "/story/": learnSidebar,
      "/paradigm/": learnSidebar,
      "/strategy/": learnSidebar,
      "/ecosystem/bibliography": learnSidebar,
      "/ecosystem/": ecosystemSidebar,
      "/members/": communitySidebar,
      "/contact/": communitySidebar,
      // Only the kernel repo ships vendored docs (see VENDORED_REPOS in
      // scripts/vendor-docs.py); its sidebar is generated from the tree.
      "/kernel/": productSidebars["/kernel/"] ?? [],
    },

    search: {
      provider: "local",
    },

    socialLinks: [{ icon: "github", link: "https://github.com/handl-lang" }],
  },
});
