/**
 * EthicalAds Integration for LITIENGINE Documentation (Zensical)
 * Privacy-preserving developer ads with instant navigation and responsive placement.
 */
(function() {
  function setupAds() {
    const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    const testAttr = isLocalhost ? ' data-ea-test="true"' : '';

    // 1. Table of Contents Sidebar Placement (Desktop)
    const tocNav = document.querySelector('.md-sidebar--secondary nav.md-nav--secondary');
    if (tocNav && !document.getElementById('ea-sidebar-container')) {
      const adSidebarWrapper = document.createElement('div');
      adSidebarWrapper.id = 'ea-sidebar-container';
      adSidebarWrapper.className = 'ea-sidebar-wrapper';
      adSidebarWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="text"${testAttr} class="adaptive flat"></div>`;
      tocNav.appendChild(adSidebarWrapper);
    }

    // 2. Article Bottom Placement (Visible when sidebar is absent or on mobile)
    const contentInner = document.querySelector('.md-content__inner article') || document.querySelector('.md-content__inner');
    if (contentInner && !document.getElementById('ea-article-container')) {
      const adArticleWrapper = document.createElement('div');
      adArticleWrapper.id = 'ea-article-container';
      adArticleWrapper.className = 'ethical-ad-article-wrapper';
      adArticleWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="image"${testAttr} class="adaptive bordered"></div>`;
      contentInner.appendChild(adArticleWrapper);
    }

    // 3. Trigger EthicalAds reload with retry for async script loading
    function tryLoadAds(attempts = 0) {
      if (window.ethicalads && typeof window.ethicalads.load === 'function') {
        window.ethicalads.load();
      } else if (attempts < 5) {
        setTimeout(() => tryLoadAds(attempts + 1), 250);
      }
    }
    tryLoadAds();
  }

  // Hook into Material/Zensical document observable stream if present
  if (typeof document$ !== 'undefined') {
    document$.subscribe(setupAds);
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupAds);
    } else {
      setupAds();
    }
  }

  // Backup observer for dynamic route changes
  window.addEventListener('popstate', setupAds);
  document.addEventListener('DOMContentSwitch', setupAds);
  window.addEventListener('load', setupAds);
})();
