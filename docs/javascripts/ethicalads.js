/**
 * EthicalAds Integration for LITIENGINE Documentation (Zensical)
 * Privacy-preserving developer ads with instant navigation and localhost test support.
 */
(function() {
  function setupAds() {
    const isLocalhost = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    const testAttr = isLocalhost ? ' data-ea-test="true"' : '';

    // 1. Target Article Content (Bottom of main article)
    const contentInner = document.querySelector('.md-content__inner article') || document.querySelector('.md-content__inner');
    if (contentInner && !document.getElementById('ea-article-container')) {
      const adArticleWrapper = document.createElement('div');
      adArticleWrapper.id = 'ea-article-container';
      adArticleWrapper.className = 'ethical-ad-article-wrapper';
      adArticleWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="image"${testAttr} class="adaptive bordered"></div>`;
      contentInner.appendChild(adArticleWrapper);
    }

    // 2. Target Table of Contents Sidebar
    const tocNav = document.querySelector('.md-sidebar--secondary nav.md-nav--secondary');
    if (tocNav && !document.getElementById('ea-sidebar-container')) {
      const adSidebarWrapper = document.createElement('div');
      adSidebarWrapper.id = 'ea-sidebar-container';
      adSidebarWrapper.className = 'ea-sidebar-wrapper';
      adSidebarWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="text"${testAttr} class="adaptive flat"></div>`;
      tocNav.appendChild(adSidebarWrapper);
    }

    // 3. Trigger EthicalAds reload
    if (window.ethicalads && typeof window.ethicalads.load === 'function') {
      window.ethicalads.load();
    }
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
})();
