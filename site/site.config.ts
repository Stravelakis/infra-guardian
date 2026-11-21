// Per-repo config for the shared docs-theme (repo standards §7).

interface SocialLink {
  kind: 'github' | 'linkedin';
  label: string;
  href: string;
}

export const siteConfig = {
  projectName: "infra-guardian",
  description: "A calm helper for people who self-host but are not sysadmins. It watches your setup, explains things in plain English, and never changes anything without a backup and your yes.",
  repoUrl: "https://github.com/Stravelakis/infra-guardian",
  // Path under /public including the base path, e.g. '/repo-name/favicon.svg'. Empty = no favicon tag.
  faviconHref: "/infra-guardian/favicon.svg",

  // What a link to the site shows when shared (Open Graph / Twitter cards).
  // seoTitle is the front page's <title> and share title; empty falls back to
  // "Overview · projectName". socialImage is a 1200x630 PNG in /public
  // (without the base path); empty means no image, and most platforms then
  // show a bare, easily-ignored link. Always set both before publishing.
  seoTitle: "infra-guardian: a safety net for your self-hosted setup",
  socialImage: "og-image.png",
  socialImageAlt: "infra-guardian: back up, preview, ask, change one thing, write it down.",
  locale: 'en_GB',

  // Left menu, top group. The "On this page" group below it is built from the
  // headings of the reading level on screen.
  nav: [
    { id: 'top', label: 'Overview' },
    { id: 'features', label: 'What it does' },
    { id: 'showcase', label: 'A real run' },
  ],

  // Buttons and chips in the hero.
  heroLinks: [
    { label: 'Get it on GitHub', href: 'https://github.com/Stravelakis/infra-guardian', primary: true },
    { label: 'Latest release', href: 'https://github.com/Stravelakis/infra-guardian/releases/latest' },
    { label: 'What changed', href: 'https://github.com/Stravelakis/infra-guardian/blob/HEAD/CHANGELOG.md' },
  ],
  heroPills: ['Backs up first', 'Asks before it acts', 'One change at a time', 'No keys needed to start'],

  // The three cards under the hero. They switch the reading level.
  levelCards: [
    { id: 'dev', tag: 'Dev', title: 'How it is built', text: 'The skill file, the four scripts, the config, the reference library, and what is enforced by code versus by instruction.' },
    { id: 'plain', tag: 'English', title: 'How to use it', text: 'For people comfortable with tech who do not write code. What it does, install, a typical session, the safety promises, fixes.' },
    { id: 'eli5', tag: 'ELI5', title: 'Start from zero', text: 'Slow and complete. What a server is, what a skill is, what a backup is, then every step with what you should see.' },
  ],

  // Reading-level switch at the top of the sidebar. The ids are fixed (they
  // match src/docs/dev.md, plain.md, eli5.md); change labels only.
  // First-visit level (STANDARDS §7: English). A saved choice still wins.
  defaultVernacular: 'plain',

  // Tally form link (STANDARDS §8). Empty = no "Send feedback" link.
  feedbackUrl: '',

  vernaculars: [
    { id: 'dev', label: 'Dev' },
    { id: 'plain', label: 'English' },
    { id: 'eli5', label: 'ELI5' },
  ],

  // infra-guardian is Python scripts plus instructions for Claude; a browser
  // sandbox cannot run it honestly. The front page shows a real captured run
  // instead (never a fake "run" button, STANDARDS §7).
  playground: {
    enabled: false,
    starterCode: `// try it\nconsole.log("hello from the playground")`,
  },

  author: {
    name: 'Stravelakis',
    links: [
      { kind: 'github', label: 'GitHub', href: 'https://github.com/Stravelakis' },
      { kind: 'linkedin', label: 'LinkedIn', href: 'https://www.linkedin.com/in/stravelakiscom/' },
    ] as SocialLink[],
  },

};
