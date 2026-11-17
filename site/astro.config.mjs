import { defineConfig } from 'astro/config';

// Served at https://docs.stravelakis.com/infra-guardian/ through the organisation Pages site.
export default defineConfig({
  site: 'https://docs.stravelakis.com',
  base: '/infra-guardian',
  outDir: './dist',
  // Inline PostCSS config so Vite never picks up a postcss.config.js from the repo root.
  vite: { css: { postcss: { plugins: [] } } },
});
