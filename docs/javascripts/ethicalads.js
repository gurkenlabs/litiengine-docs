/**
 * EthicalAds Integration for LITIENGINE Documentation (Zensical)
 * Privacy-preserving developer ads with instant navigation support.
 */
(function() {
  function injectEthicalAds() {
    // 1. Target Article Content (Bottom of main article)
    const contentInner = document.querySelector('.md-content__inner');
    if (contentInner && !document.getElementById('ea-article-container')) {
      const adArticleWrapper = document.createElement('div');
      adArticleWrapper.id = 'ea-article-container';
      adArticleWrapper.className = 'ethical-ad-article-wrapper';
      adArticleWrapper.innerHTML = '<div data-ea-publisher="litiengine" data-ea-type="image" class="adaptive bordered"></div>';
      contentInner.appendChild(adArticleWrapper);
    }

    // 2. Target Table of Contents Sidebar (if secondary sidebar exists)
    const tocInner = document.querySelector('.md-sidebar--secondary .md-sidebar__inner');
    if (tocInner && !document.getElementById('ea-sidebar-container')) {
      const adSidebarWrapper = document.createElement('div');
      adSidebarWrapper.id = 'ea-sidebar-container';
      adSidebarWrapper.className = 'ea-sidebar-wrapper';
      adSidebarWrapper.innerHTML = '<div data-ea-publisher="litiengine" data-ea-type="text" class="adaptive flat"></div>';
      tocInner.appendChild(adSidebarWrapper);
    }

    // 3. Trigger EthicalAds reload if available
    if (typeof ethicalads !== 'undefined' && typeof ethicalads.load === 'function') {
      ethicalads.load();
    }
  }

  // Initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectEthicalAds);
  } else {
    injectEthicalAds();
  }

  // Support Zensical instant navigation (SPA page transitions)
  document.addEventListener('DOMContentSwitch', injectEthicalAds);
  window.addEventListener('popstate', injectEthicalAds);
})();
